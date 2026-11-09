---
title: Troop Training Execution 2026-10-31 0704 Queue Run
created: 2026-10-31T14:10:00Z
modified: 2026-10-31T14:10:00Z
level: L0
version: 0.1.0
description: Training queue unit training-2026-10-31-0603 - partial, Drill Ground confirmed full, Lv.30 already training, collection blocked, no batch started, tracker untouched
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-10-31
  - source: owner directions of 2026-10-25, 2026-10-26 and 2026-10-28 - the standing routine, Mac control authorization and the task unit queue ticker
---

# Troop training — execution, 2026-10-31 0704 queue unit

A single task unit, executed by executor ticker-0704 under the
task unit queue. Unit training-2026-10-31-0603, priority 3.
Session window 07:04 to about 07:10 America/Los_Angeles.
Status — performed in part: no barracks queue was read
and no batch was started or collected, so the tracker is
untouched and the next tick re-produces this regular.

## What was done

- Open — the game was already on the base screen, no
  different-device dialog appeared, no login or
  verification was demanded. HUD at the open — food
  328.7M, iron 522.7M, coin 176.8M, total power
  148,939,659, matching the 03:04 training unit close.
- Window covered — the LastWar window was covered by
  Google Chrome at the start; a click on the title bar
  left segment (norm 274,18, clear of the green zoom
  button) brought the game forward, and the window
  stayed in window mode throughout, never fullscreen.
- Pinned-position check — the 03:04 record's Lv.30
  position (norm 708,602) was tapped. In this camera
  position it selected the Drill Ground Lv.30, not a
  barracks tent, and its small button at 710,638 opened
  the DRILL GROUND panel rather than TRAIN UNITS.
- Drill Ground confirmed full — the panel read Unit
  Count 39460/39460, In Base Lv.7 701, Lv.8 1,332 and
  Lv.10 37.4K, Outside "No units outside". This confirms
  and explains the 03:04 Lv.20 block ("Drill Ground
  Full: Unable to add more units"): finished batches
  cannot be collected until drill-ground space is freed.
  No troops were deployed or dismissed to free space —
  that is an owner-side decision, outside this unit.
- Panel-close note — two taps on the panel X (norm
  802,179 and 807,181) did not close the panel in the
  observed receipts. An Escape key press then exited
  the app entirely (the known Esc-crashes-LastWar
  behaviour); the app was reopened with open_app, came
  back on the base screen with the same HUD and total
  power, and no different-device dialog appeared.
  Never use Escape on this app again.
- Tent search, limited — after reopen, one tap in the
  upper-left base area and one tap on a central small
  house selected the Titanium Alloy Factory No.1
  Lv.30, not a barracks. No barracks tent with a TRAIN
  UNITS panel was located in this unit.
- Standing state carried forward — Lv.30 was already
  requeued by the 03:04 unit (1 day 17:14 at requeue,
  so not due); the 03:04 Lv.24 finished batch was
  collected but its requeue was not completed, and it
  now also sits behind the full drill ground; Lv.27
  remains unlocated; Lv.20 remains blocked as above.
- Nothing bought, no diamond spent, no speedup item
  burned, no Finish Now, no green upgrade shortcut
  tapped, no assembly or teleport. No other regular
  was merged into this unit.

## Result statistics

- barracks_checked: 0
- batches_collected: 0
- batches_started: 0
- drill_ground_checked: 1
- drill_ground_full: 1

## Close

- Next training unit should not repeat the blind tent
  search in this camera position, and should not expect
  a collection to succeed while the drill ground reads
  39460/39460. The owner-side space decision is the
  gate for the Lv.20 and Lv.24 batches.
