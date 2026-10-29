---
title: Truck dispatch and settlement queue run
created: 2026-10-29T23:58:00Z
modified: 2026-10-29T23:58:00Z
version: 1.0.0
description: Queue unit trucks-2026-10-29-1457 execution
status: partial
---

# Trucks queue run - 2026-10-29 16:48 to about 16:58 PDT

Unit: trucks-2026-10-29-1457, executor ticker-1634.
Status performed in part - settlement and dispatch done,
plunder hunt not completed, tracker untouched, so the next
tick re-produces this regular.

## Posture read first

tools/duel.py at 16:48 local: duel day 4, theme Train Heroes,
day ends 2026-10-29 19:00 local, radar posture stack. Day 4 is
not a UR truck day, so the non-UR dispatch rule applied: SR or
above only, regular dispatch, no Mega Mode.

## Settlement - one returned SR truck, intact

- Intercity Trade entered from the base left column trade icon
  at 53,605 (two taps at about 55,605 first showed no change in
  the observation, the third tap opened the screen; the
  observation's no-change reading is unreliable for this canvas).
- Your Truck tab at open: Today's Trade Count 4 of 5, two
  trucks on the road, Recover button showed no red dot, so no
  Reward Recovery record waited.
- The returned SR truck, Squad 1 escort, settled in full:
  "The vehicle is safe and secure" - intact, nothing plundered
  off it. Cargo paid: iron 2.5M, food 2.5M, coin 1.6M, chest
  20 x2, red gem 50 x1, badge 500 x1, item x1. Note for the
  next unit: taps in the road area land about 80 normalized
  units right of the tap coordinate used here (a tap at
  360,431 opened the blue SR truck; a tap at 444,431 had
  opened the purple SSR panel instead), so aim road taps
  left of the visual target by that offset.
- The other truck on the road is the SSR dispatched at 13:20,
  Squad 3, arriving in about 00:40 at the read (due about
  17:36), not yet returned.

## Dispatch - one SSR truck, free refresh only

- Free slot plus opened the panel at once. First roll N
  (chest 20 x2, red gem 50 x1, iron 1.2M, food 1.2M, coin
  810.0K, journey 04:20:50, Squad 1 escort), below SR.
- Free refresh (dice centre 787,431, as in prior units)
  rerolled to SSR (chest 10, badge 500 x3, item x1, item x1,
  badge 500 x3, red gem 100 x1, iron 3.0M, food 3.0M, coin
  1.9M, journey 04:14:59, Squad 1); the dice tag then read
  137/1 (Trade Contract stock 137, cost 1 per refresh),
  matching the prior unit's ending stock, so no contract
  was spent in this unit.
- Dispatched at once with regular Let's Go (no Mega Mode,
  non-UR day). Today's Trade Count moved 4 of 5 to 5 of 5,
  and the road then read "No more dispatches available."

## Plunder - deferred

- Others' Trucks tab was not reached in this unit; Your
  Plunder Count Today stood at 2 of 4 from the 13:04 unit.
  The plunder hunt (list check, any qualifying UR/SSR
  plunder) resumes in the next trucks unit; the unit closed
  here because the pass budget was reached, not because
  the day's caps are spent.

## Result

- Settled: 1 SR truck in full, intact.
- Dispatched: 1 SSR truck, Squad 1, journey 04:14:59.
- Plundered: 0 in this unit, Plunder Count still 2 of 4,
  Trade Count now 5 of 5.
- Spent: 1 free refresh only, 0 Trade Contracts.
  No diamonds spent, no paid buttons tapped.
