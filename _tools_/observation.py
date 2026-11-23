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

Rollover (word budget): a day file never grows past the budget. When appending a
section would take the day file past ROLL_AT (400) body words, the section goes into
the next key-named part, ``observation-p2.md``, ``observation-p3.md`` and so on, each
under HARD_MAX (450) words. The earlier files are left untouched (records are
immutable); the new part carries the cumulative day counters (the per-field maximum
over every part and the reference, plus the delta), a pointer back to the day file,
and a line in the folder's INDEX.md. ``--file`` names ``observation.md`` or any part;
the writer finds the day's parts beside it. A section that cannot fit even alone in
HARD_MAX words is refused (split it). ``check`` reads every part: a heading may not
repeat across parts and a cumulative counter may not fall from one part to the next.
A file with any other name is a single file and never rolls over.

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
from datetime import datetime, timezone

ROLL_AT, HARD_MAX = 400, 450
PART_NAME = re.compile(r"^observation(?:-p(\d+))?\.md$")
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


_COUNTER = []


def _file_words(text):
    """Body words of a whole file as the word-budget checker counts them; a plain count of the words after the
    frontmatter when that checker is not on this machine."""
    if not _COUNTER:
        _COUNTER.append(None)
        loader = os.path.expanduser("~/dtadpole/reflection/_tools_/document-word-budget/word-budget.py")
        try:
            import importlib.util
            spec = importlib.util.spec_from_file_location("observation_word_budget", loader)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            _COUNTER[0] = module.check_text
        except Exception:
            _COUNTER[0] = None
    if _COUNTER[0] is not None:
        try:
            return int(_COUNTER[0](text, "observation.md")["body_words"])
        except Exception:
            pass
    body = text.split("\n---\n", 1)[1] if text.startswith("---\n") and "\n---\n" in text else text
    return len(body.split())


def _day_parts(path):
    """The day's part files in order, observation.md first, for a path named observation.md or observation-pN.md;
    just [path] for any other name."""
    directory = os.path.dirname(os.path.abspath(path))
    if not PART_NAME.match(os.path.basename(path)):
        return [os.path.abspath(path)]
    found = []
    for name in os.listdir(directory):
        m = PART_NAME.match(name)
        if m:
            found.append((int(m.group(1) or 1), os.path.join(directory, name)))
    return [p for _n, p in sorted(found)] or [os.path.abspath(path)]


def _part_number(path):
    m = PART_NAME.match(os.path.basename(path))
    return int(m.group(1) or 1) if m else 1


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
    parts = _day_parts(path)
    if len(parts) > 1:
        info["parts"] = [os.path.basename(p) for p in parts]
        seen_by = {}
        previous = None
        for part in parts:
            p_counters, _pf, _pb, p_sections, p_error = _parse_file(part)
            if p_error is not None:
                return [p_error], warnings, info, p_error.startswith("cannot read")
            for heading, _block in p_sections:
                if heading in seen_by and seen_by[heading] != part:
                    problems.append("heading repeats across parts (a replace, not an append): %s in %s and %s" % (
                        heading, os.path.basename(seen_by[heading]), os.path.basename(part)))
                seen_by.setdefault(heading, part)
            if previous is not None:
                for field in CUMULATIVE_FIELDS:
                    if p_counters[field] < previous[1][field]:
                        problems.append("counter regression across parts: %s %d in %s below %d in %s" % (
                            field, p_counters[field], os.path.basename(part), previous[1][field],
                            os.path.basename(previous[0])))
            previous = (part, p_counters)
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


def _part_front(first_front, number):
    """Frontmatter of a new part: the day file's lines with a part title, fresh dates and version 0.1.0; counter lines stay
    in place (_rebuild rewrites them)."""
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    out = []
    for line in first_front:
        key = re.match(r"^([A-Za-z_][A-Za-z0-9_]*):\s*(.*)$", line)
        name = key.group(1) if key else ""
        if name == "title":
            title = re.sub(r"\s+part \d+$", "", key.group(2).strip())
            out.append("title: %s part %d" % (title, number))
        elif name in ("created", "modified"):
            out.append("%s: %s" % (name, now))
        elif name == "version":
            out.append("version: 0.1.0")
        else:
            out.append(line)
    return out


