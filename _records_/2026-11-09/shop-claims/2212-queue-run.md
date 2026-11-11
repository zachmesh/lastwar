---
title: Shop Claims queue run 2212
created: 2026-11-10T06:01:00Z
modified: 2026-11-10T06:01:00Z
level: L0
version: 1.0.0
description: Ticker-2148 passes unit, Weekly Pass list fully scrolled, nothing new claimable this cycle
status: unverified
---

# 2212 queue run - Shop claims (ticker-2148)

Unit: passes-2026-11-09-1857. Status: done.
Activity: shop-claims.

## Live reads

- Shop opened from the base cart icon. The HOT DEALS
  landing now shows a "Visit the Last War Store for more
  rewards!" promo with a two-banner carousel at the
  bottom. Banner 1: "Claim points and redeem great
  rewards", 1000 POINTS. Banner 2: "Participate in the
  check-in event and claim great rewards!", FREE GIFT
  ("Claim your ... today!") and FREE TOMORROW (x5, x5, x5,
  "Randomly obtain one"). One tap on the shared Go button
  while the check-in banner was active produced no
  navigation, so the check-in free gift was not opened;
  see follow-up below. The Go button was not tapped again.
- Weekly Pass page reads "Weekly Pass rewards reset at
  18:00:00" - a fixed 18:00 clock reset, not a countdown.
  The pass cycle therefore runs 18:00 to 18:00, which is
  why the 18:47 claims of ticker-1822 still stand in this
  same cycle at 22:07.
- Free Supply chest: visible on the Weekly Pass page, no
  Claim button (auto-claims on page open; already taken
  this cycle at 18:47).
- Legendary row: "Instant Gain on Purchase", Take All
  $19.99 - never tapped.
- Weekly Pass list fully scrolled (the remainder handed
  off by the 1850 record). Four cards, all purchase offers,
  none owned, no Claim button on any:
  - S2 Drone Components Weekly Pass (Legendary), Daily
    Pickup x2, Total x7, Get Now $4.99.
  - S1 Drone Parts Weekly Pass (Epic), Daily Pickup x15,
    Total x105, Get Now $4.99.
  - Iron Weekly Pass (Elite), Daily Pickup x1, Total x7,
    Get Now $4.99.
  - Coin Weekly Pass (Elite), Daily Pickup x3, Total x21,
    Get Now $4.99.
  The S1 Drone Parts and Coin passes owned on 2026-10-25
  have expired and were not renewed; they are offers now.
- Super Monthly Pass tab: Monthly Pass, Days Left 12,
  Squad 4 Lv.20. Daily Pickup button reads Claimed
  (claimed at 18:47 by ticker-1822 in this same cycle:
  gold bars x2, red gem 100, stamina 50 x2, iron x200,
  5m speedup x60). Rewards Left: 12. The $24.99 Monthly
  Pass Extension was not touched.
- The Season Battle Pass / Season Weekly Pass path was not
  hunted in the Week 8 hub, per Issue #469.

## What was done

- Weekly Pass list fully scrolled and verified: no owned
  Pickup button anywhere; the 1850 handoff is closed.
- Monthly Daily Pickup verified Claimed for this cycle.
- No money spent; the Legendary $19.99 Take All, the
  $24.99 extension and all four $4.99 Get Now buttons
  were left untouched.

## Follow-up

- The shop check-in banner ("FREE GIFT - Claim your ...
  today!") is unresolved: one Go tap did not navigate,
  and the banner was not pursued further in this unit.
  The next passes unit should try opening the check-in
  event from its own entry (Events hub or base icon) and
  record whether today's free gift is claimable, or file
  it as a candidate if no entry is found. Filed as GitHub
  Issue (class knowledge) from this unit:
  zachmesh/lastwar#553.

## Red lines

- No diamonds or money spent. No price button, Renew, or
  paid unlock tapped. No other unit's work touched.

## Stats

- target: 3
- achieved: 0
- resources_gained: none
- costs: about 6 minutes of unit time, no items spent
- verified: yes
- blocker_category: none
- points: 0

## Correction (same pass, before commit)

- The frontmatter created/modified timestamps read 06:12:00Z
  and the costs line read 14 minutes; both are wrong. The unit
  ran 21:55:34 to 22:01:23 America/Los_Angeles
  (duration_seconds 349, about 6 minutes). The closing figures
  (four Weekly Pass cards all offers, Monthly pickup Claimed,
  check-in banner unresolved, Issue #553) are unaffected.
