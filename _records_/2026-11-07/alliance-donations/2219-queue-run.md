---
title: Donations queue run 2219
created: 2026-11-08T06:19:00Z
modified: 2026-11-08T06:19:00Z
level: L0
version: 1.0.0
description: Ticker-2204 donations re-read unit, partial and unverified - 4 coin donations landed live (5->1), final tap hidden behind a 00:19:07 timer, count never read at 0
status: unverified
---

# 2219 queue run - Alliance donations

Executor: ticker-2204. Unit: donations-2026-11-08-0323 (re-read
after the 1924 unit's 00:19:01 cooldown; not-before 19:40
local). Session windows about 22:11 to 22:19
America/Los_Angeles (sessions cc-56 and cc-57; cc-56 dropped
during a 95-second timer wait and was restarted with no game
state lost).

## Performed

- Entry route (rule R2): the Alliance shield was re-grounded
  fresh with the visual-grounding tool on the current
  screenshot - centre (936, 700) in the 763x1050 windowed
  layout. The tap opened the Alliance menu on the first try
  with no camera pan to the Drill Ground - the 11-02 entry
  blocker did not recur. Alliance: [AP3x] The Apex, Leader
  Abŷss Apex, power 13,360,041,845, members 96/100, English.
  Red dots on Help and Alliance Gifts tiles, both mapping to
  their own regulars, already queued.
- Alliance Techs, Development tab: Auto Rally Max Level,
  Quick Construction 8/10 carrying the recommended marker,
  Great Helper Max Level, one node below at 2/10 (cut off).
  Tech Donation Today read 1150 at entry (above the 1000
  reward threshold), matching the Strength Ranking Donation
  Daily 1150 read by the 21:07 scout unit.
- Donation panel, Quick Construction (8/10, +20% building
  speed, Tech EXP 1.1M/6.0M, reward EXP 50 + badge 50 per
  donation): Donation Count read live 5/30 at entry.
- Coin donations made in this unit, all on the green coin
  button (900 coin each), diamond button never touched,
  single taps with a live count read after each:
  5/30 -> 4/30, 4/30 -> 3/30, 3/30 -> 2/30, 2/30 -> 1/30.
  Four coin donations landed on live reads. Coin spent
  3,600. Coin HUD 6.9M at entry, 6.976M after the fourth
  tap (consistent with 3,600 spent from about 6.980M).
  Badge counter in the top bar rose 298.9K to 299.5K across
  the unit (verbatim reads; per-donation rate not inferred).
- Third tap note: a "Hold down for easier Continuous
  donations" tooltip appeared over the button; the tap still
  landed (count moved 3/30 -> 2/30 on the next read).
- After the 1/30 read, one more single tap: the coin button
  greyed with a 00:01:27 timer and the count label hid. The
  full 95-second wait was done inside the unit; the count
  then read 1/30 live with the button green again - that tap
  was eaten by the grey-out, the same failure mode as the
  1924 unit's third batch tap.
- One more single tap on the green button at 1/30: the
  button greyed again, this time with a 00:19:07 timer, and
  the count label is hidden behind it. The 19-minute timer
  cannot be waited out inside this unit's 15-minute cap.

## Not verified - why this unit closes partial

- The Donation Count was never read live at 0/30 in this
  unit, so the day cannot be closed as done (rule R1 /
  hard closing rule in the activity profile). The last tap's
  effect is unconfirmed: the count is either 0/30 (tap
  landed, timer is the exhaustion timer) or still 1/30
  (tap eaten by the grey-out, as the previous tap was).
- Count-rise anomaly, new and unexplained: the 1924 unit
  closed at 19:24 with a last live read of 1/30 and an
  unconfirmed final tap; this unit opened at 22:11 to a
  live read of 5/30. No donations unit ran between the two
  (no record in _records_/2026-11-07/alliance-donations/
  between 1924 and this unit) and no owner donation is
  recorded. A remaining count rising 1 -> 5 with no
  recorded donations does not fit the model; the footer
  also moved 750 -> 1150 in the same interval (plus 400
  points, about 8 donations at 50 points each, against a
  count that should have fallen). No inference about the
  count is drawn from the footer or from arithmetic. Filed
  as a GitHub Issue (knowledge class) from this unit.
- Tracker untouched (unverified close). A named re-read
  unit is enqueued by this pass for after the cooldown
  (not-before 22:40 local): it opens the panel, reads the
  count live, donates the last one if it reads 1/30, and
  closes the day only on a live 0/30 read.

## Closing reads

- Donation Count last live read 1/30 (before the final
  tap), coin donations landed 4, coin spent 3,600,
  Tech Donation Today 1150 at entry (footer not re-read
  at close), coin button greyed with 00:19:07 timer at
  close, badge counter 299.5K at close.
- Game left on the Quick Construction donation panel with
  the coin button greyed on the timer. No reward button
  was tapped anywhere in this unit.

## Outcome

Partial, unverified. Four of the five remaining coin
donations landed on live reads; the fifth is unconfirmed
behind the 00:19:07 timer. No diamonds, money, speedups
or other spending. No alliance diplomacy, no assembly,
no teleport.

## Result stats

- target 5, achieved 4, resources_gained none,
  costs 9m_wall_3600_coin, verified no,
  blocker_category d, donations_landed 4,
  donation_count_before 5, donation_count_last_read 1,
  coin_spent 3600, donation_points_today 1150,
  device_takeovers 0

## Post-record note

- The count-rise anomaly in this record is filed as GitHub
  Issue #423 (knowledge class).

## Correction note (appended before delivery, 22:24)

- The claim in this record that "no donations unit ran
  between the two" is WRONG. The ticker-2006 pass executed
  this same unit (donations-2026-11-08-0323) at 20:11-20:18
  local - record _records_/2026-11-07/alliance-donations/
  2018-queue-run.md, already on the records branch. It read
  the count live at 2/30, landed 1 donation (2->1), proved
  its second tap eaten (waited 155 seconds, count still
  1/30), and left its third tap unconfirmed behind a
  00:18:46 timer. This pass re-executed the unit because the
  local queue still carried it in inbox after the 2006
  partial (tracker untouched for partials, so the sync
  re-produced the same unit id) - a duplicate production,
  not a fresh unit.
- Corrected count trajectory: 1/30 (19:24, 1924) -> 2/30
  (20:11, 2018) -> 1/30 (20:18, 2018) -> 5/30 (22:11, this
  unit). The count RISES between units while only falling
  inside a unit. The footer rose 750 -> 1150 between 20:18
  and about 21:10 (scout read). Working hypothesis, still
  unverified: the coin-donation allowance regenerates over
  time (about +1 per 30 minutes, or per 19-minute cooldown
  cycle) - it needs a dedicated read sequence across a
  reset boundary to pin down. No inference about the count
  is drawn from the footer or from arithmetic (rule R1).
- The 2018 record already established the HUD badge figure
  is NOT donation-linked (it moved after a provably eaten
  tap); this unit's badge reads (298.9K -> 299.5K) are
  recorded as observed only, consistent with that.
- Branch handling: the records branch keeps the 2006 unit
  file for donations-2026-11-08-0323 per the ticker-2104
  precedent (branch file kept when already carried); this
  execution is evidenced by this record file and the day
  INDEX entry. Issue #423's premise is corrected in a
  comment on the issue.
