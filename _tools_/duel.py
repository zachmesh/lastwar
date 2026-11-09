#!/usr/bin/env python3
"""Alliance Duel day calculator and gating advisor.

Reads _tools_/duel_schedule.json, works out which duel day is live right
now (duel days roll every 24 hours absolute from the 2026-10-25 anchor,
02:00 UTC daily - 19:00 PDT before the 2026-11-02 daylight-saving end,
18:00 PST after it) and prints the gating advice the playbook attaches
to that day - most importantly when to preserve radar tasks for Radar
Training day.

The schedule declares its timezone (America/Los_Angeles) and the anchor
is a local wall time, so the day is always computed in that timezone,
never in the host clock timezone. A naive datetime.now() on a UTC host
used to roll to the next duel day at 11:00 PT, eight hours early - that
is what made 2026-11-03 14:03 PT read as Day 3 (Age of Science, release)
while the live game dialog said radar tasks score nothing today (Day 2,
Base Expansion, stack). See issue #235.

The boundary is NOT a fixed local wall time: the 2026-11-03 18:07 PST
panel in issue #242 already showed the new Age of Science day running
with 23:52 left, while the old wall-clock count would have kept Day 2
until 19:00 PST. Both observations fit one absolute cycle - the anchor
2026-10-25 19:00 PDT and the 2026-11-03 18:00 PST roll are both
02:00 UTC - so day boundaries are counted in absolute 24 hour steps
from the anchor, and the local wall time shifts with daylight saving.

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
    # Day boundaries are absolute 24 hour steps from the anchor
    # (02:00 UTC daily), NOT fixed local wall times: across the
    # 2026-11-02 daylight-saving end the wall time of the roll
    # moved from 19:00 PDT to 18:00 PST (issue #242). Counting
    # calendar wall days would keep the old day an hour too long
    # after the transition; absolute elapsed time never does.
    # NOTE: subtracting two aware datetimes that share one
    # tzinfo object is wall-clock arithmetic in CPython, and
    # adding a timedelta to an aware datetime is wall-clock
    # too, so neither can measure absolute elapsed time here.
    # Timestamps are the absolute measure.
    day_index = int((now.timestamp() - anchor.timestamp()) // 86400)
    pos = day_index % 7  # 0..5 duel days, 6 = off day
    day = cfg["days"][pos]
    day_end = datetime.fromtimestamp(
        anchor.timestamp() + (day_index + 1) * 86400, tz=tz)
    return {
        "now": now.isoformat(timespec="seconds"),
        "duel_day": day["day"],
        "theme": day["theme"],
        "win_points": day["win_points"],
        "day_ends": day_end.isoformat(timespec="seconds"),
        "hours_left": round((day_end.timestamp() - now.timestamp()) / 3600, 1),
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
