---
title: Build
created: 2026-11-23T08:05:06Z
modified: 2026-11-23T13:52:53Z
level: L1
version: 0.3.0
description: Builders, the start rule and reserves, the order of upgrades under strategy v2.0 and the per-level building power table
status: unverified
grounded_in:
  - source: records _records_/2026-11-22/growth/2344-fill-run.md and _records_/2026-11-22/growth/2357-troop-read.md
  - source: the profile _activities_/upgrade-builders-hut-to/INDEX.md
  - source: decision records _records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md and _records_/2026-11-22/team-operations/2401-growth-strategy-decision.md and _records_/retro/owner-decisions-log/od-20261109-02.md
  - source: tool _tools_/resource_map.py (commit 99bc35b6)
---
# Build

Construction gives little power per slot compared with capacity ([the one idea](strategy-one-idea.md)).

## State

- Builders 4 of 4 busy at 2026-11-23 07:48Z, all on the Lv.25 Training Base, finishing near 2026-11-24T09:20Z; nothing was startable (`_records_/2026-11-22/growth/2344-fill-run.md`).
- Coin read 9.6M, under the 10M floor, so no coin-costing start was allowed and that is the recorded reason (same record).

## Rules and order

- Start rule (`_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`): an idle builder starts the best resource-only upgrade costing at most one third of the stock of each resource it needs, coin included; read first, fill only idle slots, never cancel or reorder a running item; no purchase, diamond spend or speed-up. Reserves: food 100M, iron 150M, coin 10M, diamonds untouched, plus the duel-day reservation ([charter](charter.md)).
- Strategy v2.0 (later): the first free builder goes to capacity by slots per million coin (step P2); other builders take the best power per slot-day; Oil Well levels 1 to 9 take only food and iron (step P8, [plan](strategy-plan-p2.md)). HQ 31 stays off the plan: about 510M coin, 1.44M oil and about 111 days of base timer (wave-2 research, relayed, unverified); the Lv.30 barracks upgrade also needs a Lv.31 Headquarters (`_records_/2026-11-22/growth/2357-troop-read.md`). The later record governs.
- Superseded 2026-11-23 by OD-20261123-18 (`_records_/retro/owner-decisions-log/od-20261123-18.md`): HQ 31 and Age of Oil are back on the plan; see `_records_/2026-11-22/strategy/plan-of-record.md`.
- The owner spends coin by hand in bursts, for example Training Base builds near +17.5K per level ([owner decisions](strategy-owner-decisions.md)).

## Measured and sourced

- Builders Hut Lv.25 to 26: Power 90,800 to 108,300 (+17,500) for 7d 07:16:49 displayed, about 2,400 per builder-day [M] (`_activities_/upgrade-builders-hut-to/INDEX.md`).
- [building-power-gains-L25-31.csv](building-power-gains-L25-31.csv): 211 rows over 31 buildings, one third-party guide, so [S1] and unverified.
- `resource_map.py snap` accepts K, M, G and B suffixes (commit 99bc35b6).

## Changelog

- 0.2.0, 2026-11-23 - Order rewritten for strategy v2.0 (capacity first, HQ 31 off); the tool note merged into the page; tags renamed.
