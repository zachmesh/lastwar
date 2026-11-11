---
title: Harvest queue run 1210
created: 2026-11-10T20:10:00Z
modified: 2026-11-10T20:22:00Z
version: 1.0.0
description: Ticker pass ticker-1204 harvest unit - food and iron collected, panel Collect method found, coin panel unchecked
status: unverified
---

# Harvest - ticker-1204, 12:10 to 12:22 PST

Unit harvest-2026-11-10-1003, executor ticker-1204. Status partial.

## Readings, verified live

- Before (base screen, 12:12): food 612.5M, iron 939.3M, coin
  84.1M.
- After: food 618.9M, iron 941.8M, coin 84.1M.

## Food - bubbles plus panel, both verified

- One tap on a farmland bubble (norm 117,482, centre grounded
  on the screenshot) cleared every farmland bubble at once:
  food 612.5M to 618.8M, +6.3M.
- The food resource panel (top-bar icon) then still showed
  Available Resources 88,117; its Collect button took it:
  food 618.8M to 618.9M, Available 0. Exact pre-Collect food
  was not read; the panel figure 88,117 is the claimed
  amount.

## Iron - bubble tap missed, panel Collect did the work

- Three gold bubbles with the iron icon and face value 596
  sat over the iron mines. A tap on the first bubble's centre
  (norm 104,199) fell through to the Aircraft Center and
  opened the Building Queue panel instead (closed untouched:
  Lv.29 Aircraft Center upgrade in progress, Time Left
  1d 14:12:21, queues 2 to 4 Idle; no Speed Up, no
  Construct tapped).
- A tap on the second bubble's centre (norm 167,223, freshly
  grounded on a 3x crop) produced no change and no iron
  movement: iron stayed 939.3M. A red-panda pet circle
  appeared at the tap point, so the tap most likely selected
  the roaming pet standing over the mine instead of the
  bubble. The three gold bubbles were gone from the mines on
  the next screenshot; whether the tap collected them (596
  each, +1,788 total, invisible at 0.1M rounding) or they
  despawned is unverified.
- The iron resource panel (top-bar icon) then read Owned
  939,366,406 exactly, Available Resources 2,459,903, and
  its Collect button took the pool: Owned 941,833,227
  exactly, +2,466,821 (panel figure 2,459,903 plus about
  6,918 of production accrued between the read and the tap),
  Available 0. This is the first unit to use the panel
  Collect route; the activity metadata documents only bubble
  taps, so the method gap is filed as issue #585.

## Not done in this unit

- Coin panel not opened: no coin bubbles were visible on the
  base map, and the pass budget ran out before the coin
  panel's Available Resources could be read. The next harvest
  unit opens the coin panel first.
- Armed Truck still unlocated (open issue #566, fourth
  deferral). One new candidate noted, not verified: a white
  speech bubble with a truck icon sits over the blue pad by
  the helicopter at about norm 389,260. The gold bubble with
  a capped man's face and 25 below it near the tents (about
  norm 235,545) reads as a survivor/hero bubble, not a
  resource bubble, and was left alone.

## Result stats

- target: collect all ready bubbles, claim Armed Truck loot
  when fully loaded
- achieved: food bubbles +6.3M and panel +88,117; iron panel
  +2,466,821; coin unchecked; Armed Truck not located
- resources_gained: food about 6.39M, iron 2,466,821
  (panel exact reads, live in-unit)
- points: 0
- costs: about 12 minutes, no items spent
- verified: yes for food and iron panel totals; no for the
  iron map bubbles (596 each, effect unverified)
- blocker_category: e (repeated blocker - Armed Truck
  location unrecorded, fourth deferral; issue #566)
