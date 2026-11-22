#!/usr/bin/env python3
"""Slot-coverage check for queue-ticker records: every scheduled ticker
slot must leave a record or a missed-fire marker.

The ticker fires every 30 minutes on the :04/:34 grid (design section 6;
record names evidence the anchor: 0004, 0134, 0234, ...). Issue #743 is
the live instance: the retro 2026-11-20 ruling confirmed 24 slots
recordless and left ticker-1934 pending adjudication, with no tool able
to say which slots a date is missing. A slot is covered when a file in
``_records_/<date>/queue-ticker/`` is either a record stating that slot
in its title, or a missed-fire marker naming it.

Coverage is read from the record title, never from the file name alone:
a late-starting pass names its record by its start time and states the
slot it served in its title, so ticker-1930 serves the 19:04 slot and
ticker-2037 serves the 20:34 slot. A marker is ``<slot>-missed-fire.md``
whose frontmatter carries ``status: missed-fire`` and the same slot.

A slot is past-window once the next slot starts (slot start + 30
minutes). The retro's prose ruling adjudicates a slot, but only a
record or a marker closes it for this check, so a check that passes
means the date is fully accounted for in files, not just in prose.

Three commands, standard library only:

  check --date YYYY-MM-DD [--root PATH] [--as-of DATETIME|HH:MM]
        [--format text|json]
      - report the recordless past-window slots. Exit 0 when every
        past-window slot is covered, 1 when recordless slots exist,
        2 when the root cannot be read, a record or marker is
        malformed, or an argument is bad.
  list --date YYYY-MM-DD [--root PATH] [--as-of ...] [--format text|json]
      - list every slot with its status and whether it is past-window.
        Exit 0, or 2 on the same errors as check.
  mark --date YYYY-MM-DD --slot HHMM [--reason TEXT] [--source TEXT]
       [--root PATH] [--as-of ...] [--created ISO]
      - write the missed-fire marker for a past-window slot. Refuses
        (exit 1) a slot a record already covers or a slot whose window
        has not ended; a marker that already exists is a no-op exit 0.
        Exit 2 when the slot is off the grid or an argument is bad.

``--root`` is a repository root (holds ``_records_/``), a ``_records_``
directory, or a single date directory. It defaults to the repository
this script lives in. ``--as-of`` defaults to now in America/Los_Angeles
(the records timezone); give it explicitly in fixtures so runs are
deterministic.

Usage:
  slot_coverage.py check --date 2026-11-20 [--as-of 2026-11-21T00:00]
  slot_coverage.py list --date 2026-11-20 --format json
  slot_coverage.py mark --date 2026-11-20 --slot 1934 --reason "Mac mini offline; no pass ran" --source "retro 2026-11-20 ruling"
"""

import argparse
import datetime
import json
import os
import re
import sys

TOOL_VERSION = "1.0.0"

SLOT_MINUTES = (4, 34)
WINDOW_MINUTES = 30
RECORD_SUFFIX = "-queue-run.md"
MARKER_SUFFIX = "-missed-fire.md"

_DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
_SLOT_RE = re.compile(r"^\d{4}$")
_TITLE_RE = re.compile(
    r"^# Queue ticker (\d{4}-\d{2}-\d{2}) (\d{2}):(\d{2}) to ",
    re.MULTILINE)


def _default_root():
    """Repository root, resolved from this script."""
    tools_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.dirname(tools_dir)


def _parse_date(text):
    """YYYY-MM-DD to a date, or None when malformed."""
    if not _DATE_RE.match(text or ""):
        return None
    try:
        return datetime.date.fromisoformat(text)
    except ValueError:
        return None


def _parse_as_of(text, date):
    """--as-of to a naive datetime in the records timezone.

    Accepts YYYY-MM-DDTHH:MM[:SS] or HH:MM on the --date day.
    Returns None when malformed.
    """
    if text is None:
        try:
            from zoneinfo import ZoneInfo
            now = datetime.datetime.now(ZoneInfo("America/Los_Angeles"))
        except Exception:
            now = datetime.datetime.now().astimezone()
        return now.replace(tzinfo=None)
    text = text.strip()
    match = re.match(r"^(\d{4})-(\d{2})-(\d{2})T(\d{2}):(\d{2})(?::(\d{2}))?$",
                     text)
    if match:
        try:
            return datetime.datetime(
                int(match.group(1)), int(match.group(2)),
                int(match.group(3)), int(match.group(4)),
                int(match.group(5)), int(match.group(6) or 0))
        except ValueError:
            return None
    match = re.match(r"^(\d{2}):(\d{2})(?::(\d{2}))?$", text)
    if match:
        try:
            return datetime.datetime(
                date.year, date.month, date.day, int(match.group(1)),
                int(match.group(2)), int(match.group(3) or 0))
        except ValueError:
            return None
    return None


