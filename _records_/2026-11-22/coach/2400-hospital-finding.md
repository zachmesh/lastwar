---
title: Hospital finding - healed troops waiting behind the Drill Ground cap
created: 2026-11-23T08:20:00Z
modified: 2026-11-23T08:20:00Z
version: 1.0.0
description: Coach record on the operator's hospital read - 5,306 healed and 364 severely wounded troops, the refused Collect, the unrealized power range, the corrected capacity arithmetic and what it changes in the fall analysis
status: done
activity: coach
run_id: coach-2026-11-22-2400
trigger: new operator record 2357 and the Strategist briefing
started_at: 2026-11-23T08:14:00Z
finished_at: 2026-11-23T08:20:00Z
duration_seconds: 360
verified: no
grounded_in:
  - source: _records_/2026-11-22/growth/2357-troop-read.md and ledger.csv, screen read 2026-11-23 08:00Z
  - source: _records_/2026-11-22/queue-planning/2420-coin-and-capacity-plan.md
  - source: Drill Ground upgrade panels in the 2026-11-10 records named in candidate-causes.csv
---

# Hospital finding

**Read.** Hospital Lv.25 shows Severely Wounded 364 of 7,999 (Lv.10 x364) and a bar "Completed 5306" with a Collect button. One Collect tap gave "Drill Ground Full: Unable to add 5306 units"; power stayed 150,211,809 (08:00:34Z).

**Unrealized power.** 5,306 troops at 1,063 to 1,647 each is 5.64M to 8.74M, 3.8 to 5.8 percent of total power; the tier mix is unread, so this is a range, not a measurement. Behind it in the pipeline: 364 severely wounded (0.60M at T10) and the finished batches Lv.27 T9 x726 and Lv.30 T10 x793 (2.29M).

**Capacity, corrected.** Upgrade panels read Unit Count +7,000 to +7,200, +7,200 to +7,400 and +7,400 to +7,600: about 200 slots a level, 0.33M power at T10. The planner counts 6,825 waiting troops, about 34 levels. The Lv.28 Building Details figure of +9,211 is a different readout, unread. The tier census, 40,235, exceeds the 39,460 cap read on 10-31, so the cap seems to count more than the census; an inference. My first message to the Strategist overstated what one level frees; it is corrected.

**What it changes in the fall analysis** ([candidates](candidate-causes.csv)).
- Hospitalized troops move from hypothesis to supported: troops are in the hospital, by screen read. That the 11-09 troops are these is unverified.
- Killed is weakened: 5,670 troops are wounded or healed, not lost.
- Collection is capacity-gated, verified by the refused tap. Power returns at Collect, so a drop reverses only when space allows, which fits the stepwise reversals.

**Misses.** Post-restart reads with slot state: 2 (07:47Z and 08:00Z). Idle found in both, a Lv.24 barracks blocked by the cap; startable misses 0 ([log](misses-log.csv)).

**Measurement change.** Each slot read now also records Hospital wounded and completed, the tier of the completed, and the Drill Ground owned, outside and capacity lines. A drop of 300k or more is matched to the hospital change.

**Not done.** Dismissing or promoting troops: owner decisions, irreversible, outside the coach.
