#!/usr/bin/env python3
"""Records batch cadence - the mechanical gate and audit for policy 2.3.0.

Records pull requests merge only in batches, at the first integrator
pass at or after one of six daily batch points, in
America/Los_Angeles:

    03:00, 07:00, 11:00, 15:00, 19:00, 23:00

Policy 2.3.0 (merged as PR #116; issue #126, IMP-20261101-09)
states the batch points but no minute window: "first integrator
pass at or after" a point is a pass, not a timestamp window, so an
audit needs one defined. This tool defines it, explicitly, as the
60 minutes starting at each batch point, inclusive at the start
and exclusive at the end:

    [batch point, batch point + 60 minutes)

The 60 minutes is deliberate, not a guess dressed as policy. The
integrator passes every 15 minutes, so the first pass after a
point lands well inside the hour even with pass jitter and merge
time, while a merge in the remaining three hours of a four-hour
block is still flagged. The window is a single constant
(BATCH_WINDOW_MINUTES) and a --window-minutes override, so the
integrator or the retro can tighten it without a code change;
any change to the constant must be stated in the run record that
uses it, because it changes what counts as a violation.

Two commands, both standard library only:

  due   - the integrator's gate. Reports whether a records batch
          merge is currently due, which batch window applies,
          and the next batch point. Exit 0 when due, 1 when not
          due, 2 on a usage or input error. The integrator gates
          on the exit code instead of judging the clock itself.
          With --merges FILE (the same JSON shape as `audit`
          takes), due is merge-aware (issue #335): a records
          merge already inside the current window, at or before
          the checked moment, makes the answer not due, so only
          the first pass at or after a batch point merges. A
          merge after the checked moment never blocks it, so
          --at replays still answer as of that moment. Without
          --merges, due stays clock-only, as in 1.0.0.
  audit - the retro's audit input. Reads a JSON list of records
          merges (merge timestamps as recorded by gh) and lists
          the ones that fell outside any batch window. Exit 0 on
          a successful audit even when violations are found -
          a violation is a finding, not a tool failure - and 2
          on an unreadable or malformed input file.

A merge timestamp exactly at a batch point is compliant; exactly
at the end of its window is not, because the window is half-open
and the next window starts three hours later. Timestamps with an
offset are authoritative; naive timestamps are read as
America/Los_Angeles wall time. The --at override exists so the
integrator and the retro can replay a decision for a past time
without waiting for the clock.

The merges file for `audit` is a JSON list, or an object with a
"merges" list. Each entry carries a PR number under "number"
("pr" or "pr_number" are accepted) and a merge timestamp under
"merged_at" ("merged" or "timestamp" are accepted). An entry
that cannot be parsed is an input error, never silently skipped:
the audit reports which entry failed and exits 2, so a bad
extract cannot masquerade as a clean day.

Usage:
  records_batch.py due [--at ISO] [--format text|json]
                       [--window-minutes N] [--merges FILE]
  records_batch.py audit --merges FILE [--format text|json]
                         [--window-minutes N]
"""

import argparse
import json
import sys
from datetime import datetime, time, timedelta, timezone
from zoneinfo import ZoneInfo

LOCAL_TZ = ZoneInfo("America/Los_Angeles")
BATCH_HOURS = (3, 7, 11, 15, 19, 23)
BATCH_WINDOW_MINUTES = 60
TOOL_VERSION = "1.1.0"


def parse_time(text):
    """Parse an ISO timestamp; naive input is America/Los_Angeles."""
    if not isinstance(text, str) or not text.strip():
        raise ValueError("timestamp must be a non-empty string")
    raw = text.strip()
    try:
        parsed = datetime.fromisoformat(raw.replace("Z", "+00:00"))
    except ValueError:
        raise ValueError(f"not an ISO timestamp: {raw!r}")
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=LOCAL_TZ)
    return parsed.astimezone(LOCAL_TZ)


def batch_points_for_date(day):
    """The six batch points on one local date, as aware datetimes."""
    return [datetime.combine(day, time(hour=h), tzinfo=LOCAL_TZ)
            for h in BATCH_HOURS]


def window_for(moment, window_minutes=BATCH_WINDOW_MINUTES):
    """The batch window containing `moment`, or None.

    `moment` is converted to America/Los_Angeles first. A window
    is identified by its start; the returned pair is
    (window_start, window_end), half-open.
    """
    local = moment.astimezone(LOCAL_TZ)
    span = timedelta(minutes=window_minutes)
    for start in batch_points_for_date(local.date()):
        if start <= local < start + span:
            return (start, start + span)
    return None


