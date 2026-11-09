---
title: Training queue run
created: 2026-11-01T17:17:00Z
modified: 2026-11-01T17:17:00Z
version: 1.0.0
description: Training unit training-2026-11-01-0603 executed by ticker-0904, partial, barracks tent row not located in this pan
status: partial
---

# Training queue run 2026-11-01 about 09:17 PDT

- Unit: training-2026-11-01-0603, executor ticker-0904, status partial.
- What happened: troop-training metadata read before acting, including
  the 2026-10-31 retro standing blocker (21 of 22 training units
  non-done, Drill Ground Full 39,460 of 39,460 blocking collection and
  requeue in every 2026-10-31 unit that reached a barracks) and the
  pinned tent coordinates from 2026-10-31 (Lv.30 tent at norm 708,602
  in that unit's camera position, Lv.27 tent at 617,570 in a
  lower-middle base view).
- Computer session cc-1 dropped mid-unit; session cc-2 was started and
  LastWar re-selected with no game state lost. No different-device
  dialog, no login or verification demanded.
- Tent search, not located: three taps in the current base view each
  selected a different non-barracks building, verified on a second
  observation each time, and were left untouched (no upgrade shortcut,
  no Finish Now, no Train pressed):
  - norm 405,475 selected Titanium Alloy Factory No.1 Lv.30;
  - norm 330,540 selected Titanium Alloy Factory No.2 Lv.30;
  - norm 617,570 (the pinned Lv.27 coordinate from 2026-10-31)
    selected Missile Vehicle Base Lv.10 in this camera position.
  The barracks tent row is therefore not in this pan, and its pinned
  coordinates do not transfer across camera positions. No TRAIN UNITS
  panel was reached, no batch was collected or started, and the Drill
  Ground panel was not re-read in this unit, so the Drill Ground Full
  state is carried forward unverified, not re-asserted.
- Tracker untouched (partial unit), per the queue rules: the next tick
  re-produces this regular. The next training unit should pan to the
  tent row first rather than repeat taps in this factory pan.
- No diamonds, money, speedups or paid buttons were used. No building,
  research or assembly action was taken.

## Result statistics

- barracks_checked: 0
- barracks_collected: 0
- barracks_requeued: 0
- drill_ground_checked: 0
- drill_ground_full: unverified
- target: one barracks batch collected or requeued
- achieved: 0
- resources_gained: none
- costs: about 4 minutes, no items consumed
- verified: no
- blocker_category: c
