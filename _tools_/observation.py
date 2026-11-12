#!/usr/bin/env python3
"""Append-only writer and checker for the day observation file.

The day observation file (``_records_/<local date>/perception-scout/
observation.md``) is append-only inside its day - constitution C1
in ``_conventions_/local-conventions/perception-driven-queue.md``
section 8, and rule 5 of the perception-scout activity profile:
each scout unit appends its own pass section, never rewrites
another unit's section. Its frontmatter carries the day counters
(``items_observed``, ``red_dots_seen``, ``red_dots_explained``,
``unexplained_red_dots``), which are cumulative within the day.

Issue #668 is the shape this tool prevents. The ticker-1919
events-group unit appended its section to the live-tree copy of
the 2026-11-11 observation file, which was stale: the ticker-1843
section, delivered to the records branch at 19:13 local, had not
been pulled into the live tree. The live file ended up holding
base pass + latest continued pass only, and any consumer reading
only the live copy (scout_diff, planner) missed the 1843 pass
unknowns - the small 9 beneath the Mission terminal, the second
left-column icon (white truck), the blue gift-box marker above the
dispatched truck, the 35 km blue house marker. The branch was
repaired by the delivery merge, not by the writer. The writer
itself computed its counters from the branch state it had read
elsewhere (items 21 to 29), so the counters were right while the
sections were wrong: a hand edit cannot tell the two apart.

This tool is the mechanical writer. A scout unit appends through
it instead of hand-editing the file:

  observation.py append --file _records_/2026-11-11/perception-scout/observation.md \\
      --section /tmp/scout-1919-section.md \\
      --reference /tmp/observation-branch-copy.md \\
      --add-items 8 --add-seen 7 --add-explained 5 --add-unexplained 2

The ``--reference`` is the delivered branch copy of the same day
file (``git show github/records/<date>:_records_/<date>/
perception-scout/observation.md``); the writer passes it so the
append is grounded on the latest delivered state, not on
whatever the live tree happens to hold. The deltas are the
unit's own stats (perception-driven-queue.md section 8: the
unit result carries items_observed, red_dots_seen,
red_dots_explained, unexplained_red_dots for the unit), and the
tool computes the new day totals as the per-field maximum of the
live file and the reference plus the delta - so a writer whose
live copy is stale can no longer under-count, and a writer who
recomputes from a stale base is corrected, not silently wrong.

Two commands, standard library only:

  check  - verify a day observation file is append-consistent:
           every ``## Pass ...`` heading unique (a repeated
           heading is a replace, not an append); with
           ``--reference``, every pass section the delivered
           branch copy holds is present in the file (a missing
           one is the #668 signature), and no cumulative day
           counter sits below the reference's (a drop means the
           file was written from a stale base). A
           red_dots_seen / explained / unexplained identity
           mismatch is a warning, not a failure. Exit 0 clean,
           1 problems found, 2 unreadable.
  append - append one pass section, mechanically. Refuses
           (exit 1, nothing written) when the section heading
           already exists in the file - each continued pass is
           a NEW section, never a replacement of a previous
           continued pass - and when a cumulative delta is
           negative or an unexplained delta would take the day
           total negative. With ``--reference``, any delivered
           pass section missing from the live file is restored
           verbatim, in reference order, before the new section
           is appended, so a stale live copy heals at write
           time instead of dropping the earlier pass. The
           write is atomic (temporary file plus rename) and the
           rebuilt text is re-parsed and verified before the
           write and re-read after it. Exit 0 appended, 1
           refused, 2 usage or unreadable input.

Usage:
  observation.py check --file PATH [--reference PATH]
                       [--format text|json]
  observation.py append --file PATH --section PATH
                        [--reference PATH]
                        --add-items N --add-seen N
                        --add-explained N --add-unexplained N
                        [--format text|json]
"""

import argparse
import json
import os
import re
import sys
import tempfile

COUNTER_FIELDS = ("items_observed", "red_dots_seen",
                  "red_dots_explained", "unexplained_red_dots")
# Counters that only grow within a day. unexplained_red_dots is
# NOT in this list: a later pass can explain a dot an earlier
# pass left unexplained, so the day total can legitimately fall.
CUMULATIVE_FIELDS = ("items_observed", "red_dots_seen",
                     "red_dots_explained")


# ---------------------------------------------------------------------
# Parsing
# ---------------------------------------------------------------------

