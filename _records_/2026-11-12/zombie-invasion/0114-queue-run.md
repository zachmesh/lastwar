---
title: Zombie Invasion queue run 0114
created: 2026-11-12T09:14:53Z
modified: 2026-11-12T09:14:53Z
version: 1.0.0
executor: ticker-0100
unit: zombie-invasion-zombie-2026-11-10-022
status: partial
---

# Zombie Invasion queue run 0114

Session 01:06-01:15 PST (ticker-0100, unit 022, chain zombie-2026-11-10).
Event verified live on entry: Zombie Invasion - Glacieradon, 1d 16:52:42 left,
challenge begins 2026-11-12 18:00, boss clue counter 40/40, next wave in
00:47:23 at first read.

## What was done

- Closed the leftover player-profile popup from the previous unit
  ([AP3x]Jerry) via the back-to-base button; one mis-tap on the dense map
  opened [AP3x]XualHarrassment's profile instead (Power 104,637,301) and
  was closed the same way. No state lost.
- Coin before 143.4M HUD, stamina before 68 (read live on the base screen).
- Dispatch 1: Lv.10 Invading Zombies at X:489 Y:441, Suggested Power
  670,000, stamina cost 10, despawn 11:46:39. Deploy panel Squad 1,
  25.20M vs 670.00K, Easy Win, Unit Count 2,231/2,231. March verified:
  March Queues 1/4, stamina 68 to 58.
- Dispatch 2 (parallel attempt): Events back to the Glacieradon page
  (title verified), Search found a second Lv.10 at X:504 Y:410, deploy
  panel again Squad 1 (tab 1 selected, no red X) with stamina read 69
  before March - Squad 1 had already killed and returned from the first
  target during the navigation, so the second dispatch was sequential,
  not parallel. March verified: March Queues 1/4, stamina 69 to 59.
- squads_parallel 1. Binding limit: Squad 1's round trip (about 35-50
  seconds) completed during the Events/Search navigation for the second
  dispatch - short round trips, not the march cap of 4. Same binding
  limit as units 043, 049 and 1834.
- LOOT: gift-box badge read 1 before tapping. Panel held exactly one
  row - the X:504 Y:410 kill (medal x10, green crate x1, iron 268.0K,
  food 268.0K, coin 268.0K, EXP 263.0K). Claim All (plain blue, no
  price tag) tapped; coin HUD verified 143.4M to 143.7M after the
  claim, food 698.1M to 698.4M.
- LOOT HANDOVER LOSS (fourth in this chain, after units 009, 048 and
  020): the X:489 Y:441 kill's row never materialized. The kill itself
  is proven by the stamina +10 bonus (58 to 68, plus 1 regen tick to
  69) read live before the second March, and no gift badge was visible
  for it at any check. Its 268,000 coins plus iron/food/EXP/medal are
  unrecovered. Retro action A-2026-11-11-04 (Issue #642) says to claim
  each row before the next kill; this row was never claimable because
  it never appeared - the successor should re-check the badge on
  entry, since a late row would be claimed then.
- Store not visited this unit (unit cap reached at the loot claim), so
  no live medal balance and no Coin Chest redemption. Medals +20 by
  row evidence (2 kills x 10), balance unmeasured.
- Stamina after 59. No stamina item opened (stamina never bound).
- Cleared false: next wave in about 00:45 at close, zombies remain.
  Successor 025 enqueued to start now.

## Result stats

- zombies_killed: 2 (Lv.10, X:489 Y:441 and X:504 Y:410)
- cleared: false
- coin_before: 143.4M HUD
- coin_after: 143.7M HUD
- coins_collected: 268000
- medals_before: unmeasured
- medals_after: unmeasured (plus 20 by row evidence)
- chests_opened: 0
- squads_parallel: 1 (short round trips, not the march cap)
- tasks_badge: 1
- stamina_before: 68
- stamina_after: 59
- target: 2 kills and all LOOT rows claimed
- achieved: 2 kills, 1 of 2 LOOT rows claimed
- resources_gained: coin 268000, iron 268000, food 268000, EXP 263000, medals 20, green crate 1
- costs: 20 stamina, about 12 minutes
- verified: yes
- blocker_category: h (by-design partial, chain continues; the missing LOOT row is a handover loss, fourth in this chain)
