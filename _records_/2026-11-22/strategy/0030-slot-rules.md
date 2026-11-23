---
title: Slot rules for the planner v1.2
created: 2026-11-23T08:33:00Z
modified: 2026-11-23T08:47:00Z
version: 1.2.0
level: L3
description: The allocation rules for the first free lab and builders, the speed-up order, the slot-arrival protocol with the hospital as a stuck stock, and the training rule, for the planner to turn into units
status: unverified
grounded_in:
  - source: _records_/2026-11-22/strategy/0030-dg-level-table.csv and 0030-readiness.md
  - source: operator read _records_/2026-11-22/growth/0030-capacity-read.md, hospital Collect is all or nothing
  - source: researcher note on the Extra Drill Ground node and Steer A decisions of 2026-11-23 08:23Z
---

# Slot rules v1.2

Rules, not units. Costs in [the level table](0030-dg-level-table.csv), guide times 0.85, tag D until a panel read replaces them. Change since 1.1.0: the hospital Collect has no selector and looks all or nothing (partial space untested), so capacity is valued as **training slots** and the 5,306 as a ceiling.

## Lab rule (lab 1 at 11:43Z, lab 2 on 11-26 at 07:19Z)

1. Press Complete first; log Total Power before and after.
2. Start Extra Drill Ground if startable (R1 reads gates, Valor about 700, coin about 61M); else its shortest prerequisite by lab-days; both labs may run path nodes.
3. Else the node with most slots per lab-day; else the best +15K node leaving 10M coin. Never an Age of Oil node. A lab idle over 30 minutes is a miss.

## Builder rule (four builders at 09:20Z on 11-24)

1. Keep one builder free for the new ground when its research is done or within 24 hours.
2. Else builder 1 takes the lowest ground's next level, builder 2 the second one's; skip a Lv.30 ground.
3. The rest: best power per builder-day with a preview. Never HQ or Lv.31 jobs, never the owner's running queue; every resource stays above its floor.

## Speed-up order (Steer A bounds, 10,000 minutes an upgrade, 35,000 a week)

The Extra Drill Ground path and its new ground first, then the ground level with fewest minutes per slot (L27, about 14,600). The reason is training slots, not the hospital. Scope for construction and tech speed-ups awaits Steer A.

## Slot-arrival protocol (X exceeds Y, or a ground completes)

1. Read X of Y on the Drill Ground troops panel (the small button, not Building Details; the 10-31 and 11-02 records show the route).
2. One hospital Collect tap before any training, until the answer is known (H16): if it adds a part, hospital first (free, instant); if it names the whole count, training wins.
3. Collect a finished batch if the 19:56Z test shows it needs room.
4. Train new T10 at the idle Lv.30 barracks into exactly the free slots, 793 a batch; T9 or T8 elsewhere only if a slot would idle a day.
5. Read Promote on an idle barracks; start it when the gain is positive and floors hold, T7 first.
6. Log power before and after each step.

## Training and drop rules

Requeue nothing except into measured free slots. A Total Power drop of 300K or more starts a Collect unit within 60 minutes, hospital first only if its whole count fits.
