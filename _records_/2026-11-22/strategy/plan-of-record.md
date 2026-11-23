---
title: Plan of record, strategist, version 0.3
created: 2026-11-23T08:33:00Z
modified: 2026-11-23T20:04:00Z
version: 0.5.0
level: L3
description: The plan items with ids, levers, next actions, triggers, deadlines, expected gains and the measurement that closes each, from which the planner mints units; centre moved from capacity first to training slots first
status: unverified
grounded_in:
  - source: _records_/2026-11-22/strategy/plan-of-record.csv with machine-readable trigger and start-by times
  - source: _records_/2026-11-22/strategy/0030-slot-rules.md v1.2 and operator read _records_/2026-11-22/growth/0030-capacity-read.md
---

# Plan of record 0.4

Mac UTC, daily. Units carry `serves: PL-nn` or `serves: upkeep`. Start-by is trigger plus 2 hours (30 minutes for a slot). Columns in [the sidecar](plan-of-record.csv).

**Two lines.** Long line (owner order 12:33Z): Base Expansion and oil ([decision 03](dec-20261123-03.md), [path](base-expansion-path.csv)). Short line: training slots, nine ground levels, promotion. Plunder is a supplement.

| Id | Next action | Trigger | Deadline | Gain and tag | Closes with |
|---|---|---|---|---|---|
| PL-01 | Read X of Y, Construct list (done) | now | 11-23 13:00 | 0 | table |
| PL-02 | Read Age of Oil nodes (done) | 11:43 | 13:00 | 0 | rows |
| PL-03 | Box and Choice Chest opened | done | done | 0 | popup |
| PL-04 | Iron Output V running; 550 tech min to end with Food V | idle now | 13:30 | +3.9K or more a node [M] | lab, power |
| PL-05 | Monday drone feed from preview | D1 read | 11-24 01:30 | +25K to 90K [G] | drone |
| PL-06 | Earned currencies to shards after reads | reads | 11-26 02:00 | +0.3M a milestone [S1] | buys |
| PL-07 | Collect first, read twice, diff breakdown; batch test: no collect at Full | 13:00, 02:00 | weekly | 2.29M waits [M] | power |
| PL-08 | Builders: Oil Well Lv.21 to 30, three ground levels (decisions 07, 08) | 11-23 23:20 | 23:50 | +0.36M a level via new T10 [D] | queue |
| PL-09 | Slot arrival: X of Y, one Collect, train T10, Promote | Y above X | event plus 30 min | +329K per 200 slots; promote to +2.75M [D] | X of Y |
| PL-10 | Thursday medals and held shards | 11-26 02:00 | 11-27 02:00 | unread; node power [M] | skill, lab |
| PL-11 | Name Black Market tiles; Age of Oil stage 4 on 11-29 | 09:05 | 12:30 | 0 | names |
| PL-12 | Weekly review, season plan, digest | 11-29 20:00 | 11-30 04:00 | 0 | digest |
| PL-13 | Box batch 2 in an idle gap, else stop at 10 | idle | 11-24 14:00 | 0 now [G] | tiles |
| PL-14 | Supply: harvest, trucks, chests just in time | start in 2 h | 11-24 07:20 | 0; no shortage | records |
| PL-15 | Decoration gallery, Crystal Shop reads | idle | 11-24 04:00 | decor +7.7K a day [M] | rows |
| PL-16 | Base Expansion line: the chain, one lab at a time | 12:45 | continuous | ETA 2027-01-08 to 01-23, oil row unverified [G] | rows |
| PL-17 | Oil Well Lv.21 to 30 chain, collect every 10 hours, depot daily | 11-23 23:20 | 00:30 | +60 oil an hour a level [M] | well, oil |
| PL-18 | Plunder at margin 1.2, casualty guard | roster | 11-24 02:00 | 0.73M food and iron, 0.47M coin, 4 shards a fight [M] | fights |

## Dated corrections

- **2026-11-23 18:15Z.** Builders free 23:20Z today, not 11-24 09:20Z (record 1806, two reads; "09:20" was the Oil Well Lv.21 duration). The Oil Well stands at Lv.20: B1 chains Lv.21 to 30 (record 1553). Research time is the button (base over 3.30) less a flat 4h12m; 3.678 was a short node ([decision 08](dec-20261123-08.md), [ETA](0510-base-expansion-eta.md)).

## Rules

- [Slot rules v1.5](0030-slot-rules.md), [timing lessons](0208-timing-lessons.md), [box](0117-box-policy-v1.md), [Black Market](0133-black-market-policy-v1.md), [store](0147-store-ranking-v1.md) policies.
- No forecast, no unit: see `forecast_ids` and [the ledger](forecast-ledger.csv). A playbook test serves `upkeep`; store and Black Market buys serve PL-06.