def _split_frontmatter(text):
    """Split a day observation file into frontmatter and body.

    Returns (counters, front_lines, body, error). counters maps
    each counter field to its int value; front_lines are the
    frontmatter lines in order, counter lines included as
    written; body is the text after the closing ---. error names
    the problem, or None.
    """
    lines = text.splitlines()
    if len(lines) < 3 or lines[0].strip() != "---":
        return None, None, None, "no frontmatter block"
    close = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            close = i
            break
    if close is None:
        return None, None, None, "frontmatter never closed"
    counters = {}
    for line in lines[1:close]:
        m = re.match(r"^([A-Za-z_][A-Za-z0-9_]*):\s*(.*?)\s*$", line)
        if m and m.group(1) in COUNTER_FIELDS:
            try:
                value = int(m.group(2))
            except ValueError:
                return None, None, None, \
                    "counter %s is not an integer: %r" % (
                        m.group(1), m.group(2))
            if value < 0:
                return None, None, None, \
                    "counter %s is negative: %d" % (m.group(1), value)
            counters[m.group(1)] = value
    missing = [f for f in COUNTER_FIELDS if f not in counters]
    if missing:
        return None, None, None, \
            "frontmatter missing counters: %s" % ", ".join(missing)
    body = "\n".join(lines[close + 1:])
    return counters, lines[1:close], body, None


def _pass_sections(body):
    """Return [(heading, block_text)] for each ``## `` section.

    A block runs from its ``## `` line to just before the next
    ``## `` line, or to the end of the body. Text before the
    first ``## `` line (the file intro) is not a section.
    """
    lines = body.splitlines()
    starts = [i for i, line in enumerate(lines)
              if line.startswith("## ")]
    sections = []
    for pos, start in enumerate(starts):
        end = starts[pos + 1] if pos + 1 < len(starts) else len(lines)
        block = "\n".join(lines[start:end]).rstrip("\n")
        sections.append((lines[start].strip(), block))
    return sections


def _read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def _parse_file(path):
    """Read and parse a day observation file.

    Returns (counters, front_lines, body, sections, error).
    """
    try:
        text = _read(path)
    except (OSError, UnicodeDecodeError) as exc:
        return None, None, None, None, "cannot read %s: %s" % (path, exc)
    counters, front_lines, body, error = _split_frontmatter(text)
    if error is not None:
        return None, None, None, None, "%s: %s" % (path, error)
    return counters, front_lines, body, _pass_sections(body), None


# ---------------------------------------------------------------------
# check
# ---------------------------------------------------------------------

def check_observation(path, reference_path=None):
    """Return (problems, warnings, info, unreadable).

    unreadable is True when the target file (or the reference)
    cannot be read at all - exit 2 - as opposed to a file that
    reads but breaks the append rules, which is exit 1.
    """
    problems = []
    warnings = []
    info = {"file": path, "sections": 0}
    counters, _front, _body, sections, error = _parse_file(path)
    if error is not None:
        unreadable = error.startswith("cannot read")
        return [error], warnings, info, unreadable
    info["counters"] = counters
    headings = [h for h, _b in sections]
    info["sections"] = len(sections)
    info["headings"] = headings
    seen = set()
    for heading in headings:
        if heading in seen:
            problems.append("duplicate heading (a replace, not an "
                            "append): %s" % heading)
        seen.add(heading)
        if not heading.startswith("## Pass "):
            warnings.append("non-pass section heading: %s" % heading)
    if counters["red_dots_seen"] != counters["red_dots_explained"] + \
            counters["unexplained_red_dots"]:
        warnings.append(
            "counter identity: red_dots_seen %d != "
            "red_dots_explained %d + unexplained_red_dots %d"
            % (counters["red_dots_seen"],
               counters["red_dots_explained"],
               counters["unexplained_red_dots"]))
    if reference_path is not None:
        ref_counters, _f, _b, ref_sections, error = \
            _parse_file(reference_path)
        if error is not None:
            unreadable = error.startswith("cannot read")
            return [error], warnings, info, unreadable
        ref_headings = [h for h, _b in ref_sections]
        for heading in ref_headings:
            if heading not in seen:
                problems.append(
                    "missing section the delivered copy holds "
                    "(issue #668): %s" % heading)
        for field in CUMULATIVE_FIELDS:
            if counters[field] < ref_counters[field]:
                problems.append(
                    "counter regression: %s %d below delivered %d "
                    "(written from a stale base)"
                    % (field, counters[field], ref_counters[field]))
    return problems, warnings, info, False


