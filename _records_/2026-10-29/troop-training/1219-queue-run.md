---
title: Troop Training Execution 2026-10-29 1219 Queue Run
created: 2026-10-29T19:19:00Z
modified: 2026-10-29T19:19:00Z
level: L0
version: 1.0.0
description: Training queue unit training-2026-10-29-1003 - partial, game opened on the world map so early taps selected world tiles, base view restored and the tent row tapped twice without opening a barracks button row, no TRAIN UNITS panel, no batch queued
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-10-29
  - source: owner directions of 2026-10-25, 2026-10-26 and 2026-10-28 - the standing routine, Mac control authorization and the task unit queue ticker
---

# Troop training — execution, 2026-10-29 1219 queue unit

A single task unit, executed by executor ticker-1204 under the
task unit queue. Unit training-2026-10-29-1003.
Session window about 12:04 to 12:19 America/Los_Angeles.
Status — partial; the tracker is left untouched so the
next tick re-produces this regular.

## What was done

- Open — the game was already running on the Mac mini
  in sessions cc-282, cc-283 and cc-284 (each session
  had to be restarted once its observation channel
  closed mid-unit; no access error and no
  different-device dialog appeared at any point).
  HUD food 230.6M, iron 415.5M, coin 105.8M, total
  power 149,357,472.
- Wrong view first — the game opened on the world
  map, not the base view. A tap at 833,562 selected
  a world tile with Teleport and Profession buttons,
  and a tap at 683,630 selected the world tile
  X:993 Y:952. Neither tap touched a building, and
  no Teleport was used. Lesson for the next unit -
  tap BASE first when the game opens on the world map.
- Base view restored — a tap on the BASE button
  switched the view to the base (the button then
  read WORLD), showing the tent row at the
  right-middle of the base.
- Tent taps without a panel — a tap at 810,715 on
  the tent row produced a visual change over the
  tents but no barracks button row, and a tap at
  841,736 on a tent body produced no observed change
  and no button row either. No paw details button,
  no pistol train button and no TRAIN UNITS panel
  were reached, so no batch was queued, no cost or
  timer was read, and Drill Ground Full was neither
  confirmed nor refuted in this unit.
- No batch was queued, no food or iron was spent,
  and no Finish Now, upgrade, diamond or money tap
  was made. No building or research started, no
  assembly or teleport.
- Tracker — untouched (partial unit), per the queue rules.
