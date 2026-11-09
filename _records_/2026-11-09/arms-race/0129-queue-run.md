---
title: Arms Race queue run 0129
created: 2026-11-09T09:29:00Z
modified: 2026-11-09T09:29:00Z
version: 1.0.0
description: Unit Progression phase read live, 0 points, barracks tents not located from a fresh route, fill not executed inside the unit cap
status: partial
grounded_in:
  - source: live game screen on the owner Mac mini, 2026-11-09 01:14-01:29 PT
---

# Arms Race queue run 0129 (ticker-0113)

Unit: arms-race-2026-11-09-0855. Status: partial.
Activity: arms-race. Phase: Unit Progression, Contest Segment Lv.29-30.

## Live reads

- Phase page (read about 01:16 PT): Unit Progression, points 0,
  timer 00:44:05, chest thresholds 15,000 / 30,000 / 75,000 (top
  chest 75,000), cumulative counter chest 0/2, rank #2110
  [AP3x]Bears Lair, 0 points. No scoring action was taken after
  this read, so 0 is this unit's verified closing score.
- Scoring paths as displayed: Train a Lv.10 unit pays +31; Use
  1-min Training Speed-up pays +10; Buy Packs containing Diamonds
  pays +30 per diamond.
- Base screen: food 513.8M, iron 838.3M, coin 25.2M, power
  149,209,253, diamonds 6,027.
- Drill Ground re-confirmed live: the red troop formation in the
  lower middle selects Drill Ground Lv.30 (label read on screen),
  with the paw (Building Details), train-hat and green upgrade
  buttons. The upgrade button was not tapped.

## What was done

- Read the live phase, score, thresholds, timer and scoring table.
- Completion sweep on the phase page: all three point chests locked
  at 0 points, none earned, none claimed; the cumulative counter
  chest stands at 0/2, locked, not bouncing; the ranking-row chest
  was not tapped (it opens only a contents preview while the phase
  is live, per the standing rule - the ranking reward is for the
  next run after the phase ends). Nothing earned, nothing to claim.
- Fresh-route attempt at the barracks tents (R2): panned the base
  view toward the lower middle and tapped the red troop formation
  there. It resolved to Drill Ground Lv.30 again, not a barracks
  tent. The four tents were not located in this unit either.

## What was not done - the training fill

- The barracks fill was not executed: no barracks tent was located
  inside the 15 minute cap, so no TRAIN UNITS panel was opened and
  no batch was queued. Score stays 0 against the 75,000 target.
- This is the third consecutive unit failing to ground the tents
  (0039 troop-training, 0058 arms-race, this unit) - a third
  strike under queue rule R2. The blocker and the failed routes
  (Aircraft Center structure, red troop formation = Drill Ground)
  must be written into the troop-training activity metadata, and
  the entry route must change before any further unit of this
  type runs - the next attempt must not re-tap either structure.
  The metadata write is recorded here as pending: this pass
  delivers records only (tier-1 commit), and the working tree
  sits on another job's branch, so the tier-2 metadata edit is
  left for the knowledge flow, not swept into this pass.
- Carried-forward barracks state (not re-verified live): Lv.30
  busy (batch ends about 10:22 today), Lv.27 busy (ends about
  03:27 today), Lv.24 idle but blocked by the Drill Ground Full
  toast, fourth barracks unknown. The phase ends about 02:00 PT,
  before either busy batch ends, so even a located idle barracks
  may still be blocked by Drill Ground Full - the successor must
  judge that live.
- No successor was manually enqueued: the tracker still shows
  arms-race due (partial leaves it untouched), so the next tick
  re-produces it; the phase ends about 02:00 PT and the unit
  arms-race-2026-11-09-1003 already sits in the inbox for the
  next phase window.

## Red lines

- No diamonds or money spent. No speedup item used. No building
  or research started. No stage swap. No other unit's work
  touched. No login or verification was demanded, and no
  different-device dialog appeared.

## Stats

- target: 75000
- achieved: 0
- points: 0
- resources_gained: none
- costs: about 15 minutes of unit time, no items spent
- verified: yes
- blocker_category: e
