---
title: Pool Note After The 0601Z Plan 3193 2026-11-25
created: 2026-11-24T22:05:00-08:00
modified: 2026-11-24T22:05:00-08:00
level: L0
version: 1.0.0
description: The plan run of 2026-11-25 06:02Z - 19 roster units minted for the 10:03Z wave, the 10:30Z group and the 10:57Z group, two retired, the 10:03Z wave moved to 10:06Z off the owner's job window, the standing units re-timed, the checks and two pick simulations
status: done
activity: queue-planning
run_id: queue-planning-2026-11-25-0601-plan
trigger: coordinator ping 06:02Z
started_at: 2026-11-24T22:01:30-08:00
finished_at: 2026-11-24T22:05:00-08:00
verified: queue.py plan --hours 5 output, validate, the forecast check over all units, the calm-window scan, the on-the-hour scan, the standing-line, front-clause, avatar, Lottery and Backpack scans, two pick simulations with the tool's own pick_key and actionable test
grounded_in:
  - source: _records_/2026-11-22/queue-planning/3120-next-plan-specifics.md
  - source: _records_/2026-11-22/queue-planning/3125-plan-times-and-checks.md
  - source: _records_/2026-11-22/queue-planning/3192-pool-note-0201z-plan.md
---

# Pool note, 0601Z plan, 3193

## What the plan did

`plan --hours 5` minted 19 roster units: the 10:03Z wave (8, ids -0203), the 10:30Z group (6, -0230) and the 10:57Z group (5, -0257). It retired two at 06:02Z: the roster donations unit and the roster trucks unit. The 10:03Z wave (7 units left) opens at 10:06Z, not 10:03Z: the owner's job window is 09:58Z to 10:05Z. No opening is on the hour; nothing opens or expires in 08:00Z to 08:25Z, 09:58Z to 10:05Z, or 02:58Z to 03:02Z on 11-26; the only unit in 11:25Z to 11:40Z is the gate test.

## Carried from the 02Z plan

Each unit carries its predecessor's block. The two H118 sentences left the 10:03Z building-queues and 10:30Z help units (the Oil Well Lv.24 row is gone, so the test moved to the Lv.25 job's own follow-up unit). The 10:30Z duel-score unit previews only a chest still closed whose preview the 06:30Z record did not read, and claims a reached chest by one plain Claim. The 10:30Z mail unit keeps the Arms Race and Glittering Market mail rules. The dot-first class this cycle is none.

## Standing units re-timed

The rescue-depot claim now opens at 07:13:30Z, priority 1: the secrets claim units open at the task end plus 20 s (note 3120 v1.39.0). The refugee fallback was retired (its primary ran). The base survey expires 09:55Z, the help follow-up 09:30Z, both clear of the windows. The Oil Well units -006 to -010 stay as they are until the -005 record gives the real end: each releases if more than 5 minutes remain.

## Checks

Pool       52 units, validate 'pool valid', none at or over 450 words; the forecast gate refused none; the standing line in every unit; the front clause in every unit but the last donation pass (the dispatch text carries it); no avatar coordinate, Lottery tab or Backpack read without a ban or a plan reason. A pick simulation from 06:03Z over five hours, with each unit's estimate plus one or two minutes, runs 30 and 27 of 34 roster units and expires none unrun.

## Fixed items

Cycle D at 06:40Z, pass 012 (the queue unit -011) 07:05Z to 07:50Z, the rescue-depot claim 07:13:30Z, the Lv.26 Drill Ground end 13:38:36Z with the room collect (13:39Z) and train batch (13:50Z), the Hospital read 11-27T00:25Z to 00:55Z, the lab Completes 11-25 19:39Z and 11-26 08:37Z. The owner is at the Mac: the operator holds while he is active, and a unit whose window ends is re-staged, not forced. The next plan is the 10Z ping.
