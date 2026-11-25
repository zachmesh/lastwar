---
title: Pool Note After The 1801Z Plan 3197 2026-11-25
created: 2026-11-25T10:10:00-08:00
modified: 2026-11-25T10:10:00-08:00
level: L0
version: 1.0.0
description: The plan run of 2026-11-25 18:01Z during the different-device hold - 19 units minted for the 22:16Z wave and the 22:30Z and 22:57Z groups, two retired, one held priority-1 unit's expiry shortened by the plan and restored, the window edges moved, the checks and a pick simulation
status: done
activity: queue-planning
run_id: queue-planning-2026-11-25-1801-plan
trigger: coordinator ping 18:04Z
started_at: 2026-11-25T10:00:40-08:00
finished_at: 2026-11-25T10:10:00-08:00
verified: queue.py plan --hours 5 output, the held units read before and after the plan and again at the end, validate, the forecast check over all units, the window and on-the-hour scans, the standing-line, front-clause, avatar and Lottery scans, a pick simulation with the tool's own pick_key and actionable test
grounded_in:
  - source: _records_/2026-11-22/queue-planning/3120-next-plan-specifics.md
  - source: _records_/2026-11-22/queue-planning/3125-plan-times-and-checks.md
  - source: _records_/2026-11-22/queue-planning/3196-pool-note-1401z-plan.md
---

# Pool note, 1801Z plan, 3197

## The held units: read before, after, and at the end

I read the expiries of the 14 held units before the plan, after it and again at the end. The plan SHORTENED ONE: the Drill Ground hand-off went from 11-26T06:50Z to 2026-11-25T22:00:59Z (its floor emptied and a `planned_for` stamp added, as with -005, cycle D and the UR claim at earlier plans). I restored it to 11-26T06:50Z at once. The others held: -005, the UR claim, the room collect, the train batch, the base survey and the help gesture 11-26T06:50Z; cycle D and pass 012 11-26T01:50Z; the lab complete 21:39Z. Every held unit now reads live and as set.

## What the plan did

`plan --hours 5` minted 19 units: the 22:03Z wave (8, ids -1403), the 22:30Z group (6, -1430) and the 22:57Z group (5, -1457). It expired 17 stale units: the wave that opened 10:06Z and the groups that opened 10:30Z and 10:57Z (their windows ended 14:03Z to 14:57Z while the game was held). I retired the roster donations and trucks units at 18:01Z. The radar unit of the new wave and its duel-score unit are priority 1 (Steer A, 17:47Z; the duel day ends 02:00Z).

## Window edges

My times sheet keeps 22:00Z to 22:15Z clear of openings and expiries. The 22:03Z wave (7 units) opens 22:16Z, not 22:03Z, and the 8 units that expired at 22:03Z (the 18:03Z wave with both radar units) now expire 22:16Z: the radar coverage has no gap, since the old radar units end at the minute the new one opens. The coordinator's ping omitted this window (the prompt did not come at the predicted 22:07Z on 11-24): I applied the sheet as written, a 13-minute cost.

## Checks

Pool       69 units, validate 'pool valid', none at or over 450 words; the forecast gate refused none; the standing line in every unit; the front clause in every unit but pass 012 (the dispatch text carries it); no avatar coordinate or Lottery tab without a ban. Nothing opens or expires in 22:00Z-22:15Z, 02:58Z-03:02Z, 04:30Z-04:45Z, 08:00Z-08:25Z, 09:58Z-10:05Z or 11:25Z-11:40Z, and no opening is on the hour. A pick simulation of the 17 roster units from 22:16Z over five hours, estimate plus one or two minutes, runs all 17 and expires none.

## Fixed items

The lab complete 19:39Z, the pre-reset set at 00:30Z (the 22Z plan mints it: radar and duel-score at priority 1, the last claim due 01:45Z), the VIP unit at 02:06Z (the 22Z plan, with the 11-25 route paragraph), the Hospital read 11-27T00:25Z. The dialog still stands (since 06:25:52Z). The next plan is the 22Z ping.
