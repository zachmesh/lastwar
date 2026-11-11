#!/usr/bin/env python3
"""Regulars tracker for the Last War every-4-hours routine rounds.

Keeps one state file per local date under _tools_/state/, so any run can
answer two questions fast: what regulars exist (_tools_/regulars.json),
and which of them are still expected (not yet done) in this cycle.

Usage:
  regulars.py list [--date YYYY-MM-DD]   show every regular + status
  regulars.py todo [--date YYYY-MM-DD]   show only what is still due
  regulars.py done <id> [--note TEXT]    mark a regular done (now)
  regulars.py skip <id> [--note TEXT]    mark a regular skipped (why)
  regulars.py reset [--date YYYY-MM-DD]  clear a day state

The routine is every four hours, not daily (owner rule, 2026-10-26),
and since later that day it is split into 3 segment schedules
in the same hour, 27 minutes apart (owner design): segment 1
fires at :03, segment 2 at :30, segment 3 at :57, each repeating
every 4 hours. An every-run regular
counts as done only for its own segment's current 4 hour cycle; at
the segment's next cycle boundary it becomes due again, whether it
was marked done or skipped. A daily-reset regular (VIP, reset at the absolute 02:00 UTC
daily boundary, 18:00 PST / 19:00 PDT) counts as done only if it
was marked after the most recent reset boundary; before the reset
it stays done, after the reset it becomes due again automatically.
A regular carrying reset_utc uses that absolute UTC boundary, so
the local wall time of the reset shifts with daylight saving
(issue #247, following the duel.py fix in issue #242); a regular
without reset_utc keeps the old reset_local wall-time boundary.
A weekly-thu regular is only due on Thursdays.
Use --segment N with list/todo to see one segment's regulars.
Done/skip stamps are aware America/Los_Angeles times (issue #407);
older naive stamps are still read as local wall time.
Tracker state is live pool state (issue #598): when this copy runs
from a linked worktree, done/skip marks - and todo/list reads -
resolve to the main checkout's _tools_/state, so a mark made
during a delivery-worktree pass is visible to the next tick
instead of stranding on the records branch.
"""
import argparse, json, os, subprocess, sys
from datetime import datetime, date, time as dtime, timedelta, timezone
from zoneinfo import ZoneInfo

ROOT = os.path.dirname(os.path.abspath(__file__))
DEFS = os.path.join(ROOT, "regulars.json")
STATE_DIR = os.path.join(ROOT, "state")

def live_state_dir():
    """State directory of the main checkout when this copy lives in
    a linked worktree.

    Tracker state is live pool state like the queue: a `done` mark
    written into a delivery worktree's state file reaches only the
    records branch, and the live tracker keeps reading the old
    stamp until a records batch merges it back (issue #598: the
    1806 gifts/help marks at 18:17/18:21 never reached the live
    tracker, which still read 13:06/13:21). Resolve through the
    git common dir exactly like queue.py's _shared_token_home, so
    a worktree copy reads and writes the main checkout's
    _tools_/state. A copy that is not in a repo (tests, scratch)
    or whose main checkout holds no _tools_/state keeps the local
    dir, and the main checkout itself resolves to itself.
    """
    try:
        out = subprocess.run(
            ["git", "-C", ROOT, "rev-parse", "--git-common-dir"],
            capture_output=True, text=True, timeout=10)
    except (OSError, subprocess.SubprocessError):
        return STATE_DIR
    if out.returncode != 0:
        return STATE_DIR
    common = out.stdout.strip()
    if not common:
        return STATE_DIR
    if not os.path.isabs(common):
        common = os.path.normpath(os.path.join(ROOT, common))
    if os.path.basename(os.path.normpath(common)) != ".git":
        return STATE_DIR
    main_state = os.path.join(
        os.path.dirname(os.path.normpath(common)), "_tools_", "state")
    if os.path.isdir(main_state):
        return main_state
    return STATE_DIR

def load_defs():
    with open(DEFS) as f:
        return json.load(f)["regulars"]

def state_path(day):
    return os.path.join(live_state_dir(), day.isoformat() + ".json")

def load_state(day):
    p = state_path(day)
    if os.path.exists(p):
        with open(p) as f:
            return json.load(f)
    return {}

def save_state(day, state):
    os.makedirs(live_state_dir(), exist_ok=True)
    with open(state_path(day), "w") as f:
        json.dump(state, f, indent=1, ensure_ascii=False)

SEGMENT_ANCHORS = {1: 6 * 60 + 3, 2: 6 * 60 + 30, 3: 6 * 60 + 57}
LOCAL_TZ = ZoneInfo("America/Los_Angeles")


def _as_local(dt):
    """An aware datetime in America/Los_Angeles; a naive datetime
    is read as schedule-local wall time (state stamps were written
    on the Mac in local time), never as the host clock."""
    if dt.tzinfo is None:
        return dt.replace(tzinfo=LOCAL_TZ)
    return dt.astimezone(LOCAL_TZ)


def _parse_hhmm(text):
    try:
        hh, mm = (int(x) for x in str(text).split(":"))
    except (ValueError, AttributeError):
        return None
    if not 0 <= hh <= 23 or not 0 <= mm <= 59:
        return None
    return hh, mm


