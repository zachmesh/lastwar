---
title: Resource Collection Execution 2026-10-30 2226 Queue Run
created: 2026-10-31T05:26:00Z
modified: 2026-10-31T05:26:00Z
level: L0
version: 0.1.0
description: Harvest queue unit harvest-2026-10-30-2203 - 5 bubbles seen at entry, first tap cleared 4 with iron 18.7M to 19.1M, second tap selected the High-heat Furnace instead of a bubble, Armed Truck unchecked, tracker untouched
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-10-30
  - source: owner directions of 2026-10-25, 2026-10-26 and 2026-10-28 - the standing routine, Mac control authorization and the task unit queue ticker
---

# Resource collection — execution, 2026-10-30 2226 queue unit

A single task unit, executed by executor ticker-2204 under the
task unit queue. Unit harvest-2026-10-30-2203, priority 2.
Session window about 22:20 to 22:26 America/Los_Angeles.
Computer session cc-582.
Status — partial: bubbles were collected but the Armed
Truck was not checked inside this unit, so the tracker is
untouched and the next tick re-produces this regular.

## What was observed

- Entry — base screen HUD: food 328.1M, iron 18.7M,
  coin 171.0M. Five resource bubbles were grounded over
  the base buildings at norm 398,413 / 294,461 /
  502,461 / 399,506 / 503,562.
- First tap — a tap at norm 398,413 cleared four of
  the five bubbles; iron moved 18.7M to 19.1M on the
  HUD, about 0.4M collected. Food and coin HUD
  figures did not move at this rounding.
- Second tap — a tap at norm 435,428 on the one
  remaining grounded point selected the High-heat
  Furnace Lv.30 instead (its action row opened): the
  grounding point had been a building button, not a
  resource bubble. The selection was cleared by
  tapping empty ground; no building panel was
  opened further and nothing was upgraded.
- Not done in this unit — the Armed Truck loot was
  not checked, and no further bubble was verified
  after the furnace mis-tap, because the pass
  budget ran out. Per the activity rule, bubble
  regeneration is not chased.
- Nothing else spent — no diamonds, no money, no
  speedup items, no stamina items. No other regular
  was merged into this unit. The game was left on
  the base screen. No login or verification was
  demanded, and no different-device dialog appeared.

## Result statistics

- bubbles_seen: 5
- bubbles_cleared: 4
- iron_before: 18.7M
- iron_after: 19.1M