def _index_part(part_path, words):
    """List the new part in the folder's INDEX.md (created when there is none): one line, never listed twice."""
    directory = os.path.dirname(part_path)
    index = os.path.join(directory, "INDEX.md")
    name = os.path.basename(part_path)
    line = "- [%s](%s) - the day observation file continues here (%d words)" % (name, name, words)
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    if os.path.exists(index):
        text = _read(index)
        if "](%s)" % name in text:
            return
        text = text.rstrip("\n") + "\n" + line + "\n"
        text = re.sub(r"(?m)^modified:.*$", "modified: %s" % now, text, count=1)
        m = re.search(r"(?m)^version: (\d+)\.(\d+)\.(\d+)\s*$", text)
        if m:
            text = text.replace(m.group(0), "version: %s.%d.0" % (m.group(1), int(m.group(2)) + 1), 1)
    else:
        text = ("---\ntitle: Perception scout records\ncreated: %s\nmodified: %s\nversion: 1.0.0\n"
                "description: The day observation file and its parts\n---\n\n# Perception scout records\n\n"
                "- [observation.md](observation.md) - the day observation file\n%s\n" % (now, now, line))
    tmp = index + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        fh.write(text)
    os.replace(tmp, index)


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
    parts = _day_parts(path)
    parsed = {}
    for part in parts:
        if os.path.abspath(part) == os.path.abspath(path):
            parsed[part] = (counters, front_lines, body, sections)
        else:
            p_counters, p_front, p_body, p_sections, p_error = _parse_file(part)
            if p_error is not None:
                return None, p_error, (2 if p_error.startswith("cannot read") else 1)
            parsed[part] = (p_counters, p_front, p_body, p_sections)
    if os.path.abspath(path) not in [os.path.abspath(p) for p in parts]:
        parts.append(os.path.abspath(path))
        parsed[os.path.abspath(path)] = (counters, front_lines, body, sections)
    headings = [h for part in parts for h, _b in parsed[part][3]]
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
    base = {f: max(parsed[part][0][f] for part in parts) for f in COUNTER_FIELDS}
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
    latest = parts[-1]
    l_counters, l_front, l_body, _l_sections = parsed[latest]
    rolled = False
    target = latest
    day_file = PART_NAME.match(os.path.basename(path)) is not None
    if day_file:
        latest_words = _file_words(_read(latest))
        added_words = _file_words("---\n---\n" + "\n\n".join(restored + [new_block]))
        if latest_words + added_words > ROLL_AT:
            rolled = True
            number = _part_number(latest) + 1
            target = os.path.join(os.path.dirname(os.path.abspath(path)), "observation-p%d.md" % number)
            if os.path.exists(target):
                return None, "refused: %s already exists" % os.path.basename(target), 1
            first_front = parsed[parts[0]][1]
            l_front = _part_front(first_front, number)
            l_body = ("Part %d of the day observation file: it continues the sections of the earlier parts, which stay "
                      "as written. The day counters above are the cumulative totals at this part." % number)
    text = _rebuild(new_counters, l_front, l_body, restored, new_block)
    if day_file and _file_words(text) > HARD_MAX:
        return None, "refused: the section is too long for a day file part (%d words; the limit is %d) - split it into " \
            "two pass sections" % (_file_words(text), HARD_MAX), 1
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
    directory = os.path.dirname(os.path.abspath(target))
    fd, tmp_path = tempfile.mkstemp(prefix=".observation-",
                                    dir=directory)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            fh.write(text)
        os.replace(tmp_path, target)
    except OSError as exc:
        try:
            os.unlink(tmp_path)
        except OSError:
            pass
        return None, "cannot write %s: %s" % (target, exc), 2
    # Re-read the file as written and confirm it is what we built.
    try:
        written = _read(target)
    except (OSError, UnicodeDecodeError) as exc:
        return None, "cannot re-read %s after write: %s" % (target, exc), 1
    if written != text:
        return None, "re-read mismatch after write on %s" % target, 1
    if rolled:
        _index_part(target, _file_words(text))
    path = target
    return {"file": path,
            "appended_heading": heading,
            "restored_sections": restored_headings,
            "rolled_over": rolled,
            "words": _file_words(_read(path)),
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


def _git_show(path, rev):
    """(text, repo top, repo-relative path) of the file as `rev` holds it; text None when rev has no such file."""
    import subprocess
    here = os.path.dirname(os.path.abspath(path))
    top = subprocess.run(["git", "-C", here, "rev-parse", "--show-toplevel"], capture_output=True, text=True)
    if top.returncode != 0:
        return None, None, None
    top = top.stdout.strip()
    rel = os.path.relpath(os.path.realpath(path), os.path.realpath(top))
    shown = subprocess.run(["git", "-C", top, "show", "%s:%s" % (rev, rel)], capture_output=True)
    return (shown.stdout.decode("utf-8") if shown.returncode == 0 else None), top, rel


def migrate_uncommitted(path, rev="HEAD", apply=False, require_idle=True, _before_write=None):
    """Move an UNCOMMITTED growth of a day observation file into its next part (one-off, for a file grown past the word budget
    before the rollover existed). Returns (report, error, code).

    The file as `rev` holds it must be a byte-exact prefix of the file now (the growth is appended sections and the counters,
    never a rewrite of earlier text), and the growth must be whole `## ` sections. Then the sections go into the next part
    (observation-pN.md, packed under HARD_MAX words each) with the file's CURRENT cumulative counters and a pointer back, the
    folder INDEX lists the part, and the file itself is put back to what `rev` holds, byte for byte (what `git checkout` of
    that file does). Nothing is lost and no committed text changes. A dry run (the default) only reports counts. With
    --apply and require_idle the claimed queue folder must hold no unit (the writer is the operator, mid-unit), and the
    file must be unchanged between the first read and the write. Output is counts only."""
    base_text, top, rel = _git_show(path, rev)
    if base_text is None:
        return None, "%s is not in %s (or %s is not a git checkout)" % (path, rev, path), 2
    try:
        cur_text = _read(path)
    except (OSError, UnicodeDecodeError) as exc:
        return None, "cannot read %s: %s" % (path, exc), 2
    b_counters, _bf, b_body, b_error = _split_frontmatter(base_text)
    c_counters, c_front, c_body, c_error = _split_frontmatter(cur_text)
    if b_error or c_error:
        return None, "frontmatter: %s" % (b_error or c_error), 1
    if cur_text == base_text:
        return {"nothing_to_do": True, "file": path}, None, 0
    if not c_body.startswith(b_body):
        return None, "refused: the committed text of %s is not a byte-exact prefix of the file now - earlier text was rewritten, " \
            "not appended; nothing was changed" % os.path.basename(path), 1
    for field in CUMULATIVE_FIELDS:
        if c_counters[field] < b_counters[field]:
            return None, "refused: cumulative counter %s fell from %d to %d" % (field, b_counters[field], c_counters[field]), 1
    tail = c_body[len(b_body):]
    sections = _pass_sections(tail.lstrip("\n"))
    if not sections or not tail.lstrip("\n").startswith("## "):
        return None, "refused: what follows the committed text is not a run of whole ## sections", 1
    known = [h for h, _b in _pass_sections(b_body)]
    headings = [h for h, _b in sections]
    if len(set(headings)) != len(headings) or set(headings) & set(known):
        return None, "refused: a grown section repeats a committed heading", 1
    parts = _day_parts(path)
    number = max([_part_number(p) for p in parts] + [1]) + 1
    first_front = _split_frontmatter(base_text)[1]
    def intro(n):
        return ("Part %d of the day observation file: it continues the sections of the earlier parts, which stay as written. The day "
                "counters above are the cumulative totals at this part." % n)

    def part_text(n, blocks):
        return _rebuild(c_counters, _part_front(first_front, n), intro(n), blocks[:-1], blocks[-1])

    packed, chunk = [], []
    for heading, block in sections:
        if chunk and _file_words(part_text(number + len(packed), [b for _h, b in chunk] + [block])) > HARD_MAX:
            packed.append(chunk)
            chunk = []
        chunk.append((heading, block))
        if _file_words(part_text(number + len(packed), [b for _h, b in chunk])) > HARD_MAX:
            return None, "refused: the section is too long for a day file part (limit %d words) - split it first" % HARD_MAX, 1
    packed.append(chunk)
    report = {"file": path, "committed_words": _file_words(base_text), "current_words": _file_words(cur_text),
              "sections_moved": len(sections), "parts_written": [], "counters": c_counters, "applied": False}
    texts = []
    for i, chunk in enumerate(packed):
        n = number + i
        text = part_text(n, [b for _h, b in chunk])
        target = os.path.join(os.path.dirname(os.path.abspath(path)), "observation-p%d.md" % n)
        if os.path.exists(target):
            return None, "refused: %s already exists" % os.path.basename(target), 1
        texts.append((target, text))
        report["parts_written"].append({"name": os.path.basename(target), "words": _file_words(text), "sections": len(chunk)})
    if not apply:
        return report, None, 0
    if require_idle:
        claimed = os.path.join(top, "_queue_", "claimed")
        if os.path.isdir(claimed) and any(f.endswith(".md") for f in os.listdir(claimed)):
            return None, "refused: _queue_/claimed/ holds a unit; the operator writes this file at unit close - run again between units", 1
    if _before_write:
        _before_write()
    if _read(path) != cur_text:
        return None, "refused: the file changed while it was being read; nothing was written - run again", 1
    for target, text in texts:
        fd, tmp = tempfile.mkstemp(prefix=".observation-", dir=os.path.dirname(target))
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            fh.write(text)
        os.replace(tmp, target)
        _index_part(target, _file_words(text))
    fd, tmp = tempfile.mkstemp(prefix=".observation-", dir=os.path.dirname(os.path.abspath(path)))
    with os.fdopen(fd, "w", encoding="utf-8") as fh:
        fh.write(base_text)
    os.replace(tmp, path)
    ok = _read(path) == base_text and all(_read(t) == x for t, x in texts)
    problems, _w, _i, _u = check_observation(path)
    report["applied"] = True
    report["restored_to_%s" % rev.replace("/", "_")] = _read(path) == base_text
    report["check_problems"] = len(problems)
    if not ok or problems:
        return report, "the written files do not read back as expected (%d problem(s))" % len(problems), 1
    return report, None, 0


def cmd_migrate(args):
    report, error, code = migrate_uncommitted(args.file, args.base, args.apply, not args.allow_claimed)
    if error is not None:
        _emit({"command": "migrate", "error": error, "text": ["observation migrate REFUSED on %s: %s" % (args.file, error)]}, args.format)
        return code
    if report.get("nothing_to_do"):
        _emit({"command": "migrate", "result": report, "text": ["observation migrate: nothing to do on %s (it equals %s)" % (args.file, args.base)]}, args.format)
        return 0
    text = ["observation migrate %s on %s: committed %d words, now %d words, %d section(s) %s"
            % ("APPLIED" if report["applied"] else "(dry run, nothing written)", args.file, report["committed_words"],
               report["current_words"], report["sections_moved"], "moved" if report["applied"] else "would move")]
    for part in report["parts_written"]:
        text.append("  %s: %d words, %d section(s)" % (part["name"], part["words"], part["sections"]))
    text.append("  counters: %s" % ", ".join("%s=%d" % (f, report["counters"][f]) for f in COUNTER_FIELDS))
    if report["applied"]:
        text.append("  %s is back to what %s holds; the folder INDEX lists the part; check problems %d"
                    % (os.path.basename(args.file), args.base, report["check_problems"]))
    _emit({"command": "migrate", "result": report, "text": text}, args.format)
    return 0


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
            % (result["file"], result["appended_heading"])]
    if result["rolled_over"]:
        text.append("  rolled over: the day file would pass %d words, so the section went into a new part "
                    "(%d words); the earlier files are untouched" % (ROLL_AT, result["words"]))
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

    migrate = sub.add_parser("migrate",
                             help="one-off: move an uncommitted growth of the day file into its next part and put the file back to its "
                                  "committed text (dry run unless --apply)")
    migrate.add_argument("--file", required=True)
    migrate.add_argument("--base", default="HEAD", help="the revision holding the committed text (default HEAD)")
    migrate.add_argument("--apply", action="store_true")
    migrate.add_argument("--allow-claimed", action="store_true",
                         help="skip the check that _queue_/claimed/ is empty (the operator writes this file at unit close)")
    migrate.add_argument("--format", choices=("text", "json"), default="text")
    migrate.set_defaults(func=cmd_migrate)

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
