---
title: Queue Planning Growth Units Staged 2350 2026-11-22
created: 2026-11-22T23:52:00-08:00
modified: 2026-11-22T23:52:00-08:00
level: L0
version: 1.0.0
description: Planner staging of Epic 867 growth units - ten read-only snapshot units from the scout protocol and eight read-then-fill units from the 2350 decision record, minted as two chains, with a pace simulation
status: done
activity: queue-planning
run_id: queue-planning-2026-11-22-2350-growth-units-staged
trigger: coordinator staging instruction after the scout snapshot protocol landed
started_at: 2026-11-22T23:48:00-08:00
finished_at: 2026-11-22T23:52:00-08:00
verified: 18 units read back with briefs and validate exit 0; the full pool simulated at three pace models with the tool's pick_key
grounded_in:
  - source: _records_/2026-11-22/perception-scout/2345-snapshot-protocol.md and 2345-snapshot-units.csv
  - source: _records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md
  - source: _tools_/queue.py pick_key, _chain_head_refusal and _window_aged_priority1
---

# Growth units staged, 2350

## 1. Core read-only chain

Chain `growth-snapshot-2026-11-23`, regular `scout-midday`, priority 2, ids `scout-midday-growth-snapshot-2026-11-23-001` to `-010`, in the coordinator's run order. Briefs are generated from the scout's CSV, so the route, fields, step cap and notes are not retyped, and they carry stop rules S1 to S7, the red lines and `serves: snapshot (Story 868)`.

| Seq | Unit | Window (Z) |
|---|---|---|
| 001 to 003 | P1, T2, F1 | 08:00 to 08:43, 08:44, 08:45 |
| 004 to 010 | T1, B1, R1, F2, H1, H2, H3 | 09:05 to 11:00, 11:02, 11:04, 11:06, 11:08, 11:10, 11:12 |

Run order comes from staggered expiries, since `next` sorts by expiry first. No core window overlaps 08:45Z to 09:05Z.

## 2. Fill chain

Chain `growth-fill-2026-11-23`, regular `building-queues`, priority 1, 10 minutes, ids `building-queues-growth-fill-2026-11-23-001` to `-008`. Windows start 08:15, 09:05, 09:35, 10:05, 10:35, 11:05, 11:35 and 12:05Z, each 30 minutes. Brief: the 2350 decision, the reserves (food 100M, iron 150M, coin 10M, diamonds untouched, duel-day reservation), builder priority, lab order, train from surplus, and `serves: fill idle slot`. Departure from the requested grid: the 08:45Z slot moved to 09:05Z so no growth unit runs against the 08:50Z Secrets claim.

## 3. Simulation, 08:00Z to 12:45Z

- **Flat 3.0 minutes per unit:** 44 units run, none expires unrun.
- **Mixed pace, estimate for growth units:** 44 run, none expires; core P1, T2, F1 start 08:00, 08:06, 08:26; the Secrets claim starts 08:58.
- **Every unit at its estimate:** 37 run and H2 expires unrun at 11:10Z; the pool is oversubscribed after 09:05Z at that pace. The claim starts 08:54.

## 4. Two cautions

- **Priority 1 aging:** `_window_aged_priority1` re-times a priority 1 unit older than 4 hours once its window opens. Fills 007 and 008 open after 11:49Z and could be re-timed by a `sync`. I check at the next pass and re-mint if so.
- **Secrets claim:** it runs 0 to 8 minutes late depending on pace, because a 10-minute unit may be mid-run at 08:50Z. The coordinator's own claim covers it.