# ---------------------------------------------------------------------
# append
# ---------------------------------------------------------------------

def _rebuild(counters, front_lines, body, restored_blocks, new_block):
    """Rebuild the full file text with new counters and sections.

    Counter lines are rewritten in place, so the frontmatter
    keeps its original order; the body keeps its intro and
    existing sections untouched, and the restored and new
    sections are appended after exactly one blank line each.
    """
    front = ["---"]
    for line in front_lines:
        m = re.match(r"^([A-Za-z_][A-Za-z0-9_]*):", line)
        if m and m.group(1) in COUNTER_FIELDS:
            front.append("%s: %d" % (m.group(1), counters[m.group(1)]))
        else:
            front.append(line)
    front.append("---")
    text = "\n".join(front) + "\n"
    body = body.rstrip("\n")
    parts = [body] if body else []
    parts.extend(restored_blocks)
    parts.append(new_block)
    text += "\n\n".join(parts) + "\n"
    return text


def append_section(path, section_path, reference_path, deltas):
    """Append one pass section; return (result, error, code).

    result is a dict on success; error names the refusal or input
    problem, or None. code is 0 on success, 1 on a refusal (the
    file is a valid day observation file but the append would
    break the append-only rule), 2 on a usage or unreadable-input
    problem. Nothing is written unless code is 0.
    """
    try:
        section_text = _read(section_path)
    except (OSError, UnicodeDecodeError) as exc:
        return None, "cannot read %s: %s" % (section_path, exc), 2
    section_lines = [line for line in section_text.splitlines()]
    first = next((line for line in section_lines if line.strip()), None)
    if first is None or not first.startswith("## "):
        return None, "section file %s does not start with a " \
            "'## ' heading" % section_path, 2
    heading = first.strip()
    if "Pass " not in heading:
        return None, "section heading is not a pass section: %s" \
            % heading, 2
    new_block = "\n".join(section_lines).strip("\n")
    counters, front_lines, body, sections, error = _parse_file(path)
    if error is not None:
        code = 2 if error.startswith("cannot read") else 1
        return None, error, code
    headings = [h for h, _b in sections]
    if heading in headings:
        return None, "refused: heading already present - a continued " \
            "pass is a NEW section, never a replacement: %s" % heading, 1
    for field in CUMULATIVE_FIELDS:
        if deltas[field] < 0:
            return None, "refused: %s delta is negative (%d); " \
                "cumulative day counters only grow" % (
                    field, deltas[field]), 1
    restored = []
    restored_headings = []
    base = dict(counters)
    if reference_path is not None:
        ref_counters, _f, _b, ref_sections, error = \
            _parse_file(reference_path)
        if error is not None:
            code = 2 if error.startswith("cannot read") else 1
            return None, error, code
        for ref_heading, ref_block in ref_sections:
            if ref_heading not in headings:
                restored.append(ref_block)
                restored_headings.append(ref_heading)
                headings.append(ref_heading)
        for field in COUNTER_FIELDS:
            base[field] = max(base[field], ref_counters[field])
    new_counters = {}
    for field in COUNTER_FIELDS:
        new_counters[field] = base[field] + deltas[field]
        if new_counters[field] < 0:
            return None, "refused: %s delta %d would take the day " \
                "total negative (base %d)" % (
                    field, deltas[field], base[field]), 1
    text = _rebuild(new_counters, front_lines, body, restored, new_block)
    # Verify the rebuilt text in memory before touching the disk.
    re_counters, _f, re_body, error = _split_frontmatter(text)
    if error is not None:
        return None, "rebuilt file fails to parse: %s" % error, 1
    re_headings = [h for h, _b in _pass_sections(re_body)]
    if heading not in re_headings:
        return None, "rebuilt file lost the new section heading", 1
    if re_counters != new_counters:
        return None, "rebuilt file counters mismatch: %r != %r" % (
            re_counters, new_counters), 1
    directory = os.path.dirname(os.path.abspath(path))
    fd, tmp_path = tempfile.mkstemp(prefix=".observation-",
                                    dir=directory)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            fh.write(text)
        os.replace(tmp_path, path)
    except OSError as exc:
        try:
            os.unlink(tmp_path)
        except OSError:
            pass
        return None, "cannot write %s: %s" % (path, exc), 2
    # Re-read the file as written and confirm it is what we built.
    try:
        written = _read(path)
    except (OSError, UnicodeDecodeError) as exc:
        return None, "cannot re-read %s after write: %s" % (path, exc), 1
    if written != text:
        return None, "re-read mismatch after write on %s" % path, 1
    return {"file": path,
            "appended_heading": heading,
            "restored_sections": restored_headings,
            "counters_before": base,
            "counters": new_counters}, None, 0


