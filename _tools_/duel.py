#!/usr/bin/env python3
"""Alliance Duel day calculator and gating advisor.

Reads _tools_/duel_schedule.json, works out which duel day is live right
now (duel days roll at 19:00 local per the 2026-10-25 observation) and
prints the gating advice the playbook attaches to that day - most
importantly when to preserve radar tasks for Radar Training day.

The schedule declares its timezone (America/Los_Angeles) and the anchor
is a local wall time, so the day is always computed in that timezone,
never in the host clock timezone. A naive datetime.now() on a UTC host
used to roll to the next duel day at 11:00 PT, eight hours early - that
is what made 2026-11-03 14:03 PT read as Day 3 (Age of Science, release)
while the live game dialog said radar tasks score nothing today (Day 2,
Base Expansion, stack). See issue #235.

Usage:
  duel.py            human readable status for today
  duel.py --json     machine readable, for scheduled runs
"""
import json, os, sys
from datetime import datetime, timedelta, time as dtime
from zoneinfo import ZoneInfo

ROOT = os.path.dirname(os.path.abspath(__file__))
DEFS = os.path.join(ROOT, "duel_schedule.json")

def current(now=None):
    with open(DEFS) as f:
        cfg = json.load(f)
    tz = ZoneInfo(cfg.get("timezone", "America/Los_Angeles"))
    anchor = datetime.fromisoformat(cfg["week_anchor_local"])
    if anchor.tzinfo is None:
        anchor = anchor.replace(tzinfo=tz)
    else:
        anchor = anchor.astimezone(tz)
    if now is None:
        now = datetime.now(tz)
    elif now.tzinfo is None:
        # Naive caller time is read as schedule-local wall time.
        now = now.replace(tzinfo=tz)
    else:
        now = now.astimezone(tz)
    # Day boundaries are 19:00 local wall times, so count calendar days
    # on the wall clock. Absolute timedeltas would slip an hour across
    # a daylight-saving transition; wall arithmetic never does.
    anchor_wall = anchor.replace(tzinfo=None)
    now_wall = now.replace(tzinfo=None)
    delta = now_wall - anchor_wall
    day_index = delta.days  # full duel days since Day 1 opened
    pos = day_index % 7  # 0..5 duel days, 6 = off day
    day = cfg["days"][pos]
    day_start_wall = anchor_wall + timedelta(days=day_index)
    day_end_wall = day_start_wall + timedelta(days=1)
    day_end = day_end_wall.replace(tzinfo=tz)
    return {
        "now": now.isoformat(timespec="seconds"),
        "duel_day": day["day"],
        "theme": day["theme"],
        "win_points": day["win_points"],
        "day_ends": day_end.isoformat(timespec="seconds"),
        "hours_left": round((day_end - now).total_seconds() / 3600, 1),
        "gate": day["gate"],
        "actions_that_score": day["actions_that_score"],
        "radar_posture": {1: "release", 2: "stack", 3: "release", 4: "stack", 5: "release", 6: "stack", 7: "stack"}[day["day"]],
    }

def main():
    info = current()
    if "--json" in sys.argv:
        print(json.dumps(info, indent=1, ensure_ascii=False))
        return 0
    print(f"Alliance Duel - Day {info['duel_day']}: {info['theme']} "
          f"(win points {info['win_points']}, ends {info['day_ends']}, "
          f"{info['hours_left']}h left)")
    print("Gate: " + info["gate"])
    if info["radar_posture"] == "stack":
        print("RADAR: stack day - complete tasks but do NOT claim; keep storage headroom under the cap.")
    if info["radar_posture"] == "release":
        print("RADAR: release day - complete and claim everything, early in the day.")
    print("Scores today:")
    for a in info["actions_that_score"]:
        print(" - " + a)
    return 0

if __name__ == "__main__":
    sys.exit(main())
