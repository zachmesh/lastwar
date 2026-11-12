---
title: Zombie Invasion queue run 1936
created: 2026-11-12T03:36:00Z
modified: 2026-11-12T03:36:00Z
version: 1.0.0
description: Queue unit 019, chain zombie-2026-11-10 - two parallel Lv.10 kills, both LOOT rows claimed
status: verified
grounded_in:
  - source: live game screens on Zhen's Mac mini, session cc-658 and cc-659, 2026-11-11 19:21-19:36 PT
---

# Zombie Invasion — queue run 1936 (unit 019, chain zombie-2026-11-10)

- Unit: `zombie-invasion-zombie-2026-11-10-019`, chain `zombie-2026-11-10` seq 19
- Executor: ticker-1919; token acquired 19:19 PT, claimed about 19:20 PT; finished about 19:36 PT
- Sessions: cc-658, then cc-659 after cc-658 dropped mid-unit during a wait (observe returned observation_unavailable, no session open); Last War window 676414 (windowed 642x951, not fullscreen); no game state lost, no "active on a different device" dialog, no access error
- Status: partial — chain continues, cleared false, both kills claimed in-unit

## Event state (Glacieradon variant, read live)

- Event timer 1d 22:35:44 at about 19:24; "Challenge begins in: 22:35:45"; "Your Timezone: 2026-11-12 18:00"
- Next wave of Invading Zombies in 00:30:23 at the 19:24 read (about 19:54 local)
- Alliance Finding: Lv.80 Zombie Boss 138km, Lv.80 294km, Lv.85 208km, Lv.80 212km
- 40/40 bar on the event page (unchanged from unit 018)

## Entry state (base HUD, read live)

- Food 694.1M, iron 1.0G, coin **137.5M** (coin_before, HUD-rounded), gold 13.22K, diamonds 6,717
- Total Power 149,218,973; stamina **69** (70 at first deploy-panel read, +1 regen)

## Dispatches — 2 Lv.10 kills, PARALLEL (squads_parallel 2)

- Kill 1 — Squad 1 → X:505 Y:325. Events (942,115) → first tap landed on Arms Race (tab bar shifts between openings — the normalized tap (560,125) hit the wrong tab; re-grounded the Zombie tab at (870,131) and verified the page title "Zombie Invasion - Glacieradon" before Search). Search (375,936) → card read live: Lv.10 Invading Zombies, Guaranteed Reward medal x10, book 1.3K, hero EXP 263.0K, iron 268.0K, food 268.0K; Potential Reward green crate x1, green box x4, gold ticket x1; Suggested Power 670,000, stamina cost 10, despawn 11:29:48. Crossed-swords (490,752); deploy panel Squad 1, five Lv.150 heroes, Unit Count 2,231/2,231, 25.20M vs 670.00K, Easy Win. March (500,758) dispatched; stamina 70 → 60, March Queues 1/4, outbound 00:02:12.
- Kill 2 — Squad 2 → X:569 Y:369. Second dispatch started immediately while Squad 1 was out (outbound 2:12 left room). Events reopened directly on the Zombie page this time (tab bar shifted again — Zombie tab centred at top). Search → second card at once (Lv.10, Suggested Power 670,000). Crossed-swords (490,752); deploy panel auto-selected Squad 2 (Unit Count 2,175/2,175, Easy Win, march 00:02:38) — no squad-tab tap needed, as unit 024 found. March (500,758) dispatched; stamina 60 → 50, March Queues **2/4** — first parallel dispatch at 2 in this chain since unit 047.
- The longer outbound times on this wave (2:12 and 2:38, targets 100km out) are what made parallelism possible; short round trips were the binding limit in units 018, 043 and 049.

## Claims — 2 LOOT rows × 268,000 coins = 536,000

- Rows: X:505 Y:325 (claimed after arrival, badge 1), X:569 Y:369 (claimed after arrival, badge 1).
- Gift-box icon at the right end of the March Queues bar, grounded fresh at (311,221) on this map view — badge read 1 both times and opened LOOT at once both times. Claim All at (499,765) and (499,783) is plain blue, no price tag; panel closed on the tap.
- Coin HUD verified: **137.5M → 137.8M** after the first row, **137.8M → 138.0M** after the second (+0.3M displayed per row, 268,000 by the row); food 694.1M → 694.4M → 694.6M (+268,000 per row). Gift badge gone after claiming. Both squads Returning at close (Squad 1 00:00:12, Squad 2 00:01:23 in the final read).
- Medals: before 5100 (unit 018's derived after, carried); after 5120 **derived** (+10 per kill), not live-read — Store not visited, flagged here, not a closing count.

## Store

- Not visited this unit (unit cap reached at the second claim). No medal balance re-read, no Coin Chest redemption, no medals spent.
- Chests opened: 0. The SSR chest row re-check and the Buy-step retry from units 047/052 stay open for the next unit, as does the below-fold Store scan from unit 017's follow-up.
- Stamina 51 at close (70 − 20 spent + 1 regen); no refill needed; inventory stamina count not checked, no refill conclusion drawn.

## Notes

- Grounded points on the 642x951 windowed view this unit: Events (942,115); Zombie tab (870,131) on the shifted bar — re-ground per opening, never reuse; Search (375,936); crossed-swords (490,752); March (500,758); gift box (311,221); Claim All (499,765).
- Cleared is false — both Searches found targets immediately and the next wave arrives about 19:54; successor 020 enqueued to start now.

## Result stats

- zombies_killed: 2
- cleared: false
- coin_before: 137500000 (HUD-rounded)
- coin_after: 138000000 (HUD-rounded)
- coins_collected: 536000
- medals_before: 5100 (unit 018 derived after, carried)
- medals_after: 5120 (derived, not live-read — Store not visited)
- chests_opened: 0
- squads_parallel: 2
- target: kill wave zombies and claim LOOT
- achieved: 2 Lv.10 kills dispatched in parallel, 2 LOOT rows claimed (536000 coins)
- resources_gained: coins 536000, iron 536000, food 536000, medals 20, hero EXP 526000
- costs: about 15 minutes, stamina 70 to 51
- verified: yes (coin, food and stamina figures live-read; medals_after derived, flagged)
- blocker_category: h
