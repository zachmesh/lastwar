---
title: Troop Training Execution 2026-10-31 1055 Queue Run
created: 2026-10-31T17:55:00Z
modified: 2026-10-31T17:55:00Z
level: L0
version: 0.1.0
description: Training queue unit training-2026-10-31-1003 - partial, Lv.30 tent located and its Building Details panel read, TRAIN UNITS panel not reached after two button taps, no batch collected or started, other barracks not checked
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-10-31
  - source: owner directions of 2026-10-25, 2026-10-26 and 2026-10-28 - the standing routine, Mac control authorization and the task unit queue ticker
---

# Troop training — execution, 2026-10-31 1055 queue unit

A single task unit, executed by executor ticker-1034 under the
task unit queue. Unit training-2026-10-31-1003, priority 3.
Session window about 10:50 to 10:55 America/Los_Angeles.
Status — partial: only the Lv.30 tent was located and
read, no batch was collected or started, and the other
barracks were not checked, so the tracker is untouched
and the next tick re-produces this regular.

## What was done

- Open — the game was already on the base screen from
  the preceding survivors unit, no different-device
  dialog appeared, no login or verification was
  demanded. Computer session cc-640 dropped between
  units and cc-641 resumed with no state lost,
  matching the session-drop pattern seen in earlier
  units. HUD at the open — food 337.1M, iron 523.2M,
  coin 177.1M, total power 148,939,659.
- Barracks Lv.30 located — a tap at the pinned norm
  708,602 selected the tent (label "Barracks Lv.30"
  with its round button row), confirming the camera
  position from the 2026-10-31 07:04 training unit
  still holds. The tent was re-selected the same way
  after the session resume.
- Panel mismatch, closed untouched — a tap at norm
  623,615, intended for the pistol button to open
  TRAIN UNITS, instead opened the Building Details
  panel (Training Count +793, Survivors Marcus,
  Taylor, Daniel and Michael, all Instructor, and a
  Quick Dispatch button). The Details panel does not
  show the in-training timer, so the Lv.30 batch
  state is NOT verified from it. Quick Dispatch was
  deliberately NOT tapped — survivor posting belongs
  to a different flow — and the panel was closed
  with its X button at norm 818,137.
- Second button tap, no-op — a tap at norm 720,615,
  one button spacing right of the first, opened no
  panel at all; the button row stayed visible and the
  base view was unchanged. The button-row mapping in
  norm space therefore needs re-grounding by the next
  training unit before any Train tap: the first tap
  landed on the paw/Details button, the second on a
  dead spot, so the pistol button's live norm point
  is still unpinned.
- Not attempted — no batch was collected or started,
  the Lv.24 requeue and the Lv.27 location from the
  07:04 unit's close remain open, and the Lv.20
  drill-ground-full block was not re-touched (owner
  decision, outside this unit).
- Nothing bought, no diamond spent, no speedup item
  burned, no assembly or teleport. No other regular
  was merged into this unit. The game was left on
  the base screen.

## Result statistics

- barracks_checked: 1
- batches_collected: 0
- batches_started: 0