def next_batch_point(moment):
    """The next batch point strictly after `moment`.

    A moment exactly at a batch point belongs to that point's
    window, so the next point is the following one.
    """
    local = moment.astimezone(LOCAL_TZ)
    for day_offset in (0, 1):
        day = local.date() + timedelta(days=day_offset)
        for point in batch_points_for_date(day):
            if point > local:
                return point
    raise AssertionError("unreachable: tomorrow always has points")


def first_merge_in_window(merges, window, moment):
    """The earliest merge inside `window` at or before `moment`.

    `merges` is a list of {"number", "merged_at"} with merged_at
    an aware datetime (the shape load_merges_file returns).
    Returns the merge dict, or None. A merge after the checked
    moment never counts: at that moment no merge had happened
    yet, so the pass asking was still the first. A merge in an
    earlier window never counts either: each window gets its
    own batch.
    """
    if not merges or window is None:
        return None
    start, _end = window
    in_window = [entry for entry in merges
                 if start <= entry["merged_at"] <= moment]
    if not in_window:
        return None
    in_window.sort(key=lambda item: (item["merged_at"],
                                     str(item["number"])))
    return in_window[0]


def status_for(moment, window_minutes=BATCH_WINDOW_MINUTES,
               merges=None, merges_file=None):
    """The due status of one moment, as a JSON-ready dict.

    With `merges` supplied (the loaded --merges file), due is
    merge-aware: a merge already inside the current window
    makes the answer not due, and `already_merged` names it.
    Without merges the status is clock-only, as in 1.0.0.
    """
    local = moment.astimezone(LOCAL_TZ)
    window = window_for(local, window_minutes)
    following = next_batch_point(local)
    already = first_merge_in_window(merges, window, local)
    status = {
        "tool": "records_batch",
        "version": TOOL_VERSION,
        "at": local.isoformat(),
        "timezone": "America/Los_Angeles",
        "batch_hours": list(BATCH_HOURS),
        "window_minutes": window_minutes,
        "due": window is not None and already is None,
        "next_batch_point": following.isoformat(),
        "minutes_to_next_batch_point": int(
            (following - local).total_seconds() // 60),
        "merges_file": merges_file,
        "merges_checked": len(merges) if merges is not None else 0,
        "already_merged": None,
    }
    if window is not None:
        status["window_start"] = window[0].isoformat()
        status["window_end"] = window[1].isoformat()
        status["minutes_left_in_window"] = int(
            (window[1] - local).total_seconds() // 60)
    else:
        status["window_start"] = None
        status["window_end"] = None
        status["minutes_left_in_window"] = None
    if already is not None:
        status["already_merged"] = {
            "number": already["number"],
            "merged_at": already["merged_at"].isoformat(),
            "window_start": window[0].isoformat(),
            "window_end": window[1].isoformat(),
        }
    return status


def _entry_number(entry, index):
    for key in ("number", "pr", "pr_number"):
        if key in entry and entry[key] is not None:
            return entry[key]
    raise ValueError(f"merges entry {index} carries no PR number")


def _entry_merged_at(entry, index):
    for key in ("merged_at", "merged", "timestamp"):
        if key in entry and entry[key] is not None:
            return entry[key]
    raise ValueError(f"merges entry {index} carries no merge timestamp")


def load_merges_file(path):
    """Load and validate a merges file; errors name the bad entry."""
    try:
        with open(path, encoding="utf-8") as fh:
            payload = json.load(fh)
    except OSError as exc:
        raise ValueError(f"cannot read merges file {path!r}: {exc}")
    except json.JSONDecodeError as exc:
        raise ValueError(f"merges file {path!r} is not valid JSON: {exc}")
    if isinstance(payload, dict):
        payload = payload.get("merges")
    if not isinstance(payload, list):
        raise ValueError(
            f"merges file {path!r} must hold a JSON list, or an "
            "object with a \"merges\" list")
    merges = []
    for index, entry in enumerate(payload):
        if not isinstance(entry, dict):
            raise ValueError(f"merges entry {index} is not an object")
        number = _entry_number(entry, index)
        raw = _entry_merged_at(entry, index)
        try:
            merged = parse_time(raw)
        except ValueError as exc:
            raise ValueError(f"merges entry {index} (PR {number}): {exc}")
        merges.append({"number": number, "merged_at": merged})
    return merges


def audit_merges(merges, window_minutes=BATCH_WINDOW_MINUTES):
    """Classify merges against the batch windows.

    `merges` is a list of {"number", "merged_at"} with merged_at a
    string or an aware datetime. The result is JSON-ready: every
    merge is classified, violations carry their PR number and
    timestamp, and a clean audit says so explicitly.
    """
    checked = []
    violations = []
    for entry in merges:
        merged = entry["merged_at"]
        if isinstance(merged, str):
            merged = parse_time(merged)
        local = merged.astimezone(LOCAL_TZ)
        window = window_for(local, window_minutes)
        record = {
            "number": entry["number"],
            "merged_at": local.isoformat(),
            "compliant": window is not None,
            "window_start": window[0].isoformat() if window else None,
            "window_end": window[1].isoformat() if window else None,
        }
        checked.append(record)
        if window is None:
            violations.append(record)
    checked.sort(key=lambda item: (item["merged_at"], str(item["number"])))
    violations.sort(key=lambda item: (item["merged_at"],
                                       str(item["number"])))
    return {
        "tool": "records_batch",
        "version": TOOL_VERSION,
        "audited": True,
        "batch_hours": list(BATCH_HOURS),
        "window_minutes": window_minutes,
        "merges_checked": len(checked),
        "compliant_count": len(checked) - len(violations),
        "violation_count": len(violations),
        "violation_numbers": [item["number"] for item in violations],
        "violations": violations,
        "merges": checked,
        "clean": not violations,
    }


def _render_due(status, fmt):
    if fmt == "json":
        print(json.dumps(status, indent=2, sort_keys=True,
                         ensure_ascii=False))
        return
    already = status.get("already_merged")
    if already is not None:
        print(f"due: no - PR #{already['number']} already merged "
              f"{already['merged_at']} in this batch window "
              f"({already['window_start']} to "
              f"{already['window_end']} America/Los_Angeles)")
    elif status["due"]:
        print(f"due: yes - batch window {status['window_start']} to "
              f"{status['window_end']} America/Los_Angeles "
              f"({status['minutes_left_in_window']} minutes left)")
    else:
        print("due: no - outside every batch window")
    print(f"next batch point: {status['next_batch_point']} "
          f"America/Los_Angeles "
          f"({status['minutes_to_next_batch_point']} minutes away)")


def _render_audit(audit, fmt):
    if fmt == "json":
        print(json.dumps(audit, indent=2, sort_keys=True,
                         ensure_ascii=False))
        return
    print(f"records merges checked: {audit['merges_checked']}; "
          f"compliant: {audit['compliant_count']}; "
          f"violations: {audit['violation_count']}")
    if audit["clean"]:
        print("Records batch compliance: clean - 0 off-batch "
              f"records merges out of {audit['merges_checked']} "
              "checked")
    else:
        numbers = ", ".join(f"#{n}" for n in audit["violation_numbers"])
        print(f"Records batch compliance: {audit['violation_count']} "
              f"off-batch merges - {numbers}")
        for item in audit["violations"]:
            print(f"- PR #{item['number']} merged "
                  f"{item['merged_at']} America/Los_Angeles - "
                  "outside any batch window")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    due = sub.add_parser("due", help="report whether a batch is due")
    due.add_argument("--at", default="",
                     help="ISO timestamp to check (default: now)")
    due.add_argument("--format", choices=["text", "json"],
                     default="text")
    due.add_argument("--window-minutes", type=int,
                     default=BATCH_WINDOW_MINUTES)
    due.add_argument("--merges", default="",
                     help="JSON merges file (same shape as audit) - "
                     "when given, due is merge-aware: a merge "
                     "already inside the current window makes the "
                     "answer not due (issue #335)")
    audit = sub.add_parser("audit", help="audit merges against windows")
    audit.add_argument("--merges", required=True,
                       help="JSON merges file (see module docstring)")
    audit.add_argument("--format", choices=["text", "json"],
                       default="text")
    audit.add_argument("--window-minutes", type=int,
                       default=BATCH_WINDOW_MINUTES)
    args = parser.parse_args(argv)
    if args.window_minutes < 1 or args.window_minutes > 240:
        parser.error("--window-minutes must be between 1 and 240")
    if args.command == "due":
        try:
            moment = parse_time(args.at) if args.at else \
                datetime.now(LOCAL_TZ)
            merges = load_merges_file(args.merges) \
                if args.merges else None
        except ValueError as exc:
            print(f"error: {exc}", file=sys.stderr)
            return 2
        status = status_for(moment, args.window_minutes,
                            merges=merges,
                            merges_file=args.merges or None)
        _render_due(status, args.format)
        return 0 if status["due"] else 1
    try:
        merges = load_merges_file(args.merges)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    audit_result = audit_merges(merges, args.window_minutes)
    _render_audit(audit_result, args.format)
    return 0


if __name__ == "__main__":
    sys.exit(main())
