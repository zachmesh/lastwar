---
title: Alliance donations queue run 2319
created: 2026-11-11T07:19:00Z
modified: 2026-11-11T07:19:00Z
version: 1.0.0
description: Donations unit donations-2026-11-11-0535, re-read of the 2133 unverified close; Donation Count read live 2/30, 2 coin donations made, 2nd tap landing timer-hidden, partial
status: unverified
grounded_in:
  - source: live game screen on the owner Mac mini, 2026-11-10 23:14-23:19 PT
---

# Alliance donations queue run 2319 (ticker-2312)

Unit: donations-2026-11-11-0535. Status: partial.
Activity: alliance-donations. Computer session cc-520.

## Entry

- Base screen at entry: food 655.4M, iron 978.5M, coin
  109.9M, badge item 405.9K, Total Power 149,218,973.
  A server banner read "The server will shut down for
  maintenance in 7-min" at about 23:14 PT - this unit
  ran against a closing maintenance window.
- Alliance entry: shield icon tapped at the fresh
  measured centre (927,707) from the current screenshot
  - opened the menu first try. The (903,787) centre in
  the activity metadata is stale; (930,717) confirmed
  by 2015 and 2133 and (927,707) here are the same
  point within measurement.
- Alliance menu: [AP3x] The Apex, Leader Abŷss Apex,
  Members 95/100.
- Alliance Techs tile tapped at (686,680). Development
  tab at entry: Auto Rally Max Level, Quick Construction
  8/10 (red recommended marker), Great Helper Max Level,
  bottom node 2/10. Tech Donation Today footer 1400 at
  entry (1150 at the 2133 close, so plus 250 accrued
  between 21:33 and 23:14 with no unit donating in
  between - footer points are not stable per donation
  and are never used to derive the count).

## What was donated

- Quick Construction panel, entry, read live: 8/10,
  Increased Building Speed for Allies, Donation Reward
  +20%, Tech EXP Required 3.1M/6.0M, Current +20%,
  Next Level +22.5%, Donation Reward 50 EXP + 50 badge
  per donation. Donation Count 2/30 remaining, coin
  Donate green at 900 coin, diamond Donate 2 (never
  used). The count read 2/30 live at 23:16, against
  1/30 or 0/30 at the 2133 close at 21:33 - the count
  replenished by 1 or 2 over the cooldown, further
  evidence for the replenishing burst allowance (Issue
  #599).
- Coin Donate tapped at (677,762) (fresh measured
  centre), one tap at a time with a live read after
  each.
- Tap 1 landed: Donation Count 2/30 to 1/30 on the
  screenshot after the tap. Toast "Alliance Gift (R)
  received!".
- Tap 2: the coin button greyed with a 00:09:58 timer
  and the Donation Count label hid behind the timer,
  the same end state as 1913, 2015 and 2133. The
  button was green with count 1/30 visible immediately
  before tap 2 and greyed with the timer immediately
  after - a missed tap produces no change, so tap 2
  registered; but the count label itself is
  timer-hidden, so per the hard closing rule (R1) the
  close is unverified, not a live 0/30 read.
- Corroboration only, not a closing figure: Tech
  Donation Today re-read live after closing the panel,
  1400 to 1600 (+200). The footer points per donation
  are not stable (50, 60, 100 seen across units) and
  the footer cannot derive the count. Badge item top
  bar read 405.9K at entry and 406.1K at close (+200);
  its meaning is likewise not pinned down and it is
  not used as evidence here.
- Timer note: this burst's cooldown read 00:09:58,
  shorter than the 00:13:28 / 00:14:47 / 00:14:25
  timers of the earlier bursts. Whether the cooldown
  length varies or the timer started earlier in the
  burst window is unpinned; the re-read is scheduled
  after this timer expires.

## Close

- Partial, unverified close - the same close as 1913,
  2015 and 2133. Two coin donations made (tap 1
  confirmed by live count read 2/30 to 1/30; tap 2
  evidenced by the green-to-greyed button state
  change); the final count label is timer-hidden, so
  the count after tap 2 is not a live read. The
  tracker stays untouched. A named re-read unit is
  enqueued for after the cooldown (not_before
  2026-11-11T07:30:00Z, about 23:30 PT) to read the
  final count live.
- Pass ends here: the maintenance shutdown banner gave
  about 7 minutes from 23:14, so no further game unit
  is attempted this pass; the next tick retries after
  the maintenance window.
- No diamonds or money spent. No priced button, Renew,
  paid unlock or Legendary Claim All tapped. No login
  or verification demanded. No "active on a different
  device" dialog appeared.

## Result stats

- target 30 of 30 coin donations for the reset day
- achieved 1 confirmed this unit by live count read
  (2/30 to 1/30); 2nd donation evidenced by the
  button greying, count after it timer-hidden
- resources_gained 50 Tech EXP plus 50 badge items per
  confirmed donation (100 Tech EXP plus 100 badge for
  the 2 taps as displayed)
- points Tech Donation Today 1400 to 1600 live (plus
  200, footer only, not used to derive the count)
- costs 2 coin donations at 900 coin each (1800 coin),
  about 7 minutes
- verified no
- blocker_category e
- donations_confirmed 1, donations_button_greyed 1,
  donation_count_before 2, donation_count_after
  unknown (timer-hidden), coin_cost_per_donation 900,
  tech Quick Construction 8/10, cooldown_timer 00:09:58,
  count_replenished_between_units yes (1 or 0 at 21:33
  to 2 at 23:16), maintenance_shutdown_banner yes
  (7-min warning at entry)
