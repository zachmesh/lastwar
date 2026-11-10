---
title: Alliance Donations Execution 2026-10-31 1013 Queue Run
created: 2026-10-31T17:23:00Z
modified: 2026-10-31T17:23:00Z
level: L0
version: 0.1.0
description: Donations queue unit donations-2026-10-31-1003 - target Rallied HP 5/10, count 11/30 at entry to arithmetic 0/30, 11 coin donations at 600 coin each, final count hidden under a 00:48:04 timer so the tracker is untouched
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-10-31
  - source: owner directions of 2026-10-25, 2026-10-26 and 2026-10-28 - the standing routine, Mac control authorization and the task unit queue ticker
---

# Alliance donations — execution, 2026-10-31 1013 queue unit

A single task unit, executed by executor ticker-1004 under the
task unit queue. Unit donations-2026-10-31-1003, priority 2.
Session window about 10:13 to 10:23 America/Los_Angeles.
Computer sessions cc-635 and cc-636 (cc-635 dropped
during the cooldown wait and cc-636 resumed with no game
state lost, as in earlier units).
Status — partial: 11 coin donations were made to the
recommended technology, but the final count label is
hidden under the button timer, so the tracker is
untouched and the next tick re-produces this regular
to verify the count at 0 once the timer clears.

## What was observed

- Entry — the game was left on the base screen by the
  preceding arms-race unit. The Alliance button at norm
  928,705 opened the Alliance panel; the Alliance Techs
  tile at norm 717,678 opened ALLIANCE TECHS on the War
  tab (Troop Movement 5/10, Rallied HP 5/10, Rallied
  Attack 7/10, Rallied Defense 7/10, next node 1/10).
  Tech Donation Today footer read 3850 at entry, the
  same reading the 0620 unit closed with.
- Target — Rallied HP 5/10, the node carrying the
  recommended marker on the War tab, same target as
  the 0220 and 0620 units. Panel: Increased Hero HP
  in Rallies for Allies, Current +5%, Next Level +6%,
  Donation Reward +20%, Tech EXP 1.0M/2.0M at entry
  (0.1M display rounding), Donation Reward 50 + 50
  as displayed. Coin Donate 600 per donation; the
  diamond Donate button (2 diamonds) was never
  touched.
- Grounded button point — the green coin Donate
  button at norm 660,765, as grounded by the 0220
  unit, worked on the first tap.
- Donations made — 11 in total. Count label verified
  at each step: 11/30 at entry, 6/30 after a batch
  of 5, 1/30 after a second batch of 5. The next
  single tap greyed the button with a 00:01:02
  timer; after a 75 second wait the count
  reappeared at 1/30, matching the 0220 burst
  cooldown pattern, so that tap is treated as
  burst-blocked, not landed. A further single tap
  greyed the button again, this time with a
  00:48:04 timer and the count label hidden, so
  the final 0/30 reading is arithmetic (11 minus
  11), not a directly read label — hence partial,
  not done, following the 0220 and 0620 precedents.
  Coin spent: 11 times 600 = 6,600 if the final
  tap landed as the timer pattern suggests.
- Count replenishment note — the entry reading of
  11/30 is itself new evidence: the 0620 unit
  closed at an arithmetic 0/30 about 06:20, and by
  10:15 the count stood at 11/30 again, so the
  donation count replenishes over the hours
  between units; the replenishment rate is not
  pinned down by this unit and is left unresolved.
  The 00:48:04 timer on the final tap is the
  next check constraint: the next tick should
  re-read the count once that timer clears
  (about 11:09 local).
- Footer check — after closing the panel, Tech
  Donation Today read 5150, up 1300 from the 3850
  entry reading. That delta does not match a clean
  per-donation rate, so the per-donation point
  rate is left unresolved here; the footer rise
  corroborates that donations landed, but it is not
  used as the donation count evidence.
- Daily reward — footer 5150 is above the 1000
  contribution point threshold, and per the
  2026-10-26 resolution the donation ranking reward
  is a settlement paid at the 19:00 reset with no
  Claim button to tap, so nothing further was
  claimed by hand.
- Nothing else spent — no diamonds, no money, no
  speedup or stamina items, no research or building
  started. No other regular was merged into this
  unit. The game was left on the ALLIANCE TECHS
  War tab. No login or verification was demanded,
  and no different-device dialog appeared.

## Result statistics

- donations_made: 11
- coin_spent: 6600
- donation_count_before: 11
- donation_count_after: 0
- count_after_verified: false
- tech_donation_today_before: 3850
- tech_donation_today_after: 5150
