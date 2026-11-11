---
title: Shop Claims queue run 1029
created: 2026-11-10T18:29:00Z
modified: 2026-11-10T18:29:00Z
level: L0
version: 1.0.0
description: Ticker-1004 passes unit, nothing claimable this cycle, Weekly Pass scroll method failed
status: unverified
---

# 1029 queue run - Shop claims (ticker-1004)

Unit: passes-2026-11-10-0657. Status: done.
Activity: shop-claims.

## Live reads

- Shop opened from the base cart icon. HOT DEALS landing shows
  only the "Visit the Last War Store for more rewards!" promo
  with the Go button (not tapped). No free pack on the landing
  page. No check-in banner was visible on this opening (the
  0440 record saw one; it may have rotated or expired).
- Weekly Pass page reads "Weekly Pass rewards reset at
  18:00:00" - the same cycle reading as the 0214 and 0440
  records.
- Free Supply chest: visible, no Claim button, no red dot.
  Consistent with already taken this cycle (auto-claims on
  page open per the activity metadata); no claim toast was
  observed in this unit.
- Legendary row: "Instant Gain on Purchase", Take All $19.99 -
  never tapped.
- Weekly Pass cards seen (top of the list):
  - S2 Drone Components Weekly Pass (Legendary), Daily Pickup
    x2, Total x7, Get Now $4.99.
  - S1 Drone Parts Weekly Pass (Epic), Daily Pickup x15,
    Total x105, Get Now $4.99.
  Both are purchase offers, not owned passes; no Claim button
  on either.
- Super Monthly Pass tab: Monthly Pass, Days Left 11,
  Squad 4 Lv.20. Daily Pickup button reads Claimed. Rewards
  Left: 11. The $24.99 Monthly Pass Extension was not
  touched. Same readings as the 0440 record.
- Weekly Deal tab (2026-11-9 00:00:00 - 2026-11-15
  23:59:59): Valor Badge $99.99, Base Upgrade $19.99,
  UR Set $49.99, each "1 purchases available". All paid
  bundles, nothing free.

## Scroll blocker

- The Weekly Pass list would not scroll in this unit: a
  plain scroll action, a drag from 700 to 300, and a scroll
  with scroll_direction down and scroll_amount 5 all returned
  no change. The S1 card is cut off at the bottom edge, so
  the Iron and Coin Weekly Pass cards below the fold were
  NOT re-verified in this unit. The 0440 record verified all
  four cards in this same cycle (none owned, no Claim
  button), so the unit still closes as checked with nothing
  claimable, but the scroll method needs a changed approach
  next time (try scrolling by the list container element, or
  a longer press-drag stroke).

## What was done

- Four shop tabs checked live: HOT DEALS landing, Weekly
  Pass, Super Monthly Pass, Weekly Deal. Nothing claimable
  anywhere this cycle.
- Monthly Daily Pickup verified Claimed for this cycle.
- No money spent; the Legendary $19.99 Take All, the
  $24.99 extension, all $4.99 Get Now buttons and the three
  Weekly Deal price buttons were left untouched.

## Follow-up

- Next passes unit: retry the Weekly Pass scroll with a
  changed method (list-container scroll or long press-drag)
  to re-verify the Iron and Coin cards below the fold.

## Red lines

- No diamonds or money spent. No price button, Renew, or
  paid unlock tapped. No other unit's work touched.

## Stats

- target: 3
- achieved: 0
- resources_gained: none
- costs: about 5 minutes of unit time, no items spent
- verified: yes
- blocker_category: none
- points: 0
