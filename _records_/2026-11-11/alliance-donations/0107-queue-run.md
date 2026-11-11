---
title: Alliance donations queue run 0107
created: 2026-11-11T01:07:00-08:00
modified: 2026-11-11T01:07:00-08:00
version: 1.0.0
description: Donations unit donations-2026-11-11-0757, Quick Construction 8/10, 3 coin taps, final count timer-hidden after an 18:48 cooldown, partial unverified close
status: unverified
grounded_in:
  - source: live game screen on the owner Mac mini, 2026-11-11 00:57-01:07 PST
---

# Alliance donations queue run 0107 (ticker-0055)

Unit: donations-2026-11-11-0757. Status: partial.
Activity: alliance-donations. Computer sessions cc-529, cc-530
(session cc-529 dropped mid-unit during the cooldown wait;
cc-530 recovered with no game state lost).

## Entry

- Base screen at entry: food 656.2M, iron 979.3M, coin 110.7M,
  badge item 406.4K, Total Power 149,218,973.
- Game left on the Zombie Invasion - Glacieradon event Store
  (4000 medals) by the previous unit; Store closed, back to
  base. Event page re-confirmed live: timer 2d 17:02:08,
  boss clue 40/40, challenge begins 2026-11-12 18:00 local,
  next wave in 00:56:40.
- Alliance entry: shield icon tapped at the fresh measured
  centre (931,716) from the current screenshot - opened the
  menu first try. The (903,787) centre in the activity
  metadata is stale; (931,716) here matches (930,717) and
  (927,707) from 2026-11-10 within measurement.
- Alliance menu: [AP3x] The Apex, Leader Abyss Apex,
  Members 96/100.
- Alliance Techs tile tapped at (686,679). War tab first:
  Unit Load Capacity 2/10, Quick Training 1/10, Expert
  Trainer 2/10, World Interception / Rapid Siege / Quick
  Garrison 5/10, Troop Movement 5/10, Rallied HP /
  Rallied Attack / Rallied Defense 7/10, next node 1/10.
  Development tab: Auto Rally Max Level, Quick
  Construction 8/10 (red recommended marker), Great
  Helper Max Level, bottom node 2/10. Tech Donation
  Today footer 1900 at entry.

## What was donated

- Target: Quick Construction (recommended), 8/10,
  Increased Building Speed for Allies, Donation Reward
  +20%, Tech EXP Required 3.1M/6.0M, Current +20%,
  Next Level +22.5%, Donation Reward 50 EXP + 50 badge
  per donation. Coin Donate green at 900 coin, diamond
  Donate 2 (never used).
- Donation Count read live at panel entry: 2/30 remaining.
- Coin Donate tapped at (659,764), one tap at a time
  with a live read after each.
- Tap 1 landed: Donation Count 2/30 to 1/30 on the
  screenshot after the tap.
- Tap 2: the coin button greyed with a 00:02:50 timer
  and the Donation Count label hid behind the timer,
  the same end state as 1913, 2015, 2133 and 2319.
  The button was green with count 1/30 visible
  immediately before tap 2 and greyed with the timer
  immediately after - a missed tap produces no change,
  so tap 2 registered; but the count label itself is
  timer-hidden, so per the hard closing rule (R1) the
  count after tap 2 is not a live read.
- Cooldown waited out inside the unit (170 seconds):
  after expiry the panel re-read live at Donation
  Count 1/30 with the green Donate button active
  again. Consistent with tap 2 landing (1 to 0) plus
  a +1 replenish during the cooldown - the burst
  replenishment of Issue #599 - or with tap 2
  missing; the live fact is 1/30 remaining at the
  re-read, and no arithmetic is used as a closing
  figure.
- Tap 3: button green at 1/30, tap registered (greyed
  with a 00:18:48 timer, count label hidden again).
  A toast appeared on this tap: "Hold down for easier
  continuous donations" - new knowledge, not yet in
  the activity metadata (tier-2 change, left for the
  PR flow; noted here only).
- Timer 00:18:48 is too long to wait inside the unit
  cap, so the unit closes here.

## Close

- Partial, unverified close - the same close as 1913,
  2015, 2133 and 2319. Three coin taps made (tap 1
  confirmed by live count read 2/30 to 1/30; taps 2
  and 3 evidenced by the green-to-greyed button state
  change); the final count label is timer-hidden, so
  the count after tap 3 is not a live read. The
  tracker stays untouched. A named re-read unit is
  enqueued for after the cooldown (not_before
  2026-11-11T09:29:00Z, about 01:29 PT) to read the
  final count live.
- Corroboration only, not a closing figure: Tech
  Donation Today re-read live after closing the panel,
  1900 to 2500 (+600 over 3 taps). The footer points
  per donation are not stable (50, 60, 100, 200 seen
  across units) and the footer cannot derive the
  count. Badge item top bar read 406.4K at entry and
  406.7K at close (+300, +100 per tap); its meaning
  is likewise not pinned down and it is not used as
  evidence here.
- No diamonds or money spent. No priced button, Renew,
  paid unlock or Legendary Claim All tapped. No login
  or verification demanded. No "active on a different
  device" dialog appeared.

## Result stats

- target 30 of 30 coin donations for the reset day
- achieved 1 confirmed this unit by live count read
  (2/30 to 1/30); 2 further taps evidenced by the
  button greying, counts after them timer-hidden;
  live re-read after the first cooldown 1/30
- resources_gained 50 Tech EXP plus 50 badge items per
  confirmed donation (150 Tech EXP plus 150 badge for
  the 3 taps as displayed)
- points Tech Donation Today 1900 to 2500 live (+600,
  footer only, not used to derive the count)
- costs 3 coin donations at 900 coin each (2700 coin),
  about 11 minutes
- verified no
- blocker_category e
- donations_confirmed 1, donations_button_greyed 2,
  donation_count_before 2, donation_count_after
  unknown (timer-hidden), donation_count_reread 1,
  coin_cost_per_donation 900,
  tech Quick Construction 8/10, cooldown_timer 00:18:48,
  count_replenished_between_taps yes (1 after the first
  cooldown), session_drop yes (cc-529 to cc-530, no
  state lost), hold_to_donate_toast yes
