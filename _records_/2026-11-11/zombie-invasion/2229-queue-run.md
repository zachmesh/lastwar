---
title: Zombie Invasion queue run 2229
created: 2026-11-12T06:29:00Z
modified: 2026-11-12T06:29:00Z
version: 1.0.0
description: Queue unit 021, chain zombie-2026-11-10 - two parallel Lv.10 kills, both LOOT rows claimed, 536000 coins
status: verified
grounded_in:
  - source: live game screens on Zhen's Mac mini, sessions cc-673 and cc-676, 2026-11-11 22:14-22:29 PT
---

# Zombie Invasion — queue run 2229 (unit 021, chain zombie-2026-11-10)

- Unit: `zombie-invasion-zombie-2026-11-10-021`, chain `zombie-2026-11-10` seq 21
- Executor: ticker-2211; token acquired about 22:13 PT, claimed 22:14 PT; finished about 22:29 PT
- Session: cc-673, then cc-676 after the first session dropped near the end (same failure mode as unit 020's tail - "No active authorized computer session"); screen.snap kept working throughout and no state was lost; Last War window 676414 (windowed 642x951, not fullscreen); no "active on a different device" dialog, no access error
- Status: partial — chain continues, cleared false, both LOOT rows claimed in-unit

## Event state (Glacieradon variant, read live)

- Event timer 1d 19:42:10 at about 22:24; "Challenge begins in: 19:42:11"; "Your Timezone: 2026-11-12 18:00"
- Next wave of Invading Zombies in 00:36:50 at the 22:24 read (about 22:59 local); the wave attacked arrived about 21:53 (arms-race record 2147 read 00:05:58 out at 21:47)
- Alliance Finding: Lv.90 Zombie Boss 288km, Lv.85 46km, Lv.85 68km, Lv.100 65km
- 40/40 bar on the event page (unchanged from unit 020)

## Entry state (base HUD, read live)

- Food 697.1M, iron 1.0G, coin **142.3M** (coin_before, HUD-rounded), gold 13.22K, diamonds 6,717
- Total Power 149,218,973; stamina **25** at the first deploy-panel read
- Stamina note: unit 020 closed at stamina 49 (20:15 PT); this unit read 25 at 22:24 with no zombie unit in between. The 24-point drop is unexplained — no unit in this chain spent it, and the drop is recorded here as an open question, not assumed to be regen or another regular's spend.

## Dispatches — 2 Lv.10 kills, PARALLEL (squads_parallel 2)

- Kill 1 — Squad 1 → X:481 Y:397. Events (927,147) → Zombie page already on the Zombie Invasion tab (title "Zombie Invasion - Glacieradon" verified). Search (382,952) → card read live: Lv.10 Invading Zombies, Guaranteed Reward medal x10, book 1.3K, hero EXP 263.0K, iron 268.0K, food 268.0K; Potential Reward green crate x1, green box x4, gold ticket x1; Suggested Power 670,000, stamina cost 10, despawn 11:32:14. Crossed-swords (500,753); deploy panel Squad 1, five Lv.150 heroes, Unit Count 2,231/2,231, 25.20M vs 670.00K, Easy Win, stamina 25 shown with -10 cost. March (500,759) dispatched; March Queues 1/4, outbound 00:00:30; stamina 25 → 15.
- Kill 2 — Squad 2 → X:488 Y:392. Second dispatch started immediately while Squad 1 was out. Events reopened directly on the Zombie page. Search → second card at once (Lv.10, same rewards). Crossed-swords; deploy panel opened on **Squad 1 again** (25.20M, 2,231/2,231) — unlike unit 020, it did NOT auto-select Squad 2. Tapped the squad-2 tab (397,920) — panel switched to Squad 2, Unit Count 2,175/2,175. March dispatched; March Queues **2/4** — parallel dispatch achieved. Stamina 15 → 5.
- Both squads were out at once (2/4 verified on the map view). Squad 1 home first; Squad 2 Returning 00:00:26 at the 22:27 read, home by 22:28; March Queues 0/4 at close.

## Blind-batch misfire (first attempt, before the verified dispatches above)

- The first dispatch attempt batched Search → crossed-swords → March with no screenshot reads in between (the batched method the activity metadata prescribes). It misfired: the sequence ended on a "MISSING ITEMS" popup — Advanced Teleporter Owned: 0, offering Buy buttons (VIP Store 600 diamonds, Alliance Shop 7,500 contributions, Diamond Store 1,500 diamonds). No Buy button was tapped and no purchase was made; the popup was closed with its X and the unit restarted the dispatch step by step with a screenshot verification after each tap.
- Cause unproven: the batched clicks after Search landed on the map rather than on a target card, and one of them opened a tile action that prompted for a teleporter. The batched method worked for units 006/007/010/020 but failed here — the difference may be that Search's jump-to-target animation had not settled, or that the first Search found its target a beat later than the batch assumed. Lesson for the next unit: keep the Search → card verification read, then batch only swords → March once the deploy panel is confirmed open.
- No stamina was spent by the misfire (no march was dispatched; March Queues bar absent after the popup closed) and no game state was changed beyond the popup itself.

## Claims — 2 LOOT rows × 268,000 coins = 536,000

- Gift-box icon at the right end of the March Queues bar, grounded at (311,226) — badge read **2** and opened LOOT at once.
- The panel held TWO rows, one per kill — no missing row this unit (contrast unit 020, where Squad 1's row never materialized):
  - X:488 Y:392 (Squad 2), coin 268.0K, iron 268.0K, food 268.0K, medal x10, green box x4, EXP 263.0K
  - X:481 Y:397 (Squad 1), coin 268.0K, same rewards
- Claim All at (499,765) is plain blue, no price tag; panel closed on the tap.
- Coin HUD verified: **142.3M → 142.9M** (+536,000 by the two rows; HUD-rounded, so the 0.6M step is the rounding of 142.34M → 142.87M); food 697.1M → 697.6M (+536,000). Iron stayed 1.0G (rounded). Both squads home at close; no March Queues bar visible.
- Medals: before 5140 (unit 020's derived after, carried); after 5160 **derived** (+10 per kill), not live-read — Store not visited, flagged here, not a closing count.
- Stamina at close: 6 (25 − 20 spent + 1 regen; the +10 kill bonus seen in unit 020 did not appear this unit). No refill was done in-unit; the successor starts with 6 stamina and must Free Claim first, then open inventory 10/50 stamina items, before it can march. Inventory stamina count was not checked this unit — no exhaustion conclusion is drawn.

## Store

- Not visited this unit (unit cap reached at the claim). No medal balance re-read, no Coin Chest redemption, no medals spent.
- Chests opened: 0. The SSR chest row re-check and the Buy-step retry from units 047/052 stay open for the next unit, as does the below-fold Store scan from unit 017's follow-up.
- Medal balance is now about 5,160 derived — enough for 32 SR Coin Chests at 160 medals or 10 SSR at 480. The chest-redemption backlog grows while the Store stays unvisited; a coming unit should spend a slot on the Store before more kills.

## Notes

- Grounded points on the 642x951 windowed view this unit (normalized 0-1000 window coordinates): Events (927,147); Zombie tab (802,131) when the tab bar shows it there — the bar shifts between openings, verify the title every time; Search (382,952); crossed-swords (500,753); March (500,759); squad-2 tab (397,920); gift box (311,226); Claim All (499,765); popup X (849,131).
- The "active on a different device" dialog never appeared. The computer session dropped once mid-unit (cc-673 ended by itself); a fresh session (cc-676) resumed the same window with no state lost.
- Cleared is false — both Searches found targets immediately and the next wave arrives about 22:59; successor 022 enqueued to start now.

## Result stats

- zombies_killed: 2
- cleared: false
- coin_before: 142300000 (HUD-rounded)
- coin_after: 142900000 (HUD-rounded)
- coins_collected: 536000
- medals_before: 5140 (unit 020 derived after, carried)
- medals_after: 5160 (derived, not live-read — Store not visited)
- chests_opened: 0
- squads_parallel: 2
- target: kill wave zombies and claim LOOT
- achieved: 2 Lv.10 kills dispatched in parallel, both LOOT rows claimed (536000 coins)
- resources_gained: coins 536000, iron 536000, food 536000, medals 20, hero EXP 526000
- costs: about 15 minutes, stamina 25 to 6
- verified: yes (coin, food and stamina figures live-read; medals_after derived, flagged)
- blocker_category: h
- blocker: blind-batch-misfire-teleporter-popup
