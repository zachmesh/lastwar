---
title: Shop Claims - queue run 0249
created: 2026-11-11T10:59:00Z
modified: 2026-11-11T10:49:00Z
level: L0
version: 1.0.0
description: Passes unit passes-2026-11-10-2257 - shop checked live, nothing claimable
status: done
activity: shop-claims
executor: ticker-0234
started_at: 2026-11-11T10:46:13Z
finished_at: 2026-11-11T10:49:00Z
verified: yes
grounded_in:
  - source: live game screens on the owner Mac mini, session cc-543, LastWar window 636402
---

# Shop claims - queue run 0249 (unit passes-2026-11-10-2257)

- Unit: `passes-2026-11-10-2257`, planned for 2026-11-11T06:57:00Z, expires 2026-11-11T10:57:00Z
- Executor: ticker-0234; claimed 10:46:13Z; finished about 02:49 PT
- Session: cc-543, Last War window 636402; token held until 11:01:08Z
- Status: done - checked, nothing claimable

## Entry state (base HUD, read live)

- Food 666.8M, iron 989.5M, coin **118.2M**, gold 13.22K, diamonds 6,307
- Total Power 149,218,973; stamina **6**

## Hot Deals (read live)

- Page shows the "Visit the Last War Store" web-store promo carousel with a Go button; no free pack row visible
- OCR on first open read "FREE TOMORROW" - the free pack is not available today (already claimed or not offered this cycle)
- Nothing claimed here

## Weekly Pass page (read live)

- Header: "Weekly Pass rewards reset at 18:00:00" (as displayed; see open question below)
- Free Supply chest shown top-left; **no auto-claim toast observed** on opening the page, and no payout seen - auto-claim state unverified this unit
- Four pass cards, all purchase offers with a "Get Now $4.99" button and no claim button:
  - S2 Drone Components Weekly Pass (Legendary) - Daily Pickup x2, Total x7
  - S1 Drone Parts Weekly Pass (Epic) - Daily Pickup x15, Total 105
  - Iron Weekly Pass (Elite) - Daily Pickup iron, Total x21
  - Coin Weekly Pass (Elite) - Daily Pickup coin x3, Total x21
- No weekly pass is owned, so no Daily Pickup is claimable
- Legendary row: "Take All $19.99" - NOT tapped (red line)

## Super Monthly Pass page (read live)

- Monthly Pass, Days Left **11**, Rewards Left **11**
- Daily Pickup button reads **Claimed** (grey) - today's gift already taken
- "Monthly Pass Extension $24.99" - NOT tapped (purchase)

## Notes

- The Monthly Pass Daily Pickup reads Claimed although no passes unit has run since the 19:00 reset. The previous passes unit (ticker-1834, 18:36 PT 2026-11-10, record shop-claims/1836-queue-run.md) claimed the monthly gift, the free pack and the Free Supply for its cycle. If the pass reset is 18:00 as the Weekly Pass page literally displays, that claim covers this cycle; if the reset is 19:00, the Claimed state is unexplained and the next passes unit should re-check it. Recorded here as an open question, not as a verified explanation.
- No diamonds or money spent; no price tag tapped.

## Result stats

- target: 0 (nothing claimable found live)
- achieved: 0
- resources_gained: none
- costs: about 3 minutes play
- verified: yes
- blocker_category: none
