---
title: Resource Collection Execution 2026-10-31 1046 Queue Run
created: 2026-10-31T17:46:00Z
modified: 2026-10-31T17:46:00Z
level: L0
version: 0.1.0
description: Harvest queue unit harvest-2026-10-31-1003 - farmland bubbles collected in one tap, food 329.1M to 337.1M verified on the HUD, iron and coin unchanged, Armed Truck not checked
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-10-31
  - source: owner directions of 2026-10-25, 2026-10-26 and 2026-10-28 - the standing routine, Mac control authorization and the task unit queue ticker
---

# Resource collection — execution, 2026-10-31 1052 queue unit

A single task unit, executed by executor ticker-1034 under the
task unit queue. Unit harvest-2026-10-31-1003, priority 3.
Session window about 10:41 to 10:46 America/Los_Angeles.
Status — partial: one farmland collection was verified on
the HUD, but other bubbles remain and the Armed Truck was
not checked, so the tracker is untouched and the next tick
re-produces this regular.

## What was observed

- Entry — the game was left on the radar screen by the
  preceding radar unit. The bottom-right home icon at
  norm 919,967 returned to the base.
- Base HUD at entry — food 329.1M, iron 523.2M,
  coin 177.1M, stamina 110.
- One collection — a gold bubble over the wheat field,
  tapped at norm 382,415 (a first tap at norm 417,405
  on the field moved no HUD figure), collected all
  farmland bubbles at once, as the activity metadata
  records: food 329.1M to 337.1M on the HUD (about
  8.0M collected) and the gold bubbles over the wheat
  field cleared. Iron and coin HUD figures did not
  move at this rounding. A visual-grounding call for
  bubble positions timed out after 3 minutes and was
  not retried; the successful tap was grounded from
  the screenshot by eye.
- Not attempted in this unit — no iron or coin bubble
  was tapped and the Armed Truck was not checked:
  the pass budget did not leave room for the
  north-west pan the 2026-10-31 0242 unit used to see
  the truck notice, so the 0242 unit's unclaimed truck
  loot stays open for a later unit.
- Not touched — no building panel was opened and
  nothing was upgraded; no survivor face, mail or
  alliance icon was tapped. No other regular was
  merged into this unit.
- Nothing else spent — no diamonds, no money, no
  speedup items, no stamina items. The game was left
  on the base screen. No login or verification was
  demanded, and no different-device dialog appeared.

## Result statistics

- food_before: 329.1M
- food_after: 337.1M
- food_collected: 8.0M
- iron_before: 523.2M
- iron_after: 523.2M
- coin_before: 177.1M
- coin_after: 177.1M
- armed_truck_claimed: false
