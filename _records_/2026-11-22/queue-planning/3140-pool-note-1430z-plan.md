---
title: Pool Note After The 1430Z Plan 3140 2026-11-24
created: 2026-11-24T06:35:00-08:00
modified: 2026-11-24T06:35:00-08:00
level: L0
version: 1.0.0
description: The plan run of 2026-11-24 14:30Z - 19 roster units minted for the 18:03Z wave to the 18:57Z group, two retired, the specifics of note 3120 applied, the checks and a pool simulation to 19:30Z
status: done
activity: queue-planning
run_id: queue-planning-2026-11-24-0630-plan
trigger: coordinator ping 14:31Z (the recurring ping is set: 02, 06, 10, 14, 18 and 22Z)
started_at: 2026-11-24T06:28:00-08:00
finished_at: 2026-11-24T06:35:00-08:00
verified: queue.py plan --hours 5 output, validate, the forecast check over all units, the quiet-window scan, the on-the-hour scan and a pick simulation with the tool's own pick_key and actionable test
grounded_in:
  - source: _records_/2026-11-22/queue-planning/3120-next-plan-specifics.md
  - source: _records_/2026-11-22/queue-planning/3110-trade-cycle.md
---

# Pool note, 1430Z plan, 3140

## What the plan did

`plan --hours 5` minted 19 roster units: the 18:03Z wave (8), the 18:30Z group (6) and the 18:57Z group (5), ids with the Pacific hour label (-1003, -1030, -1057). It retired the roster donations unit (the donation passes 008 to 011 carry donations) and the roster trucks unit (the trade cycles replace it), both stamped 14:30:06Z. The planner blocks of the 14:03Z, 14:30Z and 14:57Z units were copied onto their successors: HUD line, radar and mail rulings, three-class idle reads, the secrets daily assist, and for passes the Weekly Pass sequence 3130 (est 12).

## Checks

Pool 60 units, validate 'pool valid'. Forecast gate (live): no unit refused. None opens or expires inside 08:00Z to 08:25Z on 11-24 to 11-26. In 11-25 11:25Z to 11:40Z only the gate test unit (11:28:30Z to 11:40:00Z). No unit opens exactly on the hour. Every unit is under 450 words.

## Simulation to 19:30Z

With the tool's own pick order and one pick per 13 minutes: 24 picks, two units expire unrun (events and treasures of the 14:57Z group, 18:57Z). At one pick per 20 minutes: 15 picks, nine expire unrun (arms-race, five of the 14:30Z group, events, secrets and treasures). The simulation leaves out the cycle, scan, Oil Well and lab units the Coordinator dispatches by name, so the real count is lower.

## Fixed items of the next hours

Cycle A closed (5 of 5). Cycle B 15:04Z, the scans to 17:21Z, the Oil Well Lv.24 hand-off 17:28Z, the lab Complete 17:30:30Z, donation pass 007 at 17:50Z, cycle B2 at 18:50Z, pass 008 at 21:05Z. The next plan is the 18Z ping.
