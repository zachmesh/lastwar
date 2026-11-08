---
title: Troop Training Execution 2026-10-30 1613 Queue Run
created: 2026-10-30T23:13:00Z
modified: 2026-10-30T23:13:00Z
level: L0
version: 1.0.0
description: Training queue unit training-2026-10-30-1403 - partial, no barracks queue read, tracker untouched
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-10-30
  - source: owner directions of 2026-10-25, 2026-10-26 and 2026-10-28 - the standing routine, Mac control authorization and the task unit queue ticker
---

# Troop training — execution, 2026-10-30 1613 queue unit

A single task unit, executed by executor ticker-1604 under the
task unit queue. Unit training-2026-10-30-1403.
Session window about 16:05 to 16:13 America/Los_Angeles.
Status — partial; the tracker is left untouched so the
next tick re-produces this regular.

## What was done

- Open — the game was on the base screen in window mode
  (642x951), no different-device dialog appeared, no login
  or verification was demanded. Computer session cc-539.
  HUD at the open — food 300.2M, iron 483.4M, coin
  151.2M, total power 146,857,078 at the later read.
- Barracks search — a drag from norm 500,700 to 500,400
  did not move the map view, and a scroll at norm
  500,500 did not zoom it, so the current camera position
  could not be panned to a new barracks row. A tap at
  norm 780,650 produced no change. A tap at norm
  840,700 on a beige tent with a blue wave marking in
  the right-middle of the base produced a visual change
  in that tile but opened no panel — those tents carry
  survivor icons and read as survivor shelters, not
  barracks. No TRAIN UNITS panel was located in this
  unit, so no barracks queue timer was read and no
  batch was started. This is the fourth training unit
  today (0248, 0714, 1119) to end without locating a
  barracks tent in the current camera position; the
  tent row location remains unresolved and should be
  pinned down (for example from the 2026-10-25 first
  execution camera position, or via a building list)
  before further training units are attempted.
- Nothing bought, no diamond spent, no speedup item
  burned, no Finish Now, no green upgrade shortcut
  tapped, no assembly or teleport.
- Tracker — untouched (partial unit), per the queue rules.

## Result statistics

- barracks_checked: 0
- batches_started: 0
