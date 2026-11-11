---
title: Alliance donations queue run 2133
created: 2026-11-11T05:33:00Z
modified: 2026-11-11T05:33:00Z
version: 1.0.0
description: Donations unit donations-2026-11-10-1803, re-read of the 2015 unverified close; 3 coin donations confirmed, 4th tap landing unknown behind the cooldown timer, partial
status: unverified
grounded_in:
  - source: live game screen on the owner Mac mini, 2026-11-10 21:26-21:33 PT
---

# Alliance donations queue run 2133 (ticker-2122)

Unit: donations-2026-11-10-1803. Status: partial.
Activity: alliance-donations. Computer session cc-512.

## Entry - radar exit solved with a fresh measured point

- The game was left on the radar screen by the ticker-2055
  pass (points 375, stored 13/40, stamina 41 at its close).
  The ticker-2055 survivors unit failed the radar exit in
  5 attempts at y 915-936. This unit tapped the Home
  button at its fresh measured centre (927,952) from the
  current screenshot and reached the base screen on the
  first try. The 2118 taps sat above the button row
  (buttons centre near y 952); the exit blocker was a
  mis-measured point, not an unresponsive button.
- Base screen at entry: food 644.3M, iron 967.4M, coin
  105.9M (HUD-rounded), gold 405.1K, Total Power
  148,787,578, stamina 44.
- Alliance entry: shield icon tapped at the fresh
  measured centre (930,717) from the current screenshot
  (visual grounding bbox 882-978, 685-750) - opened the
  menu first try. The (903,787) centre in the activity
  metadata is stale; (927,715) confirmed by 2015 and
  (930,717) here are the same point within measurement.
- Alliance menu: [AP3x] The Apex, Leader Abŷss Apex,
  Power 13,816,852,247, Members 96/100, Language
  English. Help and Alliance Gifts carry red dots -
  other units' work, not touched here.

## Alliance Techs

- Alliance Techs tile tapped at (686,680) (bbox
  506-867, 642-718). Development tab at entry: Auto
  Rally Max Level, Quick Construction 8/10, Great
  Helper Max Level, bottom node 2/10. Tech Donation
  Today footer 700 at entry (same as 2015's close, so
  no points accrued between 20:15 and 21:26).
- War tab checked: Unit Load Capacity 2/10, Quick
  Training 1/10, Expert Trainer 2/10, bottom row
  5/10 nodes. The red thumbs-up marker sits on the
  Development tab, so the recommended node is on
  Development: Quick Construction 8/10 (red marker at
  its top-left corner).
- Quick Construction panel, entry, read live:
  8/10, Increased Building Speed for Allies, Donation
  Reward +20%, Tech EXP Required 3.0M/6.0M, Current
  +20%, Next Level +22.5%, Donation Reward 50 EXP +
  50 badge per donation. Donation Count 4/30
  remaining, coin Donate green at 900 coin, diamond
  Donate 2 (never used).

## What was donated

- Coin Donate tapped at (658,790) (bbox 543-774,
  752-828), one tap at a time with a live read after
  each.
- Tap 1 landed: Donation Count 4/30 to 3/30 on the
  screenshot after the tap. Toast "Alliance Gift (R)
  received!".
- Tap 2 landed: Donation Count 3/30 to 2/30 (receipt
  OCR "2/30").
- Tap 3 landed: Donation Count 2/30 to 1/30 on the
  screenshot after the tap.
- Tap 4: the coin button greyed with a 00:14:25 timer
  and the Donation Count label hid behind the timer,
  exactly the 1913 and 2015 end state. Whether tap 4
  landed is unknown from any live read - the count
  after tap 4 is either 0/30 or 1/30.
- Corroboration only, not a closing figure: Tech
  Donation Today re-read live after closing the panel,
  700 to 1150 (+450). The footer points per donation
  are not stable (60 on 2026-10-25, 50 on 2026-10-26,
  +150 for 2015's taps, +450 here) and the footer
  cannot derive the count - the 2015 conclusion
  stands. The top-bar badge item count read 405.1K at
  entry and 405.5K at close (+400); its meaning is
  likewise not pinned down and it is not used as
  evidence here.

## Count replenishment - new mechanism evidence

- The count read 4/30 at 21:26, but the 2015 unit left
  it at 1/30 or 0/30 at 20:15 with the footer at 700
  then and 700 at this unit's entry. The count therefore
  replenished by about 3-4 between 20:15 and 21:26
  while no donation landed and the footer did not move.
  The Donation Count is not a pure daily remaining that
  only falls: it is a replenishing burst allowance
  against the daily 30 cap, refilling over roughly an
  hour after the cooldown. The daily 30/30 target and
  the count's own reset/replenish cadence stay unpinned;
  this is further evidence for knowledge Issue #599.
- The burst pattern is now four units consistent: donate
  until the button greys with a ~14-15 minute timer
  (00:13:28 on 2026-10-26, 00:14:47 at 2015, 00:14:25
  here). The timer is the burst cooldown, not the daily
  end - the next burst becomes available after it, and
  the count refills by then.

## Close

- Partial, unverified close - the same close as 1913
  and 2015. Three coin donations confirmed by live
  count reads (4/30 to 1/30); the fourth tap's landing
  is unknown because the cooldown timer hides the
  count, and the timer cannot be waited out inside the
  unit budget. The tracker stays untouched. A named
  re-read unit is enqueued for after the cooldown
  (not_before 2026-11-11T05:48:00Z, about 21:48 PT) to
  read the final count live.
- No diamonds or money spent. No priced button, Renew,
  paid unlock or Legendary Claim All tapped. No login
  or verification demanded. No "active on a different
  device" dialog appeared.

## Result stats

- target 30 of 30 coin donations for the reset day
- achieved 3 confirmed this unit; Donation Count 4/30
  to 1/30 live, 4th tap landing unknown (0/30 or 1/30)
- resources_gained 150 Tech EXP plus 150 badge items
  (3 confirmed donations at 50 each)
- points Tech Donation Today 700 to 1150 live (plus
  450, footer only, not used to derive the count)
- costs 3 confirmed coin donations at 900 coin each
  (2700 coin), about 7 minutes
- verified no
- blocker_category e
- donations_confirmed 3, donations_unknown 1,
  donation_count_before 4, donation_count_after
  unknown (timer-hidden), coin_cost_per_donation 900,
  tech Quick Construction 8/10, cooldown_timer 00:14:25,
  count_replenished_between_units yes (1 or 0 at 20:15
  to 4 at 21:26)