def _resolve_day_dir(root, date):
    """Day directory for a date under --root, or (None, error).

    --root may be a repository root, a _records_ directory, or a single
    date directory. A missing day directory is not an error here: it
    means the date holds no records, which the caller reports as
    recordless slots.
    """
    if not os.path.isdir(root):
        return None, "root %s is not a directory" % root
    candidates = [
        os.path.join(root, "_records_", date.isoformat()),
        os.path.join(root, date.isoformat()),
        root if os.path.basename(os.path.normpath(root)) == date.isoformat()
        else None,
    ]
    for candidate in candidates:
        if candidate is None:
            continue
        if os.path.isdir(candidate):
            return candidate, None
    # No day directory anywhere: the first candidate is where it would
    # live, so the caller can treat it as an empty day.
    return candidates[0], None


def _grid_slots(date):
    """The 48 scheduled slots for a date, as HHMM strings."""
    return ["%02d%02d" % (hour, minute)
            for hour in range(24) for minute in SLOT_MINUTES]


def _slot_datetime(date, slot):
    """Naive datetime for a slot on a date."""
    return datetime.datetime(date.year, date.month, date.day,
                             int(slot[:2]), int(slot[2:]))


def _read_frontmatter(path):
    """Parse the --- frontmatter block of a marker file.

    Returns (fields, error): fields maps lowercased keys to values.
    """
    try:
        with open(path, "r", encoding="utf-8") as handle:
            text = handle.read()
    except OSError as exc:
        return None, "cannot read %s: %s" % (path, exc)
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None, "no frontmatter in %s" % path
    fields = {}
    for line in lines[1:]:
        if line.strip() == "---":
            return fields, None
        match = re.match(r"^([A-Za-z_]+):\s*(.*)$", line)
        if match:
            fields[match.group(1).lower()] = match.group(2).strip()
    return None, "unterminated frontmatter in %s" % path


def _scan_day(day_dir, date):
    """Coverage for one day directory.

    Returns (coverage, error): coverage maps slot HHMM to a dict with
    kind (record/marker), source file and title slot; error names the
    first malformed file, or None. A missing day directory or a missing
    queue-ticker/ subdirectory means no records: empty coverage.
    """
    coverage = {}
    foreign = []
    if day_dir is None or not os.path.isdir(day_dir):
        return coverage, None, foreign
    ticker_dir = os.path.join(day_dir, "queue-ticker")
    if not os.path.isdir(ticker_dir):
        return coverage, None, foreign
    for name in sorted(os.listdir(ticker_dir)):
        path = os.path.join(ticker_dir, name)
        if not os.path.isfile(path):
            continue
        if name.endswith(RECORD_SUFFIX):
            try:
                with open(path, "r", encoding="utf-8") as handle:
                    text = handle.read()
            except OSError as exc:
                return None, "cannot read %s: %s" % (path, exc), foreign
            match = _TITLE_RE.search(text)
            if match is None:
                return None, ("record %s has no '# Queue ticker "
                              "YYYY-MM-DD HH:MM to ' title" % path), foreign
            title_date = match.group(1)
            slot = match.group(2) + match.group(3)
            if title_date != date.isoformat():
                foreign.append({"file": name, "serves": title_date + " " + slot})
                continue
            if int(slot[2:]) not in SLOT_MINUTES:
                return None, ("record %s states off-grid slot %s"
                              % (path, slot)), foreign
            if slot in coverage:
                return None, ("slot %s covered twice: %s and %s"
                              % (slot, coverage[slot]["source"], name)), foreign
            coverage[slot] = {"kind": "record", "source": name, "slot": slot}
        elif name.endswith(MARKER_SUFFIX):
            slot = name[:-len(MARKER_SUFFIX)]
            if not _SLOT_RE.match(slot) or int(slot[2:]) not in SLOT_MINUTES:
                return None, "marker %s names off-grid slot %s" % (path, slot), foreign
            fields, error = _read_frontmatter(path)
            if error is not None:
                return None, error, foreign
            if fields.get("status") != "missed-fire":
                return None, ("marker %s has status %r, not missed-fire"
                              % (path, fields.get("status"))), foreign
            if fields.get("slot") != "%s %s:%s" % (date.isoformat(),
                                                   slot[:2], slot[2:]):
                return None, ("marker %s frontmatter slot %r does not match "
                              "its file slot %s"
                              % (path, fields.get("slot"), slot)), foreign
            if slot in coverage:
                return None, ("slot %s has both a %s and a marker %s"
                              % (slot, coverage[slot]["kind"], name)), foreign
            coverage[slot] = {"kind": "marker", "source": name, "slot": slot}
    return coverage, None, foreign


