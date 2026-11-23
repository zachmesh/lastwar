---
title: Operator plunder and training notes 0054
created: 2026-11-23T16:12:00Z
modified: 2026-11-23T16:12:00Z
version: 1.0.0
description: Operator sidecar page - trade truck plunder rules, the 15:20Z finding, the three fights to 16:02Z and the blocked-training stat; the per-fight rows are in the CSV beside it
status: handover
grounded_in:
  - source: handover 0.9.0 section Plunder and training, moved 2026-11-23T15:12Z into the sidecar detail page and split out 2026-11-23T16:12Z
  - source: records truck-plunder 1405, 1506, 1523 and 1600
---

# Plunder and training notes

Part of [the sidecar](0054-operator-handover-detail.md). Per-fight rows: [0054-plunder-fights.csv](0054-plunder-fights.csv). Taps (hospital, trade, fight, deselect): [0054-routes.csv](0054-routes.csv), topics plunder and camera.

## Rules (moved verbatim)

- Trade trucks only (OD-20261123-20). Read the hospital first (tag Hospital Lv.25, orange middle button; free room = 7,999 minus Completed minus wounded; stop under 1,000 or after two fights each wounding over 100). Only the opened card decides: UR or SSR, guard below 24.96M, UR shard stack in the right half. Quick Plunder once, Battle once, at most two fights; never Collect.
- Blocked training closes with `--stat slots_blocked_by_capacity=N --stat capacity_blocker="Drill Ground Full"`.

## Finding (15:20Z to 15:26Z)

One fight, stacks only in slots 2 and 3 (left half): loot shard x3, resources about a third of the cargo, 0 wounded; the right-half rule is not a game fact.

## Results to 16:02Z

Fight 1 (14:25Z) UR Lv.30 paid 9 shards from stacks in slots 1, 5, 6, 7. Fight 2 (15:23Z) SSR Lv.24 paid 3 from slots 2 and 3. Fight 3 (16:02Z) SSR Lv.30, stacks x3 in slots 2 and 3, paid NO shard; it gave iron and food +761.5K, a chest and two puzzle pieces, and one red item was Reclaimed (not won). All three: 0 wounded. Count 3/4; hospital 364 of 7,999 wounded and 5,306 completed, unchanged. The half alone does not decide the shard payout.
