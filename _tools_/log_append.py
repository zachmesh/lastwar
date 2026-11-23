#!/usr/bin/env python3
"""Newline-safe appends, checks and repairs for append-only JSONL logs.

The append-only logs under ``_logs_/`` (the input log and the action
log, ``_logs_/repo-actions/action-log.jsonl``) carry one JSON object
per line. They are appended by many jobs, and a plain shell append
(``echo "$line" >> file``) trusts the file to already end with a
newline. When it does not, the new entry is concatenated onto the
tail of the previous line: two JSON objects on one physical line,
and every line-by-line JSONL parser breaks on that line with
``Extra data``. Issue #401 counted 17 such lines in the action
log, all of them historical appends that ran while the file lacked
a trailing newline; the queue-planning 1340 run on 2026-11-07
repeated the defect the same day.

This tool is the shared append helper that ends the recurrence.
Every job that appends to a log should append through it instead
of a raw ``>>`` redirect:

  log_append.py append --file _logs_/repo-actions/action-log.jsonl \
      --json '{"timestamp": "...", "actor": "...", "action": "..."}'

Four commands, standard library only:

  append - append one line to a log file. If the file exists, is
           non-empty and does not end with a newline, a newline
           is written first, so the new entry always starts on
           its own line. The entry itself is written with exactly
           one trailing newline. ``--json`` validates the entry
           parses as a JSON object before anything is written;
           ``--line`` appends raw text. The read-last-byte and
           write happen under an exclusive advisory lock, so two
           jobs appending at the same moment cannot interleave
           into a concatenated or blank line. Exit 0 on success,
           2 on a usage or input error (bad JSON, unreadable
           file, no entry given).
  check  - scan a JSONL file line by line and report the lines
           that do not parse as JSON (line number, error, and
           the first 80 characters). A blank line is reported,
           not skipped: a blank line is not a JSON entry. Exit
           0 when every line parses, 1 when bad lines are
           found, 2 when the file cannot be read.
  repair - split concatenated lines back into one JSON object
           per line. A line that holds two or more JSON objects
           back to back is rewritten as that many lines, each
           object kept byte-for-byte as it was written; lines
           that already hold one object are left untouched, and
           the file's trailing-newline state is preserved, so
           the repair inserts only the missing newlines and
           changes no content. A blank line carries no JSON
           object, so it is dropped, not kept: the object
           multiset is still verified unchanged before anything
           is written. Dry-run by default: report what would
           split and what would drop. ``--write`` applies it,
           after verifying in memory that the multiset of parsed
           JSON objects is unchanged, and re-reads the file
           afterwards to confirm every line parses. A line that
           is not a run of complete JSON objects is
           unrepairable: the tool refuses, reports it and exits
           2, and writes nothing. Exit 0 when the file is clean
           or the repair was applied; a second repair run is a
           no-op.
  gate   - the pre-delivery gate (issue #422): check one or
           more log files, repair in place whatever is
           repairable, and re-check. Exit 0 only when every
           file is clean afterwards; 1 when a file still has
           bad lines (unrepairable content was found, so
           nothing was written for that file); 2 when a file
           cannot be read. A records-branch delivery runs
           this on the action log before bundling, so a
           stale concatenated tail from the live tree can
           never reach the branch again: the gate repairs the
           live copy in place, which is also how a
           branch-side repair propagates back to the live
           tree. The repair the gate applies is a records
           change (newlines only, blank lines dropped, no
           logged object changed) and rides the same date
           branch as the delivery.

The repair command is how the 17 historical lines from issue
#401 are fixed: it is a records change (only newlines inserted,
no content change) and rides the records branch, never a PR
branch. The tool does not decide that for the caller; it only
makes the repair mechanical and verifiable.

Usage:
  log_append.py append --file PATH (--line TEXT | --json TEXT | --stdin)
                       [--format text|json]
  log_append.py check --file PATH [--format text|json]
  log_append.py repair --file PATH [--write] [--format text|json]
  log_append.py gate --file PATH [--file PATH ...] [--format text|json]
"""

import argparse
import json
import sys

try:
    import fcntl
except ImportError:  # pragma: no cover - non-Unix platforms only
    fcntl = None

TOOL_VERSION = "1.1.0"

MAX_PREVIEW = 80


def _lock_exclusive(fd):
    if fcntl is not None:
        fcntl.flock(fd, fcntl.LOCK_EX)


def _lock_shared(fd):
    if fcntl is not None:
        fcntl.flock(fd, fcntl.LOCK_SH)