def _assess(date, as_of, coverage):
    """Per-slot status rows for a date."""
    rows = []
    for slot in _grid_slots(date):
        start = _slot_datetime(date, slot)
        past = as_of >= start + datetime.timedelta(minutes=WINDOW_MINUTES)
        entry = coverage.get(slot)
        rows.append({
            "slot": slot,
            "past_window": past,
            "status": "covered-by-%s" % entry["kind"] if entry else "recordless",
            "source": entry["source"] if entry else "",
        })
    return rows


def _print_check(date, as_of, rows, fmt):
    recordless = [r["slot"] for r in rows
                  if r["past_window"] and r["status"] == "recordless"]
    covered = sum(1 for r in rows if r["status"] != "recordless")
    if fmt == "json":
        print(json.dumps({
            "date": date.isoformat(),
            "as_of": as_of.strftime("%Y-%m-%dT%H:%M"),
            "grid_slots": len(rows),
            "covered": covered,
            "recordless_past_window": recordless,
            "slots": rows,
        }, sort_keys=True))
        return recordless
    print("slot_coverage: %s as of %s: %d covered, %d recordless past-window, "
          "%d future"
          % (date.isoformat(), as_of.strftime("%Y-%m-%dT%H:%M"), covered,
             len(recordless),
             sum(1 for r in rows if not r["past_window"])))
    if recordless:
        print("recordless: %s" % " ".join(recordless))
    return recordless


def _print_list(date, as_of, rows, fmt):
    if fmt == "json":
        print(json.dumps({
            "date": date.isoformat(),
            "as_of": as_of.strftime("%Y-%m-%dT%H:%M"),
            "slots": rows,
        }, sort_keys=True))
        return
    for row in rows:
        print("%s %s %s%s" % (
            row["slot"], row["status"],
            "past-window" if row["past_window"] else "future",
            (" " + row["source"]) if row["source"] else ""))


def _marker_text(date, slot, reason, source, created):
    """The missed-fire marker file for a slot."""
    return (
        "---\n"
        "title: Queue ticker %s %s:%s PT missed-fire - no record left\n"
        "created: %s\n"
        "status: missed-fire\n"
        "slot: %s %s:%s\n"
        "reason: %s\n"
        "grounded_in:\n"
        "  - source: %s\n"
        "---\n"
        "\n"
        "# Queue ticker %s %s:%s PT - missed-fire marker\n"
        "\n"
        "No record was left for the %s:%s scheduled slot. %s\n"
        "Written by _tools_/slot_coverage.py mark (issue #743).\n"
        % (date.isoformat(), slot[:2], slot[2:], created,
           date.isoformat(), slot[:2], slot[2:], reason, source,
           date.isoformat(), slot[:2], slot[2:],
           slot[:2], slot[2:], reason)
    )


def _cmd_check_list(args, command):
    date = _parse_date(args.date)
    if date is None:
        print("slot_coverage: --date must be YYYY-MM-DD, got %r" % args.date,
              file=sys.stderr)
        return 2
    as_of = _parse_as_of(getattr(args, "as_of", None), date)
    if as_of is None:
        print("slot_coverage: --as-of must be YYYY-MM-DDTHH:MM or HH:MM, "
              "got %r" % args.as_of, file=sys.stderr)
        return 2
    root = getattr(args, "root", None) or _default_root()
    day_dir, error = _resolve_day_dir(root, date)
    if error is not None:
        print("slot_coverage: %s" % error, file=sys.stderr)
        return 2
    coverage, error, foreign = _scan_day(day_dir, date)
    if error is not None:
        print("slot_coverage: %s" % error, file=sys.stderr)
        return 2
    rows = _assess(date, as_of, coverage)
    fmt = getattr(args, "format", "text")
    if command == "list":
        _print_list(date, as_of, rows, fmt)
        for item in foreign:
            print("foreign record: %s serves %s"
                  % (item["file"], item["serves"]), file=sys.stderr)
        return 0
    recordless = _print_check(date, as_of, rows, fmt)
    for item in foreign:
        print("foreign record: %s serves %s"
              % (item["file"], item["serves"]), file=sys.stderr)
    return 1 if recordless else 0


