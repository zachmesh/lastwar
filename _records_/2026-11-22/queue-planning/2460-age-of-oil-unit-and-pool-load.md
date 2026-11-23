---
title: Queue Planning Age Of Oil Claims Unit And Pool Load 2460 2026-11-23
created: 2026-11-23T01:42:00-08:00
modified: 2026-11-23T01:42:00-08:00
level: L0
version: 1.0.0
description: Planner pass after the SC1 season-clock read - the Age of Oil stage claims unit staged, D1 re-minted, and a pool-load simulation that led to window changes on eleven unclaimed units
status: done
activity: queue-planning
run_id: queue-planning-2026-11-23-0142-aoo-and-load
trigger: coordinator message with the Age of Oil read-and-claim unit
started_at: 2026-11-23T01:38:00-08:00
finished_at: 2026-11-23T01:42:00-08:00
verified: SC1 record read in full; the pool simulated at four paces with the tool's ordering before and after; word counts under 450; validate exit 0
grounded_in:
  - source: _records_/2026-11-22/perception-scout/0935-sc1-season-clock.md
  - source: _tools_/queue.py pick_key and _actionable
---

# Age of Oil unit and pool load, 2460

## 1. Staged

- `scout-midday-growth-snapshot-2026-11-23-022`, priority 2, 10 minutes, 09:40Z to 10:30Z, `serves: baseline Age of Oil`. Open the Age of Oil page; for each stage card read task, progress, reward and the Claim button; press Claim only for a free reward with no cost-bearing choice, the one exception to rule R1; stop and record any price, diamond, choice or cost confirmation; record what each claim paid. On the Events list only the names and timers of Desert Battlefield, Winter Battlefield and Wanted Boss, none entered. The stage 4 timer stays an open question for the unit to answer if visible.
- The Black Market buy unit is not staged: it waits for the Strategist's ranking.
- D1 was re-minted (`-023`, 09:40Z to 10:20Z) because its first window expired unrun, as did fill 001 and `secrets-0710`.

## 2. Pool load

The pool is oversubscribed. Simulated from 09:50Z to 14:30Z, as staged: 4 units expire unrun at 5 minutes per growth read and 11 at 10 minutes. The routine claims were due by 09:55Z to 10:03Z and cannot all fit.

## 3. Window changes, by hand, all unclaimed

- ST1b expiry 09:47Z to 10:25Z, so a store read does not starve harvest and trucks.
- Routine units help, arms-race 0711, the trophy unit and secrets 0712: expiry to 10:30Z.
- R1, F2, H1, H2, H3, S1b and C1: expiry to 13:30Z.

Result: 0 expire at 5 minutes per read; at 10 minutes 4 expire (trophy, secrets 0712, C1 and the Age of Oil unit), lab conversion 11:51Z, power slot B 14:13Z instead of 13:00Z. The trade-off is that the order now depends on the operator's real pace, which is unmeasured. P1 and B1 are low value and could be withdrawn to free about 14 minutes.

## 3. Not minted

The approved 10:48Z to 14:03Z catch-up set: the pool is full through 14:30Z at a 5-minute pace, so it would only add units that expire.
