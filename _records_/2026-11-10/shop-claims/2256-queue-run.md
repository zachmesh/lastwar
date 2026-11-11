---
title: Shop claims queue run 2256
created: 2026-11-11T06:56:00Z
modified: 2026-11-11T06:56:00Z
version: 1.0.0
description: Passes unit passes-2026-11-10-1857, Hot Deals promo only, Weekly Pass no owned pickup on screen, monthly gift already Claimed, app exit and clean relaunch, partial
status: unverified
grounded_in:
  - source: live game screen on the owner Mac mini, 2026-11-10 22:51-22:56 PT
---

# Shop claims queue run 2256 (ticker-2231)

Unit: passes-2026-11-10-1857. Status: partial.
Activity: shop-claims. Computer sessions cc-518 and cc-519.

## Entry - Techs tree to shop in three taps

- The game was left on the Alliance Techs tree by the
  donations unit. The panel X closed to the Alliance menu,
  the menu back arrow returned to the map, and the cart
  icon at (903,63) opened the shop on HOT DEALS, first
  try each.
- Base state at entry: food 644.6M, iron 967.7M, coin
  106.1M (HUD-rounded), gold 405.9K, Total Power
  149,218,973, signed in as HidingAnt504.

## Hot Deals - promo only, no free pack

- The page shows only the promo carousel: "Visit the Last
  War Store for more rewards!" and "Claim points and
  redeem great rewards / 1000 POINTS" with a Go button.
  No free pack is showing. The Go button was not tapped:
  per the 0114 unit it opens the external store, not a
  claim.

## Weekly Pass - no owned pickup on screen

- The reset line reads live "Weekly Pass rewards reset
  at 18:00:00", another confirmation of the 18:00 reset
  (Issue #242).
- Free Supply chest is shown with no status label read
  on this visit: no auto-claim was observed and no
  "Claimed" label was read, so its state is unverified,
  not claimed.
- Legendary row reads "Take All $19.99" - never tapped.
- S2 Drone Components Weekly Pass (Legendary) and S1
  Drone Parts Weekly Pass (Epic) both show "Get Now
  $4.99" - offers to buy, not owned pickups; not tapped.
- A drag-scroll of the pass list did not move it, so the
  cards below (Iron, Coin) are unchecked this unit.

## App exit on the monthly tab tap, clean relaunch

- Tapping the Super Monthly Pass tab quit LastWar outright
  (target_app_exited). The launch request after it
  returned outcome_unknown, so the launch was not repeated;
  list_windows showed a single new window (634238,
  642x951, pid 78374) and the game back on the map with
  state intact - no login demand, no different-device
  dialog. The duplicate 642x919 window is gone after the
  relaunch.
- Retry after the relaunch: the shop reopened and the
  Super Monthly Pass tab opened cleanly with no second
  exit, so the exit was incidental, not tab-caused.

## Super Monthly Pass - daily gift already Claimed

- Monthly Pass, Days Left 11, Rewards Left 11, Squad 4
  Lv.20, "Unlock an extra squad!". The Daily Pickup
  button reads "Claimed" - today's monthly gift is
  already claimed, nothing to claim. The Monthly Pass
  Extension $24.99 button was not tapped.
- The shop was closed back to the map before the unit
  ended; Total Power 149,218,973 at close.

## Close

- Nothing claimed, nothing spent. Status partial: the
  Weekly Pass Free Supply state and the lower pass cards
  are unverified, so the tracker stays untouched and the
  next tick re-produces the regular.
- Follow-up: the next passes unit re-checks the Weekly
  Pass Free Supply label and scrolls the full pass list.
