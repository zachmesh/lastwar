---
title: Queue Planning Catch-up Cadence And Owner Addendum Units 2315 2026-11-22
created: 2026-11-22T23:17:00-08:00
modified: 2026-11-22T23:17:00-08:00
level: L0
version: 1.0.0
description: Planner pass for assignment A-20261123-0706 and its addendum - a per-regular cadence table, 12 staggered catch-up units for 07:15Z to 10:03Z, Season Photo and trophy units, builds held, and an idle-gap simulation that falls from 168 to 15 minutes
status: done
activity: queue-planning
run_id: queue-planning-2026-11-22-2315-catchup-cadence
trigger: coordinator assignment A-20261123-0706-planner, addendum and correction
started_at: 2026-11-22T23:05:34-08:00
finished_at: 2026-11-22T23:17:00-08:00
verified: all 14 units read back with briefs and validate exit 0; pick_key simulation run before and after at two pace models
grounded_in:
  - source: _records_/2026-11-22/queue-planning/2315-catchup-cadence.csv, 18 rows
  - source: _tools_/queue.py plan_windows (step of 4 hours at line 1608), pick_key, _fixed_slots
  - source: the rule digests and records cited per row in the CSV
---

# Catch-up cadence, 2315

Rows are in [the CSV](2315-catchup-cadence.csv).

## 1. Why there was a dead zone

It is a staging gap. `plan` stages every-run regulars on a 4-hour step (`_tools_/queue.py:1608`), but the 22:03 PT wave (06:03Z to 10:03Z) was never staged: the 11-22 done units carry slot tags 0203, 0603, 1003, 1403 and 1803, and no 2203. The :57 segment (events, treasures, secrets) has no unit for the 06:57Z or 10:57Z waves either. I did not run `plan`: it would stage about 19 units, all eligible at once.

## 2. Cadence: 18 regulars, 8 with units

- **Supported in the gap:** donations (refill about 20 minutes), arms-race (open and close of the phase), secrets (30-minute tasks, plundered if left), harvest, radar, survivors, trucks (due about 08:53Z), help.
- **Not supported before 10:03Z:** research (slot 2 ends 10:03Z), building-queues (4 of 4 busy), training (batch ends unknown), treasures (fragments at zero).
- **Calendar-bound:** train (the To-do List), vip and daily-missions (00:30Z fix-ups).

## 3. How the queue can express it

- **Base layer:** `queue.py plan --hours 8` each hour, so two waves always exist.
- **Intra-window cadence:** the roster has no shorter-window field. A roster entry with `cadence: fixed-slots` and a `fixed_slots` list of HH:MM times (`_fixed_slots`, wall-clock PT) would stage them. Its window end is unverified.
- **For now:** hand-minted priority 2 units, each expiring by 10:03Z. They sort ahead of the 11-24 sweep (expiry, then priority, then creation), so the 2-hour aging rule cannot reorder it.

## 4. Units minted, all with briefs

- 12 catch-up units, 07:15Z to 10:03Z, one every 10 to 15 minutes.
- **Season Photo:** `passes-2026-11-23-0712`, priority 3, 07:45Z to 12:00Z, with the exact owner text.
- **Trophy:** `scout-midday-2026-11-23-0712`, priority 2, 10 minutes, 08:00Z to 10:03Z. It was minted read-only before your correction; I edited that one unit to identify and claim, with no fight, and left a slot for the researcher's paragraph. No second unit.
- **Quick Dispatch:** allowed in the survivors unit, survivor context only.
- **Build:** not minted; digest items 2 and 3 still read the old text at 07:12Z.

## 5. Proof

`validate` exit 0. Operator simulated, 07:15Z to 11:15Z:
- **Before:** 14 units, longest idle gap 168 minutes.
- **After, at the observed 3.0 minutes per unit:** 28 units, no gap over 15 minutes until 10:48Z, then 27 minutes because nothing is staged past the 10:30Z wave.
- **After, at each unit's estimate:** longest gap 12 minutes.

## 6. `_queue_/completed/`

Completion markers: `record_completion` writes one small file per executed closing (`unit`, `status`, `finished_at`, `executor`) so a unit closed elsewhere is never re-picked (issue #438). Live-only state: ignored by `_queue_/.gitignore` line 8, never tracked, reaped by `sync`.
