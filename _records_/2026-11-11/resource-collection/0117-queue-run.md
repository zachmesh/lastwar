---
title: Harvest queue run 0117
created: 2026-11-11T01:17:00-08:00
modified: 2026-11-11T01:17:00-08:00
version: 1.0.0
description: Harvest unit harvest-2026-11-10-2203, food plus 1.6M and coin plus 1.1M verified, iron plus 1.4M verified on the second tap, partial
status: partial
grounded_in:
  - source: live game screen on the owner Mac mini, 2026-11-11 01:09-01:17 PST
---

# Harvest queue run 0117 (ticker-0055)

Unit: harvest-2026-11-10-2203. Status: partial.
Activity: resource-collection. Computer session cc-531.

## Entry state (live HUD read at 01:09)

- Food 656.2M, iron 979.3M, coin 110.7M, gold 13.22K,
  Total Power 149,218,973, stamina 106.
- Game was left on the Alliance Techs panel by the
  donations unit; closed Techs, backed out of the
  Alliance menu, entered the base interior with BASE.

## What was collected (all figures live HUD reads)

- Food: one tap on a crop-grounded bread bubble
  (322.9K label) collected ALL food bubbles - food
  656.2M to 657.8M, plus 1.6M verified. No food
  bubbles remain over the wheat fields after the tap.
- Coin: one tap on a crop-grounded gold-coin bubble
  collected ALL coin bubbles - coin 110.7M to 111.8M,
  plus 1.1M verified. No coin bubbles remain after
  the tap.
- Iron: two taps. Tap 1 aimed at a top-row 404K iron
  bubble: the three top-row bubbles were gone on the
  next screenshot but the iron total did not move
  (979.3M before and after), so its effect is
  UNVERIFIED - see the method note below. Tap 2 on a
  middle-row 246.4K iron bubble collected the whole
  middle row (246.4K + 305.8K + 288.8K + 274.1K +
  214.7K, about 1.33M): iron 979.3M to 980.7M, plus
  1.4M verified, and the middle-row bubbles are gone.
  Iron DOES credit on a centre tap; the 2042 unit's
  no-credit iron tap is now explained in part by the
  coordinate error below, not by an iron mechanic.

## Method correction - grounding coordinates are normalized

- The visual grounding tool returns coordinates in
  the 0-1000 NORMALIZED range of the image it is
  given, not pixels. Taps 1-3 of this unit converted
  the returned numbers as if they were crop pixels
  (dividing by the upscale factor instead of by
  1000 times the crop dimension). The food and coin
  taps still landed close enough to collect (bubbles
  are large), but the iron tap 1 missed by about 48
  in x and 45 in y in normalized units and most
  likely hit the mine building instead of the
  bubble. Tap 2 used the correct normalized
  conversion and credited. Every later unit must
  convert grounding output as normalized: original
  pixel = crop origin + (returned / 1000) * crop
  size / upscale, then normalize to the 642x951
  window. Do not divide a grounding return by the
  upscale factor.

## Not done

- Armed Truck: not located, not claimed. The parked
  vehicles (red jeep, blue truck, green tank) show
  at bottom-left with a "?" marker, but no truck
  claim control was identified in this unit. Issue
  566 (Armed Truck unlocated) still stands.
- One small bubble remains at the left screen edge
  (about 368.9K, partially off-screen at the left
  margin) - unattempted; the unit budget ended.
  The top-row iron bubbles' disappearance without a
  HUD credit is recorded as unverified, not as a
  collection.

## Close

- Partial: food and coin fully collected and
  verified, iron plus 1.4M verified on tap 2, but
  tap 1's iron effect is unverified and one edge
  bubble remains. The tracker stays untouched; the
  next tick re-produces the regular and the work
  resumes as a fresh unit.
- No diamonds or money spent, no paid button tapped,
  no speedup used, no building or research started.
  No login or verification demanded. No "active on a
  different device" dialog appeared.

## Result stats

- target collect all ready resource bubbles
- achieved food plus 1.6M, coin plus 1.1M, iron plus
  1.4M, all by live HUD reads
- resources_gained food 1.6M, coin 1.1M, iron 1.4M
- points none
- costs about 8 minutes
- verified yes for food, coin and the iron tap 2
  credit; no for the iron tap 1 effect
- blocker_category e
- food_before 656.2M, food_after 657.8M,
  coin_before 110.7M, coin_after 111.8M,
  iron_before 979.3M, iron_after 980.7M,
  bubbles_cleared food all, coin all, iron middle
  row, iron_top_row_unverified yes,
  edge_bubble_remaining yes (368.9K, left margin),
  armed_truck_located no
