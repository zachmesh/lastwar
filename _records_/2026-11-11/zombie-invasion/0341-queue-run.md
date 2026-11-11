---
title: Zombie Invasion queue run 0341
created: 2026-11-11T11:41:00Z
modified: 2026-11-11T11:52:00Z
version: 1.0.0
description: Ticker-0336 zombie-invasion unit 007, chain zombie-2026-11-10, 2 Lv.10 kills in parallel, 2 LOOT rows claimed 536,000 coins, Store Coin Chest (SSR) row identified in this variant, Owned 153
status: unverified
grounded_in:
  - source: live game screen on the owner Mac mini, 2026-11-11 03:41-03:52 PT
---

# Zombie Invasion — queue run 0341 (unit 007, chain zombie-2026-11-10)

- Unit: `zombie-invasion-zombie-2026-11-10-007`, chain `zombie-2026-11-10` seq 7
- Executor: ticker-0336; claimed about 11:41:41Z; finished about 03:52 PT
- Sessions: cc-551, cc-552, Last War window 636402
- Status: partial — chain continues, cleared false

## Event state (Glacieradon variant, read live)

- Event timer 2d 14:16:06 at about 03:52; "Challenge begins in: 1d 14:16:07"; "Your Timezone: 2026-11-12 18:00"
- Boss clue 40/40; next wave arrives in about 00:10:38 at the 03:52 read (about 04:02)
- Alliance Finding: Lv.85 Zombie Boss 109km (01:19:08), Lv.80 176km, Lv.80 182km, Lv.85 103km
- Wave live throughout the unit; zombies remained nearby at unit end

## Entry state (base HUD, read live)

- Food 667.1M, iron 989.8M, coin **118.5M** (coin_before, HUD-rounded), gold 13.22K, diamonds 6,307
- Total Power 149,218,973; stamina **82** at the base screen
- March Queues 0/4; no gift badge at entry

## Dispatches — parallel, squads_parallel 2

- First Search (tap at 360,945 on the event page) found a target and opened its card: **Invading Zombies Lv.10**, Suggested Power 670,000, cost 10 stamina, despawn 11:11:16. Guaranteed Reward medal x10, 1.3K, EXP 263.0K, iron 268.0K, food 268.0K. (No coin line on the card - coins sit in the LOOT row.)
- Deploy panel: Squad 1, 25.20M power, five Lv.150 heroes, Unit Count 2,231/2,231, vs 670.00K, Easy Win, march 00:02:51. March at 500,755 dispatched at once.
- Squad 1 marched at about 03:42 to **X:414 Y:324** (March Queues row read); stamina 82 to 72, March Queues 1/4.
- Second dispatch, R2 method (Events then Search, card confirmed on screenshot, then attack then March): Search found a second **Lv.10** card (despawn 10:10:10, same reward line). Deploy panel auto-selected Squad 2 (20.92M, Unit Count 2,175/2,175, Easy Win, march 00:03:51) - no squad-tab tap needed. March at 500,755 dispatched.
- Squad 2 marched at about 03:44 to **X:337 Y:420**; stamina 72 to 62, March Queues **2/4** - parallel dispatch ACHIEVED, the first cap-2 run in this chain since unit 052's cap-4 run on 2026-10-30.
- Session notes: one transient "target app exited or restarted" on the second Search tap - the app had not died (same pid 72047, window 636402); re-selected and continued with no state lost. Later the computer session dropped during a wait (observe returned observation_unavailable); session cc-552 started, window re-selected, no state lost.

## Claims - 2 LOOT rows, 536,000 coins

- Gift badge appeared at the right end of the March Queues bar with a red badge **1** while Squad 1 was Returning, then **2** once Squad 2 had also arrived. Gift box grounded fresh on the current screenshot at (311,226) and tapped - the LOOT panel opened while both squads were Returning.
- Rows read before Claim All:
  - Lv.10 Invading Zombies, X:337 Y:420, stamina +10, medal x10, green crate x1, iron 268.0K, food 268.0K, coin **268.0K**, hero EXP 263.0K
  - Lv.10 Invading Zombies, X:414 Y:324, stamina +10, medal x10, green box x4, iron 268.0K, food 268.0K, coin **268.0K**, hero EXP 263.0K
- Claim All (plain blue, no price tag) tapped at about 03:49; panel closed, badge cleared.
- Coin HUD verified: **118.5M to 119.0M** (+536K, HUD rounds to 0.1M); food 667.1M to 667.6M, iron 989.8M to 990.3M (each +536K within rounding).
- Row stamina +10 lines did NOT land on the HUD stamina: stamina read **63 before and after the claim** (second confirmation of the 0324 open question - the +10 is not observed landing; do not count it).

## Store - Coin Chest (SSR) row identified in this variant, medals 4060

