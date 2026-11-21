---
title: Survivors queue run 1335
created: 2026-11-21T21:31:00Z
modified: 2026-11-21T21:31:00Z
version: 1.0.0
description: Queue unit survivors-2026-11-21-1003, executor ticker-1318 - partial, gate line unverified
status: unverified
---

# Survivors 13:20-13:31 PT - partial, gate line unverified

Executor ticker-1318. Unit survivors-2026-11-21-1003 (planned 10:03 PT,
expires 14:03 PT). Session 13:20-13:31 PT, about 11 minutes in game.

## What was verified live

- Mac mini online, Last War running windowed 788x1083 (window 105986,
  pid 5136), base screen, no "active on a different device" dialog, no
  login demand. Total power 149,653,371; food 730.5M, iron 1.1G, coin
  88.2M, diamonds 5,236; stamina 18 rising to 19 during the unit.
- The fullscreen precondition from Issue #648 is currently CLEAR: the
  window is no longer fullscreen 1920x1080 on its own Space (the state
  the 12:04 ticker-1204 pass recorded). The user evidently handled the
  Mac between 12:47 and 13:19. Pointer input reaches the window again
  (clicks dispatched, visual change observed on the hero select).
- Gate front, fresh grounding: visual grounding plus a 2x enlarged crop
  of the gate area (right side, arched-pipe gate). Two figures stand at
  the gate - a green-haired hero figure with a crossed-swords marker and
  a small dark-haired figure on the blue mat just inside the fence.
  Neither carries a "?" bubble in any screenshot of this unit, and no
  "?" bubble appears anywhere else on the visible base.
- Tap test: one tap on the small dark figure at window (595, 533)
  opened no survivor card or dialog; screen unchanged. That figure is
  not a tappable survivor (or the tap did not register as a game tap).

## What is NOT verified - why this closes partial, not done

- The ticker-1204 pass at 12:04 PT read TWO survivor "?" icons at the
  front door from the fullscreen screenshot. Those icons are absent now
  and I did not collect them. Whether the owner collected them, or they
  despawned, or they sit off-screen, is unestablished - so the line
  cannot be closed as empty on inference.
- The base view cannot be panned through this control channel: a plain
  drag, a stepped drag (30 steps, 1.5 s), and a scroll all produced no
  view movement (outcome_unknown / no_change_observed), and the window
  zoom-button click had no effect (window stayed 788x1083). The
  off-screen part of the gate front therefore stays unchecked.
- No Quick Dispatch: no recruit was taken in, so there is nothing to
  dispatch after, and the building panels were not opened.

## Outcome

- Survivors recruited: 0. Question bubbles found: 0. Quick Dispatch: not run.
- Status partial, verified no, blocker_category c (tap/pan method: the
  candidate-figure tap opened nothing and the view cannot be panned, so
  the full gate front is unreachable this unit).
- Tracker untouched (partial). Re-read owed at the next survivors slot:
  re-ground the gate first, and try a pinch-zoom-out or a foreground
  drag to pan before tapping; if the two "?" icons are still absent at
  the next read, the line may be recorded empty only once a full-gate
  view confirms it.
- Follow-up for Issue #648: the fullscreen precondition cleared between
  12:47 and 13:19 PT (windowed again, input works); comment owed on the
  issue naming the clearance and the still-open pan limitation.

## Red lines

No diamonds or money spent, no paid button tapped, no speedup burned,
no research, building, assembly or teleport touched.