def _unlock(fd):
    if fcntl is not None:
        fcntl.flock(fd, fcntl.LOCK_UN)


def _split_json_objects(text):
    """Split one physical line into its run of JSON objects.

    Returns a list of the exact source span of each object, or None
    when the line is not a run of complete JSON objects (a single
    valid object returns a one-element list; trailing whitespace
    after the last object is allowed and dropped).
    """
    decoder = json.JSONDecoder()
    spans = []
    index = 0
    length = len(text)
    while index < length:
        while index < length and text[index] in " \t\r\n":
            index += 1
        if index >= length:
            break
        try:
            _obj, end = decoder.raw_decode(text, index)
        except json.JSONDecodeError:
            return None
        spans.append(text[index:end])
        index = end
    if not spans:
        return None
    return spans


def _parse_line_objects(line_text):
    """Parsed JSON objects on one physical line, or None if unparseable."""
    spans = _split_json_objects(line_text)
    if spans is None:
        return None
    return [json.loads(span) for span in spans]


def _read_lines(path):
    """Physical lines of a file as text, without their newlines.

    Returns (lines, ends_with_newline). Raises OSError / ValueError
    (bad UTF-8) to the caller.
    """
    with open(path, "rb") as handle:
        data = handle.read()
    ends_with_newline = data.endswith(b"\n")
    text = data.decode("utf-8")
    if text == "":
        return [], False
    lines = text.split("\n")
    if ends_with_newline:
        lines = lines[:-1]  # the split leaves a trailing empty piece
    return lines, ends_with_newline


def _check_lines(lines):
    """Bad-line reports for already-read physical lines.

    A blank line is reported, not skipped: a blank line is not
    a JSON entry.
    """
    bad = []
    for number, line in enumerate(lines, 1):
        if not line.strip():
            bad.append({"line": number, "error": "blank line",
                        "preview": ""})
            continue
        try:
            json.loads(line)
        except json.JSONDecodeError as exc:
            bad.append({"line": number, "error": str(exc),
                        "preview": line[:MAX_PREVIEW]})
    return bad


def _plan_repair(lines):
    """Plan a repair for already-read physical lines.

    Returns the repaired line list (``new_lines``), the
    concatenated lines that would split (``splits``: line
    number, object count, preview), the blank lines that would
    drop (``dropped_blanks``: line numbers), the lines that
    cannot be repaired (``unrepairable``), and the parsed
    objects before the repair (``before_objects``). A blank
    line carries no object, so dropping it leaves the object
    multiset unchanged.
    """
    splits = []          # (line number, object count, preview)
    dropped_blanks = []  # line numbers
    unrepairable = []    # (line number, error, preview)
    new_lines = []
    before_objects = []
    for number, line in enumerate(lines, 1):
        if not line.strip():
            dropped_blanks.append(number)
            continue
        objects = _parse_line_objects(line)
        if objects is None:
            try:
                json.loads(line)
            except json.JSONDecodeError as exc:
                unrepairable.append((number, str(exc),
                                      line[:MAX_PREVIEW]))
            else:  # pragma: no cover - _parse_line_objects agrees
                unrepairable.append((number, "unparseable line",
                                      line[:MAX_PREVIEW]))
            new_lines.append(line)
            continue
        before_objects.extend(objects)
        if len(objects) == 1:
            new_lines.append(line)
        else:
            spans = _split_json_objects(line)
            new_lines.extend(spans)
            splits.append((number, len(objects), line[:MAX_PREVIEW]))
    return {
        "new_lines": new_lines,
        "splits": splits,
        "dropped_blanks": dropped_blanks,
        "unrepairable": unrepairable,
        "before_objects": before_objects,
    }


def _repair_preserves_objects(before_objects, new_lines):
    """True when the planned lines hold exactly the same objects."""
    after_objects = []
    for line in new_lines:
        parsed = _parse_line_objects(line)
        if parsed is None:
            return False
        after_objects.extend(parsed)
    before_key = sorted(json.dumps(o, sort_keys=True, ensure_ascii=False)
                        for o in before_objects)
    after_key = sorted(json.dumps(o, sort_keys=True, ensure_ascii=False)
                       for o in after_objects)
    return before_key == after_key


