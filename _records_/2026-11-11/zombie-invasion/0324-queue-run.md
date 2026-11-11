---
title: Zombie Invasion queue run 0324
created: 2026-11-11T11:24:00Z
modified: 2026-11-11T11:24:00Z
version: 1.0.0
description: Ticker-0313 zombie-invasion unit 006, chain zombie-2026-11-10, 1 Lv.10 kill X:414 Y:344, 1 LOOT row claimed 268,000 coins, parallel dispatch failed on a mistargeted batch, cleared false
status: unverified
grounded_in:
  - source: live game screen on the owner Mac mini, 2026-11-11 03:24-03:30 PT
---

# Zombie Invasion — queue run 0324 (unit 006, chain zombie-2026-11-10)

- Unit: `zombie-invasion-zombie-2026-11-10-006`, chain `zombie-2026-11-10` seq 6
- Executor: ticker-0313; claimed 11:23:45Z; finished about 03:30 PT
- Session: cc-550, Last War window 636402 (session cc-549 ended mid-pass with a transient stale_observation; re-started as cc-550, no game state lost)
- Status: partial — chain continues, cleared false

## Event state (Glacieradon variant, read live)

- Event timer 2d 14:35:04 at about 03:27; "Challenge begins in: 1d 14:35:05"; "Your Timezone: 2026-11-12 18:00"
- Boss clue 40/40; next wave arrives in about 00:29:36 at the 03:27 read
- Alliance Finding: Lv.85 Zombie Boss 109km (01:38:06, OatmealDragon), Lv.80 176km, Lv.80 182km, Lv.85 103km (01:58:55)
- Wave live throughout the unit; zombies remained nearby at unit end

## Entry state (base HUD, read live)

- Food 666.8M, iron 989.5M, coin **118.2M** (coin_before, HUD-rounded), gold 13.22K, diamonds 6,307
- Total Power 149,218,973; stamina **13** at the base screen (4 at the 005 close, slow regen plus the 005 kill-drop pattern)

## Dispatches — Squad 1 only (squads_parallel 1)

- Search (second tap, re-grounded at (382,942)) found a target and opened its card: **Invading Zombies Lv.10**, Suggested Power 670,000, cost 10 stamina, despawn 11:28:59. Guaranteed Reward medal x10, 1.3K, EXP 263.0K, iron 268.0K, food 268.0K. (No coin line on the card - coins sit in the LOOT row.)
- Deploy panel: Squad 1, 25.20M power, five Lv.150 heroes, Unit Count 2,231/2,231, vs 670.00K, Easy Win. March button showed 00:02:29.
- Squad 1 marched at about 03:28 to **X:414 Y:344** (March Queues row read); stamina 14 to 4 on the march (stamina read 14 in the deploy panel, 13 on the base HUD just before - regen between reads).
- March Queues 1/4 after the march. The squad arrived about 03:29 and returned on the 00:02:29 leg; Returning with 00:01:44 left at unit end.

## Parallel dispatch failure - the batched second dispatch mistargeted

