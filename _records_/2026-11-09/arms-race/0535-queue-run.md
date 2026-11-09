---
title: Arms Race queue run 0535
created: 2026-11-09T13:39:00Z
modified: 2026-11-09T13:39:00Z
version: 1.0.0
description: Hero Advancement phase re-read live before phase end, 82,500 points stand, all earned chests already claimed, completion sweep clean
status: done
grounded_in:
  - source: live game screen on the owner Mac mini, 2026-11-09 05:35-05:39 PT
---

# Arms Race queue run 0535 (ticker-0534)

Unit: arms-race-2026-11-09-1248. Status: done.
Activity: arms-race. Phase: Hero Advancement, Contest Segment Lv.29-30.

## Live reads

- Phase page (read about 05:38 PT): Hero Advancement, points
  82,500 at entry, timer 00:21:49, chest thresholds 2,000 / 4,000 /
  12,000 (top chest 12,000), cumulative counter chest 6/8, rank
  #2110 [AP3x]Bears Lair, segment rank 8, 82,500 points.
- The 82,500 figure is unchanged from the 0306 unit's closing
  read (McGregor Lv.145 to 146, 165.0M EXP, 82,500 points) - the
  phase target was already met in this phase by that unit and
  nothing has scored since.
- Scoring paths as displayed: 1 Hero Recruitment pays +400; Use
  at least 2,000 Hero EXP at a time pays +1; Buy Packs containing
  Diamonds (1 Diamond) pays +30 (red line, never used).
- Base screen (image read about 05:38 PT): food 540.1M, iron
  864.9M, coin 42.9M, gold 13.22K, diamonds 6,077, power
  149,217,331. VS timer 12:22:38 (duel day 1). A later compact
  observation OCR-read the power as 149,117,331; that single-digit
  OCR variant is not relied on.
- Events hub tab bar: Arms Race, Winter Battlefield, Desert
  Battlefield, Wanted Boss (red dot), Survey Center - no Zombie
  Invasion tab, confirming the event ended 2026-10-30 (chain
  closed by unit 066). No fresh zombie chain seeded.

## What was done

- Pre-phase-end verification, not a new scoring push: the phase
  was already met at 03:06, so no hero EXP was spent and no
  further level-up was made - the just-enough rule is satisfied
  by the single level the 0306 unit already took.
- Completion sweep: all three point chests show claimed (open
  chests, full green progress bar with gold stars, no red dot,
  no bounce). The cumulative counter chest reads 6/8 with a
  partial bar, not full, not claimable, no bounce. The ranking-row
  chest was not tapped - it is preview-only while the phase is
  live (verified by the 0306 unit in this same phase); the
  ranking reward falls to the first run after the phase ends
  about 06:03 PT, per the standing rule.
- Events hub re-scan: the Arms Race tab carries no red dot and
  no bouncing chest. The base-screen Events icon badge 1 matches
  the Wanted Boss tab red dot seen in the hub - that is the
  events regular's work, not this unit's, and was left untouched.
- No reward was claimed in this unit because nothing new was
  earned since the 0306 claim.

## Follow-up

- The first arms-race unit after the 06:03 PT phase roll should
  check the ranking-row chest for the finished Hero Advancement
  phase and claim it if it has become claimable.

## Red lines

- No diamonds or money spent. No speedup item used. No building
  or research started. No stage swap. No hero EXP spent in this
  unit. No other unit's work touched (Hidden Treasure page left
  as found on entry, no dig; Wanted Boss red dot left untouched).
  No login or verification was demanded, no different-device
  dialog appeared, and no password or Touch ID step was used.
- Session cc-225 dropped no frames: one open_app returned
  outcome_unknown and was not replayed; the window was verified
  open by observation instead. One click was refused with
  privacy_unverified and succeeded after a fresh observation.

## Stats

- target: 12000
- achieved: 82500
- points: 0 (no scoring action in this unit; the 82,500 is the
  phase total read live, carried in achieved, not gained here -
  corrected from an initial points 82500 after the queue tool
  warned it duplicated achieved)
- resources_gained: none claimed in this unit (phase rewards claimed by the 0306 unit)
- costs: none (no EXP spent, no items used), 216 seconds of unit time
- verified: yes
- blocker_category: none
