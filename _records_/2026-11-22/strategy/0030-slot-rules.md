---
title: Slot rules for the planner v1.3
created: 2026-11-23T08:33:00Z
modified: 2026-11-23T12:45:00Z
version: 1.4.0
level: L3
description: The allocation rules for the free labs and builders, the speed-up order, the slot-arrival protocol and the training rule once four Drill Grounds are known to exist
status: unverified
grounded_in:
  - source: _records_/2026-11-22/strategy/0030-dg-level-table.csv and 0250-read-identity-rule.md
  - source: operator record _records_/2026-11-22/growth/1047-f1b-drill-ground.md, four Drill Grounds at Lv.26, 27, 28 and 30
  - source: operator read 0030-capacity-read.md, hospital Collect has no selector
---

# Slot rules v1.3

Rules, not units. Costs in [the level table](0030-dg-level-table.csv). Change since 1.2.0 (F1b, 10:52Z): all four Drill Grounds exist, so the Extra Drill Ground path and the builder kept for a new ground are gone. Nine levels remain (+1,800 slots). The Lv.26, 27 and 30 previews are unread; the first builder choice is re-ranked after F1c.

## Lab rule (lab 1 at 11:43Z, lab 2 on 11-26 at 07:19Z)

1. Press Complete first; log Total Power before and after.
2. Owner order 12:33Z: start the first available critical-path node of the Age of Oil tree in dependency order from the real preview (cost, time, power, oil); if none is startable (locked or oil short) report in one pass, start no other line.
3. Tech speed-up items first (at least 15,360 minutes), then general items up to 15 percent of the general stock a week; never Finish Now; log minutes and the new finish time. A lab idle over 30 minutes is a miss.

## Builder rule (four builders at 09:20Z on 11-24)

1. One builder on the Oil Well if the Construct list offers it. For the rest, after F1c, take the next levels in order of power per builder-day: Lv.26 ground L27 (about 34.7K, 59.5M coin), Lv.27 ground L28 (25.1K, 83.3M), Lv.28 ground L29 (19.6K measured, 119.0M). Skip the Lv.30 ground. Start as many as coin, food and iron allow; three need coin 262M, food 978M, iron 321M.
2. The fourth builder: best power per builder-day with a preview. Never HQ or Lv.31 jobs, never the owner's running queue; every resource stays above its floor.
3. Chests are converted 2 hours before, by the box policy.

## Speed-up order (Steer A bounds)

Construction items first (about 167,760 minutes, building only; general items stay in reserve). The level with the fewest minutes per slot first: L27 (14,550), L28 (20,370), L29 (26,481); at most 10,000 minutes an upgrade, 30,000 in all, 35,000 a week; inside the Tuesday window on 11-24.

## Slot-arrival protocol (X exceeds Y, or a level completes)

1. Read X of Y on the Drill Ground troops panel (small button, not Building Details).
2. One hospital Collect tap before any training (H16); if it adds a part, hospital first, else training wins.
3. Collect a finished batch if the 19:56Z test shows it needs room.
4. Train new T10 at the idle Lv.30 barracks into exactly the free slots, 793 a batch.
5. Read Promote on an idle barracks; start it when the gain is positive, T7 first.
6. Log power before and after each step.

## Training and drop rules

Requeue only into measured free slots. A Total Power drop of 300K or more starts a Collect unit within 60 minutes.
