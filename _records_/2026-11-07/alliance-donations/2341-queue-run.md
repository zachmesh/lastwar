---
title: Donations queue run 2341
created: 2026-11-08T07:41:00Z
modified: 2026-11-08T07:47:00Z
level: L0
version: 1.0.0
description: Ticker-2334 donations re-read unit, partial and unverified - 3 coin donations landed live (4->1), final tap hidden behind a 00:15:41 timer, count never read at 0
status: unverified
---

# 2341 queue run - Alliance donations

Executor: ticker-2334. Unit: donations-2026-11-08-0419 (re-read
after the 2018 unit's 00:18:46 cooldown; not-before 20:38
local). Session about 23:37 to 23:41 America/Los_Angeles
(session cc-62; no drop, no takeover dialog).

Note on the unit's lineage: this 0419 unit was enqueued by the
2018 unit (ticker-2006, record 2018-queue-run.md). The 2219
unit (ticker-2204) re-executed the parent 0323 unit at 22:11
and enqueued its own successor, donations-2026-11-08-0618
(not-before 22:40 local), which still sits in the inbox. This
unit is the 2018 unit's own successor, executed now because
the tool picked it first; the work below is the same re-read
the 0618 unit would have done.

## Performed

- Entry route (rule R2): the Alliance shield was re-grounded
  fresh with the visual-grounding tool on the current
  screenshot - centre (936, 710) in the 763x1050 windowed
  layout. The tap opened the Alliance menu on the first try
  with no camera pan to the Drill Ground - the 11-02 entry
  blocker did not recur. Alliance: [AP3x] The Apex, Leader
  Abyss Apex, power 13,350,333,388, members 96/100, English.
  Red dots on Help, Alliance Gifts and Alliance Techs, all
  mapping to their own regulars, already queued.
- Alliance Techs, Development tab: Auto Rally Max Level,
  Quick Construction 8/10 carrying the recommended marker,
  Great Helper Max Level, one node below at 2/10 (cut off).
  Tech Donation Today read 1600 at entry (above the 1000
  reward threshold).
- Donation panel, Quick Construction (8/10, +20% building
  speed, Tech EXP 1.2M/6.0M, reward EXP 50 + badge 50 per
  donation): Donation Count read live 4/30 at entry.
- Coin donations made in this unit, all on the green coin
  button (900 coin each), diamond button never touched,
  single taps with a live count read after each:
  4/30 -> 3/30, 3/30 -> 2/30, 2/30 -> 1/30.
  Three coin donations landed on live reads. Coin spent
  2,700 confirmed. Coin HUD 6.9M at entry and at close
  (0.1M rounding, cannot resolve 2,700). Badge counter in
  the top bar rose 299.6K to 300.0K across the unit
  (verbatim reads; per the 2018 record the badge figure is
  NOT donation-linked, recorded as observed only).
- Third tap note: a "Hold down for easier continuous
  donations" tooltip appeared over the button; the tap still
  landed (count moved 2/30 -> 1/30 on the next read).
- After the 1/30 read, one more single tap: the coin button
  greyed with a 00:15:41 timer and the count label hid. The
  15-minute timer cannot be waited out inside this unit's
  15-minute cap.

## Not verified - why this unit closes partial

- The Donation Count was never read live at 0/30 in this
  unit, so the day cannot be closed as done (rule R1 /
  hard closing rule in the activity profile). The last tap's
  effect is unconfirmed: the count is either 0/30 (tap
  landed, timer is the exhaustion timer) or still 1/30
  (tap eaten by the grey-out, as the 2219 unit proved can
  happen).
- Count-rise data point, third confirmation of the
  regeneration picture: the 2219 unit closed at 22:19 with
  a last live read of 1/30 and an unconfirmed final tap;
  this unit opened at 23:37 to a live read of 4/30. The
  count rose 1 -> 4 over about 1 hour 18 minutes with no
  recorded donations in between, about 1 per 26 minutes
  as a two-endpoint estimate only, NOT a measured rate.
  The footer also moved 1150 -> 1600 in the same interval
  (plus 450 points, against 3 donations at 50 points each
  in this unit - it does not divide cleanly, so the footer
  is not a per-donation counter and is not used as a
  closing figure, as the 0545 record already established).
  No inference about the count is drawn from the footer or
  from arithmetic. Filed as GitHub Issue #423 (knowledge
  class) from the 2219 unit; this is a further data point
  for it, not a new issue.
- Timer-length data point for Issue #160: this unit's
  cooldown read 00:15:41, against 00:19:01 (1924),
  00:18:46 (2018) and 00:19:07 (2219). The cooldown is
  variable, roughly 15 to 19 minutes, not a fixed 19.
- Tracker untouched (unverified close). A named re-read
  unit is enqueued by this pass for after the cooldown
  (not-before 23:59 local): it opens the panel, reads the
  count live, donates the last one if it reads 1/30, and
  closes the day only on a live 0/30 read. The 0618 unit
  from the 2219 unit remains in the inbox alongside it;
  whichever runs first does the re-read, and the other
  then reads the post-timer state.

## Closing reads

- Donation Count last live read 1/30 (before the final
  tap), coin donations landed 3 confirmed (+1 unconfirmed),
  coin spent 2,700 confirmed (+900 unconfirmed),
  Tech Donation Today 1600 at entry (footer not re-read
  at close), coin button greyed with 00:15:41 timer at
  close, badge counter 300.0K at close.
- Game left on the Quick Construction donation panel with
  the coin button greyed on the timer. No reward button
  was tapped anywhere in this unit.

## Outcome

Partial, unverified. Three of the four remaining coin
donations landed on live reads; the fourth is unconfirmed
behind the 00:15:41 timer. No diamonds, money, speedups
or other spending. No alliance diplomacy, no assembly,
no teleport.

## Result stats

- target 4, achieved 3, resources_gained none,
  costs 4m_wall_2700_coin, verified no,
  blocker_category d, donations_landed 3,
  donation_count_before 4, donation_count_last_read 1,
  coin_spent 2700, donation_points_today 1600,
  device_takeovers 0

## Recovery note - worktree loss mid-pass (appended 23:47)

- The pass first ran in a fresh worktree at
  /tmp/ticker-2334-1107 (branch ticker-2334-records-1107,
  from github/records/2026-11-07 at 17a837f631). Between
  about 23:42 and 23:43 local that directory vanished -
  /tmp/ticker-2204-1107 and /tmp/ticker-2304-1107 vanished
  in the same window, while ~/workspace/lastwar-worktrees/
  and the main checkout were untouched and /tmp showed no
  space pressure (7% used). The deleter is unidentified;
  /tmp is not safe for ticker worktrees and no later pass
  should use it. This record, the day INDEX entry and the
  unit completion were all lost with the directory and were
  re-applied from the executor's session notes into a
  replacement worktree at
  ~/workspace/lastwar-worktrees/ticker-2334-1107 on the
  same branch.
- The re-claim stamps a fresh claimed_at (about 23:47), so
  the unit's duration_seconds in the queue tool reflects
  the re-claim-to-complete window (about 1 minute), not
  the true execution window 23:37-23:41 stated above. The
  game state was not re-read after the loss: the completion
  rests on the live reads made before it (count 4->1,
  timer 00:15:41), which stand as recorded.
- The token file was never in the lost directory (it lives
  in the main checkout's _queue_/claimed/) and survived;
  the computer session cc-62 stayed open through the loss.
