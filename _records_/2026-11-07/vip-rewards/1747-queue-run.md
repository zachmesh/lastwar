---
title: VIP queue run 1747
created: 2026-11-08T01:47:00Z
modified: 2026-11-08T01:47:00Z
level: L0
version: 1.0.0
description: Ticker-1727 VIP unit, partial - freebie on a live countdown to about 18:02, login chest already collected
status: unverified
---

# 1747 queue run - VIP Rewards

Executor: ticker-1727. Unit: vip-2026-11-06-1900.
Session window about 17:43 to 17:47 America/Los_Angeles
(01:43 to 01:47Z). Computer session cc-20, LastWar already
running. One stale-observation error on a back tap (input
not sent); a fresh observe showed the app unchanged and the
retry landed.

## What was found

- VIP screen: VIP13, points 1,603,930 of 2,000,000 toward
  VIP 14 (live read). Login streak reads 1 day in a row,
  "Collect 60 VIP points tomorrow".
- Daily Freebie NOT claimable: its button is a live
  countdown reading 00:16:52, then 00:16:40, then
  00:15:48 across this unit's reads - it unlocks at about
  18:02, not at the 19:00 reset. The rewards shown are
  the usual VIP13 set (puzzle piece x2, crates x13, x13,
  coin x13).
- Login chest (top right): no red dot; one tap produced
  no change, so today's login points are already
  collected. Nothing further was claimed.
- The VIP Exclusive offer ($99.99), the points + button
  and the cart shortcut were not tapped.

## Mechanism correction (live read vs activity metadata)

- The activity metadata states the post-claim Freebie
  countdown runs to the 19:00 daily reset. Today's live
  countdown unlocks at about 18:02, a full 58 minutes
  before the reset - so the Freebie is on a cycle of its
  own (most plausibly 24 hours from the last claim,
  last claimed about 18:02 on 2026-11-06), not on the
  reset clock. The metadata's reset-clock claim needs a
  correction by the knowledge organiser; this unit does
  not edit tier-2 files. The 18:30 zero sweep (unit 002)
  and the next ticker both fall after 18:02 and can
  verify the claim then.

## Figures read live on screen

- VIP points 1,603,930 of 2,000,000; streak 1 day;
  Freebie countdown 00:16:52 to 00:15:48 across the unit.
- Power 149,850,353; food 476.8M, iron 800.4M, coin 5.7M.
- No diamonds, money, speedups or paid buttons were used.
  No other task type was executed in this unit. No login
  or verification was demanded, and no different-device
  dialog appeared.

## Result statistics

- target 1, achieved 0, resources_gained none, costs about
  4 minutes play, verified yes, blocker_category h,
  device_takeovers 0
