---
title: Pool Note After The 1001Z Plan 3194 2026-11-25
created: 2026-11-25T02:10:00-08:00
modified: 2026-11-25T02:10:00-08:00
level: L0
version: 1.0.0
description: The plan run of 2026-11-25 10:01Z during the different-device hold - 20 units minted for the 14:03Z wave, the 14:30Z and 14:57Z groups and the midday scout, two retired, the held priority-1 units rewritten by the tool, the checks and two pick simulations
status: done
activity: queue-planning
run_id: queue-planning-2026-11-25-1001-plan
trigger: coordinator ping 10:01Z
started_at: 2026-11-25T02:00:40-08:00
finished_at: 2026-11-25T02:10:00-08:00
verified: queue.py plan --hours 5 output, validate, queue.py next, the forecast check over all units, the window and on-the-hour scans, the standing-line, front-clause, avatar, Lottery and Backpack scans, two pick simulations with the tool's own pick_key and actionable test
grounded_in:
  - source: _records_/2026-11-22/queue-planning/3120-next-plan-specifics.md
  - source: _records_/2026-11-22/queue-planning/3125-plan-times-and-checks.md
  - source: _records_/2026-11-22/queue-planning/3193-pool-note-0601z-plan.md
---

# Pool note, 1001Z plan, 3194

## What the plan did

`plan --hours 5` minted 20 units: the 14:03Z wave (8, ids -0603), the 14:30Z group (6, -0630), the 14:57Z group (5, -0657) and the daily midday scout (-0700). It retired two at 10:01Z: the roster donations unit and the roster trucks unit. It expired seven held units, the 06:03Z wave (never run: the Mac's game stands behind the different-device dialog since 06:25:52Z, and nothing is pressed without the owner's word); the 06:30Z group ends at 10:30Z and the 06:57Z group at 10:57Z the same way.

## A finding about the tool

The plan rewrote three held priority-1 units (the Oil Well hand-off -005, cycle D and the UR secret claim): their `not_before` is now empty (no floor) and their `expires_at` 14:01:28Z, four hours after the plan, with a `planned_for` stamp; my helper reads the empty floor as a nested field, but `queue.py next` and `validate` handle it. Their text, priority and attempts are untouched. The floors were past, so nothing is lost; the expiries are later than my 11:50Z and 12:50Z.

## Fixed in the minted units

Each unit carries its predecessor's block from the 06Z plan. The midday scout lacked the standing line and the front clause: I added a planner block (PL-07, read only, no avatar or bubble). Its opening moved from 15:00Z to 15:04Z (not on the hour). The 14:03Z wave opens 14:03Z: the owner's window is past.

## Checks

Pool       62 units, validate 'pool valid', none at or over 450 words; the forecast gate refused none; the standing line in every unit; the front clause in every unit but the last donation pass (the dispatch text carries it); no avatar coordinate, Lottery tab or unreasoned Backpack read. Windows: only the gate test in 11:25Z to 11:40Z on 11-25; nothing in 02:58Z-03:02Z, 04:30Z-04:45Z, 08:00Z-08:25Z or 09:58Z-10:05Z on 11-26. A pick simulation from 10:06Z over five hours, with each unit's estimate plus one or two minutes, runs 40 and 37 of 45 roster units and expires one unrun (the held 06:30Z star-ceremony).

## Fixed items

The held units behind the dialog (order after the owner's word: -005, cycle D, the UR claim, pass 012, the help gesture, the survey); the gate test 11:28:30Z; the room collect 13:35Z (dispatch 13:39Z) and train batch 13:50Z; the Lv.26 Drill Ground end 13:38:36Z with the freed builder's job still unnamed; the labs 19:39Z and 11-26 08:37Z; the 11-26 VIP unit (minted by the 22Z plan, copy the 11-25 route paragraph); the Hospital read 11-27T00:25Z. The next plan is the 14Z ping.
