#!/usr/bin/env python3
"""Alliance Duel day calculator and gating advisor.

Reads _tools_/duel_schedule.json, works out which duel day is live right
now (duel days roll at 19:00 local per the 2026-10-25 observation) and
prints the gating advice the playbook attaches to that day - most
importantly when to preserve radar tasks for Radar Training day.

Usage:
  duel.py            human readable status for today
  duel.py --json     machine readable, for scheduled runs
"""
import json, os, sys
from datetime import datetime, timedelta, time as dtime

ROOT = os.path.dirname(os.path.abspath(__file__))
DEFS = os.path.join(ROOT, "duel_schedule.json")

def current():
    with open(DEFS) as f:
        cfg = json.load(f)
    anchor = datetime.fromisoformat(cfg["week_anchor_local"])
    now = datetime.now()
    delta = now - anchor
    day_index = delta.days  # full 24h duel days since Day 1 opened
    pos = day_index % 7  # 0..5 duel days, 6 = off day
    day = cfg["days"][pos]
    day_start = anchor + timedelta(days=day_index)
    day_end = day_start + timedelta(days=1)
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
