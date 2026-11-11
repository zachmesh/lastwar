---
title: VIP queue run 1812
created: 2026-11-08T02:12:00Z
modified: 2026-11-08T02:12:00Z
level: L0
version: 1.0.0
description: Ticker-1734 VIP unit, partial - login chest claimed for 60 VIP points, Daily Freebie button unresponsive across four input variants
status: unverified
---

# 1812 queue run - VIP Rewards

Executor: ticker-1734. Unit: vip-2026-11-06-1800.
Session window about 17:57 to 18:12 America/Los_Angeles
(01:57 to 02:12Z). Computer session cc-28, LastWar already
running on the base screen. One stale-observation error on the
first avatar tap (input not sent); a fresh observe and the
retry landed.

## What was found

- VIP screen: VIP13, points 1,603,930 of 2,000,000 on entry.
  Streak reads "logged in 2 days in a row, collect 80 VIP
  points tomorrow".
- Login chest (top right): red dot present. One tap opened a
  CONGRATULATIONS popup - "Today's VIP Points 60,
  Consecutive Login Days 2, Next Day's VIP Points 80".
  Points after: 1,603,990 of 2,000,000 (plus 60, live read).
  The chest stands open afterwards and its red dot is gone.
- Daily Freebie: green Claim button, rewards puzzle piece x2,
  crates x13, x13, coin x13. The button did NOT respond to
  four input variants, each with a fresh observation and a
  fresh measured centre (norm about 739, 637): two background
  clicks, one 1-second long-press, and one click after the
  game window came to the foreground. Points and button
  unchanged after every attempt. This is the known repeat
  blocker the activity metadata already names (claim buttons
  intermittently unresponsive; 2026-10-31 took neither after
  5 variants). The foreground-window variant tried here is
  new: the chest tap on the same screen in the same session
  DID land, so input reaches the screen and only the
  Freebie button is dead.
- The VIP Exclusive offer ($99.99), the points + button and
  the cart shortcut were not tapped.
- An "Alliance Gifts received!" toast crossed the screen
  during the unit; it is a background event, not this unit's
  work, and nothing was claimed for it here.

## Mechanism notes (live read vs activity metadata)

- The Freebie unlocked at about 18:02, confirming the
  ticker-1727 finding that it runs on its own roughly 24-hour
  cycle from the last claim, not on the 19:00 reset clock.
  The metadata's reset-clock claim still needs the knowledge
  organiser's correction; this unit does not edit tier-2 files.
- The streak display moved from 1 day / 60 tomorrow (ticker-1727
  at 17:43) to 2 days / 80 tomorrow (this unit) with no new
  login in between: the day-2 chest claim itself pays 60 and
  advances the streak to 2. No contradiction; the 1727 read
  was the pre-claim state.
- The failed Freebie claim re-enters the pre-reset sweep per
  the metadata: the 18:30 zero sweep (unit 002) and the next
  ticker should retry it before the 19:00 reset.

## Figures read live on screen

- VIP points 1,603,930 before, 1,603,990 after the chest
  claim; streak 2 days; next day 80 points.
- Power 149,850,353; food 476.8M, iron 800.4M, coin 5.7M
  (unchanged - the Freebie crates were not claimed).
- No diamonds, money, speedups or paid buttons were used.
  No other task type was executed in this unit. No login
  or verification was demanded, and no different-device
  dialog appeared.

## Result statistics

- target 2, achieved 1, resources_gained VIP points 60,
  costs about 15 minutes play, verified yes,
  blocker_category e, device_takeovers 0