def _apply_repair(path, new_lines, ends_with_newline):
    """Write planned lines to a file and verify the result parses.

    Returns (True, None) on success, (False, error text) when
    the write or the post-write verification fails.
    """
    import os
    new_text = "\n".join(new_lines)
    if new_lines and ends_with_newline:
        new_text += "\n"
    try:
        fd = os.open(path, os.O_RDWR, 0o644)
    except OSError as exc:
        return False, f"cannot open {path}: {exc}"
    try:
        _lock_exclusive(fd)
        os.lseek(fd, 0, os.SEEK_SET)
        os.write(fd, new_text.encode("utf-8"))
        os.ftruncate(fd, len(new_text.encode("utf-8")))
    except OSError as exc:
        return False, f"cannot write {path}: {exc}"
    finally:
        _unlock(fd)
        os.close(fd)
    try:
        check_lines, _ends = _read_lines(path)
    except (OSError, ValueError) as exc:
        return False, f"cannot re-read {path} after repair: {exc}"
    for line in check_lines:
        if not line.strip():
            return False, ("repair left a blank line; file needs "
                           "manual inspection")
        try:
            json.loads(line)
        except json.JSONDecodeError as exc:
            return False, f"repair left an unparseable line: {exc}"
    return True, None


def _render(result, fmt):
    if fmt == "json":
        print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    else:
        for line in result["text"]:
            print(line)


def cmd_append(args):
    sources = [args.line is not None, args.json is not None, args.stdin]
    if sum(sources) != 1:
        print("error: exactly one of --line, --json, --stdin is required",
              file=sys.stderr)
        return 2
    if args.line is not None:
        entry = args.line
    elif args.json is not None:
        entry = args.json
        try:
            parsed = json.loads(entry)
        except json.JSONDecodeError as exc:
            print(f"error: --json entry is not valid JSON: {exc}",
                  file=sys.stderr)
            return 2
        if not isinstance(parsed, dict):
            print("error: --json entry must be a JSON object, not "
                  f"{type(parsed).__name__}", file=sys.stderr)
            return 2
    else:
        entry = sys.stdin.read()
    entry = entry.rstrip("\r\n")
    if not entry:
        print("error: entry is empty", file=sys.stderr)
        return 2
    if "\n" in entry or "\r" in entry:
        print("error: entry must be a single line", file=sys.stderr)
        return 2

    import os
    try:
        fd = os.open(args.file, os.O_RDWR | os.O_CREAT | os.O_APPEND, 0o644)
    except OSError as exc:
        print(f"error: cannot open {args.file}: {exc}", file=sys.stderr)
        return 2
    try:
        _lock_exclusive(fd)
        size = os.lseek(fd, 0, os.SEEK_END)
        prepended = False
        if size > 0:
            os.lseek(fd, size - 1, os.SEEK_SET)
            last = os.read(fd, 1)
            if last != b"\n":
                os.write(fd, b"\n")
                prepended = True
        os.write(fd, entry.encode("utf-8") + b"\n")
    except OSError as exc:
        print(f"error: cannot append to {args.file}: {exc}", file=sys.stderr)
        return 2
    finally:
        _unlock(fd)
        os.close(fd)
    result = {
        "version": TOOL_VERSION,
        "file": args.file,
        "appended": True,
        "prepended_newline": prepended,
        "text": [f"appended to {args.file}"
                 + (" (prepended missing newline first)"
                    if prepended else "")],
    }
    _render(result, args.format)
    return 0


def cmd_check(args):
    try:
        lines, _ends = _read_lines(args.file)
    except OSError as exc:
        print(f"error: cannot read {args.file}: {exc}", file=sys.stderr)
        return 2
    except ValueError as exc:
        print(f"error: {args.file} is not valid UTF-8: {exc}",
              file=sys.stderr)
        return 2
    bad = _check_lines(lines)
    result = {
        "version": TOOL_VERSION,
        "file": args.file,
        "lines": len(lines),
        "bad_lines": len(bad),
        "bad": bad,
        "text": ([f"{args.file}: {len(lines)} lines, all valid JSON"]
                 if not bad else
                 [f"{args.file}: {len(bad)} of {len(lines)} lines "
                  f"do not parse as JSON"]
                 + [f"  line {b['line']}: {b['error']}"
                    + (f" :: {b['preview']}" if b["preview"] else "")
                    for b in bad]),
    }
    _render(result, args.format)
    return 0 if not bad else 1


