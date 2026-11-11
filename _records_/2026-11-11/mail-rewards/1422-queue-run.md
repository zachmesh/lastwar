---
title: Mail rewards queue run 1422
created: 2026-11-11T22:35:00Z
modified: 2026-11-11T22:35:00Z
level: L0
version: 1.0.0
description: Mail unit mail-2026-11-11-1030, Event Claim All done, other categories unchecked, partial
status: unverified
---

# Mail rewards 14:22 to 14:35 - ticker-1408

Unit mail-2026-11-11-1030 (planned for the 10:30 cycle,
expires 14:30 - the unit finished about 5 minutes after
its expiry; the Event claims are unaffected, mail does not
reset at 14:30). Executor ticker-1408. Session cc-626 on
the owner Mac mini.

## Live reads

- Base screen at entry: Mail button on the right rail
  needed two taps - the first at (650,795) did nothing,
  the second at the envelope centre (656,775) with the
  click-offset compensation opened Mail.
- Mail categories: Battle Report, Alliance, Event (gift
  icon - claimable), System, Regular (red dot), In-app
  Purchases (red dot), Favorite. No Season row is shown
  any more; Event is the visible reward-bearing tab.
- Event list: three "Zombie Invasion - Intel Reward"
  mails (5h, 6h ago) and "[AP3x] Missile Apex's train
  has..." train arrival mails (6h, 8h, 10h ago).
- Claim All pressed in Event. The game answered
  CONGRATULATIONS! and the reward popup read: medal 280,
  EXP 2.4M, Battle Data 1.5K, 10-stamina x2, coin 969.0K,
  food 769.0K, iron 769.0K. One tap on a reward icon
  opened its detail (Battle Data - Owned 5.8M, "Use this
  item to enhance drone algorithm progress"); the detail
  was dismissed and the popup was left open at the unit's
  end.
- Delete All was never pressed; no mail was deleted.

## Outcome - partial

- Event category fully claimed (see rewards above).
- Alliance, Battle Report, System and Regular were NOT
  checked - the pass budget ran out inside this unit.
  The tracker is left untouched, so the next tick
  re-produces the mail regular and the work resumes as a
  fresh unit.
- In-app Purchases was not opened (receipts only, nothing
  to claim, per the activity metadata). Favorite was not
  checked either.

## Figures read live on screen

- Food 687.5M, iron 1.0G, coin 134.7M, power 149,218,973,
  diamonds 6,717 at entry (unchanged from the help unit).
- No login or verification was demanded, and no
  different-device dialog appeared.

## Result statistics

- target 1, achieved 0, categories_claimed 1, categories_total 5,
  points_gained 0, verified yes, blocker_category none,
  device_takeovers 0, resources_gained none,
  costs about 13 minutes play

## Note for the activity metadata (tier 2, not edited here)

- The mail hub now lists Event and Favorite and no Season
  row; Event carries the gift icon when claimable. The
  click-offset compensation (about +23 x, -10 y in
  normalized coordinates, measured in this pass) applies
  to the Mail envelope too.

No diamonds or money spent. No other task type was executed
in this unit.
