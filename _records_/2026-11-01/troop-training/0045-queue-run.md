---
title: Troop Training Execution 2026-11-01 0045 Queue Run
created: 2026-11-01T07:45:00Z
modified: 2026-11-01T07:45:00Z
level: L0
version: 0.1.0
description: Training queue unit training-2026-10-31-2203 - partial, no barracks selected in a drifted camera view, inherited tap points missed, Drill Ground panel not reached, no batch collected or started, tracker untouched
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-11-01
  - source: owner directions of 2026-10-25, 2026-10-26 and 2026-10-28 - the standing routine, Mac control authorization and the task unit queue ticker
---

# Troop training — execution, 2026-11-01 0045 queue unit

A single task unit, executed by executor ticker-0034 under the
task unit queue. Unit training-2026-10-31-2203, priority 3.
Session window about 00:42 to 00:45 America/Los_Angeles.
Computer session cc-729, window mode (642x951).
Status — partial: no barracks was selected, no batch was
collected or started, so the tracker is untouched and
the next tick re-produces this regular.

## What was done

- Open — the game was already on the base screen from
  the preceding survivors unit, no different-device
  dialog appeared, no login or verification was
  demanded. HUD at the open — food 289.2M, iron 477.2M,
  coin 10.6M, total power 148,957,193.
- Standing instruction attempted — the activity metadata
  directs this unit to read the Drill Ground screen live
  first. That read was attempted and not achieved: see
  below.
- Inherited points missed, camera drifted — a tap at
  norm 708,602 (the pinned Drill Ground / Lv.30 point
  from the 2026-10-31 03:04 and 07:04 units) selected
  nothing visible in this camera view, and a tap at
  norm 617,570 (the pinned Lv.27 tent point from the
  15:44 unit) likewise selected nothing — no label, no
  button row. The camera had drifted through the
  survivors unit's pans, so both inherited points were
  stale here. This is the queue rule R2 failure mode in
  miniature: points must be measured fresh in the
  unit's own camera view, never inherited, and this
  unit records the miss instead of repeating the taps.
- Fresh grounding attempted — an enlarged crop of the
  base centre in this view shows production houses
  carrying 59.6K resource bubbles, a helicopter pad and
  a green military vehicle, but no barracks tent row
  that could be grounded with confidence. No further
  tap was made on an ungrounded candidate, so no
  TRAIN UNITS panel opened, no Drill Ground panel
  opened, and no toast (including Drill Ground Full)
  was read live in this unit. The standing full-drill-
  ground block from 2026-10-31 (39,460/39,460) is
  therefore carried forward unverified, not re-
  confirmed and not cleared.
- Focus note — pans in this unit again stopped moving
  the view after a focus loss and resumed only after a
  title-bar left-segment tap at norm 274,18, matching
  the survivors unit in the same pass.
- Not attempted — no batch was collected, no batch was
  started, no troops were deployed or dismissed to free
  drill-ground space (an owner-side decision, outside
  this unit). No Finish Now, no green upgrade shortcut,
  no purchase, no diamond spend, no speedup item
  burned, no assembly or teleport. No other regular
  was merged into this unit. The game was left on the
  base screen.

## Result statistics

- barracks_checked: 0
- batches_collected: 0
- batches_started: 0
- drill_ground_checked: 0
- target: all-idle-barracks-requeued
- achieved: 0
- resources_gained: none
- costs: about-3-minutes-no-items
- verified: no
- blocker_category: e