- Store header read live: **medals 4060**. Carried balance before this unit was 4010 (unit 005's Store-header read, unverified since); the live 4060 is consistent with the 4000 baseline from unit 005 plus 6 kills at 10 medals each since (005's 3, 006's 1, this unit's 2) - the derived 4040 from the carried 4010 was wrong, as in units 043/047. Only a Store header read counts.
- Store first screen: gold chest x1 120 medals Limit 10; gold bar x1 80 Limit 10; gold bar x1 80 Limit 30; **50 Stamina x1 10 medals Limit 3** (available in this variant - the October event's was sold out at Limit 0); crate x1 160 Limit 50.
- Scrolled screen: crate x1 160 Limit 50; **gold-coins chest 160 medals Limit 100**; gold-coins chest 480 Limit 20; badge item x10 200 Limit 50; gear 200 Limit 50; Lv.3 chest below.
- Tooltip on the 160-medal Limit 100 row (gold-coins icon) read live: **Coin Chest (SSR), Owned: 153, "At the current Base Level, you can obtain 812.16K coins"**. This answers the open question from unit 001: the Coin Chest (SSR) row in the Glacieradon variant is the 160-medal Limit 100 row, same price and yield as October's corrected row. The 480-medal Limit 20 row's tooltip was NOT read (orange gold-coins icon; October's pattern says Coin Chest (UR), unverified in this variant).
- **Owned 153 is the discovery of this unit**: the account holds 153 Coin Chest (SSR) - about 124.3M coins at 812.16K each - unopened. Their inventory location is still unknown (October units 005/014 never pinned it down). No chest was opened this unit and no medal redemption was made; opening that stock is the successor/retro's call, filed as GitHub Issue #629 from this record.
- Store navigation note: the scroll action did not move the Store list; a drag from (500,700) to (500,350) scrolled it one screen. Use drag, not scroll, for this list.

## Stamina

- Stamina 82 at entry, 72 after the first march, 62 after the second, 63 at close (regen ticks). No Free Claim used (Remaining Today 1/2 from unit 006 still available); no 10/50 stamina item opened - stamina never bound this unit. Inventory stamina counts carried from unit 006 (10-stamina x647, 50-stamina x669, counted live then), not re-counted this unit.

## Not done this unit

- The 480-medal Limit 20 chest row's tooltip was not read; its name and yield in this variant stay open for the successor.
- No owned Coin Chest was opened (location unknown); the 153-owned stock is filed as an Issue from this record.
- Squad 2 was still Returning (00:02:36) at unit close; no third dispatch was attempted - the unit cap was reached at the Store tooltip read.

## Close

- Partial - cleared false: the wave is live, zombies remain nearby, next wave arrives about 04:02. Successor enqueued in the same chain (zombie-2026-11-10 seq 8) to start now.
- Duration: the unit ran about 10 minutes, inside the 15-minute cap. (An earlier draft of this record said 16 minutes from a misread clock; the live clock read 03:52 PT at the close tap, and the claim was 11:41:41Z - about 10 minutes. Corrected before the record was committed.)
- No diamonds or money spent. No priced button, Renew, paid unlock or Legendary Claim All tapped. No login or verification demanded. No "active on a different device" dialog appeared. The game was left on the Events hub (Zombie Invasion - Glacieradon page) with Squad 2 Returning.
- Queue hygiene in this pass: the live pool held three pending zombie units (006, 007, 008) - 006 was a stale duplicate of the branch-done 006 executed by ticker-0313 (its result lives in done/ on records/2026-11-11), and 008 was enqueued by this pass on a stale worktree-snapshot read that showed no zombie unit pending. Both were removed from the live pool inbox before execution; 007 was the legitimate pending successor and the unit executed here. The worktree snapshot's _queue_ (46 inbox) lags the live pool (72 inbox after sync); queue.py sync production and enqueue resolve to the live pool (issue #598), while next/claim/complete in a worktree read the snapshot - noted for the retro.

## Result stats

- zombies_killed: 2
- cleared: false
- coin_before: 118500000 (HUD-rounded)
- coin_after: 119000000 (HUD-rounded)
- coins_collected: 536000
- medals_before: 4010 (carried from unit 005 Store-header read, unverified)
- medals_after: 4060 (live Store header read)
- chests_opened: 0
- squads_parallel: 2
- target: kill wave zombies and claim LOOT
- achieved: 2 Lv.10 kills in parallel, 2 LOOT rows claimed (536,000 coins); Store Coin Chest (SSR) row identified (160 medals, Limit 100, Owned 153, 812.16K coins)
- resources_gained: coins 536000, iron 536000, food 536000, medals 20, hero EXP 526000
- points: 0
- costs: about 10 minutes, stamina 82 to 63 (two 10-cost marches, regen ticks)
- verified: coin HUD 118.5M to 119.0M, food and iron each plus 536K, both LOOT rows read before Claim All, Store header 4060 and SSR tooltip read live
- blocker_category: h
- tasks_badge: 1 at first sight, 2 after the second arrival, cleared after claim
- stamina_inventory_10: 647 (carried from unit 006, not re-read)
- stamina_inventory_50: 669 (carried from unit 006, not re-read)
- stamina_free_claim: 0 (not used; Remaining Today 1/2)
- device_takeovers: 0
