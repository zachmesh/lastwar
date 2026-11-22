#!/usr/bin/env python3
"""Missed-VIP-days count from the queue pool: one auditable number.

The ticker states an "Nth consecutive missed VIP day" count in its run
records, but the count was kept by hand and the two chains disagreed:
issue #742 - the ticker counted seven missed days (Nov 14 to Nov 20)
while the knowledge-organizer chain counted eight (Nov 13 to Nov 20),
and the Nov 20 retro ruled eight. The Nov 13 unit is the tell: it
closed expired with finished_at 2026-11-15T02:22:15Z, a full day after
its own reset day, so any count keyed on finished dates drops Nov 13
and lands on seven.

This tool counts from the pool instead of from memory. A missed VIP
day is a day whose daily VIP unit - the 1800 slot, one per reset day -
closed without the loop claiming anything:

  - result.status expired or failed: missed;
  - result.status done or partial with claimed_count 0: missed (the
    Nov 20 case: the unit closed DONE because both items were already
    claimed before it ran, so the loop itself claimed nothing);
  - result.status done or partial with claimed_count > 0: claimed;
  - no outcome file for the day, or a marker-only done/partial whose
    claimed_count is unseen: unknown, never counted, always flagged.

The day is keyed on the date embedded in the unit id
(vip-YYYY-MM-DD-HHMM), never on finished_at, so a late reap cannot
move a miss to another day. Only the 1800 slot defines a day: a
pre-reset fix-up unit (vip-2026-11-14-1630, expired) is listed as an
extra and can never double-count its day. Sources are the done unit
files in ``_queue_/done/`` and the completion markers in
``_queue_/completed/`` (live-only, never committed; a marker carries
status and finished_at but no claimed_count, so a marker-only
done/partial is unknown). When several outcome files name the same
day and slot, the latest finished_at wins and the conflict is
reported; the day is still counted once.

Two commands, standard library only:

  count [--from YYYY-MM-DD] [--to YYYY-MM-DD] [--root PATH]
        [--format text|json]
      - report the missed days in the window, the claimed days, the
        unknown days, and the consecutive missed run ending at --to.
        --from defaults to the earliest day with an 1800 outcome in
        the pool; --to defaults to the latest such day. Exit 0 when
        every day in the window is determined, 1 when unknown days
        are present in the window (the count may be incomplete), 2
        when the root cannot be read, a unit file is malformed, or
        an argument is bad.
  list [--from YYYY-MM-DD] [--to YYYY-MM-DD] [--root PATH]
       [--format text|json]
      - list every day in the window with its unit, outcome and
        verdict. Same exit codes as count.

``--root`` is a repository root (holds ``_queue_/``), a ``_queue_``
directory, or a pool root holding ``done/`` and ``completed/``
directly. It defaults to the repository this script lives in. The
tool never writes: it is read-only, so re-runs are idempotent.

Usage:
  vip_missed.py count --to 2026-11-20
  vip_missed.py count --from 2026-11-13 --to 2026-11-20 --format json
  vip_missed.py list --from 2026-11-13 --to 2026-11-21
"""

import argparse
import datetime
import json
import os
import re
import sys

TOOL_VERSION = "1.0.0"

DAILY_SLOT = "1800"
_MISSED_STATUSES = ("expired", "failed")
_CLAIMED_STATUSES = ("done", "partial")
_UNIT_RE = re.compile(r"^vip-(\d{4})-(\d{2})-(\d{2})-(\d{4})\.md$")
_DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def _default_root():
    """Repository root, resolved from this script."""
    tools_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.dirname(tools_dir)


def _resolve_queue(root):
    """_queue_ directory under root, or root itself when it is one.

    Accepts a repository root (holds _queue_/), a _queue_ directory,
    or a pool root holding done/ and completed/ directly.
    """
    if not root:
        return None
    if os.path.isdir(os.path.join(root, "done")):
        return root
    queue = os.path.join(root, "_queue_")
    if os.path.isdir(os.path.join(queue, "done")):
        return queue
    return None


