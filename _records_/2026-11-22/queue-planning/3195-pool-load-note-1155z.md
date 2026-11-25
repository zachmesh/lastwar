---
title: Pool Load Note And Duration Medians 1155Z 3195 2026-11-25
created: 2026-11-25T04:05:00-08:00
modified: 2026-11-25T04:05:00-08:00
level: L0
version: 1.0.0
description: The daily pool-load note of 2026-11-25 11:55Z - the duration medians of the done units by the method of sheet 2470, what they can say when nothing has run since 05:28Z, the expired and held units
status: done
activity: queue-planning
run_id: queue-planning-2026-11-25-1155-pool-load
trigger: coordinator wake 11:55Z
started_at: 2026-11-25T03:58:00-08:00
finished_at: 2026-11-25T04:05:00-08:00
verified: list_units on the done folder, the numeric result.duration_seconds of units whose finished_at falls on the date, the expired results split by their summary, typical_minutes called with the queue folder
grounded_in:
  - source: _records_/2026-11-22/queue-planning/2470-durations-and-priority-order.md
---

# Pool load note, 1155Z, 3195

## Duration medians (sheet 2470 method)

2026-11-24 UTC: 194 units with a numeric duration (138 done): median 1.8 minutes, mean 2.8, p90 5.4, max 27.6. 2026-11-25 UTC to the last run at 05:28:15Z: 43 units (39 done): median 2.3, mean 4.2, p90 8.5, max 33.2 (the trade cycle C). By regular, 11-25 against 11-24: building-queues median 8.0 (4 units) against 3.0, secrets 6.6 (2) against 1.9, passes 5.3 (2) against 2.2, donations 4.2 (3) against 3.5, gifts 1.7 against 1.8, mail 2.3 against 1.7. The samples are small; the longer jobs of the day (the builders, the secrets redeploys, cycle C) fall inside them [G, not tested].

## What the medians say with no runs

Nothing new: no unit has finished since 05:28:15Z, so the 11-25 figures are the first five and a half hours and do not move. They say the typical wall time is the median plus the 1 to 2 minute hand-off, 3 to 5 minutes, and the pick simulations at the estimate plus one or two minutes still hold. The tool's learned estimates (`typical_minutes`, whole pool) are building-queues 4, trucks 7, secrets 5, passes 4, harvest 4, scout 3, zero sweep 9: close to what the units carry. The hold is the finding: 6 hours 32 minutes without a run, a builder idle since before 05:25Z.

## Expired and held

Real expiries on 11-25: 8: the seven units of the 06:03Z wave at 10:01Z (never run) and the duel-chest insurance unit (by design). The 12 planner retirements are not counted. Fourteen units are past their expiry and await the next reaping: the 06:30Z group (6), the 06:57Z group (4), the nightly cu gate test (11:40Z, unrun), pass 012, the base survey and the help gesture. By the rule in sheet 2470 (more than 2 expire in an hour) I say so: 7 in the 10Z hour, and the 10:30Z and 10:57Z hours will count 6 and 4 once reaped. The cause is outside the pool: the different-device dialog since 06:25:52Z, nothing pressed without the owner's word. P1 and B1 of that sheet are the 11-23 items: nothing to withdraw.

## Re-staged now

Pass 012, the base survey and the help gesture expire 15:30Z (were 11:20Z and 11:50Z). The Oil Well hand-off -005, cycle D and the UR claim expire 14:01:28Z (the 10Z plan rewrote them). The Drill Ground hand-off expires 17:00Z.

## Fixed items

The room collect 13:35Z (dispatch 13:39Z), the Drill Ground hand-off with its preconvert 13:38:40Z, the train batch 13:50Z, the 14:03Z wave, the labs 19:39Z and 11-26 08:37Z, the Hospital read 11-27T00:25Z. The next plan is the 14Z ping.
