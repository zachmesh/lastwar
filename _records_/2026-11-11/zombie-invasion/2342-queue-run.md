---
title: Zombie Invasion queue run 2342
created: 2026-11-12T07:42:00Z
modified: 2026-11-12T07:42:00Z
version: 1.0.0
description: Queue unit 022, chain zombie-2026-11-10 - two parallel Lv.10 kills, both LOOT rows claimed, 536000 coins
status: verified
grounded_in:
  - source: live game screens on Zhen's Mac mini, session cc-679, 2026-11-11 23:34-23:42 PT
---

# Zombie Invasion — queue run 2342 (unit 022, chain zombie-2026-11-10)

- Unit: `zombie-invasion-zombie-2026-11-10-022`, chain `zombie-2026-11-10` seq 22
- Executor: ticker-2333; token acquired about 23:34 PT, claimed 23:34 PT; finished about 23:42 PT
- Session: cc-679, single session, no drop; Last War window 676414 (windowed 642x951, not fullscreen); no "active on a different device" dialog, no access error
- Status: partial — chain continues, cleared false, both LOOT rows claimed in-unit

## Event state (Glacieradon variant, read live)

- Event timer 1d 18:24:08 at about 23:38; "Challenge begins in: 18:24:09"; "Your Timezone: 2026-11-12 18:00"
- Next wave of Invading Zombies in 00:18:49 at the 23:38 read (about 23:57 local); the wave that arrived about 22:59 still had targets — both Searches found Lv.10 cards at once
- Alliance Finding: Lv.80 Zombie Boss 376km, Lv.85 407km, Lv.80 421km, Lv.80 323km
- 40/40 bar (unchanged from unit 021)

## Entry state (base HUD, read live)

- Food 697.6M, iron 1.0G, coin **142.9M** (coin_before, HUD-rounded), gold 13.22K, diamonds 6,717
- Total Power 149,218,973; stamina **20** at entry (unit 021 closed at 6 at 22:29; +14 over about 67 minutes, about 1 per 5 minutes regen)
- Stamina note: the exact coin panel was not opened this unit; coin figures are HUD-rounded like unit 021

## Dispatches — 2 Lv.10 kills, PARALLEL (squads_parallel 2)

- Kill 1 — Squad 1 → X:410 Y:347. Events (927,147) → Zombie page title verified. Search (382,952) → card read live: Lv.10 Invading Zombies, Guaranteed Reward medal x10, book 1.3K, hero EXP 263.0K, iron 268.0K, food 268.0K; Potential Reward green crate x1, green box x4, gold ticket x1; Suggested Power 670,000, stamina cost 10, despawn 10:18:16. Crossed-swords (500,753); deploy panel Squad 1, five Lv.150 heroes, Unit Count 2,231/2,231, Easy Win. March (500,759) dispatched; March Queues 1/4, outbound 00:02:22; stamina 20 → 10.
- Kill 2 — Squad 2 → X:607 Y:426. Second dispatch started immediately while Squad 1 was out. Events reopened directly on the Zombie page (title verified). Search (382,952) → second card at once (Lv.10, same rewards). Crossed-swords; deploy panel had already auto-selected Squad 2, Unit Count 2,175/2,175, Easy Win — no squad-tab tap needed. March dispatched; March Queues **2/4** — parallel dispatch achieved. Stamina 10 → 0.
- Both squads were out at once (2/4 verified on the map view). Squad 1 arrived first and went Returning 00:01:44; Squad 2 arrived about 2 minutes later and went Returning 00:02:32. Squad 1 was home by close; Squad 2 still Returning 00:01:54 at close, returns on its own.

## Claims — 2 LOOT rows × 268,000 coins = 536,000

- Gift-box icon at the right end of the March Queues bar, re-grounded at (308,237) on the live map view — badge read **1** for each kill and opened LOOT at once.
- Row 1 — X:410 Y:347 (Squad 1), coin 268.0K, iron 268.0K, food 268.0K, medal x10, green box x4, EXP 263.0K. Claim All at (499,765) plain blue, no price tag. Coin HUD verified: **142.9M → 143.1M**; food 697.6M → 697.9M.
- Row 2 — X:607 Y:426 (Squad 2), coin 268.0K, same rewards. Claim All at (499,765). Coin HUD verified: **143.1M → 143.4M**; food 697.9M → 698.1M. Total claimed in-unit 536,000 coins.
- Medals: before 5160 (unit 021's derived after, carried); after 5180 **derived** (+10 per kill), not live-read — Store not visited, flagged here, not a closing count.
- Stamina at close: 1 (0 after the marches + 1 regen). No refill was done in-unit; the successor starts with about 1 stamina and must Free Claim first, then open inventory 10/50 stamina items, before it can march. Inventory stamina count was not checked this unit — no exhaustion conclusion is drawn.

## Store

- Not visited this unit (unit cap reached at the second claim). No medal balance re-read, no Coin Chest redemption, no medals spent.
- Chests opened: 0. The SSR chest row re-check and the Buy-step retry from units 047/052 stay open for the next unit, as does the below-fold Store scan from unit 017's follow-up.
- Medal balance is now about 5,180 derived — enough for 32 SR Coin Chests at 160 medals or 10 SSR at 480. The chest-redemption backlog grows while the Store stays unvisited; a coming unit should spend a slot on the Store before more kills.

## Notes

- Grounded points on the 642x951 windowed view this unit (normalized 0-1000 window coordinates): Events (927,147); Search (382,952); crossed-swords (500,753); March (500,759); gift box (308,237) on this map view — re-ground it on the live screenshot every time, the bar moves with the map; Claim All (499,765).
- The Search → card verification read, then swords → March once the deploy panel is confirmed open, worked cleanly for both kills — no teleporter-popup misfire this unit (contrast unit 021's blind batch).
- Cleared is false — both Searches found targets immediately and the next wave arrives about 23:57; successor 023 enqueued to start now.

## Result stats

- zombies_killed: 2
- cleared: false
- coin_before: 142900000 (HUD-rounded)
- coin_after: 143400000 (HUD-rounded)
- coins_collected: 536000
- medals_before: 5160 (unit 021 derived after, carried)
- medals_after: 5180 (derived, not live-read — Store not visited)
- chests_opened: 0
- squads_parallel: 2
- target: kill wave zombies and claim LOOT
- achieved: 2 Lv.10 kills dispatched in parallel, both LOOT rows claimed (536000 coins)
- resources_gained: coins 536000, iron 536000, food 536000, medals 20, hero EXP 526000
- costs: about 8 minutes, stamina 20 to 1
- verified: yes (coin, food and stamina figures live-read; medals_after derived, flagged)
- blocker_category: h
- blocker: none — Store redemption backlog (standing open item, not a blocker this unit)
