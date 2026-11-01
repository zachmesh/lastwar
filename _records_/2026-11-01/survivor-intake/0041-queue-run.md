---
title: Survivor Intake Execution 2026-11-01 0041 Queue Run
created: 2026-11-01T07:41:00Z
modified: 2026-11-01T07:41:00Z
level: L0
version: 0.1.0
description: Survivors queue unit survivors-2026-10-31-2203 - partial, gate line not found in four pans, no question-mark bubbles verified, no recruit taken, tracker untouched, duplicate-attempt disclosure
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-11-01
  - source: owner directions of 2026-10-25, 2026-10-26 and 2026-10-28 - the standing routine, Mac control authorization and the task unit queue ticker
---

# Survivor intake — execution, 2026-11-01 0041 queue unit

A single task unit, executed by executor ticker-0034 under the
task unit queue. Unit survivors-2026-10-31-2203, priority 3.
Session window about 00:35 to 00:41 America/Los_Angeles.
Computer session cc-729, window mode (642x951).
Status — partial: the gate line was not found in this unit,
no survivor was taken in, Quick Dispatch was not run, so
the tracker is untouched and the next tick re-produces
this regular.

## What was observed

- Open — the game was already on the base screen, no
  different-device dialog appeared, no login or
  verification was demanded. HUD at the open — food
  289.2M, iron 477.2M, coin 10.6M, total power
  148,957,193.
- Focus lesson, re-confirmed — the game window was not
  frontmost at the start (UserNotificationCenter was),
  and pans sent as background input did not move the
  view until a title-bar left-segment tap at norm
  274,18 (clear of the green zoom button) brought the
  game forward. The same focus loss recurred later in
  the pass and was fixed the same way. Never tap near
  the green zoom button; the window stayed in window
  mode throughout, never fullscreen.
- Gate search, four pans — the opening pan showed the
  central base with production houses carrying resource
  bubbles and no question-mark survivor line. A drag
  from norm 400,600 to 650,350 moved the view to the
  headquarters corner; a drag from 623,736 to 389,526
  moved it to the outer snow field; enlarged crops of
  the left edge and the top-right road showed turrets,
  a STOP sign and formation vehicles, but no gate line
  and no question-mark bubbles. A fourth drag from
  350,350 to 600,600 did not move the view at all
  (focus had been lost again) and was not counted as
  a searched pan.
- Grounding note — a visual-grounding call for the
  survivor line timed out without a result and was not
  retried; all conclusions here rest on the screenshots
  and crops read directly, not on grounding output.
- Not verified — the line was not verified across all
  pans, so no survivor figure was tapped and no
  recruit card or dialog was opened. This unit does
  not claim the gate is empty, only that no waiting
  line was found in the pans searched.
- Not touched — no other regular was merged into this
  unit. No purchase, no diamond spend, no speedup item
  burned, no assembly or teleport. The game was left
  on the base screen.

## Duplicate-attempt disclosure

- This unit id had already been completed partial by
  ticker-0004 earlier the same morning (evidence
  _records_/2026-11-01/survivor-intake/0016-queue-run.md,
  result in _queue_/done/survivors-2026-10-31-2203.md).
  This pass re-ran it because the local working tree
  still carried the unit in inbox — its queue state had
  not caught up with the records branch. The branch's
  done file for this unit is left exactly as
  ticker-0004 wrote it; this record is the only
  survivors artifact this pass commits, and the
  re-execution is recorded here rather than hidden.
  The queue-state divergence between the working tree
  and the records branch is an open process item for
  the next queue review, not a game-state change.

## Result statistics

- survivors_recruited: 0
- survivors_dialog: 0
- question_bubbles_found: 0
- target: all-waiting-survivors
- achieved: 0
- resources_gained: none
- costs: about-7-minutes-no-items
- verified: no
- blocker_category: e
