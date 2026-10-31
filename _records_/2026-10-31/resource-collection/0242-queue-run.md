---
title: Resource Collection Execution 2026-10-31 0242 Queue Run
created: 2026-10-31T09:42:00Z
modified: 2026-10-31T09:42:00Z
level: L0
version: 0.1.0
description: Harvest queue unit harvest-2026-10-31-0203 - one tap collected iron 515.0M to 522.1M, later taps panned the map instead of collecting, Armed Truck fully-loaded notice seen but not claimed, tracker untouched
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-10-31
  - source: owner directions of 2026-10-25, 2026-10-26 and 2026-10-28 - the standing routine, Mac control authorization and the task unit queue ticker
---

# Resource collection — execution, 2026-10-31 0242 queue unit

A single task unit, executed by executor ticker-0234 under the
task unit queue. Unit harvest-2026-10-31-0203, priority 3.
Session window about 02:40 to 02:42 America/Los_Angeles.
Computer session cc-599, window mode (642x951).
Status — partial: one collection verified on the HUD,
but farmland bubbles were not verifiably collected and
the Armed Truck was not claimed, so the tracker is
untouched and the next tick re-produces this regular.

## What was observed

- Entry — base screen HUD: food 328.1M, iron 515.0M,
  coin 171.0M. The game was left on the radar screen
  by the previous unit; the radar home button returned
  to the base.
- First tap — a tap at norm 199,202 moved iron
  515.0M to 522.1M on the HUD (about 7.1M collected).
  Food and coin HUD figures did not move at this
  rounding.
- Map-pan taps — two further taps on apparent bubble
  points (norm 137,186 and 252,187) moved no HUD
  figure and instead panned the map view to the
  north-west sector and back. Those points were
  empty ground or building decoration, not
  collectable bubbles; no building panel was opened
  and nothing was upgraded.
- Armed Truck — in the north-west panned view a
  notice read "Supplies are fully loaded, please
  claim them" at the left edge, the Armed Truck
  loot ready to claim. Taps at norm 62,545 and
  62,575 on the left-edge truck icon opened no
  panel and re-panned the view, so the truck loot
  was NOT claimed in this unit. The notice stays
  open for the next tick, which should ground the
  truck's tap point on a fresh screenshot before
  tapping rather than reusing these points.
- Not touched — the green survivor faces at the
  left edge belong to survivor intake, a different
  regular, and were not tapped in this unit.
- Nothing else spent — no diamonds, no money, no
  speedup items, no stamina items. No other regular
  was merged into this unit. The game was left on
  the base screen. No login or verification was
  demanded, and no different-device dialog appeared.

## Result statistics

- iron_before: 515.0M
- iron_after: 522.1M
- food_before: 328.1M
- food_after: 328.1M
- coin_before: 171.0M
- coin_after: 171.0M
- armed_truck_claimed: false
