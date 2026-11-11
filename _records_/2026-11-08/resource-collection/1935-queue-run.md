---
title: Queue Run 1935 Harvest
created: 2026-11-09T03:48:00Z
modified: 2026-11-09T03:48:00Z
level: L0
version: 1.0.0
description: Unit harvest-2026-11-08-1803, partial - food plus 5.1M and iron plus 1.2M HUD-verified in two taps, coin bubbles still standing
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-11-08 about 19:35-19:51 America/Los_Angeles
---

# 1935 queue run - harvest (harvest-2026-11-08-1803)

- Unit: harvest-2026-11-08-1803, executor ticker-1935.
  Status: partial - two bubble taps collected verified
  gains (food +5.1M, iron +1.2M), but coin bubbles are
  still standing and the token window ran out, so the
  sweep is unfinished. The tracker is untouched; the
  next harvest unit picks up the remainder.
- Session: computer session cc-154 on the owner Mac mini
  (1c817413-83e2-0545-cb90-36d5e096a6bd). No
  device-access error, no different-device dialog, no
  login demanded. LastWar was already running and
  selected, verified by list_apps and observe before
  any input. One transient observe error
  ("target app exited or restarted") self-resolved on
  re-list - the app never left the frontmost list
  (pid 1908 throughout).
- Evidence: this file; the HUD reads below are all live
  in this unit.

## What was read and collected, live in this unit

- Entry, read live about 19:37 local: base screen, power
  149,209,253; food 494.0M, iron 820.0M, coin 15.9M;
  diamonds 13.22K; cart 4,467; stamina 120. Note: food
  is +3.2M and iron +3.1M against the 1759 unit closing
  read (food 490.8M, iron 816.9M at about 18:00), with
  coin unchanged at 15.9M. No harvest record exists
  between 1759 and this unit, so the rise is
  unexplained - possibly collected by another session
  or at the reset. Recorded as observed, not explained.
- The game opened on the Events screen (Desert Storm
  Battlefield enlistment confirmation, Squad [A],
  Battle Day 2026-11-13 03:00-03:30, Participants
  20/20, Enlisted stamp; tabs The Age of Oil with red
  dot 1, Arms Race, Winter Battlefield). Two back-arrow
  taps returned to the base view. No event action was
  taken - this unit is harvest only.
- Wrong tap, about 19:38 local: a tap at norm 490,352
  on what looked like an orange resource bubble opened
  a UR Trade Truck panel instead ([BI0d]Whodat34,
  Times plundered 0/2, Next Station 04:58:41, Your
  Plunder Count Today 0/4). Closed at once with the
  panel X. No plunder, no dispatch - truck work belongs
  to the trucks unit.
- Tap 1, about 19:44 local: one tap grounded fresh at
  norm 335,489 on a green wheat bubble centre in the
  base interior (BASE view, after the map had drifted
  to a neighbour and was recentered). After: food
  494.0M to 499.1M (+5.1M, HUD-verified), iron
  unchanged 820.0M, coin unchanged 15.9M. The green
  wheat bubbles cleared from the cluster in the same
  screenshot. This confirms the food all-at-once
  behaviour: one tap clears the standing food bubbles.
- Tap 2, about 19:47 local: one tap grounded fresh at
  norm 156,352 on a blue iron bubble centre. After:
  iron 820.0M to 821.2M (+1.2M, HUD-verified), food
  unchanged 499.1M, coin unchanged 15.9M. One tap,
  one iron bubble - iron still collects one by one,
  as the activity metadata says. This also resolves
  the 1759 open question in part: the identical
  +3.6M on its two taps was two different bubbles
  holding similar amounts, not a shared clear.
- Tap 3 (miss), about 19:49 local: a tap at norm
  234,452 aimed at a yellow coin bubble landed on the
  Iron Mine building underneath and opened its action
  panel (Iron Mine Lv.27, paw and upgrade buttons).
  Dismissed by tapping empty ground; no button was
  touched, nothing spent, nothing started. HUD
  unchanged (food 499.1M, iron 821.2M, coin 15.9M).
  The coin bubbles were still standing at close.
- Closing state, read live about 19:50 local: food
  499.1M, iron 821.2M, coin 15.9M; power 149,209,253;
  diamonds 13.22K. Game left on the base screen.

## What was NOT verified - read this before the next harvest unit

- Coin bubbles: several yellow coin bubbles still
  standing at close (left cluster, around norm
  132,436 and 234,452). The coin tap missed its
  bubble centre and hit the building below, so the
  coin centre coordinates above are NOT verified -
  re-ground fresh in the next unit; do not reuse
  them blindly. Per rule R2 the method must change:
  zoom the base view in before tapping coin bubbles,
  or tap only a bubble whose yellow coin icon and
  value label are both readable in the screenshot.
- Iron bubbles: at least one more blue iron bubble
  was standing at close; the remainder carries to the
  next harvest unit with the coin bubbles.
- Armed Truck: the bottom-left toast fragment was
  visible again in this unit's screenshots, still cut
  off at the screen edge and not transcribed, so the
  fully-loaded notice is still unverified and the
  truck loot unclaimed. It carries to the next
  harvest unit - read the notice in full before
  deciding.
- The pre-unit HUD rise (food +3.2M, iron +3.1M
  since 18:00 with no intervening harvest record)
  is unexplained; if a later unit finds the same
  pattern, file it as an Issue rather than leaving
  it in prose.

## Red lines

- No diamonds spent, no money spent, no Go button
  tapped, no research or building started, no player
  attacked, no assemble or teleport. The Iron Mine
  panel's upgrade button was visible and was not
  touched. The UR truck panel was closed without
  plundering. Game left on the base screen.
