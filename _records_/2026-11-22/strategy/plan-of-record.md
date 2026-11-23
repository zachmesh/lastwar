---
title: Plan of record, strategist, version 0.3
created: 2026-11-23T08:33:00Z
modified: 2026-11-23T12:55:00Z
version: 0.4.0
level: L3
description: The plan items with ids, levers, next actions, triggers, deadlines, expected gains and the measurement that closes each, from which the planner mints units; centre moved from capacity first to training slots first
status: unverified
grounded_in:
  - source: _records_/2026-11-22/strategy/plan-of-record.csv with machine-readable trigger and start-by times
  - source: _records_/2026-11-22/strategy/0030-slot-rules.md v1.2 and operator read _records_/2026-11-22/growth/0030-capacity-read.md
---

# Plan of record 0.4

Mac UTC, daily. The planner mints units only from these ids; each unit carries `serves: PL-nn` or `serves: upkeep`. Start-by is trigger plus 2 hours (30 minutes for a slot). Full columns in [the sidecar](plan-of-record.csv).

**Two lines (12:45Z).** Long line, owner order 12:33Z: Base Expansion and oil ([decision 03](dec-20261123-03.md), [path](base-expansion-path.csv)). Short line: training slots first, nine ground levels and promotion. Plunder is last ([decision 04](dec-20261123-04.md)).

| Id | Next action | Trigger | Deadline | Gain and tag | Closes with |
|---|---|---|---|---|---|
| PL-01 | Read X of Y, Construct list | now | 11-23 13:00 | 0, decides rules | ground table |
| PL-02 | Read the Age of Oil nodes: cost, oil, time, power | 11:43 | 13:00 | 0, decides labs | node rows |
| PL-03 | Box and Choice Chest opened | done | done | 0 | popup text |
| PL-04 | Lab 1: FOOD OUTPUT V now; tech speed-ups first; read M | idle now | 13:30 | +3.9K or more a node [M] | lab item, power |
| PL-05 | Monday drone feed from the preview | D1 read | 11-24 01:30 | +25K to 90K [G] | drone line |
| PL-06 | Earned currencies to shards after reads | reads | 11-26 02:00 | +0.3M a milestone [S1] | purchases, power |
| PL-07 | Collect first, read twice; batch tests 19:56, 11-24 11:18 | 13:00, 02:00 | weekly | A +0.98M and +1.31M free; B none [M] | toast, power |
| PL-08 | Builders: Oil Well, HQ 31 prerequisite if red, two or three ground levels | 11-24 09:20 | 10:00 | +0.36M a level via new T10 [D] | queue, Y up 200 |
| PL-09 | Slot arrival: X of Y, one Collect tap, train T10, Promote | Y above X | event plus 30 min | +329,400 per 200 slots; promotion up to +2.75M [D] | X of Y, power |
| PL-10 | Thursday skill medals; lab 2 Complete and next node | 11-26 02:00, 07:19 | 11-27 02:00 | unread; node power [M] | skill line, lab item |
| PL-11 | Name Black Market tiles; read Age of Oil stage 4 on 11-29 | 09:05 | 12:30 | 0 | names |
| PL-12 | Weekly review, season plan, owner digest | 11-29 20:00 | 11-30 04:00 | 0 | digest draft |
| PL-13 | Box batch 2 as one slider Use of 11 in an idle gap, else stop at 10 | idle | 11-24 14:00 | 0 now [G] | popup tiles |
| PL-14 | Convert chests just in time | start in 2 h | 11-24 07:20 | 0; no shortage | convert records |
| PL-15 | Decoration gallery and Crystal Shop reads | idle | 11-24 04:00 | decor line +7.7K a day [M] | rows, prices |
| PL-16 | Base Expansion line: both labs on the critical path | 12:45 | continuous | ETA 5 to 15 weeks [G] | node rows |
| PL-17 | Oil Well from 09:20Z, collect every 8 hours, depot secret daily | 11-24 09:20 | 12:00 | 60 oil an hour a level [S1] | well level, oil |
| PL-18 | Truck plunder under the casualty guard | roster | 11-24 02:00 | coin 0.2M to 0.58M a fight [S1] | fight records |

## Rules the table relies on

- [Slot rules v1.4](0030-slot-rules.md); [timing lessons](0208-timing-lessons.md). Policies: [box](0117-box-policy-v1.md), [Black Market](0133-black-market-policy-v1.md), [stores](0147-store-ranking-v1.md).
- No forecast, no unit: see `forecast_ids` and [the ledger](forecast-ledger.csv).
