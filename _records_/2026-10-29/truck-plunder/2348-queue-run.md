---
title: Truck entry failed queue run
created: 2026-10-30T06:48:00Z
modified: 2026-10-30T06:48:00Z
version: 1.0.0
description: Queue unit trucks-2026-10-29-2257 execution
status: partial
---

# Trucks queue run - 2026-10-29 about 23:35 to 23:48 PDT

Unit: trucks-2026-10-29-2257, executor ticker-2334.
Status performed in part - trade screen never entered,
tracker untouched, so the next tick re-produces this regular.

## Posture read first

tools/duel.py at 23:35 local: duel day 5, theme Total
Mobilization, day ends 2026-10-30 19:00 local, radar posture
release. Day 5 is not a UR truck day, so the non-UR dispatch
rule would have applied: SR or above only, regular dispatch,
no Mega Mode; plunder UR or SSR trucks only with guard below
Squad 1 24.96M and right-sided UR shard stacks, to the daily
caps. None of that was reached in this unit.

## What happened

- Base screen at entry was normal, no "active on a different
  device" dialog, no login demand. HUD: food 260.0M, iron
  443.6M, coin 122.0M, Total Power 146,850,228.
- Entry attempts, all verified by screenshot, not by the
  OCR no-change reading (unreliable for this canvas):
  - Three taps at 53,605, the coordinate that opened
    Intercity Trade in the 16:58 and 21:28 units, produced
    no trade screen. The screenshot after them still
    showed the base, with the alliance train selected
    (Abyss Apex, timer about 03:22).
  - A drag up the left icon column produced no change.
  - One tap at 53,590 also produced no trade screen.
- Left-column identification in this unit (enlarged crop
  of the screenshot): green face, blue bus/train-front
  icon, white pickup with a red badge, satellite dish,
  hammer. The slot at 53,605 now lands on the blue
  bus/train icon and selects the alliance train on the
  map; it is NOT the blue truck-front trade icon of the
  2026-10-28 0257 set. The icon set has rotated since
  the 21:28 unit, when 53,605 still opened trade.
- No truck dispatched, none settled, none plundered, no
  Trade Contracts spent, no diamonds spent, no paid
  buttons tapped. The train selection was left untouched
  (no boarding, no ticket spent) - it is not this unit's
  task type.

## Result

- Settled: 0. Dispatched: 0. Plundered: 0.
- Trade Count, Plunder Count, returned trucks and Reward
  Recovery were not checked in this unit because the
  trade screen was never entered.
- Entry lesson for the next attempt: do not keep tapping
  53,605 while the train icon occupies that slot. The
  next unit should first identify which slot, if any,
  carries the blue truck-front trade icon with a red
  badge in the then-current set, and only then tap it;
  if no trade slot is present, record the same entry
  failure rather than spending the unit hunting, as
  the 2026-10-28 1913 unit did.
