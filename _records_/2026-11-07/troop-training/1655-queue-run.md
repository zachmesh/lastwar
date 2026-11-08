---
title: Troop training queue run 1655
created: 2026-11-08T01:21:00Z
modified: 2026-11-08T01:21:00Z
level: L0
version: 1.0.0
description: Ticker-1655 training unit, partial - two barracks requeued (Lv.27 T9 and Lv.30 T10), two not checked, Drill Ground full blocker not seen
status: unverified
---

# 1655 queue run - Troop Training

Executor: ticker-1655. Unit: training-2026-11-07-1403.
Session window about 17:08 to 17:12 America/Los_Angeles
(01:08 to 01:12Z). Computer session cc-19, LastWar already
running on the Mac mini.

## What was done

- Lv.27 barracks (center tent, timer bubble now above it):
  TRAIN UNITS panel read Power 1352, Morale 625.0, Squad
  Load 2000, Unit HP 4121.49, Attack 33.5, Defense 6.74;
  Lv.9 selected, count 726 at cap, cost 4.1M food plus 4.1M
  iron, time 1d 10:19:35. Train tapped; panel closed and
  the HUD moved food 486.5M to 482.3M and iron 810.0M to
  805.9M. Batch started.
- Lv.30 barracks (tent below-right of the first, its
  portrait circle overlaps the tent body - tap the body,
  not the circle): TRAIN UNITS panel read Power 1647,
  Morale 750.0, Squad Load 2200, Unit HP 4726.34, Attack
  38.45, Defense 7.7; Lv.10 selected, count 793 at cap,
  cost 5.5M food plus 5.5M iron, time 1d 17:14:37. Train
  tapped; panel closed and the HUD moved food 482.3M to
  476.8M and iron 805.9M to 800.4M. Batch started.
- Total spent in this unit: 9.6M food and 9.6M iron for
  726 T9 plus 793 T10 troops. Both requeued barracks now
  carry a clock timer bubble. Finish Now was never tapped.

## What was not done

- The other two barracks (upper-right tents) were not
  checked in this unit, so the "keep every barracks busy"
  aim is not fully met. The next training unit starts with
  those two. Tracker untouched, per the partial rule; the
  next tick re-produces the training regular.
- The Drill Ground Full blocker from the 2026-10-31 retro
  was not seen: both Train taps succeeded and no capacity
  message appeared. No Drill Ground screen was read live
  in this unit, so the blocker is not closed, only not
  encountered.
- Handover observation for the next survivors unit: a white
  "?" speech bubble stands at the left edge near the front
  gate (norm about 113,582) in the closing screenshots of
  this unit - a waiting survivor may have arrived after
  the survivors unit closed unverified minutes earlier.

## Figures read live on screen

- Food 486.5M at entry, 482.3M after the first batch,
  476.8M at close; iron 810.0M, 805.9M, 800.4M; coin
  5.7M; stone 25.0M; 922.2K; power 149,850,353.
- No diamonds, money, speedups or paid buttons were used.
  No other task type was executed in this unit. No login
  or verification was demanded, and no different-device
  dialog appeared.

## Result statistics

- target 4, achieved 2, resources_gained 726 T9 plus 793 T10
  troops queued, costs 9.6M food plus 9.6M iron and about
  4 minutes play, verified yes, blocker_category h,
  device_takeovers 0
