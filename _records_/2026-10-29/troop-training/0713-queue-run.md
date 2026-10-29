---
title: Troop Training Execution 2026-10-29 0713 Queue Run
created: 2026-10-29T14:13:00Z
modified: 2026-10-29T14:13:00Z
level: L0
version: 1.0.0
description: Training queue unit training-2026-10-29-0603 - failed, Barracks Lv.24 pistol tap returned a Drill Ground Full toast and no TRAIN UNITS panel, then the Mac mini device channel went offline and stayed offline through repeated session retries, no batch queued
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-10-29
  - source: owner directions of 2026-10-25, 2026-10-26 and 2026-10-28 - the standing routine, Mac control authorization and the task unit queue ticker
---

# Troop training — execution, 2026-10-29 0713 queue unit

A single task unit, executed by executor ticker-0704 under the
task unit queue. Unit training-2026-10-29-0603.
Session window about 07:04 to 07:13 America/Los_Angeles.
Status — failed; the tracker is left untouched so the
next tick re-produces this regular.

## What was done

- Open — the game was already on the base screen in
  session cc-248, HUD food 224.6M, iron 410.5M,
  coin 102.1M, total power 149,357,472. No
  different-device dialog appeared.
- Barracks Lv.24 located — a tent tap at 833,562
  selected Barracks Lv.24, with its button row showing
  the paw details button, the pistol train button and
  the green upgrade arrow (the upgrade arrow was not
  touched, per the activity limits).
- Drill Ground Full — a tap on the pistol button at
  817,572 did not open TRAIN UNITS; the observation
  captured the toast "Drill Ground Full: Unable to
  add more units" and the view returned to the
  standard base screen with the barracks deselected.
  No batch was queued from this barracks, and no cost
  or timer was read.
- Second tent tap — a tap at 683,630 on a neighbouring
  tent was dispatched but its evidence capture went
  stale, so no selection from that tap is claimed.
- Device channel offline — the next observation
  returned node_offline for the Mac mini, with no
  wake-up path advertised; its last seen time was
  2026-10-29T14:07:36Z. Five further computer session
  starts on the Mac mini returned the same offline
  error, meeting and exceeding the at-least-3-attempts
  rule in the recording rules before this unit is
  written down as access-failed. A connection repair
  check on the recovery channel reported healthy, but
  the main Mac mini channel still returned offline
  afterwards. No input after the offline error is
  known to have been dispatched, so no batch, claim
  or purchase can be attributed to this unit after
  that point.
- No batch was queued, no food or iron was spent,
  and no Finish Now, upgrade, diamond or money tap
  was made. No building or research started, no
  assembly or teleport.
- Tracker — untouched (failed unit), per the queue rules.
