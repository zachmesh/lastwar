---
title: Queue Run 1508 Arms Race
created: 2026-11-02T23:08:00Z
modified: 2026-11-02T23:08:00Z
level: L0
version: 1.0.0
description: Arms-race unit partial, first unit of the Hero Advancement phase, phase and score read live, level-up blocked by a 20M hero EXP shortfall
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-11-02
---

# 1508 queue run - arms race (partial, first unit of phase)

Unit arms-race-2026-11-02-1403, executor ticker-1452,
session about 14:55 to 15:08 America/Los_Angeles.
Status partial under queue rule R4: this is the first
unit inside the Hero Advancement phase, so it reads the
phase, the score and every scoring path and sets the
just-enough plan; the scoring itself falls to the next
unit because the chosen level-up is short of hero EXP.
Tracker untouched, so the next tick re-produces this
regular.

## Live phase read

- Phase: Hero Advancement, Contest Segment Lv.29-30,
  03:00:17 left at the first read (about 14:57). Phase
  window runs to about 17:57 local.
- Live score: 0, read from the star bar at the top left
  of the phase page. The ranking row's 40,500 for
  [AP3x]Bears Lair is the lagging previous-phase row
  (the same figure the 2026-11-02 1015 record flagged
  as lag), not this phase's score.
- Point chest thresholds: 2,000 / 4,000 / 12,000
  (ruby tags 2,360 / 4,800 / 11,800). No chest is earned
  yet; no red dot or bouncing chest on the page.
- Cumulative counter chest at the top left: 6 of 8,
  purple, not full, not claimable.
- Ranking row chest: not tapped this unit; preview-only
  is expected while the phase is live, and the sweep
  falls to the scoring unit.

## Scoring paths, read live

- 1 Hero Recruitment: +400 points.
- Use at least 2,000 Hero EXP at a time: +1 point per
  2,000 EXP (verified rate, 2026-10-26 record: a
  75.0M EXP one-level spend read back as 37,500
  points).
- Buy Packs containing Diamonds: +30 per diamond -
  red line, never used.
- Tier-3 gap: 12,000 points, equal to 24,000,000 Hero
  EXP used.

## Just-enough plan

- Level UR Titan Adam Lv.124 to Lv.125 exactly once
  and no further. Adam's level cost reads 83.0M EXP,
  so one level spends 83.0M EXP and scores about
  41,500 points, clearing the 12,000 tier-3 threshold
  by design of the level cost; the just-enough rule is
  satisfied by taking exactly one level and no more,
  as in the 2026-10-26 Hero Advancement close.

## What blocked the scoring

- Adam's EXP bar reads 63.0M / 83.0M with the current
  figure in red: a 20.0M EXP shortfall against the
  level cost. The Upgrade button was tapped twice on
  the hero detail screen (single tap, then a
  double-click on the freshly grounded centre at norm
  502,813) with no change on either attempt; per queue
  rule R2 that tap method is retired inside this unit
  and the shortfall, not the tap, is the blocker.
- Next unit's first action: open experience boxes
  from the inventory to top up at least 20.0M Hero
  EXP (owner instruction, 2026-10-26, recorded in the
  activity metadata), then level Adam once, re-read
  the phase score live, claim all three earned point
  chests, and run the completion sweep (cumulative
  counter chest, ranking row chest, Events screen
  re-scan) before closing.

## Navigation notes

- The Events icon at norm 925,130 opened Events
  directly on the Arms Race page, as in the 2026-11-02
  0608 record.
- The Events back arrow at norm 160,947 worked on a
  double-click, as in the 1015 record.
- The game was found on the Drill Ground panel the
  1412 radar unit left open; its X at norm 869,139
  closed it to the base on the first tap.
- No different-device dialog was seen, no login or
  verification was demanded, and no password or Touch
  ID step was used.

## Outcome

- Status: partial, first-phase assessment plus a
  blocked scoring attempt.
- Tracker: untouched.
- Red lines: nothing spent, no paid button tapped, no
  stage swap, no research or building started.
