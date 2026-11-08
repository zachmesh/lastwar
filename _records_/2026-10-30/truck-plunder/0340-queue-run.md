---
title: Truck entry failed queue run
created: 2026-10-30T10:40:00Z
modified: 2026-10-30T10:40:00Z
version: 1.0.0
description: Queue unit trucks-2026-10-30-0257 execution
status: partial
---

# Trucks queue run - 2026-10-30 about 03:34 to 03:41 PDT

Unit: trucks-2026-10-30-0257, executor ticker-0334.
Status performed in part - trade screen never entered,
tracker untouched, so the next tick re-produces this regular.

## Posture read first

tools/duel.py at 03:34 local: duel day 5, theme Total
Mobilization, day ends 2026-10-30 19:00 local, radar posture
release. Day 5 is not a UR truck day, so the non-UR dispatch
rule would have applied: SR or above only, regular dispatch,
no Mega Mode; plunder UR or SSR trucks only with guard below
Squad 1 24.96M and right-sided UR shard stacks, to the daily
caps. None of that was reached in this unit.

## What happened

- Base screen at entry was normal, no "active on a different
  device" dialog, no login demand. HUD: food 270.8M, iron
  462.8M, coin 133.6M, Total Power 146,850,228.
- Entry attempts, verified by screenshot:
  - One tap at 53,713 opened a world-map-like screen
    carrying a radar task restoration timer, not
    Intercity Trade. Returned home with the home icon,
    untouched, no claim, no dispatch.
  - An enlarged crop of the base left column was then
    read before any further tap: top to bottom - hammer
    2/4, flask 0/2, green face 0C, blue bus/train-front
    icon with a red badge, white pickup truck, satellite
    dish, hammer, yellow walkie-talkie with a red badge.
    No blue truck-front Intercity Trade icon with a red
    badge is present in this set, so no further trade
    tap was made.
- This matches the 2026-10-29 23:48 unit, where the slot
  at 53,605 had rotated to the blue bus/train icon and
  trade entry failed the same way. The trade slot is
  absent in the current shortcut set, and no flip
  control was identified in this unit.

## Result

- Settled: 0. Dispatched: 0. Plundered: 0.
- Trade Count, Plunder Count, returned trucks and Reward
  Recovery were not checked in this unit because the
  trade screen was never entered.
- No Trade Contracts spent, no diamonds spent, no paid
  buttons tapped. The map screen visit was left
  untouched.
- Entry lesson carried forward: do not keep tapping
  53,605 or 53,713 while those slots hold train or map
  icons. The next unit should first identify which slot,
  if any, carries the blue truck-front trade icon with a
  red badge in the then-current set, and only then tap
  it; if no trade slot is present, record the same
  entry failure rather than spending the unit hunting.
