---
title: Alliance donations queue run 1919
created: 2026-11-11T03:35:00Z
modified: 2026-11-11T03:35:00Z
level: L0
version: 1.0.0
description: Donations unit donations-2026-11-11-0122, re-read of the 1704 unverified close; 2 coin donations confirmed, final count hidden by cooldown timer, donation-day counter reset mid-unit
status: unverified
---

# Alliance donations 19:19 to 19:35 - ticker-1913

Unit donations-2026-11-11-0122 (the re-read unit enqueued by
ticker-1704 for its unverified close; not_before 01:40Z). Executor
ticker-1913. Session cc-493 on the owner Mac mini, LastWar already
open on the base screen.

## What was read live

- Alliance entry: the Alliance shield icon tapped at the fresh
  measured centre (927,715) opened the menu first try. The
  (903,787) centre in the activity metadata is stale; 1704's
  (927,715) is confirmed again.
- Alliance menu: [AP3x] The Apex, Leader Abŷss Apex, Power
  13,769,825,549, Members 96/100, Language English. Help carries
  a red dot - that is the help unit's work, not this unit's; no
  Help All was tapped.
- Alliance Techs, Development tab: Auto Rally Max Level, Quick
  Construction 8/10, Great Helper Max Level, bottom node 2/10.
  Tech EXP Required 3.0M/6.0M, Current +20%, Next Level +22.5%.
  Donation Reward 50 EXP + 50 badge per donation.
- Quick Construction panel, entry: Donation Count 6/30, coin
  Donate button green at 900 coin, diamond Donate button 2
  (never used). Tech Donation Today footer 9300.
- The 19:00 reset had already passed when the unit started
  (19:19), yet the count read 6/30 and the footer 9300 - the
  donation day did NOT reset at 19:00.

## What was donated

- Coin Donate tapped 5 times in total. Count moved 6/30 to 4/30
  on live image reads after the first three taps: 2 coin
  donations confirmed landed (1800 coin, 100 Tech EXP, 100
  badge).
- The final two taps (batched, 2 seconds apart) greyed the coin
  button with a 00:14:57 timer and hid the Donation Count label
  behind the timer. Whether 0, 1 or 2 of those taps landed is
  unknown from any live read.
- Donate button flakiness, rule R2 note: the first two taps
  (snap default, (646,752)) showed no change; the third tap
  (snap_to_control false, (646,741)) coincided with the count
  moving. A hint appeared during the batch: "Hold down for
  easier continuous donations" - the button supports
  hold-to-donate. Future units should try a press-hold instead
  of repeated taps.
- An "Alliance Gifts received!" toast appeared while the panel
  was open; gifts are another unit's work and were not touched.

## The mid-unit counter reset (new finding)

- After closing the panel, the footer was re-read live: Tech
  Donation Today 550, down from 9300 at entry. The donation-day
  counter reset inside this unit, between about 19:24 and 19:34
  PST - not at the assumed 19:00 reset. The footer therefore
  cannot derive this unit's final count, and the Donation
  Count's own reset time is unpinned. Filed as knowledge
  Issue #599.
- The old day's remainder (4/30 at about 19:30) is moot after
  the reset; the new day's count is unknown from any live read.

## Close

- Partial, unverified close. The final Donation Count could not
  be read live: hidden by the 00:14:57 cooldown timer, which
  cannot be waited out inside the unit budget. The tracker stays
  untouched. A named re-read unit is enqueued for after the
  cooldown (not_before 03:48Z) to read the new-day count live
  and donate any remainder.
- No diamonds or money spent. No price button, Renew, paid
  unlock or Legendary Take All tapped. No login or
  different-device dialog appeared.

## Figures read live on screen

- Food 631.4M, iron 954.2M, coin 97.8M, diamonds 6,267,
  power 148,787,578 at entry.
- Quick Construction 8/10, Tech EXP 3.0M/6.0M, coin cost 900
  per donation, diamond cost 2 (never used).
- Donation Count 6/30 at entry, 4/30 live mid-unit, hidden at
  close behind a 00:14:57 timer. Tech Donation Today 9300 at
  entry, 550 at close.

## Result statistics

- target 30/30 count read with 0 remaining, achieved count
  unread (2 coin donations confirmed, final batch unknown),
  resources_gained 100 Tech EXP + 100 badge confirmed (final
  batch unknown), costs about 16 minutes play and 1800 coin
  confirmed, verified no, blocker_category e (repeated blocker -
  cooldown timer hiding the count, same mechanism as the 1704
  close), device_takeovers 0

No other task type was executed in this unit.
