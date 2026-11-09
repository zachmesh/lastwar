---
title: Arms Race queue run 0058
created: 2026-11-09T08:59:00Z
modified: 2026-11-09T08:59:00Z
version: 1.0.0
description: Unit Progression phase read live, 0 points, scoring path identified, training fill not executed inside the unit cap
status: partial
grounded_in:
  - source: live game screen on the owner Mac mini, 2026-11-09 00:47-00:59 PT
---

# Arms Race queue run 0058 (ticker-0034)

Unit: arms-race-2026-11-08-2203. Status: partial.
Activity: arms-race. Phase: Unit Progression, Contest Segment Lv.29-30.

## Live reads

- Phase page (first read about 00:50 PT): Unit Progression, points 0,
  timer 01:09:14, chest thresholds 15,000 / 30,000 / 75,000 (top
  chest 75,000), cumulative counter chest 0/2, rank #2110
  [AP3x]Bears Lair, segment rank 9, 0 points. Closing read about
  00:58 PT: points still 0, timer about 01:06:05.
- Scoring paths as displayed: Train a Lv.10 unit pays +31; Use
  1-min Training Speed-up pays +10; Buy Packs containing Diamonds
  pays +30 per diamond.
- Base screen: food 513.8M, iron 838.3M, coin 25.2M, power
  149,209,253, diamonds 6,027.

## What was done

- Read the live phase, score, thresholds, timer and scoring table
  (rule R4: first executed unit of this phase - the phase started
  about 22:05 PT 2026-11-08 and this unit, planned for 22:03, only
  reached execution at 00:47 PT, so the judgment lands about 2h40m
  into the phase; the queue latency that delayed it is a retro
  item, not this unit's work).
- Completion sweep on the phase page: all three point chests locked
  at 0 points, none earned, none claimed; the cumulative counter
  chest stands at 0/2, locked, not bouncing; the ranking-row chest
  was not tapped (it opens only a contents preview while the phase
  is live, per the standing rule - the ranking reward is for the
  next run after the phase ends).
- The phase IS winnable in principle: 75,000 points needs about
  2,420 Lv.10 units queued (75,000 / 31), the same order of fill
  that put the account at 75,047 in the 2026-10-25 intake round.
  The fill itself was not executed in this unit (see below).

## What was not done - the training fill

- The barracks fill was not executed: the unit's 15 minutes went
  to entry and navigation (a mis-tap opened Wall of Honor, and the
  Events back arrow took three attempts - see Navigation notes).
- Barracks state was NOT verified live in this unit. Carried
  forward from the training unit of this same pass (ticker-0019,
  0039-queue-run, 00:25-00:39 PT today, not re-verified here):
  Lv.30 barracks busy (batch requeued 2026-11-07 about 17:08,
  ends about 10:22 today), Lv.27 busy (ends about 03:27 today),
  Lv.24 idle but blocked by the Drill Ground Full toast, fourth
  barracks unknown; the barracks tents were not located in that
  unit either, and its R2 instruction stands - the next unit
  must ground the tents from a fresh route, not re-tap the
  Aircraft Center structure.
- If the carried-forward state holds, no new batch can be queued
  until the Lv.27 batch ends about 03:27 today (after this phase
  ends about 02:00 PT) or the Drill Ground Full block clears -
  the successor unit must judge that live; a phase that cannot
  be filled inside the red lines is a miss to record, not a
  fill to force.

## Navigation notes (grounded points for the next unit)

- The orange medal icon on the base screen is Wall of Honor, NOT
  Events - do not tap it for event entry.
- Events icon: top right of the base screen, globe-like icon
  labelled Events with a red badge, grounded at normalized
  (672, 132) in fullscreen.
- The task rows and ">>" arrows on the Arms Race page are
  informational only - tapping the Train row and its ">>"
  produced no navigation.
- The Events back arrow: background clicks at normalized
  (334, 949) failed twice with no change (R2 pivot); the
  grounded centre of the blue arrow button is (355, 944) and
  a tap there exited to the base at once. Future units: ground
  the arrow fresh and tap its centre, never the (334, 949)
  edge point.
- No login or verification was demanded, and no
  different-device dialog appeared.

## Successor

- Priority 1 successor arms-race-2026-11-09-0855 enqueued by this
  unit, expires 2026-11-09T10:00:00Z (phase end), window "Unit
  Progression phase fill Lv.10 training queues to 75000": locate
  the barracks from a fresh route, queue Lv.10 units toward
  75,000 points just enough, claim every earned chest, and run
  the completion sweep. Tracker untouched, per the partial rule.

## Red lines

- No diamonds or money spent. No speedup item used. No building
  or research started. No stage swap. No other unit's work
  touched.

## Stats

- target: 75000
- achieved: 0
- points: 0
- resources_gained: none
- costs: about 12 minutes of unit time, no items spent
- verified: yes
- blocker_category: c
