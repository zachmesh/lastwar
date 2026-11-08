---
title: Queue Run 2048 Survivor Intake Partial
created: 2026-11-01T20:48:00-08:00
modified: 2026-11-01T20:48:00-08:00
version: 1.0.0
description: Ticker pass ticker-2034 survivors unit, partial, gate line not verified after a base sweep
status: partial
---

# 2048 queue run - survivor intake, partial

Session window: 2026-11-01 about 20:35 to 20:48 America/Los_Angeles.
Executor: ticker-2034. Unit: survivors-2026-11-01-1803 (regular
survivors, activity survivor-intake).

## Outcome

- Status: partial. No survivor was processed in this unit: the
  front-gate line was never verified, so no recruit card or
  dialog survivor was tapped and no claim is made about the
  line state. Tracker untouched; the next tick re-produces
  the regular and the work resumes as a fresh unit.
- No different-device dialog, no login or verification demanded.
  No diamonds or money spent, no paid button tapped, no other
  activity worked from this unit.

## What was done

1. LastWar already running on the Mac mini, window 642 by 951,
   base screen read live: food 353.1M, iron 543.9M, coin
   30.1M, diamonds 2,396, total power 149,288,895.
2. A visual-grounding call on the opening base screenshot
   timed out (180 seconds, no result), so the gate was
   sought by panning instead.
3. Base sweep, in order: one horizontal drag produced no view
   change; two vertical drags panned the view south past the
   base edge into empty snow and rock; a partial drag back
   showed the south-west wall; a diagonal drag panned the
   view north-east to the built area's east wall and fence
   corner; a further diagonal drag in the same direction hit
   the pan limit with no view change; a return drag
   south-west also produced no view change. No
   question-mark bubble and no survivor line was visible in
   any of these views.
4. One tap on a small round world icon at norm 249,641
   (pixel about 160,610) produced no change and no dialog:
   that icon is not a tappable survivor figure, and it was
   left alone after the single tap.
5. Re-read pointer for the next unit, from the same day's
   successful 1644 run (survivors-2026-11-01-1403, done):
   that unit located the gate survivor fresh by visual
   grounding at question-mark bubble norm 460,632 and
   survivor figure norm 458,678, in front of the signed
   gate at the bottom centre of the base. The next unit
   should start from the opening base view and pan toward
   the base's bottom centre, not north-east, and should
   ground the gate figure before any tap.

## Quick Dispatch

- Not run: no survivor was taken in, so no newcomer took a
  building post in this unit.

## Closing figures, read live in this unit

- Survivors processed: 0, verified by the absence of any
  recruit card, dialog or bubble change in this unit.
- Gate line at close: unverified, not claimed clear and not
  claimed occupied.
- Resources gained: none observed.

## Issue handling

- No new issue filed: this is the known repeated
  survivors gate-verification failure mode already recorded
  as a standing blocker in the survivor-intake activity
  metadata, not a new gap. The matching open issue #123
  (screenshot-grounded tap calibration) received a comment
  with this unit's evidence and the 1644 re-read pointer.

## Red lines

- No diamonds or money spent, no paid button tapped, no
  Renew, Finish Now, Legendary Claim All or Battle Pass paid
  unlock touched. No base move, no Assemble, no teleport.
