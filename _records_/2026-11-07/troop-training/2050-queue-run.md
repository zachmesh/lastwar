---
title: Troop training queue run 2050
created: 2026-11-08T04:52:00Z
modified: 2026-11-08T04:52:00Z
level: L0
version: 1.0.0
description: Ticker-2034 training unit, partial - Lv.30 busy, Lv.24 blocked by Drill Ground Full, Drill Ground screen read live
status: unverified
---

# 2050 queue run - Troop Training

Executor: ticker-2034. Unit: training-2026-11-07-1803.
Session window about 20:43 to 20:50 America/Los_Angeles
(04:43 to 04:50Z). Computer session cc-47, LastWar already
running on the Mac mini.

## What was done

- Lv.30 barracks: TRAIN UNITS panel read Power 1647,
  Morale 750.0, Squad Load 2200, Unit HP 4726.34, Attack
  38.45, Defense 7.7; Lv.10 selected, count 793,
  "Training in progress 1d 13:41:04" at about 20:47.
  This is the batch requeued by the 1655 unit at about
  17:08 today (1d 17:14:37 at start), so the remaining
  time is consistent. Busy; Speed Up was never tapped.
- Lv.24 barracks: selected (label "Barracks Lv.24" with
  the paw, pistol and green up-arrow button row). Tapping
  the pistol TRAIN UNITS button produced the toast
  "Drill Ground Full: Unable to add more units" (read
  live by OCR); no TRAIN UNITS panel stayed open and no
  batch was started. This barracks is idle and blocked,
  not busy.
- Drill Ground screen read live, as the activity's
  third-strike instruction requires: tapping the troop
  formation selected "Drill Ground Lv.25"; its Building
  Details panel (paw button) reads Unit Count +7812,
  Survivors Officers Joe, Marcus, Karen and John, and a
  single action button "Quick Dispatch" at the panel
  bottom. No 39,460 of 39,460 figure appears on this
  screen; that figure comes from earlier units and was
  not re-read live here. Quick Dispatch was NOT tapped:
  its effect is unverified and it may march troops out,
  so it is left for an owner decision or a learn-first
  exploration unit, not pressed blind inside a training
  unit.

## What was not done

- No barracks was requeued in this unit: one confirmed
  busy, one idle but blocked by the full Drill Ground,
  two not checked. The Lv.27 barracks was requeued by
  the 1655 unit at about 17:08 today and should still
  be busy, but that was not re-verified live in this
  unit. Tracker untouched, per the partial rule; the
  next tick re-produces the training regular.
- The clearing method for a full Drill Ground is still
  unknown from a live read. The only candidate control
  seen is Quick Dispatch on the Drill Ground Details
  panel, untested.

## Tap method note (rule R2)

- Direct coordinate taps on tent bodies missed twice
  (norm 393,600 and 511,557, both no panel). The
  visual-grounding point (435,518) selected the Lv.24
  barracks, and the pistol button grounded at (425,581).
  The observation "no_change_observed" flag proved
  unreliable twice: the view had in fact changed after
  the tap. Next units should screenshot to verify after
  every tap instead of trusting that flag.

## Figures read live on screen

- Food 478.8M, iron 802.1M, coin 6.9M, stone 25.0M,
  922.2K, power 149,850,353, diamonds 4,217, energy
  118 at entry rising to 119 during the unit.
- No diamonds, money, speedups or paid buttons were used.
  No other task type was executed in this unit. No login
  or verification was demanded, and no different-device
  dialog appeared.

## Result statistics

- target 4, achieved 0, resources_gained none, costs
  about 7 minutes play, verified yes, blocker_category e,
  device_takeovers 0
