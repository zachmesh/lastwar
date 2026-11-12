---
title: Zombie Invasion queue run 2020
created: 2026-11-12T04:22:00Z
modified: 2026-11-12T04:22:00Z
version: 1.0.0
description: Queue unit 020, chain zombie-2026-11-10 - two parallel Lv.10 kills, one LOOT row claimed, one row missing
status: verified
grounded_in:
  - source: live game screens on Zhen's Mac mini, session cc-662, 2026-11-11 20:04-20:21 PT
---

# Zombie Invasion — queue run 2020 (unit 020, chain zombie-2026-11-10)

- Unit: `zombie-invasion-zombie-2026-11-10-020`, chain `zombie-2026-11-10` seq 20
- Executor: ticker-2001; token acquired about 20:03 PT, claimed 20:04 PT; finished about 20:21 PT
- Session: cc-662; one wait call failed near the end ("No active authorized computer session is available for evidence"), recovered by screen.snap with no state lost; Last War window 676414 (windowed 642x951, not fullscreen); no "active on a different device" dialog, no access error
- Status: partial — chain continues, cleared false, one LOOT row claimed in-unit, one row missing

## Event state (Glacieradon variant, read live)

- Event timer 1d 21:53:31 at about 20:08; "Challenge begins in: 21:53:32"; "Your Timezone: 2026-11-12 18:00"
- Next wave of Invading Zombies in 00:48:11 at the 20:08 read (about 20:56 local)
- Alliance Finding: Lv.80 Zombie Boss 294km, Lv.85 208km, Lv.85 209km, Lv.80 210km
- 40/40 bar on the event page (unchanged from unit 019)

## Entry state (base HUD, read live)

- Food 694.6M, iron 1.0G, coin **138.0M** (coin_before, HUD-rounded), gold 13.22K, diamonds 6,717
- Total Power 149,218,973; stamina **58**

## Dispatches — 2 Lv.10 kills, PARALLEL (squads_parallel 2)

- Kill 1 — Squad 1 → X:443 Y:436. Events (927,147) → Zombie Invasion tab (311,134), page title "Zombie Invasion - Glacieradon" verified before Search (the tab bar shifts between openings, as units 011/048/057 warned). Search (385,941) → card read live: Lv.10 Invading Zombies, Guaranteed Reward medal x10, book 1.3K, hero EXP 263.0K, iron 268.0K, food 268.0K; Potential Reward green crate x1, green box x4, gold ticket x1; Suggested Power 670,000, stamina cost 10, despawn 11:47:40. Crossed-swords (500,753); deploy panel Squad 1, five Lv.150 heroes, Unit Count 2,231/2,231, 25.20M vs 670.00K, Easy Win, march 00:01. March (500,759) dispatched; stamina 58 → 48, March Queues 1/4, outbound 00:00:54.
- Kill 2 — Squad 2 → X:505 Y:383. Second dispatch started immediately while Squad 1 was out. Events reopened directly on the Zombie page this time. Search → second card at once (Lv.10, same rewards, despawn 11:46:11). Crossed-swords (500,753); deploy panel auto-selected Squad 2 (Unit Count 2,175/2,175, 21.02M vs 670.00K, Easy Win) — no squad-tab tap needed, as unit 024 found. March (500,759) dispatched; March Queues **2/4** — parallel dispatch achieved. The deploy panel read stamina 58 before this March (48 after Squad 1's march, then +10 — the unexplained plus-10 stamina read after a kill, also seen in round 1 and unit 001); 48 after, 49 at close (+1 regen).
- Short round trips again: Squad 1 was already Returning 00:00:10 by the 20:16 read while Squad 2 was still outbound (00:00:43), so the parallel window was brief but real — both squads were out at once (2/4 verified).

## Claims — 1 LOOT row × 268,000 coins = 268,000; 1 row missing

- Gift-box icon at the right end of the March Queues bar, grounded fresh at (311,226) on this map view — badge read 1 and opened LOOT at once.
- The panel held only ONE row: X:505 Y:383 (Squad 2's kill), coin 268.0K. Squad 1's row (X:443 Y:436) never materialized — the third handover-style loss in this chain after units 009 and 048 (a completed march whose row never appears). Its 268,000 coins plus the iron/food/EXP on that row are unrecovered; the successor must re-check the badge, but unit 049 already proved a missing row does not reappear later.
- Claim All at (499,765) is plain blue, no price tag; panel closed on the tap.
- Coin HUD verified: **138.0M → 138.3M** (+268,000 by the row); food 694.6M → 694.9M (+268,000). Iron stayed 1.0G (rounded). Both squads home at close; no March Queues bar visible.
- Medals: before 5120 (unit 019's derived after, carried); after 5140 **derived** (+10 per kill), not live-read — Store not visited, flagged here, not a closing count.

## Store

- Not visited this unit (unit cap reached at the claim). No medal balance re-read, no Coin Chest redemption, no medals spent.
- Chests opened: 0. The SSR chest row re-check and the Buy-step retry from units 047/052 stay open for the next unit, as does the below-fold Store scan from unit 017's follow-up.
- Stamina 49 at close (58 − 20 spent + 10 kill bonus + 1 regen); no refill needed; inventory stamina count not checked, no refill conclusion drawn.

## Notes

- Grounded points on the 642x951 windowed view this unit: Events (927,147); Zombie tab (311,134); Search (385,941); crossed-swords (500,753); March (500,759); gift box (311,226); Claim All (499,765).
- Cleared is false — both Searches found targets immediately and the next wave arrives about 20:56; successor 021 enqueued to start now.

## Result stats

- zombies_killed: 2
- cleared: false
- coin_before: 138000000 (HUD-rounded)
- coin_after: 138300000 (HUD-rounded)
- coins_collected: 268000
- medals_before: 5120 (unit 019 derived after, carried)
- medals_after: 5140 (derived, not live-read — Store not visited)
- chests_opened: 0
- squads_parallel: 2
- target: kill wave zombies and claim LOOT
- achieved: 2 Lv.10 kills dispatched in parallel, 1 LOOT row claimed (268000 coins)
- resources_gained: coins 268000, iron 268000, food 268000, medals 20, hero EXP 263000
- costs: about 17 minutes, stamina 58 to 49
- verified: yes (coin, food and stamina figures live-read; medals_after derived, flagged)
- blocker_category: h
- blocker: missing-loot-row-squad-1
