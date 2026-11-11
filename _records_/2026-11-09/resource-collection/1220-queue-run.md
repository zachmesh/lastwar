---
title: Harvest queue run 1220
created: 2026-11-09T20:33:00Z
modified: 2026-11-09T20:33:00Z
version: 1.0.0
description: Ticker-1204 harvest unit - all visible resource bubbles collected, HUD verified
status: done
grounded_in:
  - source: live game screen on the owner Mac mini, 2026-11-09 12:20 to 12:33 PT (computer session cc-268)
---

# Harvest queue run 1220 (ticker-1204)

Unit: harvest-2026-11-09-1003. Status: done.
Activity: resource-collection.
Chain: none.

## Live reads (HUD, before to after)

- Food 544.5M to 548.4M (plus 3.9M)
- Iron 871.8M to 875.4M (plus 3.6M)
- Coin 46.2M to 48.8M (plus 2.6M)
- Diamonds 6,077, Total Power 149,217,331, Stamina 120,
  building queue 1/4, research 1/2 - unchanged.

## What was done

- Iron: 5 bubbles collected (630.7K, 719.9K, 739.5K,
  701.3K, 703.9K as read on the enlarged crop) - the HUD
  rise of 3.6M covers them plus a little regeneration.
- Coin: 4 bubbles collected (569.4K, 523.9K, 526.2K,
  453.0K as re-read just before the taps) - HUD rise 2.6M.
- Food: one tap on the 862.2K bread bubble collected all
  farmland at once, per the standing rule - the second
  bread bubble (669.0K) cleared with it and the HUD rose
  3.9M, more than the two visible bread bubbles, so
  further farmland bubbles off the crop were collected
  too. Confirmed: one farmland tap collects all food.
- After the sweep no iron, coin or food bubble remains
  visible anywhere on the base screen (verified on the
  closing screenshot).
- Armed Truck loot NOT checked this unit - the unit hit
  its 15 minute cap at the food verification; the truck
  check is the follow-up for the next harvest unit.

## Panel incidents (no harm, nothing spent)

- The iron batch's last tap opened the iron mine's
  Building Details panel (Lv.27, Output/hr plus 110,681,
  Max Production Time 11hr 36min, Survivors Charles,
  Jolene, Alyssa as Miners) and then its Survivor List
  (Alyssa already assigned, Harry's row highlighted by a
  batch tap). The Select button was never tapped - no
  survivor was assigned or changed.
- The coin batch's third tap opened the gold mine's
  Building Details panel (Lv.30, Output/hr plus 98,064,
  Max Production Time 12hr, Survivors Madison, William,
  Amanda, Rebecca as Gold Miners). Quick Dispatch was
  never tapped.
- Both panels were left by the left-edge swipe back
  gesture (drag from x 20 to 200 at y 500), which the
  upgrade panel in unit 018 also needed: the panel X
  does not respond to background clicks (single, double,
  1s and 2s holds all no-change), while the swipe closes
  one level per drag. The swipe is now the working panel
  close method for this input route.
- Lesson for the next harvest unit: tap bubbles one at a
  time with a screen read between taps when a batch tap
  has just opened a panel - a batch that continues into
  an open panel taps panel rows. Bubble centres must be
  re-grounded from an enlarged crop, never from the
  downscaled full screenshot (the first tap of this unit
  at 210,589 hit a building, not a bubble, for exactly
  that reason).
- A "treasure map" congrats toast for an alliance member
  crossed the screen during the sweep - observed,
  untouched. The yellow question-mark chest bubble near
  the truck is not a resource bubble and was left for
  the treasures unit.

## Red lines

- No diamonds or money spent. No priced button tapped.
  No survivor assigned, no dispatch used, no building
  started. No other unit's work touched.

## Stats

- target: collect-all-visible-resource-bubbles
- achieved: 1
- resources_gained: food-plus-3.9M-iron-plus-3.6M-coin-plus-2.6M
- costs: about-14-minutes-no-items-spent
- verified: yes
- blocker_category: none
- points: 0
- surfaces_walked: base-screen-resource-bubbles-iron-mine-panel-gold-mine-panel
- items_observed: 11
