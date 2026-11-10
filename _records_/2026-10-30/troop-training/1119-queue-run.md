---
title: Troop Training Execution 2026-10-30 1119 Queue Run
created: 2026-10-30T18:19:00Z
modified: 2026-10-30T18:19:00Z
level: L0
version: 1.0.0
description: Training queue unit training-2026-10-30-1003 - partial, no barracks queue read, tracker untouched
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-10-30
  - source: owner directions of 2026-10-25, 2026-10-26 and 2026-10-28 - the standing routine, Mac control authorization and the task unit queue ticker
---

# Troop training — execution, 2026-10-30 1119 queue unit

A single task unit, executed by executor ticker-1104 under the
task unit queue. Unit training-2026-10-30-1003.
Session window about 11:05 to 11:19 America/Los_Angeles.
Status — partial; the tracker is left untouched so the
next tick re-produces this regular.

## What was done

- Open — the game was on the base screen in window mode
  (642x951), no different-device dialog appeared, no login
  or verification was demanded. Computer sessions cc-485
  then cc-488 after a mid-unit session drop; the drop lost
  no game state and the game was re-selected cleanly.
  HUD at the open — food 289.2M, iron 476.6M, coin
  145.9M, total power 146,857,078 at the later read
  (up from 146,850,228 at the 0714 unit).
- Barracks search — a tap at norm 520,600 hit a supply
  truck area and showed the tooltip "Collecting
  supplies, ready to depart again", with the tank-icon
  and green-upgrade buttons already visible below it
  (green upgrade shortcut not tapped). A tap at norm
  180,220 left the base view with no barracks panel and
  no TRAIN UNITS panel; the view then showed the full
  base UI with left sidebar and right Events panel.
  No individual barracks tent with a TRAIN UNITS panel
  was located in this unit, so no barracks queue timer
  was read and no batch was started. This is the third
  training unit today (0248, 0714) to end without
  locating a barracks tent in the current camera
  position; the tent row location remains unresolved
  and should be pinned down (for example from the
  2026-10-25 first execution camera position) before
  further training units are attempted.
- Nothing bought, no diamond spent, no speedup item
  burned, no Finish Now, no green upgrade shortcut
  tapped, no assembly or teleport.
- Tracker — untouched (partial unit), per the queue rules.

## Result statistics

- barracks_checked: 0
- batches_started: 0
