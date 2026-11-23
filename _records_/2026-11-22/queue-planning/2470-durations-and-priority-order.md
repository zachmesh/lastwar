---
title: Queue Planning Unit Durations And Operator Priority Order 2470 2026-11-23
created: 2026-11-23T01:45:00-08:00
modified: 2026-11-23T01:45:00-08:00
level: L0
version: 1.0.0
description: Planner pass after the measured unit durations - the operator priority order mapped onto staged units, the 12:51Z Secrets claim staged, batch end times corrected, and the daily duration median method
status: done
activity: queue-planning
run_id: queue-planning-2026-11-23-0145-durations-and-order
trigger: coordinator message with the measured durations and the priority order
started_at: 2026-11-23T01:43:00-08:00
finished_at: 2026-11-23T01:45:00-08:00
verified: durations recomputed from the done units; pick order simulated at 12:51Z and 19:58Z; validate exit 0
grounded_in:
  - source: result.duration_seconds in the done units under _queue_/done
  - source: _queue_/done/scout-midday-growth-snapshot-2026-11-23-004.md, the T1 barracks read
---

# Durations and priority order, 2470

## 1. Measured

From the done units whose `finished_at` falls on 2026-11-23 UTC and whose `duration_seconds` is a number (39 units): median 1.9 minutes, mean 2.1, p90 3.5, max 5.1; growth units alone (9) median 2.2. The coordinator's 15 units gave median 2.0 and max 4.7, so the two agree. With the dispatch handoff of 1 to 2 minutes the real wall time is about 4 to 5 minutes, the scenario in which no staged unit expires. Older done units carry an empty `duration_seconds` and are skipped. Each morning I add this figure to the pool-load note with: `list_units(root, "done")`, keep `result.finished_at` on the date, keep numeric `result.duration_seconds`, report median, mean, p90 and max, and count the units that expired. If more than 2 expire in an hour I say so and withdraw P1 and B1.

## 2. Priority order, as staged

1. The 4-hour Secrets claim: `secrets-2026-11-23-0944`, 12:50Z to 13:20Z, an earlier expiry than every other unit open then.
2. The lab conversion `research-growth-convert-2026-11-23-001` at 11:44Z and the builders `building-queues-growth-convert-2026-11-24-001` at 09:22Z on 2026-11-24.
3. The fixed-state power pair: slot B 13:00Z, slot A 02:00Z on 2026-11-24.
4. The Age of Oil claim unit `-022`, before 10:30Z.
5. Routine claims, then 6. the reads.
7. The second Mystery Supply Box batch is not staged: the Strategist decides, and it runs only in an idle gap.

## 3. Batch times corrected

The T1 read puts the Lv.27 T9 x726 batch end at 19:56:34Z (11:49:49 left at 08:06:45Z) and the Lv.30 T10 x793 batch at 2026-11-24T11:18:31Z. I had 19:53Z and 11:13Z. The collect unit opened at 19:55Z, before the batch ended, so it could have run and failed; it now opens at 19:58Z, and the power units say 19:56Z and 11:18Z.
