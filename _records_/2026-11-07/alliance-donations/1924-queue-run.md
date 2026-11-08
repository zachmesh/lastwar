---
title: Donations queue run 1924
created: 2026-11-08T03:24:00Z
modified: 2026-11-08T03:24:00Z
level: L0
version: 1.0.0
description: Ticker-1904 donations unit, partial and unverified - 6 coin donations landed live, final tap unconfirmed behind a 00:19:01 timer, count never read at 0
status: unverified
---

# 1924 queue run - Alliance donations

Executor: ticker-1904. Unit: donations-2026-11-07-1803 (no
window text; planned 18:03 local 2026-11-07, expires 02:03
local 2026-11-08). Session window about 19:12 to 19:24
America/Los_Angeles.

## Performed

- Entry route fixed (rule R2): the Alliance shield was
  re-grounded fresh from a magnified crop of the right icon
  column - centre norm 928,717 in the current 763x1050
  windowed layout, not the profile's 903,787 (measured
  2026-11-02, likely fullscreen layout). The tap opened the
  Alliance menu on the first try with no camera pan to the
  Drill Ground - the 11-02 entry blocker did not recur.
  Alliance: [AP3x] The Apex, Leader Abŷss Apex, power
  13,326,895,949, members 96/100, rating 5.0.
- Alliance Techs, Development tab: Auto Rally Max Level,
  Quick Construction 8/10 carrying the recommended marker,
  Great Helper Max Level, one node below at 2/10 (cut off).
  Tech Donation Today read 2700 at entry (above the 1000
  reward threshold).
- Donation panel, Quick Construction (8/10, +20% building
  speed, Tech EXP 1.1M/6.0M, reward EXP 50 + badge 50 per
  donation): Donation Count read live 7/30 at entry.
  Remaining-count semantics confirmed by the first tap:
  7/30 fell to 6/30 after one 900-coin donation.
- Coin donations made in this unit, all on the green coin
  button (900 coin each), diamond button never touched:
  7/30 -> 6/30 (1 tap), 6/30 -> 3/30 (3 taps),
  3/30 -> 1/30 (2 of 3 taps landed - the third tap hit the
  button while it was greyed). Six coin donations landed
  on live count reads. Coin spent 5,400. Coin balance on
  the HUD stayed 5.7M (rounded display).
- Burst cooldown observed: after the second tap of the
  third batch the coin button greyed with a 00:00:50 timer
  and the count label hid behind it. Waited the full 60
  seconds inside the unit; the count then read 1/30 live
  with the button green again. Lesson: batched taps can be
  eaten by the grey-out - verify the count after every
  batch, never assume a batch landed whole.
- Final tap on 1/30: the button greyed again, this time
  with a 00:19:01 timer. The count label is hidden behind
  the timer and the timer (about 19 minutes) cannot be
  waited out inside this unit's 15-minute cap.

## Not verified - why this unit closes partial

- The Donation Count was never read live at 0/30 in this
  unit, so the day cannot be closed as done (rule R1 /
  hard closing rule in the activity profile). The final
  tap's effect is unconfirmed: the count is either 0/30
  (tap landed, timer is the exhaustion timer seen on
  2026-10-26) or still 1/30 (tap eaten by the grey-out,
  as happened to one tap in the previous batch).
- Cross-check attempted from another surface, per the
  profile: the ALLIANCE TECHS footer and the Strength
  Ranking Donation tab (Daily) both read the player's
  Daily Donation Points as 750, rank 29 - but that number
  DROPPED from 2700 at entry to 750 after the donations,
  while six confirmed donations should have added about
  300 points. The drop is unexplained and the two reads
  do not reconcile, so the footer cannot confirm the
  count either way. The drop is recorded here as an open
  question for the activity profile - possibly a
  mid-session reset of the points counter, a different
  reset time for donation points than the 19:00 game
  reset, or a display the profile misreads. No inference
  about the count is drawn from it.
- Tracker untouched (unverified close). A named re-read
  unit is enqueued by this pass for after the cooldown
  (not-before 19:40 local): it opens the panel, reads the
  count live, donates the last one if it reads 1/30, and
  closes the day only on a live 0/30 read.

## Closing reads

- Donation Count last live read 1/30 (before the final
  tap), coin donations landed 6, coin spent 5,400,
  Tech Donation Today 750 at close (2700 at entry -
  unexplained drop, see above), Daily Donation Points
  750, rank 29, coin button greyed with 00:19:01 timer
  at close.
- Game left on the Strength Ranking screen (Donation tab,
  Daily). The computer session had dropped by the close,
  so no return-to-base tap was made; the next unit
  re-grounds fresh as always. No reward button was
  tapped anywhere in this unit.

## Outcome

Partial, unverified. Six of the seven remaining coin
donations landed on live reads; the seventh is
unconfirmed behind the cooldown timer. No diamonds, money,
speedups or other spending. No alliance diplomacy, no
assembly, no teleport.

## Result stats

- target 7, achieved 6, resources_gained none,
  costs 12m_wall_5400_coin, verified no,
  blocker_category d, donations_landed 6,
  donation_count_before 7, donation_count_last_read 1,
  coin_spent 5400, donation_points_today 750,
  donation_rank_daily 29, device_takeovers 0