# ---------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------

def _emit(payload, fmt):
    if fmt == "json":
        print(json.dumps(payload, ensure_ascii=False, sort_keys=True))
    else:
        for line in payload["text"]:
            print(line)


def cmd_check(args):
    problems, warnings, info, unreadable = check_observation(
        args.file, args.reference)
    text = []
    if problems:
        text.append("observation check FAILED on %s:" % args.file)
        text.extend("  - %s" % p for p in problems)
    else:
        text.append("observation check clean on %s: %d pass sections, "
                    "counters %s" % (
                        args.file, info["sections"],
                        ", ".join("%s=%d" % (f, info["counters"][f])
                                  for f in COUNTER_FIELDS)))
    text.extend("  warning: %s" % w for w in warnings)
    payload = {"command": "check", "file": args.file,
               "clean": not problems, "problems": problems,
               "warnings": warnings, "info": info, "text": text}
    _emit(payload, args.format)
    if unreadable:
        return 2
    return 0 if not problems else 1


def cmd_append(args):
    deltas = {"items_observed": args.add_items,
              "red_dots_seen": args.add_seen,
              "red_dots_explained": args.add_explained,
              "unexplained_red_dots": args.add_unexplained}
    result, error, code = append_section(args.file, args.section,
                                         args.reference, deltas)
    if error is not None:
        text = ["observation append REFUSED on %s: %s"
                % (args.file, error)]
        payload = {"command": "append", "file": args.file,
                   "appended": False, "error": error, "text": text}
        _emit(payload, args.format)
        return code
    text = ["observation append ok on %s: %s"
            % (args.file, result["appended_heading"])]
    if result["restored_sections"]:
        text.append("  restored %d delivered section(s) missing from "
                    "the live file:" % len(result["restored_sections"]))
        text.extend("    - %s" % h
                    for h in result["restored_sections"])
    text.append("  counters: %s"
                % ", ".join("%s=%d" % (f, result["counters"][f])
                            for f in COUNTER_FIELDS))
    payload = {"command": "append", "file": args.file,
               "appended": True, "result": result, "text": text}
    _emit(payload, args.format)
    return 0


def main(argv=None):
    parser = argparse.ArgumentParser(
        prog="observation.py",
        description="Append-only writer and checker for the day "
                    "observation file (issue #668).")
    sub = parser.add_subparsers(dest="command", required=True)

    check = sub.add_parser("check",
                           help="verify a day observation file is "
                                "append-consistent")
    check.add_argument("--file", required=True)
    check.add_argument("--reference", default=None,
                       help="delivered branch copy of the same day "
                            "file, for the missing-section and "
                            "counter-regression checks")
    check.add_argument("--format", choices=("text", "json"),
                       default="text")
    check.set_defaults(func=cmd_check)

    append = sub.add_parser("append",
                            help="append one pass section, "
                                 "mechanically")
    append.add_argument("--file", required=True)
    append.add_argument("--section", required=True,
                        help="file holding the new '## Pass ...' "
                             "section to append")
    append.add_argument("--reference", default=None,
                        help="delivered branch copy of the same day "
                             "file; missing delivered sections are "
                             "restored before the append")
    append.add_argument("--add-items", type=int, required=True)
    append.add_argument("--add-seen", type=int, required=True)
    append.add_argument("--add-explained", type=int, required=True)
    append.add_argument("--add-unexplained", type=int, required=True,
                        help="may be negative when this pass explains "
                             "dots an earlier pass left unexplained")
    append.add_argument("--format", choices=("text", "json"),
                        default="text")
    append.set_defaults(func=cmd_append)

    args = parser.parse_args(argv)
    try:
        return args.func(args)
    except (OSError, UnicodeDecodeError) as exc:
        payload = {"command": args.command, "error": str(exc),
                   "text": ["observation %s failed: %s"
                            % (args.command, exc)]}
        _emit(payload, args.format)
        return 2


if __name__ == "__main__":
    sys.exit(main())
