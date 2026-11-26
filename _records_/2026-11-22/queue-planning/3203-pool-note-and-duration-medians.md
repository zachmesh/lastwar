---
title: Pool Note And Duration Medians At 1204Z 3203 2026-11-26
created: 2026-11-26T04:04:04-08:00
modified: 2026-11-26T04:04:04-08:00
level: L0
version: 1.0.0
description: The pool state at 12:04Z on 2026-11-26, the duration medians per regular of the 33 units that ran since 11-25T12:03Z set against their estimates, and the finding that no unit carries donations or the continuation rule since the donation passes ended
status: done
activity: queue-planning
run_id: queue-planning-2026-11-26-1204-medians
trigger: coordinator wake 12:05Z
started_at: 2026-11-26T04:02:00-08:00
finished_at: 2026-11-26T04:04:04-08:00
verified: durations computed from the started_at and finished_at of every unit in the done folder that finished since 11-25T12:03Z, the pool counted by queue.py list_units, the donation retirement reason read in notes 3100 and 3140, the continuation line read in note 3120
grounded_in:
  - source: _records_/2026-11-22/team-operations/1203-word-budget-review.md
  - source: _records_/2026-11-22/queue-planning/3202-pool-note-1001z-plan.md
---

# Pool note and duration medians, 1204Z, 3203

## The pool at 12:04Z

52 units in the inbox: 40 live, 12 past their end and waiting for the 14Z plan's reap (the 10:03Z, 10:30Z and 10:57Z roster units that ran behind the chain). 14 are open now (priority 2: 3, priority 3: 10, a fallback at priority 9: 1); 30 live units are roster class. The mail unit (14:30Z, floor lowered to 12:10Z) carries Steer A's event-list pan and the wider Claim All ban; the harvest unit carries the two building taps; the bubble probe opens 12:45Z.

## Duration medians, units that ran since 11-25T12:03Z

33 units ran (26 done, 7 partial; 129 more closed expired). Median minutes against the estimate: building-queues 6.1 (4 runs, max 20.8) against 11.5; trucks 8.0 (5, max 11.5) against 15; scout-midday 5.9 (6, max 12.5) against 6; radar 2.2 against 3; harvest 3.3 against 4; vip 1.9 against 4; passes 2.8 against 4; secrets 2.5 against 8; training 3.6 against 12; scout 2.1 against 6; gifts 1.9 against 5; events 2.2 against 5. Over the estimate: daily-missions 17.6 against 10 (one run, with the helper window), mail 8.5 against 4 (one run). The full table is `3203-duration-medians-2026-11-26.csv`: one to six runs a regular, so a median under three runs is a reading, not a rate.

What follows: the roster estimates in the tool (the Toolsmith's `regulars.json`) overstate secrets, training, scout, gifts and events by 2 to 4 times, so a pick simulation at those estimates is pessimistic; the Drill Ground hand-off ran 20.8 minutes against an estimate of 15.

## The donations precedent (the Coordinator's 12:05Z check)

No unit in the pool carries the continuation rule, because no donations unit is in the pool. The rule exists only as a line in note 3120 ('a run at max_steps with the count live is continued by part two'). Since 11-24 I have retired the roster donations unit at every plan on the premise 'the donation passes carry donations' (notes 3100 and 3140); those donation passes (008 to 011) are gone, so no unit runs donations today. This needs Steer A's word before any change.
