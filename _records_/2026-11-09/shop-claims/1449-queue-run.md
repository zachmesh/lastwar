---
title: Shop Claims 2026-11-09 1449 Queue Run
created: 2026-11-09T22:49:00Z
modified: 2026-11-09T22:49:00Z
version: 1.0.0
description: Passes unit passes-2026-11-09-1057, ticker-1434
---

# Shop claims 1449 queue run

- Executor: ticker-1434
- Unit: passes-2026-11-09-1057 (regular passes, activity shop-claims)
- Session window: 14:38-14:49 PT (claimed 22:37:44Z)
- Status: partial - checked every shop/pass surface in scope; one free
  item (check-in FREE GIFT) remains unclaimed behind an unresponsive
  button; nothing else claimable today.

## What was checked (live reads)

- Hot Deals (Official Event tab): no free pack showing today. The
  carousel has two pages: page 1 is the Last War Store promo (ID
  points 1000), page 2 is a check-in event card with FREE GIFT
  ("Claim your gift today!") and FREE TOMORROW ("Randomly obtain
  one", x5 x5 x5). The FREE TOMORROW pack is not claimable until
  tomorrow.
- Check-in FREE GIFT: three taps on the Go button produced no change
  (two at 500,937, one at the freshly measured centre 500,955; the
  control layer reported background clicks not reaching the control).
  The computer session dropped once mid-unit (cc-295 lost, cc-297
  restarted, no game state lost). Per rule R2 the Go-button method
  is ended inside this unit; the next passes unit should try the
  Events-hub route to the check-in event instead of re-tapping Go.
- Weekly Pass page: "Weekly Pass rewards reset at 18:00:00" (countdown
  read). Free Supply chest: page opened, no claim toast observed -
  auto-claim unverified (may have paid silently or already been
  claimed). No owned weekly pass: S2 Drone Components Weekly Pass
  (Legendary, Daily Pickup x2, Total x7) and S1 Drone Parts Weekly
  Pass (Epic, Daily Pickup x15, Total x105) both show a $4.99
  Get Now offer, i.e. not owned - nothing to claim, nothing tapped.
  The Legendary Take All $19.99 row was not tapped.
- Super Monthly Pass page: Monthly Pass, Squad 4 Lv.20, Days Left 12,
  Rewards Left 12. The Daily Pickup button reads "Claimed" - today's
  monthly gift was already claimed before this unit (no passes unit
  ran earlier today, so most likely by the owner). The $24.99 Monthly
  Pass Extension was not tapped.
- Passing observation for the donations unit (not acted on here):
  the Alliance Tech panel the game was left on read Donation Count
  20/30 at about 14:38 PT.

## Claimed

- None in this unit. Monthly daily gift already claimed today;
  weekly passes not owned; Hot Deals free pack not showing.

## Follow-up

- Next passes unit (passes-2026-11-09-1457): try the check-in event
  from the Events hub (base screen Events icon carried a red badge 1)
  to claim the FREE GIFT; do not re-tap the shop Go button.
- Free Supply auto-claim stays unverified; a later unit that opens
  the Weekly Pass page should watch for the claim toast.
- Note for the activity metadata: the S1 Drone Parts and Coin Weekly
  Passes owned on 2026-10-25 have expired (S1 3 days left then,
  Coin 9 days left then); the page now offers S2 Drone Components
  and S1 Drone Parts as $4.99 purchases. No owned weekly pass
  remains, so the Daily Pickup step has nothing to claim until a
  pass is bought (owner decision, never bought by the agent).

## Red lines

- No diamonds or money spent. No price tag tapped. Legendary
  Take All $19.99 not tapped. No speedup items used.
