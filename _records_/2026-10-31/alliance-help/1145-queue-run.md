---
title: Alliance Help Execution 2026-10-31 1145 Queue Run
created: 2026-10-31T18:45:00Z
modified: 2026-10-31T18:45:00Z
level: L0
version: 0.1.0
description: Help queue unit help-2026-10-31-1030 - partial, Alliance panel never opened, no helps pressed, tracker untouched
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-10-31
  - source: owner directions of 2026-10-25, 2026-10-26 and 2026-10-28 - the standing routine, Mac control authorization and the task unit queue ticker
---

# Alliance help — execution, 2026-10-31 1145 queue unit

A single task unit, executed by executor ticker-1134 under the
task unit queue. Unit help-2026-10-31-1030, priority 3.
Session window about 11:36 to 11:47 America/Los_Angeles.
Status — performed in part: the Alliance panel was never
opened and no Help All was pressed, so the tracker is
untouched and the next tick re-produces this regular.

## What was done

- Computer sessions cc-644 then cc-645 after a session
  drop (observe returned observation_unavailable); the
  drop lost no game state and the game was re-selected
  cleanly. No different-device dialog appeared, no
  login or verification was demanded.
- The game was on the base screen in window mode
  (642x951), resources food 337.1M, iron 523.2M,
  coin 177.1M, power 148,939,659 at the first read.
  A visual-grounding call timed out and was not
  retried; it cost no game state.
- The base camera drifts on its own between a wide
  view (HEROES and WORLD visible, Alliance column on
  the right) and a south-east panned view (Drill
  Ground Lv.25 labelled at the right, three round
  buttons at the lower right). A tap on the green
  up-arrow button at norm 911,631 in the panned view
  restored the wide view once, as judged by the
  HEROES and WORLD elements returning.
- Alliance taps at norm 864,683 (twice) and 860,710
  produced no Alliance panel. The 864,683 taps
  reported a visual change in the 796,625 to 922,750
  region and the Drill Ground label appeared, which
  reads as a map-building tap reaching the game, not
  the Alliance UI button. The 860,710 tap produced no
  observed change. This is the same failure mode as
  unit gifts-2026-10-31-1030: background clicks reach
  map figures but do not reach the Alliance column
  button while Google Chrome stays frontmost, and
  computer control never brings an app to the front.
  The user's Chrome window was not moved or
  minimised, to avoid disturbing the foreground app.
- No Help All pressed, no ally request list read, no
  points header read, no diamonds or money spent.
  No other regular was merged into this unit.
- The game was left in window mode on the base
  screen. No other regular was merged into this unit.

## Result statistics

- help_all_pressed: 0
- ally_requests_cleared: 0

## Close

- Next help unit should first get LastWar actually
  frontmost before tapping Alliance, since background
  taps on that button repeatedly produced no change
  in this unit and in unit gifts-2026-10-31-1030,
  while map-figure taps did reach the game. The
  green up-arrow at norm 911,631 in the panned view
  restored the wide view once and may be reused as
  a camera reset before the Alliance tap.
