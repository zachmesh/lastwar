---
title: Plan of record, strategist, version 0.3
created: 2026-11-23T08:33:00Z
modified: 2026-11-23T09:39:00Z
version: 0.3.2
level: L3
description: The plan items with ids, levers, next actions, triggers, deadlines, expected gains and the measurement that closes each, from which the planner mints units; centre moved from capacity first to training slots first
status: unverified
grounded_in:
  - source: _records_/2026-11-22/strategy/plan-of-record.csv with machine-readable trigger and start-by times
  - source: _records_/2026-11-22/strategy/0030-slot-rules.md v1.2 and operator read _records_/2026-11-22/growth/0030-capacity-read.md
---

# Plan of record 0.3

Mac UTC, daily. The planner mints units only from these ids; each unit carries `serves: PL-nn` or `serves: upkeep`. Start-by is trigger plus 2 hours (30 minutes for a slot). Full columns in [the sidecar](plan-of-record.csv).

**Centre, 08:42Z.** Training slots first. The hospital Collect looks all or nothing (untested): the 5,306 are a ceiling. A slot is +1,647 as new T10, once a level or ground completes.

| Id | Next action | Trigger | Deadline | Gain and tag | Closes with |
|---|---|---|---|---|---|
| PL-01 | Read capacity: X of Y, every ground, coin lines | now | 11-23 09:30 | 0, decides rules | ground table |
| PL-02 | Read research: Extra Drill Ground, Valor, Expansion text | 09:05 | 11:30 | 0, decides lab | node rows |
| PL-03 | Open one Mystery Supply Box, one Choice Chest | 09:30 | 12:00 | 0, decides shards, coin | popup text |
| PL-04 | Lab 1: Complete, then Extra Drill Ground or its shortest prerequisite | lab free 11:43 | 12:15 | up to +3.29M, 2,000 slots as new T10 [D] | lab item, power |
| PL-05 | Monday drone feed from the preview | D1 read | 11-24 01:30 | +15K to 60K a week [G] | drone line |
| PL-06 | Earned currencies to shards by the Black Market policy | PL-02, PL-03 | 11-24 18:00 | +0.3M a milestone [S1] | purchases, power |
| PL-07 | Collect first, read twice; batch tests 19:56, 11-24 11:18 | 13:00, 02:00 | weekly | A: +0.98M and +1.31M free; B: none [M per unit] | toast, exact power change |
| PL-08 | Builders: two ground levels or one kept for the new ground; speed-up 10,000 minutes at most | 11-24 09:20 | 11-24 10:00 | +0.35M a level via new T10 [D] | queue, Y up 200 |
| PL-09 | Slot arrival: read X of Y; one hospital Collect tap (test); train new T10 into free slots; Promote | Y above X | event plus 30 min | +329,400 per 200 slots; promotion up to +2.75M [D] | X of Y, tiers, power |
| PL-10 | Thursday skill medals; lab 2 Complete and start | 11-26 02:00, 07:19 | 11-27 02:00 | unread; +15K a node [M] | skill line, lab item |
| PL-11 | Name Black Market tiles; claim free Age of Oil stage 3 rewards | 09:05 | 12:30 | 0 | names, claim |
| PL-12 | Weekly review, season plan, owner digest | 11-29 20:00 | 11-30 04:00 | 0 | digest draft |
| PL-13 | Sample up to 22 boxes in two batches, quantity 1 each, stop at a rare hit | 09:15 | 11-23 14:00 | 0 now; unknown [G] | 22 popups |
| PL-14 | Convert chests just in time per the box policy | start in 2 h | 11-24 07:20 | 0; no shortage | convert records |

## The 19:56Z test and what each outcome does

- **A, Collect works under Full.** Queued batches already count: +0.98M and +1.31M on 11-24 are free; a requeue costs a slot.
- **B, refused naming 726.** The first 1,519 slots go to the two batches, then new T10; the new ground is more urgent.

## Rules the table relies on

- [Slot rules v1.2](0030-slot-rules.md); speed-up cap 35,000 minutes a week. Conversions: [box policy](0117-box-policy-v1.md); Black Market: [policy](0133-black-market-policy-v1.md).
- No forecast, no unit: see `forecast_ids` and [the ledger](forecast-ledger.csv).
