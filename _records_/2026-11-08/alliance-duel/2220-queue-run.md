---
title: Alliance duel score queue run 2220
created: 2026-11-09T06:20:00Z
modified: 2026-11-09T06:20:00Z
level: L0
version: 1.0.0
description: Ticker-2201 duel-score unit, personal total 0 on the new duel day
status: unverified
---

# 2220 queue run - Alliance duel score

Executor: ticker-2201. Unit: duel-score-2026-11-08-1830.
Session window about 22:12 to 22:20 America/Los_Angeles.

## Performed

- Opened the VS medallion, Duel Progress, Today's Duel.
  Theme: Radar Training, 19:47 remaining at entry.
  Alliance score: [AP3x] The Apex 261,068,886 (41%) vs
  [TFox] Fox 380,634,584 (59%) - the alliance trails.
  Top scorers: [TFox] Mihye 41,111,404; [AP3x] Texas Boy
  32,838,375; [TFox] yang godain ditabok 32,593,063.
- Scrolled the Today's Duel ranking down through ranks 6-14
  (scores 16.6M down to 9.0M) without finding Bears Lair.
- Opened Ranking, Daily Rank: the Mon. tab is selected and
  the pinned own row reads Bears Lair [AP3x] The Apex,
  Unlisted, 0 points.
- Opened Today's Theme: the personal points counter at the
  top reads 0. Two independent live reads agree: today's
  personal duel total is 0.
- Theme scoring actions read live: Use 1 Stamina +375,
  Complete 1 Radar Task +30,000, Use 660 Hero EXP +2.5,
  Use 1 Drone Battle Data point +7.5, Use 1 Drone Part
  +6,250, Buy Packs +30 per Diamond, Gather 100 Food +50.
  Chest thresholds: 40,000 / 150,000 / 540,000 points.
- Returned to the base screen and checked for the Star
  Ceremony trophy icon beside the Alliance button: none
  present, so no ceremony is waiting.

## Reading of the 0

- This unit's slot is 18:30, but it executed at 22:12,
  after the 19:00 daily reset, so it reads the NEW duel
  day, not the closing figure of the day that ended at
  19:00. The new day is 3 hours old, the theme is Radar
  Training, and no radar task, stamina use or drone part
  has been spent since the reset, so 0 is the true
  opening figure for the new day. The 22:30 unit reads
  later tonight. Gap against the 3,600,000 owner target:
  3,600,000.
- No grinding was done: scoring by spending resources or
  speedups is the owner's decision, not part of a score
  read.

## Closing reads

- Personal duel total 0 of 3,600,000 target. Alliance
  261,068,886 vs 380,634,584. No ceremony waiting.

## Outcome

Done. Personal daily total read live twice, both 0.

## Correction (same pass, before commit)

- The session window above is wrong: the unit ran 22:10 to
  22:14 America/Los_Angeles (unit duration_seconds 235, about
  4 minutes), not 22:12 to 22:20. The costs line should read
  4m_wall_no_stamina, and blocker_category is none. The
  closing figures (personal total 0, read twice) are
  unaffected.

## Result stats

- target 3600000, achieved 0, resources_gained none,
  costs 4m_wall_no_stamina, verified yes, blocker_category none,
  points 0, gap 3600000, alliance_score 261068886,
  opponent_score 380634584, theme Radar Training,
  ceremony_waiting false, device_takeovers 0