def _parse_date(text):
    """YYYY-MM-DD to a date, or None when malformed."""
    if not _DATE_RE.match(text or ""):
        return None
    try:
        return datetime.date.fromisoformat(text)
    except ValueError:
        return None


def _parse_frontmatter(text):
    """Frontmatter of a unit file or marker as a flat dict.

    Reads the ``---``-delimited block at the top of the file. Top
    level ``key: value`` lines become entries; the ``result:`` block
    contributes its two-space-indented fields under the "result"
    key. Deeper nesting (the ``stats:`` block) is ignored. Returns
    None when the file carries no parseable frontmatter.
    """
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None
    fields = {}
    result = None
    closed = False
    for line in lines[1:]:
        stripped = line.strip()
        if stripped == "---":
            closed = True
            break
        if not stripped:
            continue
        if line.startswith("  ") and result is not None:
            if line.startswith("    "):
                continue
            key, sep, value = stripped.partition(":")
            if sep:
                result[key.strip()] = value.strip()
            continue
        if line[0].isspace():
            continue
        key, sep, value = stripped.partition(":")
        if not sep:
            return None
        key = key.strip()
        if key == "result":
            result = {}
            fields["result"] = result
        else:
            result = None
            fields[key] = value.strip()
    if not closed:
        return None
    return fields


def _parse_int(text):
    """A claimed_count value to int, or None when absent/unparseable."""
    if text is None or text == "":
        return None
    try:
        return int(str(text).strip())
    except (TypeError, ValueError):
        return None


def _load_outcomes(queue_dir):
    """Outcome records for VIP units in done/ and completed/.

    Returns (outcomes, errors): outcomes is a list of dicts with
    unit, day, slot, source, status, claimed_count and finished_at;
    errors names every file that could not be read or parsed. A done
    file without a result.status is malformed: an outcome the tool
    cannot classify must fail loudly instead of silently dropping
    a day.
    """
    outcomes = []
    errors = []
    for subdir, source in (("done", "done"), ("completed", "marker")):
        folder = os.path.join(queue_dir, subdir)
        if not os.path.isdir(folder):
            continue
        for name in sorted(os.listdir(folder)):
            match = _UNIT_RE.match(name)
            if not match:
                continue
            path = os.path.join(folder, name)
            try:
                with open(path, encoding="utf-8") as handle:
                    text = handle.read()
            except OSError as exc:
                errors.append("%s: unreadable (%s)" % (path, exc))
                continue
            fields = _parse_frontmatter(text)
            if fields is None:
                errors.append("%s: no parseable frontmatter" % path)
                continue
            regular = fields.get("regular")
            if regular not in (None, "", "vip"):
                continue
            unit = fields.get("unit") or name[:-3]
            if unit != name[:-3]:
                errors.append(
                    "%s: frontmatter unit %r names a different unit"
                    % (path, unit))
                continue
            if source == "done":
                result = fields.get("result")
                if not isinstance(result, dict):
                    errors.append("%s: no result block" % path)
                    continue
                status = result.get("status") or ""
                claimed = _parse_int(result.get("claimed_count"))
                finished = result.get("finished_at") or ""
            else:
                status = fields.get("status") or ""
                claimed = None
                finished = fields.get("finished_at") or ""
            if not status:
                errors.append("%s: no status" % path)
                continue
            try:
                day = datetime.date(
                    int(match.group(1)), int(match.group(2)),
                    int(match.group(3)))
            except ValueError:
                errors.append("%s: bad date in unit id" % path)
                continue
            outcomes.append({
                "unit": unit,
                "day": day,
                "slot": match.group(4),
                "source": source,
                "status": status,
                "claimed_count": claimed,
                "finished_at": finished,
                "path": path,
            })
    return outcomes, errors


