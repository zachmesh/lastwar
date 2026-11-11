---
title: Passes queue run
created: 2026-11-11T23:31:00Z
modified: 2026-11-11T23:31:00Z
version: 1.0.0
description: Ticker passes unit - checked only, nothing claimable, Free Supply and monthly already claimed
status: unverified
---

# Passes queue run - 2026-11-11 15:31 local

- Executor: ticker-1507
- Unit: passes-2026-11-11-1057 (planned 10:57 local, expires 14:57 local)
- Session window: about 15:18-15:31 local (23:18-23:31 UTC)
- Status: done (checked, nothing claimable)

## What was done

- Game was found open on the base screen, no "active on a different
  device" dialog. Entry read live: Total Power 149,218,973; food
  688.3M, iron 1.0G, coin 135.6M, gold 13.22K, diamonds 6,717;
  stamina 70; March Queues 0/4; gift badge 2.
- Shop opened from the base cart icon (tap at normalized 912,68,
  first try). Hot Deals: only the external-store promo ("Visit the
  Last War Store for more rewards!") and the check-in banner
  ("Participate in the check-in event and claim great rewards!",
  FREE GIFT "Claim your gift today!", FREE TOMORROW x5 x5 x5) with
  a Go button. No free pack showing. Go was not tapped: the
  check-in entry is unproven and tracked on Issue #553; the
  foreground-click idea for it stays open.
- Shop, Weekly Pass tab: page reads "Weekly Pass rewards reset at
  18:00:00" (twenty-second live confirmation). Free Supply chest
  reads Claimed; no auto-claim popup fired on this visit.
  Legendary row "Take All $19.99" seen and NOT tapped.
- Weekly Pass list, walked to its end: S2 Drone Components Weekly
  Pass (Legendary) Get Now $4.99, S1 Drone Parts Weekly Pass (Epic)
  Get Now $4.99, Coin Weekly Pass (Elite) Get Now $4.99 - all three
  are purchase offers, none is an owned pass with a claimable Daily
  Pickup. The list scrolled once on the long drag (500,850 to
  500,250); three further drags (same endpoints, a maximum-length
  drag, and a bottom-strip drag) moved nothing, so the list ends at
  the Coin card. The EXP and Iron cards from the 2026-11-02 read
  are absent from the list today - the list has rotated. No price
  button was tapped.
- Shop, Super Monthly Pass tab: Monthly Pass, Squad 4 Lv.20, Days
  Left 10, Rewards Left 10, Daily Pickup button reads Claimed. The
  $24.99 Monthly Pass Extension button was NOT tapped. Days Left 10
  repeats the 06:46 read today, so no further tick intraday.
- Game left on the base screen: stamina 72 (regen plus 2 during the
  unit), coin 135.6M unchanged, gift badge still 2. The 2 pending
  LOOT rows belong to the zombie-invasion chain (unit 016 closed
  with both squads in flight); they were not touched - the zombie
  successor (017, already in the live inbox) claims them.

## Lateness

- This unit serves the 10:57 local slot and was executed 15:18-15:31,
  past its 14:57 expiry. The queue handed it out as earliest expiry
  and the sweep itself stays valid - pass claims do not lapse at the
  slot end - so it was executed rather than expired. It counts as
  late in the statistics.

## Result statistics

- target: all claimable pass/shop freebies for the slot
- achieved: 1 shop claim sweep performed; Free Supply verified
  already claimed, monthly daily gift verified already claimed,
  no owned weekly pickup exists
- resources_gained: none
- points: none
- costs: about 13 minutes, no stamina or items spent
- verified: yes - every figure above was read live on screen in this unit
- blocker_category: none

## Red lines

- No diamonds or money spent. No price button tapped. Legendary Take
  All ($19.99) untouched. No donation, no assembly, no teleport.
