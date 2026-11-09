---
title: Training queue run
created: 2026-11-01T20:16:00Z
modified: 2026-11-01T20:16:00Z
version: 1.0.0
description: Training unit training-2026-11-01-1003 executed by ticker-1204, partial, barracks tent row not located after a four-direction pan sweep
status: partial
---

# Training queue run 2026-11-01 about 12:16 PDT

- Unit: training-2026-11-01-1003, executor ticker-1204, status partial.
- What happened: troop-training metadata read before acting, including
  the 2026-10-31 retro standing blocker (Drill Ground Full 39,460 of
  39,460 blocking collection and requeue) and the 0917 unit's finding
  that the barracks tent row is not in the factory pan and its pinned
  coordinates do not transfer across camera positions. This unit
  changed method per queue rule R2: instead of repeating taps in the
  factory pan, it panned the base view in four directions looking
  for the tent row.
- Tent search, not located: the opening pan showed the Titanium Alloy
  Factory cluster in the walled compound; one tap at norm 400,535
  selected Titanium Alloy Factory No.4 Lv.30 and was left untouched
  (no upgrade shortcut, no Train, no Finish Now). Four drags then
  swept the view - up, right, diagonal down-left, and up again -
  showing the HQ and furnace sector, the vehicle Formation 2 and 3
  parking sector, and empty snowfield to the south and east. No
  barracks tent row appeared in any swept pan, so no TRAIN UNITS
  panel was reached, no batch was collected or started, and the
  Drill Ground panel was not re-read in this unit; the Drill Ground
  Full state is carried forward unverified, not re-asserted.
- No different-device dialog, no login or verification demanded.
  Chat line visible during the unit, "thorsey: need to lose some
  troops", is consistent with a full drill ground but is not a
  live read of the Drill Ground panel and is not used as one.
- HUD at open: food 289.2M, iron 477.2M, coin 10.6M, total power
  148,957,193, unchanged at close.
- Tracker untouched (partial unit), per the queue rules: the next
  tick re-produces this regular. The next training unit should try
  a zoomed-out whole-base view first (the current pans cover the
  compound and the surrounding snowfield but never show a tent
  row), and should ground the Drill Ground building itself before
  any further tent taps, since the drill-ground gate is the
  standing blocker and its panel has not been read live since
  2026-10-31.
- No diamonds, money, speedups or paid buttons were used. No
  building, research or assembly action was taken. The red
  target icon with a countdown seen at the right edge of the
  closing pan was left untouched: it belongs to another task
  type, not this unit.

## Result statistics

- barracks_checked: 0
- barracks_collected: 0
- barracks_requeued: 0
- drill_ground_checked: 0
- drill_ground_full: unverified
- target: one barracks batch collected or requeued
- achieved: 0
- resources_gained: none
- costs: about 9 minutes, no items consumed
- verified: no
- blocker_category: c
