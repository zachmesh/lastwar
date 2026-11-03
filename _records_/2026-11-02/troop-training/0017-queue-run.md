---
title: Queue Run 0017 Troop Training Partial
created: 2026-11-02T00:17:00-08:00
modified: 2026-11-02T00:17:00-08:00
version: 1.0.0
description: Ticker pass ticker-0004 training unit, partial, barracks tents not located after the changed east-pan route
status: partial
---

# 0017 queue run - troop training, partial

Session window: 2026-11-02 about 00:16 to 00:17 America/Los_Angeles.
Executor: ticker-0004. Unit: training-2026-11-01-2203 (regular
training, activity troop-training).

## Outcome

- Status: partial. No barracks panel was opened, no batch was
  queued, no Drill Ground screen was read, and nothing was
  claimed. The tracker is left untouched, so the next tick
  re-produces the regular and the work resumes as a fresh unit.
- No different-device dialog, no login or verification demanded.
  No diamonds or money spent, no paid button tapped, no
  Finish Now, no upgrade shortcut, no other activity worked
  from this unit.

## What was done

1. Troop-training metadata read before acting, including the
   standing blocker: the 2026-10-31 retro recorded Drill
   Ground Full (39,460 of 39,460) blocking collection and
   requeue in every 2026-10-31 unit that reached a barracks,
   and the 2120 unit of 2026-11-01 ruled out the map south
   and north edges and directed the next unit to pan east
   toward the dense red-roofed formation instead of
   repeating the south or north pans.
2. Changed route taken, per queue rule R2: one east pan
   (drag norm 320,450 to 120,450) from the opening base
   view. The resulting view shows formation lots 2 and 3,
   parked tanks and a blue structure at the top, and
   production buildings at the left edge - no row of four
   barracks tents, and no tent was visually verified, so
   no tent was tapped on a guess.
3. Base screen read live at unit start: food 362.4M, iron
   555.0M, coin 36.7M, diamonds 2,476, total power
   149,198,310.

## What this rules out

- The formation-lot view reached by the east pan is not the
  barracks tent row. The 2026-10-31 pinned tent coordinates
  (Lv.30 tent at norm 708,602, Lv.27 tent at 617,570 in a
  lower-middle base view) were not reproduced in this
  unit's camera position, so they were not tapped as fixed
  points. The next unit must change the route again: pan
  from the opening view toward the lower-middle base area
  where the pinned coordinates were measured, and only tap
  a tent visually verified as a tent.
- The Drill Ground Full blocker was neither confirmed nor
  cleared in this unit: no barracks was reached, so no
  Drill Ground figure is claimed here.

## Closing figures

- Batches queued: 0, read live as no panel opened.
- Barracks checked: 0 of 4. Drill Ground count: not read.
- Resources gained: none observed.

## Red lines

- No diamonds or money spent, no paid button tapped, no
  Renew, Finish Now, Legendary Claim All or Battle Pass paid
  unlock touched. No base move, no Assemble, no teleport.