def _classify(day_outcome):
    """One day's verdict from its 1800 outcome.

    Returns (verdict, note): verdict is missed, claimed or unknown.
    """
    if day_outcome is None:
        return "unknown", "no 1800 outcome file in the pool"
    status = day_outcome["status"]
    if status in _MISSED_STATUSES:
        return "missed", "1800 unit %s" % status
    if status in _CLAIMED_STATUSES:
        claimed = day_outcome["claimed_count"]
        if claimed is None:
            return ("unknown",
                    "1800 unit %s, claimed_count unseen "
                    "(marker only)" % status)
        if claimed == 0:
            return ("missed",
                    "1800 unit %s with claimed_count 0 - the loop "
                    "claimed nothing" % status)
        return "claimed", "1800 unit %s, claimed_count %d" % (
            status, claimed)
    return "unknown", "1800 unit status %r unclassified" % status


def _build_days(outcomes, start, end):
    """Per-day rows for the window, with extras and conflicts."""
    by_day = {}
    for outcome in outcomes:
        by_day.setdefault(outcome["day"], []).append(outcome)
    extras = []
    conflicts = []
    days = []
    day = start
    one = datetime.timedelta(days=1)
    while day <= end:
        rows = by_day.get(day, [])
        daily = [row for row in rows if row["slot"] == DAILY_SLOT]
        extras.extend(row for row in rows if row["slot"] != DAILY_SLOT)
        if len(daily) > 1:
            daily.sort(key=lambda row: row["finished_at"] or "")
            conflicts.append({
                "day": day.isoformat(),
                "units": [row["unit"] for row in daily],
                "kept": daily[-1]["unit"],
            })
        chosen = daily[-1] if daily else None
        verdict, note = _classify(chosen)
        days.append({
            "day": day.isoformat(),
            "unit": chosen["unit"] if chosen else None,
            "status": chosen["status"] if chosen else None,
            "claimed_count": (chosen["claimed_count"]
                              if chosen else None),
            "finished_at": chosen["finished_at"] if chosen else None,
            "source": chosen["source"] if chosen else None,
            "verdict": verdict,
            "note": note,
        })
        day += one
    return days, extras, conflicts


def _consecutive_run(days, end):
    """Consecutive missed run ending at end (inclusive).

    Walks back from end while days are missed; stops at the first
    claimed or unknown day. Returns (length, start, end) with start
    None when the run is empty.
    """
    by_day = {row["day"]: row for row in days}
    length = 0
    cursor = end
    one = datetime.timedelta(days=1)
    while True:
        row = by_day.get(cursor.isoformat())
        if row is None or row["verdict"] != "missed":
            break
        length += 1
        cursor -= one
    if length == 0:
        return 0, None, None
    return length, (end - datetime.timedelta(days=length - 1)), end


def _analyse(queue_dir, start, end):
    """Load the pool and build the window report.

    Returns (report, errors): report is None when the pool cannot
    be loaded at all.
    """
    outcomes, errors = _load_outcomes(queue_dir)
    if errors:
        return None, errors
    daily_days = sorted({row["day"] for row in outcomes
                         if row["slot"] == DAILY_SLOT})
    if start is None:
        start = daily_days[0] if daily_days else None
    if end is None:
        end = daily_days[-1] if daily_days else None
    if start is None or end is None:
        return None, ["no VIP 1800 outcomes in the pool; pass "
                      "--from/--to explicitly"]
    if start > end:
        return None, ["--from %s is after --to %s" % (
            start.isoformat(), end.isoformat())]
    days, extras, conflicts = _build_days(outcomes, start, end)
    length, run_start, run_end = _consecutive_run(days, end)
    unknown = [row["day"] for row in days if row["verdict"] == "unknown"]
    missed = [row["day"] for row in days if row["verdict"] == "missed"]
    report = {
        "tool": "vip_missed.py",
        "version": TOOL_VERSION,
        "window": {
            "from": start.isoformat(),
            "to": end.isoformat(),
        },
        "days": days,
        "extras": [{
            "unit": row["unit"],
            "day": row["day"].isoformat(),
            "slot": row["slot"],
            "status": row["status"],
            "source": row["source"],
        } for row in extras],
        "conflicts": conflicts,
        "missed_days": missed,
        "missed_count": len(missed),
        "unknown_days": unknown,
        "consecutive": {
            "ending": end.isoformat(),
            "length": length,
            "start": run_start.isoformat() if run_start else None,
            "end": run_end.isoformat() if run_end else None,
        },
    }
    return report, []


