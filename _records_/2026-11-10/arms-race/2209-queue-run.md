---
title: Arms Race queue run 2209
created: 2026-11-10T22:09:00-08:00
modified: 2026-11-10T22:09:00-08:00
version: 1.0.0
description: Arms Race unit arms-race-2026-11-10-1803, Hero Advancement phase, one hero level to 41,500, all three point chests and the cumulative chest claimed
status: done
grounded_in:
  - source: live game screen on the owner Mac mini, 2026-11-10 21:57-22:09 PST
---

# Arms Race queue run 2209

- Unit: arms-race-2026-11-10-1803, executor ticker-2154, session cc-515.
- Window: 21:57-22:09 PST. Duel day 2. The unit was produced for the
  18:03 slot (Base Building phase) and executed across the 22:00 phase
  roll, so the phase-start read and the tier-3 work below are in the
  live Hero Advancement phase.

## Login recovery

- The game window was frontmost but login had failed with an [E118]
  network connection error dialog ("Please check your connection and
  try logging in again"), Reconnect and Contact Us buttons.
- First Reconnect tap (element tap) produced no change; second tap
  (coordinate tap on the same button, R2 variant change) cleared the
  dialog and the game retried login, which then succeeded to the base
  screen. No password, no Touch ID, no fresh login demanded.

## Live read

- Phase: Hero Advancement, Contest Segment Lv.29-30, timer 03:58:14
  at first read (03:51:26 at close).
- Score: 0 at entry, segment rank unranked in the live phase;
  thresholds 2,000 / 4,000 / 12,000 (ruby tags 2,360 / 4,800 /
  11,800). Gap to tier 3: 12,000.
- Cumulative counter chest top-left read 1/2 at entry.
- Ranking row at entry showed #2110 [AP3x]Bears Lair rank 9 with
  9,000 - recorded as observed; it is not the live phase score
  (0), and matches the documented ranking-row lag pattern.
- Scoring paths as displayed: 1 Hero Recruitment +400; Use at least
  2,000 Hero EXP at a time +1; Buy Packs containing Diamonds +30 per
  diamond (red line, not used).

## Scoring action - one hero level, just enough

- Morrison "The Reaper" (UR), Lv.124 -> Lv.125, exactly one level
  with Hero EXP, per the standing Hero Advancement authorization.
  EXP bar 1.5G/83.0M before, 1.4G/85.0M after (about 83M EXP
  spent for the level). Hero power 1,733,222 -> 1,741,441 (+8,219);
  Attack 40.6K -> 40.9K; March Size 399. No experience boxes
  opened; the EXP on hand covered the level.
- Re-read after the level-up: score 41,500 (about 83M EXP at +1 per
  2,000 EXP), clearing the 12,000 top chest. Ranking row now rank 4
  with 50,500 (9,000 + 41,500 - the ranking row accumulates across
  the phases of the day; recorded as observed). No further scoring
  work done, per the just-enough rule.

## Claimed

- Point chest 1 (2,000) tapped once: claimed all three earned point
  chests at once (as in the 2026-10-26 Hero Advancement run).
  CONGRATULATIONS contents combined: Skill Medal 1.6K, Arms Race
  Badge 6, Iron Chest (SR) 32, Food Chest (SR) 32, Coin Chest
  (SR) 32, 5m Speed-up 68.
- Point chest 2 (4,000) re-tap opened its contents preview only
  (Skill Medal 400, Arms Race Badge 2, Coin Chest (SR) 8, Food
  Chest (SR) 8, Iron Chest (SR) 8, 5m Speed-up 20), confirming it
  was already claimed by the first tap.
- Cumulative counter chest tapped after the point-chest claim and
  claimed: gold ticket x1, pink puzzle-piece item x2, red gem x1
  (tagged 50). Counter now reads 7/8 (purple, next tier), not yet
  claimable. The counter moved 1/2 at entry to claimable after the
  point chests were claimed, then to 7/8 after its own claim -
  progress carries past a claimed tier into the next, as in the
  2026-10-26 run.
- Ranking row chest: preview only while the phase is live - Iron
  Chest (SR) 6, Food Chest (SR) 6, Coin Chest (SR) 6, no Claim
  button. The ended Base Building phase's ranking reward was not
  found claimable anywhere on this page; the ranking chest previews
  the current phase's reward. Where the ended phase's ranking
  reward is paid remains the open question already recorded in the
  activity metadata.

## Completion sweep

- Events screen and Arms Race page re-scanned: no bouncing chest or
  reward red dot remains on the Arms Race card or page. The Age of
  Oil tab still carries a red (1) badge - a different event, left
  for its own unit.
- Base power 149,210,754 at entry -> 149,218,973 at close (+8,219,
  the hero level-up).
- Train boarding banner observed closing during this unit (00:02:56
  at 22:01, 00:00:08 at about 22:05) - noted for the train unit;
  boarding is not this unit's type.
- Nothing spent: no diamonds, no money, no speedup items, no
  stamina items. One hero level with EXP only.

## Result

- Status: done. Target 12,000, achieved 41,500, verified yes
  (same-unit live reads). Blocker category: none.
- Note: the 1712 run's priority 1 successor
  arms-race-2026-11-11-0112 (re-check for a finished Oil Well
  upgrade inside the Base Building phase) is now moot - that phase
  ended at 22:00 with the Oil Well still [0/1]; the unit expires
  at 02:00Z and the reaper will expire it.
