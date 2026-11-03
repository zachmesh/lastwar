---
title: Queue Run 1845 Truck Plunder
created: 2026-11-02T18:43:00Z
modified: 2026-11-02T18:43:00Z
level: L0
version: 1.0.0
description: Trucks unit entry blocked, partial, tracker untouched
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-11-02
---

# 1845 queue run - truck plunder (partial)

Unit trucks-2026-11-02-1457, executor ticker-1834, session
about 18:35 to 18:43 America/Los_Angeles. Status partial:
the trade screen could not be entered, so no counter was
read live, no truck was dispatched and no plunder was made.
Tracker untouched (partial units do not mark the
tracker). The trade day ends at 19:00 local.

## Duel posture

- Duel day 2, Base Expansion, from tools/duel.py at unit
  start. UR truck dispatches score on a duel UR day, but
  no dispatch was reached. Radar posture stack.

## Device dialog, two takeovers

- The game opened on the "Your account is currently
  active on a different device!" dialog. Confirm was
  tapped at its measured centre, norm 501,568, after an
  earlier mis-read of the coordinate system sent two
  taps to norm 780,597, near the dialog right edge,
  which did nothing. Lesson: the OCR coordinates in
  this control channel are already 0 to 1000
  normalised, not window pixels; do not rescale them.
- Confirm took over once and the app exited, as the
  owner rule expects; it was reopened and the dialog
  returned a second time, was confirmed a second
  time, and the app was reopened again. After the
  second takeover the base screen stayed clean with
  no further dialog. Takeover count for this pass: 2.
  No third dialog appeared, so the pass did not stop
  as contested.

## Entry blocker, methods tried

- Base left column re-grounded fresh with visual
  grounding on the current screenshot. Round icons,
  top to bottom: green face at norm 53,577, white
  pickup at 53,639, radar dish at 53,707, hammer
  below. No blue train-front trade icon is present
  in this set, and no left-column icon carries a
  trade badge.
- Tap at norm 52,553 (the 0935 and 1325 units'
  grounding) opened the season warming panel
  (Location final temp 6.5 degrees C, Permafrost
  Area, Alliance Furnace), not trade. The panel was
  closed with its X, first at 896,152 missed, then
  at 915,150 closed it.
- World map route tried next, per the 0114
  successor instruction: WORLD opened the map
  centred on the own base [AP3x]Bears Lair, showing
  alliance bases only and no trade entry on that
  view. BASE returned to the base screen.
- White pickup at 53,639 opened the Secret Command
  Post (Secret Mobile Squad, Your Tasks), as the
  metadata predicts, not trade. Its back arrow
  returned to the base. No Mega button was touched.
- Per queue rule R2 this is the entry blocker for
  the next trucks unit: do NOT re-tap the points
  above. The successor must find the set-flip
  control or another trade entry route before any
  column tap, and re-ground the column from a fresh
  screenshot. The 2026-10-30 hypothesis still fits:
  the trade slot surfaces only while a returned
  truck awaits settlement, and none awaited here
  (Trade Count already 5 of 5 at the 1325 close).

## Counters

- Not read live in this unit: the trade screen was
  never entered, so no live counter exists for this
  unit. The plunder shortfall of 1 (Plunder Count
  3 of 4, Trade Count 5 of 5) is carried from the
  1325 record only, NOT re-read, and is not claimed
  as a live figure. The next trucks unit must read
  both counters live on entry.
- This is a last-hour shortfall: the trade day ends
  at 19:00 local, under 20 minutes after this unit
  closed. Under queue rule R6 the shortfall is named
  here and the next trucks unit, if any runs before
  the reset, must work it inside itself.

## Outcome

- Status: partial, blocker_category e (repeated
  blocker, entry method).
- Claimed in this unit: none.
- Counters: not read live (see above).
- Red lines: no diamonds, no Trade Contracts, no
  paid button, no alliance mate plundered, no Mega
  button touched, no assembly.
- Zombie seeding: not enqueued. The Zombie Invasion
  event ended 2026-10-30 and no live return sighting
  occurred in this pass; the chain stands at 66 done
  units with no pending unit.
