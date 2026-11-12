---
title: Resource collection queue run 2048
created: 2026-11-12T04:48:00Z
modified: 2026-11-12T04:48:00Z
version: 1.0.0
description: Ticker-2031 harvest unit - food bubbles collected in one tap (+2.2M), one coin bubble collected (+4.0M); iron bubbles and the Armed Truck remain
status: verified
grounded_in:
  - source: live game screens on Zhen's Mac mini, session cc-665, 2026-11-11 20:43-20:48 PT
---

# Resource Collection — queue run 2048 (unit harvest-2026-11-11-1803)

- Unit: `harvest-2026-11-11-1803`, regular `harvest`, activity `resource-collection`
- Executor: ticker-2031; token re-acquired 20:41 PT, claimed about 20:41 PT; finished about 20:48 PT
- Session: cc-665; Last War window 676414 (windowed 642x951, not fullscreen); no drop, no "active on a different device" dialog, no access error
- Status: partial — food and one coin collection done; iron bubbles remain standing; the Armed Truck was not checked

## Entry state (base HUD, read live)

- Food 694.9M, iron 1.0G, coin 138.3M, diamonds 13.22K
- Total Power 149,218,973; stamina 55 (56 at close)
- The base view opened zoomed out with no bubbles visible; tapping the bottom-right BASE toggle recentred on the zoomed-in base, where the bubbles stand (same as unit 1740)

## Collections (HUD-verified)

| Tap | Result (HUD) |
| --- | --- |
| Food bubble, exact pointer tap at normalized 311,478 (snap off) | Food 694.9M → 697.1M (+2.2M); the farmland bubbles restarted at small figures at once, as the activity metadata says |
| Gold coin bubble at the left base edge, exact pointer tap at normalized 59,394 (snap off) | Coin 138.3M → 142.3M (+4.0M). The tap's own receipt reported no_change_observed, but the before/after HUD screenshots bracket only this tap, so the collection is verified by HUD |

- Final HUD: food **697.1M**, iron **1.0G**, coin **142.3M** (+2.2M food, +4.0M coin over the unit)

## Tap method - what worked and what did not

- A `visual_grounding` count call on the base screenshot timed out after 180 seconds and returned nothing; bubble grounding fell back to reading the screenshot directly. Do not spend a grounding call on the full base screen again - read the screenshot and tap by eye.
- Exact pointer taps (snap_to_control false) work first try on bubble centres, as in unit 1740.
- The coin tap's receipt said no_change_observed while the HUD moved +4.0M - receipts can miss a collection; always verify by the HUD before/after, not by the receipt alone.

## Not done

- Iron bubbles (blue circles over the upper base) remain standing - about 8 by unit 1740's count, not re-counted here; the next harvest unit collects them.
- The Armed Truck (blue truck, centre-right of the zoomed-in base) was not checked for fully-loaded state; its loot was not claimed. Ledger line 6 stays open - the truck is still unlocated as a claimable (issue #566).
- No building was upgraded, no survivor reassigned, nothing spent.

## Result stats

- target: all standing bubbles plus the Armed Truck check
- achieved: food bubbles collected (+2.2M); one coin bubble collected (+4.0M); iron bubbles remain; Armed Truck unchecked
- resources_gained: food +2.2M, coin +4.0M
- points: 0
- costs: about 7 minutes, no items spent
- verified: yes (the food and coin before/after figures are same-unit live HUD reads; remaining bubbles are reported as remaining, not as collected)
- blocker_category: h (by-design partial - the unit reached its 15 minute cap with iron bubbles still standing)
- bubbles_collected: food all (one tap), coin 1, iron 0
- food_before: 694900000 (HUD-rounded)
- food_after: 697100000 (HUD-rounded)
- iron_before: 1000000000 (HUD-rounded)
- iron_after: 1000000000 (HUD-rounded)
- coin_before: 138300000 (HUD-rounded)
- coin_after: 142300000 (HUD-rounded)
