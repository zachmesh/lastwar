---
title: Truck entry failed queue run
created: 2026-10-30T12:40:00Z
modified: 2026-10-30T12:40:00Z
version: 1.0.0
description: Queue unit trucks-2026-10-30-1230 execution
status: partial
---

# Trucks queue run - 2026-10-30 about 05:34 to 05:40 PDT

Unit: trucks-2026-10-30-1230, executor ticker-0534.
Status performed in part - trade screen never entered,
tracker untouched, so the next tick re-produces this regular.

## Posture read first

tools/duel.py at 05:34 local: duel day 5, theme Total
Mobilization, day ends 2026-10-30 19:00 local, radar posture
release. Day 5 is not a UR truck day, so the non-UR dispatch
rule would have applied: SR or above only, regular dispatch,
no Mega Mode; plunder UR or SSR trucks only with guard below
Squad 1 24.96M and right-sided UR shard stacks, to the daily
quotas (dispatch 5 of 5, plunder 4 of 4, owner rule
2026-10-30). None of that was reached in this unit.

## What happened

- The game was found on the Zombie Invasion Events page,
  left from the previous zombie unit (event timer about
  13:24 remaining, next wave about 00:05). No "active on
  a different device" dialog, no login demand.
- Fullscreen clicks did not reach the game at all: three
  taps on the Events back arrow and taps on the My
  Findings tab, in fullscreen, produced no change, on
  either LastWar window. Menu View then Exit Full Screen
  worked, and in windowed mode (642 by 951) the back
  arrow tap at 109,939 closed Events to the base at once.
  Lesson for successors: keep the game windowed for this
  work; fullscreen clicks were dead in this pass, while
  the menu command and windowed taps responded.
- Base screen at entry, HUD: food 273.2M, iron 465.3M,
  coin 136.0M, Total Power 146,850,228. This matches the
  zombie unit 058 close (coin 136.0M).
- Left column identification, verified by screenshot,
  an enlarged crop, and visual grounding on that
  screenshot (windowed coordinates, x 53): green face
  season icon 494, blue train-front icon 556, white
  pickup (Secret Command Post) 619, satellite dish
  (radar) 682, magnifying glass 744, yellow
  walkie-talkie (Missions) 856. No blue truck-front
  Intercity Trade icon with a red badge is present in
  this set, so no trade tap was made at a trade slot.
- One tap at 53,536, between the green face and train
  slots, opened the temperature panel (Nuclear Furnace
  Lv.7 turned on, Thaw Area Lv.1, High-Heat Furnace
  Lv.30 not turned on). It was closed at once with its
  X, untouched: no furnace setting was changed, no
  temperature item was toggled, no other panel item
  was tapped. That tap is recorded here so the next
  unit does not repeat it as a trade entry attempt.
- The trade slot at 53,605 that opened Intercity Trade
  in the 2026-10-29 16:58 and 21:28 units is occupied in
  this set by the white pickup / train area, not by a
  trade icon, matching the 2026-10-29 23:48 and
  2026-10-30 03:34 entry failures. The icon set has not
  rotated back to a trade slot.

## Result

- Settled: 0. Dispatched: 0. Plundered: 0.
- Trade Count, Plunder Count, returned trucks and Reward
  Recovery were not checked in this unit because the
  trade screen was never entered; the live counters
  remain dispatch 1 of 5 and plunder 0 of 4 for the
  trade day that began 2026-10-29 19:00 local, per the
  activity metadata note at 05:29 local. Those counters
  are not re-derived here.
- No Trade Contracts spent, no diamonds spent, no paid
  buttons tapped, no train boarded, no furnace changed.
- Entry failure does not close the day: the quota
  shortfall (dispatch 4, plunder 4) stays open for the
  next trucks unit, which should first re-identify the
  left column and only tap a verified blue truck-front
  trade icon.
