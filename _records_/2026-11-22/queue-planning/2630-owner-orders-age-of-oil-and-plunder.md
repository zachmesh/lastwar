---
title: Queue Planning Owner Orders Age Of Oil Research And Truck Plunder 2630 2026-11-23
created: 2026-11-23T04:49:00-08:00
modified: 2026-11-23T04:49:00-08:00
level: L0
version: 1.0.0
description: Planner pass on the three owner orders of 12:36Z - the lab unit re-pointed at the Age of Oil critical path with a survey unit staged, two guarded trade-truck plunder units staged, the near-zero coin checked against the builder formulas, and the pool simulated from the 12:49Z resume
status: done
activity: queue-planning
run_id: queue-planning-2026-11-23-0449-owner-orders
trigger: coordinator message with OD-20261123-18, -19 and -20 and the resume at 12:49:13Z
started_at: 2026-11-23T04:44:00-08:00
finished_at: 2026-11-23T04:49:00-08:00
verified: the three decision records read in full; the plunder articles and the 0953 trucks record read; coin arithmetic recomputed; pool simulated at 5 and 8 minutes per unit; validate exit 0
grounded_in:
  - source: _records_/retro/owner-decisions-log/od-20261123-18.md, -19.md and -20.md
  - source: _activities_/truck-plunder/how-it-p1-2.md and rule-digest.md
---

# Owner orders, Age of Oil research and truck plunder, 2630

## 1. Research

The Special Forces fill is withdrawn. `research-growth-convert-2026-11-23-002` (12:55Z to 14:30Z) now says: NODE is the node the Strategist names, none named is a read-only survey; both lab slots are read first; conversion only just in time under the formula, capped at 24 UR chests (87 minus the 63 the builders need from near-zero coin). `research-age-of-oil-survey-2026-11-23-001` (priority 1, read-only, window 12:55Z to 14:00Z) reads every node of the tree that holds Unlock Oil Well: tag text, level, effect, coin, iron, food and oil cost, effective time, prerequisite, power gain, with the Oil Output chains, More Oil Wells and Base Expansion marked, pressing nothing. OD-19 also amends the speed-up rule for research (tech items first, at least 15,360 minutes, then general items up to 15 percent of the stock a week, about 53,000 minutes, never Finish Now); I will use it when the research units are staged.

## 2. Plunder

OD-20 re-enables plunder for trade trucks only; the Arena, gold-trophy fights, rallies, General's Trial and base attacks stay forbidden. `trucks-plunder-2026-11-23-001` (13:30Z to 18:00Z) and `-002` (18:00Z to 2026-11-24T01:30Z) each read the Hospital first, stop at free room under 1,000 or two fights in a row wounding more than 100 troops each, take only gold or purple trucks carrying UR shard stacks with a guard under Squad 1 and the shard on the right, use Quick Plunder, fight at most twice, and record wounded, coin and shards per fight without player names. The Plunder Count read 0/4 and resets at 02:00Z. Free room is about 2,300, so the guard is tight: four fights that each wound 150 troops would end at about 1,700. The rule digest for truck-plunder still says plunder is barred, which the scribe must update.

## 3. Coin

Coin is 55.9K, so tomorrow's formulas give N = 63 UR chests for the first two grounds (not 59), leaving 24 UR, 71 SSR and 122 SR, about 128.6M, above the 50M fixed-chest reserve; the coin after the first two starts is about 10.8M and the plain-chest count about 19,700. Nothing staged spends coin except just-in-time conversions.

## 4. Pool

Simulated from 12:49:13Z at 5 and at 8 minutes per growth, survey and plunder unit: no unit expires. The Secrets claim runs at about 12:54Z, the Age of Oil survey at about 13:12Z, the lab unit at about 14:00Z, the weapon and hero reads from about 14:24Z, and plunder at about 14:19Z and 18:00Z.
