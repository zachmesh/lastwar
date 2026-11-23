---
title: Queue Planning The Donation Passes After The Refill Test 2980 2026-11-23
created: 2026-11-23T09:55:00-08:00
modified: 2026-11-23T09:55:00-08:00
level: L0
version: 1.0.0
description: Planner pass rewriting the donation passes around the confirmed 20 minute refill, with an early-run guard and the two overnight passes
status: done
activity: queue-planning
run_id: queue-planning-2026-11-23-0955-donation-passes
trigger: coordinator message 17:52Z, operator record 1745
started_at: 2026-11-23T09:50:00-08:00
finished_at: 2026-11-23T09:55:00-08:00
verified: grid predictions computed by script from 17:57:57Z; word counts under 450; validate exit 0
grounded_in:
  - source: _records_/2026-11-22/alliance-donations/1745-queue-run.md (as relayed by the coordinator)
---

# The donation passes after the refill test, 2980

The refill test settled it: an entry count of 9 at 17:45:43Z and a first cooldown timer ending 17:57:57, within 0.5 s of the 20-minute grid, confirm one refill per 20 minutes (H20) and reject 35 (H35, which predicted 5). The count is 3 an hour, 72 a day, and fills the cap of 30 in 10 hours; the 8 counts at 14:39Z were counts used elsewhere or partial accrual.

All three later passes now carry only the confirmed rule: the grid is 17:57:57Z plus 20 minutes times n, the predicted entry count is the count left after the previous pass plus the grid points passed since its last tap (pass 002 at 21:15:00Z predicts 10, then 11 from 21:18, 12 from 21:38, 13 from 21:58), and each pass logs the entry count and time, every tap, the first cooldown timer after the last tap with its read time, and the count left. Because a run costs about 0.3 USD, a pass runs at a count of about 10 to 12 and is released unrun if the entry count is under 6; the stated cost cap is 0.60 USD since 10 to 13 taps cost more than nine. The schedule stands at about every 3.5 hours: `donations-pass-2026-11-23-002` (21:15Z to 22:15Z), `donations-2026-11-23-1630` (00:30Z to 02:00Z), and two new overnight passes `-003` (03:45Z to 05:00Z) and `-004` (07:00Z to 07:55Z, before the 08:00Z quiet window). The passes after 08:25Z are staged at the daily pass. The optional tail and the two-hypothesis text are gone. The roster mints its own donations unit for each four-hour wave; I retire it when it appears, since these four cover the schedule.
