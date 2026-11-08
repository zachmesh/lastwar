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

Three commands, standard library only:

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
           changes no content. Dry-run by default: report what
           would split. ``--write`` applies it, after verifying
           in memory that the multiset of parsed JSON objects
           is unchanged, and re-reads the file afterwards to
           confirm every line parses. A line that is not a
           run of complete JSON objects is unrepairable: the
           tool refuses, reports it and exits 2, and writes
           nothing. Exit 0 when the file is clean or the
           repair was applied; a second repair run is a no-op.

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
"""

import argparse
import json
import sys

try:
    import fcntl
except ImportError:  # pragma: no cover - non-Unix platforms only
    fcntl = None

TOOL_VERSION = "1.0.0"

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
    splits = []       # (line number, object count, preview)
    unrepairable = []  # (line number, error, preview)
    new_lines = []
    before_objects = []
    for number, line in enumerate(lines, 1):
        objects = _parse_line_objects(line)
        if objects is None:
            if not line.strip():
                unrepairable.append((number, "blank line", ""))
                new_lines.append(line)
                continue
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
    if unrepairable:
        for number, error, preview in unrepairable:
            print(f"error: line {number}: {error}"
                  + (f" :: {preview}" if preview else ""),
                  file=sys.stderr)
        print(f"error: {len(unrepairable)} line(s) cannot be repaired; "
              "nothing was written", file=sys.stderr)
        return 2

    after_objects = []
    for line in new_lines:
        after_objects.extend(_parse_line_objects(line))
    before_key = sorted(json.dumps(o, sort_keys=True, ensure_ascii=False)
                        for o in before_objects)
    after_key = sorted(json.dumps(o, sort_keys=True, ensure_ascii=False)
                       for o in after_objects)
    if before_key != after_key:
        print("error: repair would change the logged objects; "
              "nothing was written", file=sys.stderr)
        return 2

    text = [f"{args.file}: {len(splits)} line(s) would split into "
            f"{sum(c for _n, c, _p in splits)} objects"
            if splits else
            f"{args.file}: clean, nothing to repair"]
    for number, count, preview in splits:
        text.append(f"  line {number}: {count} objects :: {preview}")
    result = {
        "version": TOOL_VERSION,
        "file": args.file,
        "lines": len(lines),
        "split_lines": len(splits),
        "splits": [{"line": n, "objects": c, "preview": p}
                   for n, c, p in splits],
        "objects_before": len(before_objects),
        "objects_after": len(after_objects),
        "written": False,
        "text": text,
    }
    if not args.write:
        _render(result, args.format)
        return 0
    if not splits:
        _render(result, args.format)
        return 0
    new_text = "\n".join(new_lines)
    if ends_with_newline:
        new_text += "\n"
    import os
    try:
        fd = os.open(args.file, os.O_RDWR, 0o644)
    except OSError as exc:
        print(f"error: cannot open {args.file}: {exc}", file=sys.stderr)
        return 2
    try:
        _lock_exclusive(fd)
        os.lseek(fd, 0, os.SEEK_SET)
        os.write(fd, new_text.encode("utf-8"))
        os.ftruncate(fd, len(new_text.encode("utf-8")))
    except OSError as exc:
        print(f"error: cannot write {args.file}: {exc}", file=sys.stderr)
        return 2
    finally:
        _unlock(fd)
        os.close(fd)
    try:
        check_lines, _ends = _read_lines(args.file)
    except (OSError, ValueError) as exc:
        print(f"error: cannot re-read {args.file} after repair: {exc}",
              file=sys.stderr)
        return 2
    for line in check_lines:
        if not line.strip():
            print("error: repair left a blank line; file needs "
                  "manual inspection", file=sys.stderr)
            return 2
        try:
            json.loads(line)
        except json.JSONDecodeError as exc:
            print(f"error: repair left an unparseable line: {exc}",
                  file=sys.stderr)
            return 2
    result["written"] = True
    result["text"] = [f"{args.file}: repaired {len(splits)} line(s) into "
                      f"{sum(c for _n, c, _p in splits)} objects; "
                      f"{len(check_lines)} lines now, all valid JSON"]
    _render(result, args.format)
    return 0


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
    return parser


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
