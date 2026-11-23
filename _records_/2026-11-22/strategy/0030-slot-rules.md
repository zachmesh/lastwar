---
title: Slot rules for the planner v1.5
created: 2026-11-23T08:33:00Z
modified: 2026-11-23T18:12:00Z
version: 1.5.0
level: L3
description: The allocation rules for the free labs and builders, the speed-up order, the slot-arrival protocol and the training rule once four Drill Grounds are known to exist
status: unverified
grounded_in:
  - source: _records_/2026-11-22/strategy/0030-dg-level-table.csv and 0250-read-identity-rule.md
  - source: operator record _records_/2026-11-22/growth/1047-f1b-drill-ground.md, four Drill Grounds at Lv.26, 27, 28 and 30
  - source: operator read 0030-capacity-read.md, hospital Collect has no selector
---

# Slot rules v1.5

Rules, not units. Costs in [the level table](0030-dg-level-table.csv). Change since 1.4: decisions 05 to 07 and the measured research times.

## Lab rule

1. Press Complete at once at every finish; log Total Power before and after.
2. The chain (decision 05): the Output V trio, then Oil Output I levels 1 to 10 serial on one lab (43 days natural), then the pairs. Before each start read the full cost list (any oil row), the oil counter and the Finish Now clock (the Research button minus 15,120 s); if nothing is startable, report in one pass.
3. Speed-ups: tech items first (9,895 left), then general up to 30 percent of the stock a week, keeping 100,000 general minutes until Steer A releases them; never Finish Now; spend only on time-bound levels (oil held for the next); log minutes, new finish and oil.
4. Free lab: fill it with the best power per lab-day node from a real preview (Special Forces about +15K a level, 3 days, about 750 power per million coin [D]); coin under 25M a node, ending before the chain needs the lab; coin for the path comes first. Defense Training VIII is not restarted without the owner.
5. A lab idle over 30 minutes is a miss.

## Builder rule (four builders at 23:20Z on 11-23, decisions 07 and 08)

1. B1 the Oil Well from Lv.21 (it stands at Lv.20) without idling: one building, one builder, Lv.21 to 30 in 22 days naturally. B2, B3 and B4 the Lv.26, 27 and 28 ground levels, lowest first (34.7K, 25.1K and 19.6K a builder-day with T10, 23.2K for the first with T8); three need coin 262M, food 978M, iron 321M. Skip the Lv.30 ground, Hut, Gold Mine and Farmland steps (3.2K or less).
2. HQ 31 is the last builder job, after Base Expansion; never the owner's running queue; every resource stays above its floor. Chests are converted 2 hours before, by the box policy.

## Speed-up pools

Construction items (167,895 minutes) are for builders only: the well, the ground ladder (14,550, 20,370 and 26,481 minutes), then HQ 31; at most 10,000 minutes an upgrade and 35,000 a week, applied after the Tuesday window opens at 02:00Z on 11-24. Tech and general items are for research only.

## Slot-arrival protocol (X exceeds Y, or a level completes)

1. Read X of Y on the Drill Ground troops panel (small button).
2. One hospital Collect tap before any training (H16).
3. Collect a finished batch if the batch test shows it needs room.
4. Train T10 at the idle Lv.30 barracks into exactly the free slots (T8 at the Lv.24 barracks if it is busy).
5. Start Promote on an idle barracks when its gain is positive, T7 first; log power before and after each step.

## Training and drop rules

Requeue only into measured free slots. A power drop of 300K or more starts a Collect unit within 60 minutes.
