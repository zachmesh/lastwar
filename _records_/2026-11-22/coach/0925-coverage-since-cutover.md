---
title: Coverage since the cutover, the 14 units with no serves line, and hours serving nothing
created: 2026-11-23T17:27:00Z
modified: 2026-11-23T18:02:00Z
version: 1.0.1
description: Coach preparation for the next daily report, with the first since-cutover reading - the honest serves coverage by units and unit-hours, the check of the planner's account of the fourteen units with no serves line by name, and the hours that serve nothing
status: done
activity: coach
run_id: coach-2026-11-23-0925
trigger: coordinator message for Steer A's condition on the daily report
started_at: 2026-11-23T17:20:00Z
finished_at: 2026-11-23T17:27:00Z
duration_seconds: 420
verified: no
grounded_in:
  - source: _queue_/done frontmatter read at 17:22Z; _tools_/queue.py forecast_class and the newest forecast ledger
  - source: _records_/2026-11-22/queue-planning/2960-other-wording-and-no-serves-units.md
---

# Coverage since the cutover

Method and rows: [method](coverage-honest-method.py), [table](coverage-honest.csv). Classes follow `forecast_class`: ranked by plan item id or by the fill idle slot phrase, exempt (exactly upkeep, snapshot or baseline), other wording, no serves line. Threshold 60 percent for units and unit-hours.

**The verdict, since the cutover.** The cutover is 17:30:53Z (`strategy-cutover.json`: roster-serves, PR 925, reached the live checkout at 17:30:53Z). At 17:56Z two units have executed since it: the donations pass 001 (ranked, PL-04) and `events-2026-11-23-0657` (exempt upkeep): 50 percent of units and 46 percent of unit-hours, not ranked 1 unit, 0.08 h of 0.15 h. This matches the conformance tool's first reading. Under the 60 percent limit on a sample of 2: it will climb as the units minted after 17:30Z execute, and the verdict line in each daily report is this one (`--cutover`).

**Context.** Last 12 hours: 75 executed, coverage 17 percent of units and 30 percent of unit-hours (ranked 8 by id and 5 by name, exempt 27, other wording 21, no serves line 14); your baseline of 15 and 26 uses a window a few minutes earlier, and the other-wording and no-serves counts agree exactly. Last 6 hours: 23 and 39 percent. Units created after the requirement went live at 09:51:47Z: 31 executed, 26 percent of units and 50 percent of unit-hours, every one with a serves line. Both are under 60.

## The 14 units with no serves line: the planner's note checks out

Five were minted on 2026-11-22: `scout-midday-2026-11-22-0700` (created 03:41Z), `daily-missions`, `vip` and `scout` for 18:00 (14:42Z), and `events-2026-11-22-1857` (15:43Z). Nine were enqueued by hand on 11-23 between 06:56Z and 08:08Z: `scout-midday-2026-11-23-0656`, `arms-race`, `secrets`, `donations`, `passes` and `building-queues` (07:09Z to 07:20Z), and the growth-snapshot units 004, 002 and 011. None was created after 08:08Z, and none after the requirement went live. One difference: the note says eight of the nine had no chain id; three, the snapshot units, carry `growth-snapshot-2026-11-23`.

## Hours that serve nothing

Last 6 hours, 3.03 h executed. Strict, counting other wording: 0.83 h: `snapshot (Story 868)` 0.30, `baseline coin conversion` 0.14, `baseline Age of Oil research tree` 0.07, `playbook card test T2` 0.04, and `capacity source: Drill Ground Expansion` 0.29, which serves a ranked item but in free text. Counting snapshot and baseline lines as knowingly exempt: 0.33 h, near your 0.34. The target is zero; the planner now writes exact words.

## Limits

Frontmatter only: a unit whose serves is in its body counts as no serves line. Hours are the result duration, else the estimate.
