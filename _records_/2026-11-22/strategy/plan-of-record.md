---
title: Plan of record, strategist, version 0.3
created: 2026-11-23T08:33:00Z
modified: 2026-11-23T16:09:00Z
version: 0.4.0
level: L3
description: The plan items with ids, levers, next actions, triggers, deadlines, expected gains and the measurement that closes each, from which the planner mints units; centre moved from capacity first to training slots first
status: unverified
grounded_in:
  - source: _records_/2026-11-22/strategy/plan-of-record.csv with machine-readable trigger and start-by times
  - source: _records_/2026-11-22/strategy/0030-slot-rules.md v1.2 and operator read _records_/2026-11-22/growth/0030-capacity-read.md
---

# Plan of record 0.4

Mac UTC, daily. Units carry `serves: PL-nn` or `serves: upkeep`. Start-by is trigger plus 2 hours (30 minutes for a slot). Columns in [the sidecar](plan-of-record.csv).

**Two lines (12:45Z).** Long line, owner order 12:33Z: Base Expansion and oil ([decision 03](dec-20261123-03.md), [path](base-expansion-path.csv)). Short line: training slots first, nine ground levels and promotion. Plunder is last ([decision 04](dec-20261123-04.md)).

| Id | Next action | Trigger | Deadline | Gain and tag | Closes with |
|---|---|---|---|---|---|
| PL-01 | Read X of Y, Construct list | now | 11-23 13:00 | 0, decides rules | ground table |
| PL-02 | Read the Age of Oil nodes: cost, oil, time, power | 11:43 | 13:00 | 0, decides labs | node rows |
| PL-03 | Box and Choice Chest opened | done | done | 0 | popup text |
| PL-04 | Iron Output V running; 550 tech min to end with Food V | idle now | 13:30 | +3.9K or more a node [M] | lab item, power |
| PL-05 | Monday drone feed from the preview | D1 read | 11-24 01:30 | +25K to 90K [G] | drone line |
| PL-06 | Earned currencies to shards after reads | reads | 11-26 02:00 | +0.3M a milestone [S1] | purchases, power |
| PL-07 | Collect first, read twice, diff breakdown; batch tests 19:56, 11:18 | 13:00, 02:00 | weekly | A +0.98M and +1.31M free; B none [M] | toast, power |
| PL-08 | Builders: Oil Well Lv.21 to 30, three ground levels (decision 07) | 11-24 09:20 | 10:00 | +0.36M a level via new T10 [D] | queue, Y up 200 |
| PL-09 | Slot arrival: X of Y, one Collect tap, train T10, Promote | Y above X | event plus 30 min | +329,400 per 200 slots; promotion up to +2.75M [D] | X of Y, power |
| PL-10 | Thursday skill medals and held shards; lab 2 Iron Output V | 11-26 02:00 | 11-27 02:00 | unread; node power [M] | skill line, lab item |
| PL-11 | Name Black Market tiles; Age of Oil stage 4 on 11-29 | 09:05 | 12:30 | 0 | names |
| PL-12 | Weekly review, season plan, owner digest | 11-29 20:00 | 11-30 04:00 | 0 | digest draft |
| PL-13 | Box batch 2: one slider Use of 11 in an idle gap, else stop at 10 | idle | 11-24 14:00 | 0 now [G] | popup tiles |
| PL-14 | Convert chests just in time | start in 2 h | 11-24 07:20 | 0; no shortage | convert records |
| PL-15 | Decoration gallery, Crystal Shop reads | idle | 11-24 04:00 | decor +7.7K a day [M] | rows, prices |
| PL-16 | Base Expansion line: both labs on the critical path | 12:45 | continuous | ETA 2027-01-08 to 01-23, oil row unverified [G] | node rows |
| PL-17 | Oil Well Lv.21 to 30 chain, collect every 10 hours, depot daily | 11-24 09:20 | 12:00 | +60 oil an hour a level [M] | well level, oil |
| PL-18 | Truck plunder at margin 1.2 or more, casualty guard | roster | 11-24 02:00 | 0.73M food and iron, 0.47M coin, 4 shards a fight [M] | fight records |

## Rules the table relies on

- [Slot rules v1.4](0030-slot-rules.md); [timing lessons](0208-timing-lessons.md). Policies: [box](0117-box-policy-v1.md), [Black Market](0133-black-market-policy-v1.md), [stores](0147-store-ranking-v1.md).
- No forecast, no unit: see `forecast_ids` and [the ledger](forecast-ledger.csv). A playbook test with no growth claim serves `upkeep`; store and Black Market buys serve PL-06.