def daily_reset_boundary(reg, now):
    """Most recent daily-reset boundary at or before now, as an
    aware America/Los_Angeles datetime. With reset_utc the boundary
    is the latest reset_utc instant in UTC (absolute, DST-proof);
    without it, the latest reset_local wall time in
    America/Los_Angeles."""
    now_local = _as_local(now)
    parsed_utc = _parse_hhmm(reg.get("reset_utc", ""))
    if parsed_utc is not None:
        hh, mm = parsed_utc
        now_utc = now_local.astimezone(timezone.utc)
        cand = now_utc.replace(hour=hh, minute=mm, second=0,
                               microsecond=0)
        if cand > now_utc:
            cand -= timedelta(days=1)
        return cand.astimezone(LOCAL_TZ)
    reset_t = dtime.fromisoformat(reg.get("reset_local", "19:00"))
    boundary = now_local.replace(hour=reset_t.hour, minute=reset_t.minute,
                                 second=0, microsecond=0)
    if now_local < boundary:
        boundary -= timedelta(days=1)
    return boundary

def latest_cycle_start(now, anchor_min):
    """Most recent 4 hour cycle boundary for a segment whose fires
    are anchored at anchor_min (minute of day of any one fire)."""
    cur = now.hour * 60 + now.minute
    delta = (cur - anchor_min) % 240
    return now - timedelta(minutes=delta, seconds=now.second,
                           microseconds=now.microsecond)

def status_of(reg, state, now):
    """Return (due: bool, label: str)."""
    now = _as_local(now)
    cadence = reg["cadence"]
    if cadence == "weekly-thu" and now.weekday() != 3:  # Thursday = 3
        return False, "not today (Thu only)"
    entry = state.get(reg["id"])
    if not entry:
        return True, "pending"
    done_at = _as_local(datetime.fromisoformat(entry["at"]))
    if cadence == "every-run":
        anchor = SEGMENT_ANCHORS[reg.get("segment", 1)]
        if done_at < latest_cycle_start(now, anchor):
            return True, "due again (new 4h cycle)"
        if entry.get("status") == "skipped":
            return False, "skipped - " + entry.get("note", "")
        return False, "done " + done_at.strftime("%H:%M") + " (redo next run)"
    if entry.get("status") == "skipped":
        return False, "skipped - " + entry.get("note", "")
    if cadence == "daily-reset":
        if done_at < daily_reset_boundary(reg, now):
            return True, "due again (reset passed)"
    return False, "done " + done_at.strftime("%H:%M")

def show(day, only_due, segment=None, as_json=False):
    regs = load_defs()
    state = load_state(day)
    now = datetime.now(LOCAL_TZ)
    rows = []
    items = []
    for reg in regs:
        if segment is not None and reg.get("segment", 1) != segment:
            continue
        due, label = status_of(reg, state, now)
        if only_due and not due:
            continue
        mark = "DUE " if due else "ok  "
        rows.append(f"{mark} [{reg['id']}] {reg['name']} -- {label}")
        items.append({
            "id": reg["id"], "activity": reg.get("activity", ""),
            "segment": reg.get("segment", 1),
            "cadence": reg.get("cadence", ""),
            "reset_local": reg.get("reset_local", ""),
            "reset_utc": reg.get("reset_utc", ""),
            "due": due, "label": label,
        })
    if as_json:
        print(json.dumps({"date": day.isoformat(), "items": items},
                         ensure_ascii=False))
        return
    print(f"Regulars for {day.isoformat()} ({len(rows)} shown)")
    print("\n".join(rows) if rows else "Nothing due.")

def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    for name in ("list", "todo", "reset"):
        p = sub.add_parser(name)
        p.add_argument("--date", default=None)
        p.add_argument("--segment", type=int, default=None)
        p.add_argument("--json", action="store_true")
    for name in ("done", "skip"):
        p = sub.add_parser(name)
        p.add_argument("id")
        p.add_argument("--note", default="")
        p.add_argument("--date", default=None)
    args = ap.parse_args()
    day = date.fromisoformat(args.date) if getattr(args, "date", None) else datetime.now(LOCAL_TZ).date()
    if args.cmd in ("list", "todo"):
        show(day, args.cmd == "todo", getattr(args, "segment", None),
             getattr(args, "json", False))
    elif args.cmd == "reset":
        p = state_path(day)
        if os.path.exists(p):
            os.remove(p)
        print("cleared", p)
    else:
        regs = {r["id"]: r for r in load_defs()}
        if args.id not in regs:
            print("unknown regular id:", args.id, file=sys.stderr)
            print("known:", ", ".join(sorted(regs)), file=sys.stderr)
            return 1
        state = load_state(day)
        state[args.id] = {
            "status": "done" if args.cmd == "done" else "skipped",
            "at": datetime.now(LOCAL_TZ).isoformat(timespec="seconds"),
            "note": args.note,
        }
        save_state(day, state)
        print(f"{args.id}: {state[args.id]['status']} at {state[args.id]['at']}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