- After Squad 1 marched, stamina 4 was short of the 10 for a second march. Free Claim taken first (see below), stamina 4 to 79.
- The second dispatch was batched as one action batch (Events, Search, attack, March - no reads in between, per the units 006/007 standard). All 4 clicks reported dispatched in 3.2s, but the end state was a **Lv.23 Ironhead** card (Suggested Power 1,430,500, despawn 14:25:24), not a Lv.10 deploy panel - the Search/attack taps landed on a world-map elite tile instead of the event target, and no second squad marched (March Queues stayed 1/4, stamina stayed 79).
- The batch ran too fast for the Events hub to load before the Search tap fired (the first Search tap of this unit also failed once and needed a re-grounded re-tap). Per rule R2 the next unit changes the method: batch only Events then Search, confirm the Lv.10 card on a screenshot, then batch attack then March. The Ironhead was NOT attacked (not the event target, rewards 61.0K iron against the Lv.10's 268.0K plus medals and coins).
- squads_parallel 1 for this unit, for the stated reason - not a game cap (march queue cap is 4).

## Stamina - Free Claim taken, inventory counted

- REGAIN STAMINA panel (lightning icon): stamina **4/120**, restores 1 per 300s, fully replenished in 09:38:40.
- **75 Stamina Free Claim tapped** (green Claim, cooldown 4 hr, Remaining Today 1/2): toast "you've acquired 75 Stamina x1", stamina 4 to 79. The 100 Stamina Buy 300 (diamond) row was not touched.
- Inventory stamina items counted live in the same panel: **10 Stamina Owned 647** (x12 batch button), **50 Stamina Owned 669** (x3 batch button). No 10/50 item was opened this unit - the Free Claim covered the need, and no second march happened to spend it.
- Stamina at unit end: **79**.

## Claims - 1 LOOT row, 268,000 coins

- The gift box appeared at the right end of the March Queues bar with a red badge **1** while Squad 1 was Returning. First tap at (296,250) missed and opened a Teleport/Profession tile menu (the 2219 mistap shape); re-grounded fresh at **(332,228)** and tapped - the LOOT panel opened while the squad was still returning, so the row was saved (the 005 mitigation).
- Row: Lv.10 Invading Zombies, X:414 Y:344, **stamina +10**, medal x10, green box x4, iron 268.0K, food 268.0K, coin 268.0K, hero EXP 263.0K.
- Claim All (plain blue, no price tag) tapped at about 03:38; "Gifts Received" toast; badge cleared.
- Coin HUD verified: **118.2M to 118.5M** (+268K, HUD rounds to 0.1M); food 666.8M to 667.1M, iron 989.5M to 989.8M (each +268K within rounding).
- Open question for the successor/retro: the row carried a **stamina +10** line, but the HUD stamina read **79 before and after the claim** - the +10 was not observed landing. It may apply at the squad's return, to another pool, or on a delay. Do not count it until a live read shows it.

## Not done this unit

- Store not visited: medals after not read live (medals_before 4010 from the 005 Store-header read; this kill pays medal x10, so 4020 is expected but NOT verified - no arithmetic figure is claimed). No Coin Chest row established in this variant yet (005 found the 160-medal row is Iron Chest SSR); the successor checks the Store.
- No second kill: Squad 2 never marched (batch mistarget above). One Lv.10 target remains the wave's supply; next wave in about 00:25 at unit end.
- The 005 unit's lost Squad 1 row was not recoverable - no late row appeared; the badge showed 1 only for this unit's kill.

## Close

- Partial - cleared false: the wave is live, zombies remain nearby, Squad 1 is still returning. Successor enqueued in the same chain (zombie-2026-11-10 seq 7) to start now.
- No diamonds or money spent. No priced button, Renew, paid unlock or Legendary Claim All tapped. No login or verification demanded. No "active on a different device" dialog appeared. The game was left on the world map with Squad 1 Returning.
- No "active on a different device" dialog appeared at any point in this pass. One transient stale_observation ended session cc-549; session cc-550 re-selected the same window with no state lost.

## Result stats

- zombies_killed: 1
- cleared: false
- coin_before: 118200000 (HUD-rounded)
- coin_after: 118500000 (HUD-rounded)
- coins_collected: 268000
- medals_before: 4010
- medals_after: unverified (Store not visited; 4020 expected from 4010 plus 10, not claimed)
- chests_opened: 0
- squads_parallel: 1
- target: kill wave zombies and claim LOOT
- achieved: 1 kill, 1 LOOT row claimed (268,000 coins)
- resources_gained: coins 268000, iron 268000, food 268000, medals 10, hero EXP 263000
- points: 0
- costs: about 6 minutes, stamina 13 to 79 (Free Claim plus 75, march minus 10, kill-drop plus 10 unverified)
- verified: coin HUD 118.2M to 118.5M, food and iron each plus 268K
- blocker_category: c
- tasks_badge: 1 at first sight, cleared after claim
- stamina_inventory_10: 647
- stamina_inventory_50: 669
- stamina_free_claim: 75
- device_takeovers: 0
