---
title: Queue Run 1759 Harvest Pre-reset Sweep
created: 2026-11-09T01:59:00Z
modified: 2026-11-09T01:59:00Z
level: L0
version: 1.0.0
description: Unit harvest-2026-11-08-1403, partial - iron plus 3.6M and coin plus 3.6M HUD-verified in two taps, food bubbles still standing, reset arrived mid-sweep
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-11-08 about 17:56-18:00 America/Los_Angeles
---

# 1759 queue run - harvest pre-reset sweep (harvest-2026-11-08-1403)

- Unit: harvest-2026-11-08-1403, executor ticker-1724.
  Status: partial - two bubble taps collected verified
  gains (iron +3.6M, coin +3.6M), but the food bubbles are
  still standing and the 18:00 reset arrived mid-sweep, so
  the sweep is unfinished. The tracker is untouched and the
  harvest-2026-11-08-1803 unit, queued with not_before
  18:03, picks up the remainder in the new reset day.
  This unit is the overdue 1403-slot harvest unit; it was
  picked by the loop after the sweep and missions units
  because it expires 18:03 and its bubbles were the last
  collectible value before the reset.
- Session: computer session cc-146 on the owner Mac mini
  (1c817413-83e2-0545-cb90-36d5e096a6bd). Sessions cc-143
  and cc-144 closed between units of this pass without an
  error; each unit re-opened its session, no
  device-access error, no different-device dialog, no
  login demanded. No control call failed in this unit.
  LastWar was already running and selected, verified by
  list_apps and observe before any input.
- Evidence: this file; the HUD reads below are all live
  in this unit.

## What was read and collected, live in this unit

- Entry, read live about 17:56 local: base screen, power
  149,209,253 (unchanged all day since 17:12); food
  490.8M, iron 813.3M, coin 12.3M; diamonds 13.22K; cart
  4,417; stamina 120; Season II 7d 00:03:54. Bubbles
  standing over the central building cluster - food,
  iron and coin, values in the hundreds of K.
- Tap 1, about 17:58 local: one tap grounded fresh at
  norm 249,355 on a bubble centre in the central cluster.
  After: iron 813.3M to 816.9M (+3.6M, HUD-verified),
  food unchanged 490.8M, coin unchanged 12.3M.
- Tap 2, about 17:59 local: one tap grounded fresh at
  norm 179,468 on a bubble centre over the farmland.
  After: coin 12.3M to 15.9M (+3.6M, HUD-verified),
  food unchanged 490.8M, iron unchanged 816.9M.
- Closing state, read live about 17:59-18:00 local: food
  490.8M, iron 816.9M, coin 15.9M; power 149,209,253.
  Wheat (food) bubbles are still standing over the
  farmland in the closing screenshot. Season II 7d
  00:01:22 at the last read, reset about 18:00.

## What was NOT verified - read this before the next harvest unit

- Both taps were aimed at food bubbles and both collected
  a different resource (iron, then coin). The
  bubble-type identification from the downscaled base
  screenshot is unreliable: a tap point that looks like a
  wheat bubble can sit on an iron or coin bubble. Per
  rule R2 the method must change before the next unit of
  this type taps again: verify the bubble's identity
  before tapping - read its value label and icon at full
  resolution, or confirm the resource total that moves
  after the first tap before tapping a second bubble of
  the same supposed type.
- The identical +3.6M on both taps is recorded as
  observed, not explained. One candidate mechanism, NOT
  verified: a tap clears all standing bubbles of one
  resource type at once (the food all-at-once behaviour
  is already recorded; iron and coin may share it). The
  activity metadata still says iron and coin collect one
  by one (2026-10-25); that line is now suspect and the
  next harvest unit should test it with one tap and a
  HUD re-read, not assume it.
- Armed Truck: the bottom-left toast fragment ("...ies
  ... loaded,") was visible again in this unit's
  screenshots, still cut off at the screen edge and not
  transcribed, so the fully-loaded notice is still
  unverified and the truck loot unclaimed. The 1803 unit
  should read the notice in full before deciding.
- Titanium bubbles, EXP bubbles: no separate read taken
  in this unit; they carry to the 1803 unit with the
  food bubbles.
- The 1803 unit should also re-ground every bubble
  centre fresh in its own screenshots; no point from this
  unit carries over.

## Red lines

- No diamonds spent, no money spent, no Go button tapped,
  no research or building started, no player attacked, no
  assemble or teleport. Game left on the base screen.