def _format_text(report):
    """Human-readable report: one row per day, then the summary."""
    lines = []
    for row in report["days"]:
        unit = row["unit"] or "-"
        status = row["status"] or "-"
        claimed = row["claimed_count"]
        claimed_text = "-" if claimed is None else str(claimed)
        finished = row["finished_at"] or "-"
        lines.append("%s %-24s %-8s claimed=%-3s %-9s finished=%s (%s)"
                     % (row["day"], unit, status, claimed_text,
                        row["verdict"], finished, row["note"]))
    for extra in report["extras"]:
        lines.append("extra: %s (%s, %s, %s)"
                     % (extra["unit"], extra["day"], extra["status"],
                        extra["source"]))
    for conflict in report["conflicts"]:
        lines.append("conflict: %s has %s, kept %s"
                     % (conflict["day"],
                        ", ".join(conflict["units"]), conflict["kept"]))
    run = report["consecutive"]
    if run["length"]:
        lines.append("consecutive missed run ending %s: %d days "
                     "(%s to %s)"
                     % (run["ending"], run["length"], run["start"],
                        run["end"]))
    else:
        lines.append("consecutive missed run ending %s: 0 days"
                     % run["ending"])
    lines.append("missed: %d (%s)"
                 % (report["missed_count"],
                    ", ".join(report["missed_days"]) or "none"))
    lines.append("unknown: %d (%s)"
                 % (len(report["unknown_days"]),
                    ", ".join(report["unknown_days"]) or "none"))
    return "\n".join(lines) + "\n"


def _run_command(args):
    queue_dir = _resolve_queue(args.root)
    if queue_dir is None:
        print("vip_missed: cannot find _queue_/done under %s"
              % args.root, file=sys.stderr)
        return 2
    start = _parse_date(args.from_date)
    if args.from_date is not None and start is None:
        print("vip_missed: bad --from date %r" % args.from_date,
              file=sys.stderr)
        return 2
    end = _parse_date(args.to_date)
    if args.to_date is not None and end is None:
        print("vip_missed: bad --to date %r" % args.to_date,
              file=sys.stderr)
        return 2
    report, errors = _analyse(queue_dir, start, end)
    if report is None:
        for error in errors:
            print("vip_missed: %s" % error, file=sys.stderr)
        return 2
    if args.format == "json":
        print(json.dumps(report, indent=1, ensure_ascii=False))
    elif args.command == "list":
        for row in report["days"]:
            print("%s %-24s %-8s %s"
                  % (row["day"], row["unit"] or "-",
                     row["status"] or "-", row["verdict"]))
        for extra in report["extras"]:
            print("extra: %s (%s, %s)"
                  % (extra["unit"], extra["day"], extra["status"]))
    else:
        sys.stdout.write(_format_text(report))
    if report["unknown_days"]:
        return 1
    return 0


def main(argv=None):
    parser = argparse.ArgumentParser(
        prog="vip_missed.py",
        description="Count missed VIP days from the queue pool.")
    parser.add_argument("--version", action="version",
                        version="vip_missed.py %s" % TOOL_VERSION)
    sub = parser.add_subparsers(dest="command", required=True)
    for name, help_text in (
            ("count", "missed days, unknown days and the consecutive "
                      "missed run ending at --to"),
            ("list", "one row per day in the window")):
        cmd = sub.add_parser(name, help=help_text)
        cmd.add_argument("--from", dest="from_date", default=None,
                         help="window start YYYY-MM-DD (default: "
                              "earliest day with an 1800 outcome)")
        cmd.add_argument("--to", dest="to_date", default=None,
                         help="window end YYYY-MM-DD (default: latest "
                              "day with an 1800 outcome)")
        cmd.add_argument("--root", default=_default_root(),
                         help="repository root, _queue_ directory or "
                              "pool root (default: this repository)")
        cmd.add_argument("--format", choices=("text", "json"),
                         default="text")
    args = parser.parse_args(argv)
    return _run_command(args)


if __name__ == "__main__":
    sys.exit(main())
