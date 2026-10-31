---
title: Troop Training Execution 2026-10-30 2245 Queue Run
created: 2026-10-31T05:47:00Z
modified: 2026-10-31T05:47:00Z
level: L0
version: 0.1.0
description: Training queue unit training-2026-10-30-2203 - partial, no new barracks search, tracker untouched, following repeated failed location units today
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-10-30
  - source: owner directions of 2026-10-25, 2026-10-26 and 2026-10-28 - the standing routine, Mac control authorization and the task unit queue ticker
---

# Troop training — execution, 2026-10-30 2245 queue unit

A single task unit, executed by executor ticker-2234 under the
task unit queue. Unit training-2026-10-30-2203, priority 3.
Session window 22:45 to about 22:47 America/Los_Angeles.
Status — performed in part: no barracks queue was read
and no batch was started, so the tracker is untouched
and the next tick re-produces this regular.

## What was done

- No new blind barracks search was run in this unit.
  Five training units today (0248, 0714, 1119, 1613,
  1918) already searched for the barracks tent row and
  each ended without locating a tent with a TRAIN
  UNITS panel; the 1918 record explicitly recommends
  pinning the tent row down (for example from the
  2026-10-25 first-execution camera position, or via
  a building list) before further training units are
  attempted. Repeating the same blind taps in the
  gate-area camera position left by the preceding
  survivors unit would not change that evidence.
- The game was left on the plain base view from the
  preceding survivors unit, with no different-device
  dialog, no login or verification demanded.
- Nothing bought, no diamond spent, no speedup item
  burned, no Finish Now, no green upgrade shortcut
  tapped, no assembly or teleport. No other regular
  was merged into this unit.

## Result statistics

- barracks_checked: 0
- batches_started: 0

## Close

- Next training attempt should first pin the barracks
  tent row location from a known-good camera position
  or building list, rather than re-running the blind
  search in this camera position.