def cmd_repair(args):
    try:
        lines, ends_with_newline = _read_lines(args.file)
    except OSError as exc:
        print(f"error: cannot read {args.file}: {exc}", file=sys.stderr)
        return 2
    except ValueError as exc:
        print(f"error: {args.file} is not valid UTF-8: {exc}",
              file=sys.stderr)
        return 2
    plan = _plan_repair(lines)
    splits = plan["splits"]
    dropped_blanks = plan["dropped_blanks"]
    unrepairable = plan["unrepairable"]
    if unrepairable:
        for number, error, preview in unrepairable:
            print(f"error: line {number}: {error}"
                  + (f" :: {preview}" if preview else ""),
                  file=sys.stderr)
        print(f"error: {len(unrepairable)} line(s) cannot be repaired; "
              "nothing was written", file=sys.stderr)
        return 2
    if not _repair_preserves_objects(plan["before_objects"],
                                     plan["new_lines"]):
        print("error: repair would change the logged objects; "
              "nothing was written", file=sys.stderr)
        return 2

    text = [f"{args.file}: {len(splits)} line(s) would split into "
            f"{sum(c for _n, c, _p in splits)} objects"
            if splits else
            f"{args.file}: clean, nothing to repair"]
    for number, count, preview in splits:
        text.append(f"  line {number}: {count} objects :: {preview}")
    for number in dropped_blanks:
        text.append(f"  line {number}: blank line would drop")
    result = {
        "version": TOOL_VERSION,
        "file": args.file,
        "lines": len(lines),
        "split_lines": len(splits),
        "splits": [{"line": n, "objects": c, "preview": p}
                   for n, c, p in splits],
        "dropped_blanks": len(dropped_blanks),
        "blanks": dropped_blanks,
        "objects_before": len(plan["before_objects"]),
        "objects_after": len(plan["before_objects"]),
        "written": False,
        "text": text,
    }
    if not args.write:
        _render(result, args.format)
        return 0
    if not splits and not dropped_blanks:
        _render(result, args.format)
        return 0
    ok, error = _apply_repair(args.file, plan["new_lines"],
                              ends_with_newline)
    if not ok:
        print(f"error: {error}", file=sys.stderr)
        return 2
    check_lines, _ends = _read_lines(args.file)
    result["written"] = True
    result["objects_after"] = sum(
        len(_parse_line_objects(line)) for line in check_lines)
    result["text"] = [f"{args.file}: repaired {len(splits)} line(s) into "
                      f"{sum(c for _n, c, _p in splits)} objects"
                      + (f", dropped {len(dropped_blanks)} blank line(s)"
                         if dropped_blanks else "")
                      + f"; {len(check_lines)} lines now, all valid JSON"]
    _render(result, args.format)
    return 0


