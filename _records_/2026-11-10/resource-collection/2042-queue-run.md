---
title: Harvest queue run 2042
created: 2026-11-11T04:42:00Z
modified: 2026-11-11T04:42:00Z
version: 1.0.0
description: Harvest unit harvest-2026-11-10-1803 partial - food and coin bubbles collected, iron unverified, Armed Truck not located
status: unverified
grounded_in:
  - source: live game screen on the owner Mac mini, 2026-11-10 20:28 to 20:42 PST, session cc-504
---

# Harvest queue run 2042

- Executor: ticker-2028
- Unit: harvest-2026-11-10-1803 (planned 18:03 slot, claimed 20:28)
- Session window: 20:28 to 20:42 PST, about 14 minutes
- Status: partial

## Entry state (live HUD read at 20:28)

- Food 631.7M, iron 954.4M, coin 98.1M, gold 13.22K, power 148,787,578
- Game was left on the Alliance Techs panel by the previous
  donations unit; closed Techs, backed out of the Alliance
  panel, entered the base interior with the BASE button.

## What was collected (all figures live HUD reads)

- Food: one tap on a crop-grounded bread-icon bubble
  (731.6K) collected ALL food bubbles - food 631.7M to
  635.2M, plus 3.5M verified. The wheat field shows no food
  bubbles after the tap.
- Coin: one tap on a crop-grounded coin-icon bubble
  (513.3K) collected ALL coin bubbles - coin 98.1M to
  100.4M, plus 2.3M verified. No coin bubbles remain in the
  farm area after the tap.
- Iron: UNVERIFIED. Iron read 954.4M at entry and 957.6M
  after the first tap, plus 3.2M with no verified cause (no
  iron bubble was seen collected at that moment; a Lucky
  Gift system message was on screen). A later crop-grounded
  tap on an iron bubble (label 416) made the iron bubbles
  disappear from the mines with NO movement in the iron
  total (957.6M before and after). Either the bubbles hold
  416 iron each (negligible at 0.1M HUD precision) or the
  collection did not credit. Do not assume the iron was
  collected. Next unit must re-read the mines live first.

## Not done

- Armed Truck: not located, not claimed. The bottom-left
  hint tooltip cycled twice during the unit ("...ies are
  fully loaded, ...e claim them" and "...lecting supplies,
  ...dy to depart again") pointing at the parked vehicles
  (red jeep, blue truck, green tank), but no truck claim
  control was identified. Issue 566 (Armed Truck
  unlocated) still stands.
- Iron bubbles: state unresolved as above.

## Method learning (for the next harvest unit)

- Bubble centres MUST be crop-grounded: crop the
  screenshot region and upscale it before tapping.
  Eyeball estimates from the 642px view missed by about
  30px repeatedly - two taps opened the Iron Mine panel
  instead of collecting, one tap missed a coin bubble
  entirely.
- Bubble icons: bread is food, gold coin is coin, blue
  triangle is iron; all three sit in green circles over
  the farm and mine areas. Food and coin each collect-all
  with one centre tap (verified by HUD). Iron collect-all
  is unproven.
- Two large round buttons appear near the farm after taps
  (blue paw, green up-arrow) plus a red-panda pet icon;
  their function is unknown and they were NOT tapped.
- The map view pans when a building is selected; re-ground
  every tap on the current screenshot, never reuse a point
  from an earlier screenshot.

## Red lines

- No diamonds or money spent, no paid button tapped, no
  speedup used, no building or research started. The Iron
  Mine panel was opened twice by mistaps and closed
  untouched (Quick Dispatch never tapped).
