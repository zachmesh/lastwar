---
title: Resource collection queue run 1623
created: 2026-11-10T00:23:00Z
modified: 2026-11-10T00:23:00Z
version: 1.0.0
description: Harvest sweep of the visible main base - iron plus 2.4M, coin plus 1.7M, food plus 2.6M HUD-verified, one tap per type clears all visible of that type, far-left edge bubble and Armed Truck check carried
status: partial
grounded_in:
  - source: live game screen on the owner Mac mini, 2026-11-09 16:14-16:23 PT
---

# Resource collection queue run 1623 (ticker-1534)

Unit: harvest-2026-11-09-1403. Status: partial.
Activity: resource-collection. Chain: none.
Window: sweep the visible main base, one tap per resource type.
Computer session cc-312. Nothing bought, no building panel
action taken, no speedup used. The device token lease expired
at 16:16 during the unit (taken 16:01, 15-minute lease); no
other pass runs before the 16:34 tick, so no contention arose
and the unit finished inside the pass budget.

## Live reads

- Entry HUD about 16:15: food 554.0M, iron 879.2M, coin 51.9M,
  13.22K, stamina 82, cart 6,137, power 149,217,331, VS timer
  01:45:44, Season II 6d 01:45:44. Game left on the base screen
  by the preceding scout unit.
- Bubble grounding, visual grounding tool on the live
  screenshot: 5 green bubbles (166,324), (231,353), (164,388),
  (231,413), (299,386); 8 yellow coin bubbles (93,418),
  (157,446), (84,483), (152,500), (226,496), (148,533),
  (221,550), (149,571). Centres grounded, then tapped - never
  estimated.
- Tap 1, green bubble (166,324): iron 879.2M to 881.6M, plus
  2.4M HUD-verified; food and coin unchanged. The tapped
  bubble was iron, not food - bubble-type identification from
  the downscaled screenshot is unreliable, as rule R2 warns.
  All 5 grounded green bubbles cleared from the top-left
  cluster. Their visible values summed about 1.78M against the
  2.4M HUD delta, so the delta again exceeds the visible sum,
  consistent with the Issue #502 base-wide-collection
  candidate, not proven.
- Tap 2, yellow coin bubble (93,418): coin 51.9M to 53.6M,
  plus 1.7M HUD-verified; food and iron unchanged. All 8
  grounded coin bubbles cleared at once - one tap per type
  clears all visible bubbles of that type, re-confirming the
  0340 finding for coin.
- Tap 3, centre food bubble (371,394): food 554.0M to 556.6M,
  plus 2.6M HUD-verified; iron and coin unchanged. All 4
  visible centre food bubbles cleared at once.
- Closing HUD about 16:22: food 556.6M, iron 881.6M, coin
  53.6M, stamina 83, cart 6,137, VS timer 01:39:43, Season II
  6d 01:39:44. No bubbles remain in the centred main-base
  view.
- Skull timer, Issue #498, further datapoints this unit:
  badge 3 with 00:00:25 at about 16:15, badge 3 with 00:00:29
  at about 16:18, badge 1 with 00:00:50 at about 16:20, badge
  3 with 00:00:37 at about 16:22. The timer re-arms
  repeatedly with a fresh countdown in the tens of seconds
  and the badge does not count down monotonically (1, 2, 3,
  1, 3 across the two units) - the sequence is recorded as
  observed, not explained. The next scout unit should tap it
  while its timer is live.
- Unverified toast fragment: at about 16:20 a toast ending
  "...lly loa..." appeared at the bottom left and vanished
  before it could be read in full. Possibly truck-related;
  recorded as unverified, not claimed.

## Remainder, carried

- One green 308.8K bubble at the far left edge, half
  off-frame, still standing after the food tap - either a
  different type (EXP candidate) or outside the per-type
  clear. Not tapped: the 2006 rule bars tapping an
  ambiguous half-off-frame edge shape.
- Armed Truck loot: no collectable loot bubble seen over the
  parked vehicles in any view this unit; the loot-panel entry
  remains unlocated (standing). The truck toast fragment
  above is unverified.
- The Season 2 area at the bottom was left out of the sweep,
  per the standing rule that it is not main-base harvest.
- The full-map zero-remaining acceptance is not met (edge
  bubble outstanding), so the tracker is untouched and the
  regular stays due.

## Result statistics

- bubbles_cleared: 17 visible (5 iron, 8 coin, 4 food)
- food_gained_m: 2.6
- iron_gained_m: 2.4
- coin_gained_m: 1.7
- resources_gained: food 2.6M, iron 2.4M, coin 1.7M HUD-verified