def _cmd_mark(args):
    date = _parse_date(args.date)
    if date is None:
        print("slot_coverage: --date must be YYYY-MM-DD, got %r" % args.date,
              file=sys.stderr)
        return 2
    slot = (args.slot or "").strip()
    if not _SLOT_RE.match(slot) or int(slot[2:]) not in SLOT_MINUTES:
        print("slot_coverage: --slot must be a grid slot (HH04 or HH34), "
              "got %r" % args.slot, file=sys.stderr)
        return 2
    as_of = _parse_as_of(getattr(args, "as_of", None), date)
    if as_of is None:
        print("slot_coverage: --as-of must be YYYY-MM-DDTHH:MM or HH:MM, "
              "got %r" % args.as_of, file=sys.stderr)
        return 2
    root = getattr(args, "root", None) or _default_root()
    day_dir, error = _resolve_day_dir(root, date)
    if error is not None:
        print("slot_coverage: %s" % error, file=sys.stderr)
        return 2
    coverage, error, _foreign = _scan_day(day_dir, date)
    if error is not None:
        print("slot_coverage: %s" % error, file=sys.stderr)
        return 2
    entry = coverage.get(slot)
    if entry is not None and entry["kind"] == "record":
        print("slot_coverage: slot %s already covered by record %s; "
              "refusing to mark" % (slot, entry["source"]), file=sys.stderr)
        return 1
    if entry is not None and entry["kind"] == "marker":
        print("slot %s already marked by %s; no change"
              % (slot, entry["source"]))
        return 0
    start = _slot_datetime(date, slot)
    if as_of < start + datetime.timedelta(minutes=WINDOW_MINUTES):
        print("slot_coverage: slot %s window has not ended as of %s; "
              "refusing to mark" % (slot, as_of.strftime("%Y-%m-%dT%H:%M")),
              file=sys.stderr)
        return 1
    ticker_dir = os.path.join(day_dir, "queue-ticker")
    try:
        os.makedirs(ticker_dir, exist_ok=True)
    except OSError as exc:
        print("slot_coverage: cannot create %s: %s" % (ticker_dir, exc),
              file=sys.stderr)
        return 2
    created = args.created or datetime.datetime.now(
        datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    reason = args.reason or "No record was left for this slot."
    source = args.source or "slot_coverage.py mark (issue #743)"
    marker_path = os.path.join(ticker_dir, slot + MARKER_SUFFIX)
    try:
        with open(marker_path, "x", encoding="utf-8") as handle:
            handle.write(_marker_text(date, slot, reason, source, created))
    except FileExistsError:
        print("slot %s already marked by %s; no change"
              % (slot, slot + MARKER_SUFFIX))
        return 0
    except OSError as exc:
        print("slot_coverage: cannot write %s: %s" % (marker_path, exc),
              file=sys.stderr)
        return 2
    print("marked slot %s: %s" % (slot, marker_path))
    return 0


def main(argv=None):
    # Shared options live on the top parser and on each subparser, so they
    # work before and after the subcommand. SUPPRESS keeps a subparser
    # default from overwriting a value already given before the
    # subcommand (argparse would otherwise reset it to None).
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--root", default=argparse.SUPPRESS,
                        help="repository root, _records_ dir or date dir "
                             "(default: this repository)")
    common.add_argument("--format", choices=("text", "json"),
                        default=argparse.SUPPRESS,
                        help="output shape (default text)")
    common.add_argument("--as-of", default=argparse.SUPPRESS,
                        help="cutoff as YYYY-MM-DDTHH:MM or HH:MM "
                             "(default: now, America/Los_Angeles)")
    parser = argparse.ArgumentParser(
        description="Slot-coverage check for queue-ticker records "
                    "(issue #743).",
        parents=[common])
    sub = parser.add_subparsers(dest="command", required=True)

    check = sub.add_parser("check", help="report recordless past-window "
                                         "slots", parents=[common])
    check.add_argument("--date", required=True, help="date as YYYY-MM-DD")
    sub.add_parser("list", help="list every slot with its status",
                   parents=[common]).add_argument(
                       "--date", required=True, help="date as YYYY-MM-DD")

    mark = sub.add_parser("mark", help="write a missed-fire marker",
                          parents=[common])
    mark.add_argument("--date", required=True, help="date as YYYY-MM-DD")
    mark.add_argument("--slot", required=True, help="slot as HHMM")
    mark.add_argument("--reason", default=None,
                      help="why no record was left")
    mark.add_argument("--source", default=None,
                      help="evidence the marker cites")
    mark.add_argument("--created", default=None,
                      help="created timestamp (default: now, UTC)")
    args = parser.parse_args(argv)

    if args.command in ("check", "list"):
        return _cmd_check_list(args, args.command)
    return _cmd_mark(args)


if __name__ == "__main__":
    sys.exit(main())