def cmd_gate(args):
    """Check each file, repair in place what is repairable, re-check.

    Exit 0 only when every file is clean afterwards; 1 when a
    file still has bad lines (unrepairable content was found, so
    nothing was written for that file, or the repair did not
    leave a clean file); 2 when a file cannot be read.
    """
    results = []
    worst = 0
    text = []
    for path in args.file:
        try:
            lines, ends_with_newline = _read_lines(path)
        except OSError as exc:
            print(f"error: cannot read {path}: {exc}", file=sys.stderr)
            worst = max(worst, 2)
            results.append({"file": path, "status": "unreadable",
                            "lines": 0, "bad_lines": 0})
            text.append(f"{path}: cannot read")
            continue
        except ValueError as exc:
            print(f"error: {path} is not valid UTF-8: {exc}",
                  file=sys.stderr)
            worst = max(worst, 2)
            results.append({"file": path, "status": "unreadable",
                            "lines": 0, "bad_lines": 0})
            text.append(f"{path}: not valid UTF-8")
            continue
        bad = _check_lines(lines)
        if not bad:
            results.append({"file": path, "status": "clean",
                            "lines": len(lines), "bad_lines": 0,
                            "split_lines": 0, "dropped_blanks": 0})
            text.append(f"{path}: {len(lines)} lines, all valid JSON")
            continue
        plan = _plan_repair(lines)
        if plan["unrepairable"]:
            for number, error, preview in plan["unrepairable"]:
                print(f"error: {path}: line {number}: {error}"
                      + (f" :: {preview}" if preview else ""),
                      file=sys.stderr)
            print(f"error: {path}: {len(plan['unrepairable'])} line(s) "
                  "cannot be repaired; nothing was written",
                  file=sys.stderr)
            worst = max(worst, 1)
            results.append({"file": path, "status": "unrepairable",
                            "lines": len(lines),
                            "bad_lines": len(bad),
                            "split_lines": 0, "dropped_blanks": 0})
            text.append(f"{path}: {len(bad)} of {len(lines)} lines do "
                        "not parse as JSON; unrepairable, gate blocked")
            continue
        if not _repair_preserves_objects(plan["before_objects"],
                                         plan["new_lines"]):
            print(f"error: {path}: repair would change the logged "
                  "objects; nothing was written", file=sys.stderr)
            worst = max(worst, 1)
            results.append({"file": path, "status": "unrepairable",
                            "lines": len(lines),
                            "bad_lines": len(bad),
                            "split_lines": 0, "dropped_blanks": 0})
            text.append(f"{path}: repair would change the logged "
                        "objects; gate blocked")
            continue
        ok, error = _apply_repair(path, plan["new_lines"],
                                  ends_with_newline)
        if not ok:
            print(f"error: {path}: {error}", file=sys.stderr)
            worst = max(worst, 1)
            results.append({"file": path, "status": "unrepairable",
                            "lines": len(lines),
                            "bad_lines": len(bad),
                            "split_lines": 0, "dropped_blanks": 0})
            text.append(f"{path}: repair failed; gate blocked")
            continue
        try:
            check_lines, _ends = _read_lines(path)
        except (OSError, ValueError) as exc:
            print(f"error: cannot re-read {path} after repair: {exc}",
                  file=sys.stderr)
            worst = max(worst, 1)
            results.append({"file": path, "status": "unrepairable",
                            "lines": len(lines),
                            "bad_lines": len(bad),
                            "split_lines": 0, "dropped_blanks": 0})
            text.append(f"{path}: cannot re-read after repair; "
                        "gate blocked")
            continue
        bad_after = _check_lines(check_lines)
        if bad_after:
            print(f"error: {path}: repair left {len(bad_after)} bad "
                  "line(s); gate blocked", file=sys.stderr)
            worst = max(worst, 1)
            results.append({"file": path, "status": "unrepairable",
                            "lines": len(check_lines),
                            "bad_lines": len(bad_after),
                            "split_lines": len(plan["splits"]),
                            "dropped_blanks": len(
                                plan["dropped_blanks"])})
            text.append(f"{path}: repair left {len(bad_after)} bad "
                        "line(s); gate blocked")
            continue
        results.append({"file": path, "status": "repaired",
                        "lines": len(check_lines),
                        "bad_lines": 0,
                        "split_lines": len(plan["splits"]),
                        "dropped_blanks": len(plan["dropped_blanks"])})
        text.append(f"{path}: repaired {len(plan['splits'])} line(s)"
                    + (f", dropped {len(plan['dropped_blanks'])} "
                       "blank line(s)" if plan["dropped_blanks"] else "")
                    + f"; {len(check_lines)} lines now, all valid JSON")
    result = {
        "version": TOOL_VERSION,
        "files": results,
        "gate_passed": worst == 0,
        "text": text,
    }
    _render(result, args.format)
    return worst


def build_parser():
    parser = argparse.ArgumentParser(
        prog="log_append.py",
        description="Newline-safe appends, checks and repairs for "
                    "append-only JSONL logs (issue #401).")
    parser.add_argument("--version", action="version",
                        version=f"%(prog)s {TOOL_VERSION}")
    sub = parser.add_subparsers(dest="command", required=True)

    p_append = sub.add_parser(
        "append", help="append one newline-safe entry to a log file")
    p_append.add_argument("--file", required=True, help="log file path")
    group = p_append.add_mutually_exclusive_group(required=True)
    group.add_argument("--line", help="raw line to append")
    group.add_argument("--json",
                       help="JSON object to append (validated first)")
    group.add_argument("--stdin", action="store_true",
                       help="read the entry from stdin")
    p_append.add_argument("--format", choices=["text", "json"],
                          default="text")
    p_append.set_defaults(func=cmd_append)

    p_check = sub.add_parser(
        "check", help="report the lines of a JSONL file that do not parse")
    p_check.add_argument("--file", required=True, help="log file path")
    p_check.add_argument("--format", choices=["text", "json"],
                         default="text")
    p_check.set_defaults(func=cmd_check)

    p_repair = sub.add_parser(
        "repair", help="split concatenated JSON objects onto their own "
                       "lines (dry-run unless --write)")
    p_repair.add_argument("--file", required=True, help="log file path")
    p_repair.add_argument("--write", action="store_true",
                          help="apply the repair instead of dry-running")
    p_repair.add_argument("--format", choices=["text", "json"],
                          default="text")
    p_repair.set_defaults(func=cmd_repair)

    p_gate = sub.add_parser(
        "gate", help="pre-delivery gate: check, repair in place what "
                     "is repairable, and re-check (exit 0 only when "
                     "every file is clean)")
    p_gate.add_argument("--file", required=True, action="append",
                        help="log file path (repeatable)")
    p_gate.add_argument("--format", choices=["text", "json"],
                        default="text")
    p_gate.set_defaults(func=cmd_gate)
    return parser


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
