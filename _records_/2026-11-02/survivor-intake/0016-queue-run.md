---
title: Queue Run 0016 Survivor Intake Partial
created: 2026-11-02T00:16:00-08:00
modified: 2026-11-02T00:16:00-08:00
version: 1.0.0
description: Ticker pass ticker-0004 survivors unit, partial, gate line not verified after a base sweep
status: partial
---

# 0016 queue run - survivor intake, partial

Session window: 2026-11-02 about 00:05 to 00:16 America/Los_Angeles.
Executor: ticker-0004. Unit: survivors-2026-11-01-2203 (regular
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
   base screen read live: food 362.4M, iron 555.0M, coin
   36.7M, diamonds 2,476, total power 149,198,310.
2. Own PRs first: the only open PR for zachmesh/lastwar is
   PR 157 (records/2026-11-01, Owner: lastwar-pr-integrator),
   with no comments and merge state clean, so nothing was
   addressed to this job and nothing was answered or fixed
   there before the game work.
3. Sync reaped nothing and produced nothing new - all 20 due
   regulars were already queued by the planner. No zombie
   chain was seeded: the Zombie Invasion event ended at
   about the 19:00 reset on 2026-10-30 (chain unit 066) and
   no zombie-invasion unit sits in the pool, matching the
   standing event-closed state.
4. Gate search: one tap on a visual-grounding box at norm
   207,556 produced no change and no dialog - that box did
   not resolve to a survivor figure. Two further visual
   grounding calls on fresh base screenshots returned
   unreliable boxes (top-left UI icons, and a vehicle
   parking area), so no tap was taken from them.
5. Panning: a horizontal drag moved the view north-east and
   a reverse drag returned it to the opening view; a
   vertical drag produced no view change. No question-mark
   bubble and no survivor line was visible in any view.
   The computer session dropped once mid-unit and was
   restarted; the game window was re-selected and the base
   screen re-read live after the restart.
6. Re-read pointer for the next unit, from the successful
   1644 run of 2026-11-01 (survivors-2026-11-01-1403,
   done): that unit located the gate survivor fresh by
   visual grounding at question-mark bubble norm 460,632
   and survivor figure norm 458,678, in front of the signed
   gate at the bottom centre of the base. In this unit's
   opening view, norm 458,678 showed only snow, a bare
   tree and a wall corner - no survivor figure - so the
   pointer was not tapped on a guess. The next unit should
   re-ground the gate figure fresh before any tap, and
   should not treat the 1644 coordinates as a fixed tap
   point.

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
  metadata and in issue #123 (screenshot-grounded tap
  calibration), not a new gap. This unit is the second
  consecutive partial after the 1644 done, not a fourth
  identical partial in a row, so it is recorded as a
  partial here rather than reported as a process failure.

## Red lines

- No diamonds or money spent, no paid button tapped, no
  Renew, Finish Now, Legendary Claim All or Battle Pass paid
  unlock touched. No base move, no Assemble, no teleport.
