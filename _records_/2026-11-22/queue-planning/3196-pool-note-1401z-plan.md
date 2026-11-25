---
title: Pool Note After The 1401Z Plan 3196 2026-11-25
created: 2026-11-25T06:10:00-08:00
modified: 2026-11-25T06:10:00-08:00
level: L0
version: 1.0.0
description: The plan run of 2026-11-25 14:01Z during the different-device hold - 19 units minted for the 18:03Z wave and the 18:30Z and 18:57Z groups, two retired, eleven stale units reaped, the held chain with its length, the checks and a pick simulation
status: done
activity: queue-planning
run_id: queue-planning-2026-11-25-1401-plan
trigger: coordinator ping 14:01Z
started_at: 2026-11-25T06:00:40-08:00
finished_at: 2026-11-25T06:10:00-08:00
verified: queue.py plan --hours 5 output, validate, the held units re-read after the plan, the forecast check over all units, the window and on-the-hour scans, the standing-line, front-clause, avatar and Lottery scans, one pick simulation, the chain length from the units' est_minutes
grounded_in:
  - source: _records_/2026-11-22/queue-planning/3120-next-plan-specifics.md
  - source: _records_/2026-11-22/queue-planning/3125-plan-times-and-checks.md
  - source: _records_/2026-11-22/queue-planning/3194-pool-note-1001z-plan.md
---

# Pool note, 1401Z plan, 3196

## What the plan did

`plan --hours 5` minted 19 units: the 18:03Z wave (8, ids -1003), the 18:30Z group (6, -1030) and the 18:57Z group (5, -1057). I retired two at 14:01Z, the roster donations unit and the roster trucks unit. The plan reaped 11 stale units (the 06:30Z and 06:57Z groups and the cu gate test). The new units open at 18:03Z or later, after the held chain's 17:30Z expiries, so they are not in its way.

## The held units after the plan

I re-read them: the plan did not rewrite any expiry this time. The Oil Well hand-off -005, cycle D and the UR secret claim (empty floor since the 10Z plan), the Drill Ground hand-off, the room collect, the train batch, pass 012, the base survey and the help gesture all expire 17:30Z. The plan left every floor, priority and text as it was.

## The chain after the owner's word

Nine units: -005 (est 8), the room collect (12), the Drill Ground hand-off with its preview and preconvert (15), cycle D (15), the UR claim (8), the train batch (14), pass 012 (10), the help gesture (4), the base survey (12). Sum of estimates 98 minutes; 107 to 116 with a 1 to 2 minute hand-off each. The first six, the priority-1 units and the room units, are 72 minutes, 78 to 84 with hand-offs. The tool's learned medians (building-queues 4, trucks 7, secrets 5, training 6) would make it about 65 to 75 minutes if the units run at their median: cycle C took 34 minutes with four plunders, and cycle D has none to fight, so it should take less [G, not measured].

## Checks

Pool       69 units, validate 'pool valid', none at or over 450 words; the forecast gate refused none; the standing line in every unit; the front clause in every unit but the last donation pass (the dispatch text carries it); no avatar coordinate or Lottery tab without a ban. Nothing opens or expires in 02:58Z-03:02Z, 04:30Z-04:45Z, 08:00Z-08:25Z, 09:58Z-10:05Z or 11:25Z-11:40Z on 11-26, and no opening is on the hour. A pick simulation of the 17 roster units from the 18:03Z wave on, from 18:06Z over five hours with each unit's estimate plus one or two minutes, runs all 17 and expires none unrun.

## Fixed items

The 11-26 VIP unit (the 22Z plan mints it, with the 11-25 route paragraph), the labs 19:39Z and 11-26 08:37Z, the Hospital read 11-27T00:25Z. The game is still behind the different-device dialog (since 06:25:52Z): nothing runs until the owner answers. The next plan is the 18Z ping.
