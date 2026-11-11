---
title: Zombie invasion queue run 2219
created: 2026-11-10T22:19:00-08:00
modified: 2026-11-10T22:19:00-08:00
version: 1.0.0
description: Zombie invasion unit zombie-invasion-zombie-2026-11-10-002, Glacieradon wave, one Lv.10 kill and its LOOT row claimed for 268,000 coins
status: partial
grounded_in:
  - source: live game screen on the owner Mac mini, 2026-11-10 22:12-22:19 PST
---

# Zombie invasion queue run 2219

- Unit: zombie-invasion-zombie-2026-11-10-002, executor ticker-2154,
  chain zombie-2026-11-10 seq 2, session cc-516.
- Window: 22:12-22:19 PST. Status partial - the pass budget ended
  mid-chain with the wave still live, so the chain continues.
  Successor enqueued to start now.

## Entry state

- Zombie Invasion - Glacieradon page verified live again: event
  timer 2d 19:46:33, "Zombies are invading! Protect our City!
  Challenge the fearsome Beast Glacieradon!", Store / Ranking /
  Rewards buttons, Alliance Finding / My Findings tabs.
- Boss clue counter now reads 40/40 (was 0/40 in unit 001):
  "Challenge begins in: 1d 19:46:34. Your Timezone: 2026-11-12
  18:00" - the boss challenge opens 2026-11-12 18:00 local.
- Alliance Finding lists Lv.85 and Lv.80 Zombie Bosses at 395km,
  423km, 405km, 573km, despawn timers about 02:17-02:40.
- Next wave of Invading Zombies arrives in 00:39:19 at entry
  (about 22:54) - the current wave is part-spent but targets
  remain.
- HUD at entry (world map read): food 644.3M, iron 967.4M, coin
  105.9M (HUD-rounded), gold 13.22K. Stamina 54 at the deploy
  panel. March Queues 0/4.

## The kill

- Search at 382,936 (fresh-grounded on the event page screenshot)
  found a Lv.10 Invading Zombies target: Guaranteed Reward medal
  x10, drone data 1.3K, hero EXP 263.0K, iron 268.0K, food 268.0K;
  Potential Reward green crate x1, green box x4, gold ticket x1;
  Suggested Power 670,000; stamina cost 10; despawn 11:38:27.
- Crossed-swords at 496,736 opened the deploy panel: Squad 1,
  five Lv.150 heroes, Unit Count 2,231/2,231, 25.20M vs 670.00K,
  Easy Win, march 00:01:01, stamina 54 with -10 shown.
- March at 500,760 dispatched at once. Stamina 54 to 44, March
  Queues 1/4, target X:516 Y:394, ETA 00:00:34. Squad 1 was
  Returning 00:00:46 on the next read and home (0/4) by the
  LOOT claim.
- Unexplained toast: "Alliance Gifts received!" appeared in the
  observation immediately after the March tap, before any LOOT
  claim in this unit (the row was still unclaimed then). Quoted
  verbatim; cause unknown - possibly a delayed toast. The LOOT
  row itself was verified unclaimed until this unit claimed it
  below.

## Parallel dispatch not achieved

- squads_parallel 1. While Squad 1 was out, a second dispatch was
  attempted on a nearby Lv.10 pile, but the tap at 498,505 opened
  a Teleport/Profession tile menu instead (the map view had
  shifted under the aim point), and the follow-up tap at 450,350
  opened a Lv.28 Ironhead card instead of dismissing the menu.
  No second march was dispatched, and Squad 1's round trip was
  about 80 seconds, so the parallel window closed before a
  re-grounded second attempt could land. Short round trips plus
  the two mistaps, not the march cap of 4, were the binding
  limit. Re-ground every map tap on the current screenshot; the
  map is dense with tappable tiles here.
- Lv.28 Ironhead sighted (not attacked): Suggested Power
  2,396,500, stamina cost 10, despawn 19:35:38; Guaranteed Reward
  drone data 780, hero EXP 105.0K, iron (value obscured by the
  cursor); Potential Reward green crate x1, green box x4, gold
  ticket x1. Higher-level zombies exist in this event variant;
  their LOOT coin line is still unmeasured.

## LOOT claim

- Gift badge read 1 at the right end of the March Queues bar
  after Squad 1's return; the gift box re-grounded fresh on the
  current screenshot at 288,216 opened the LOOT panel at once.
- One row, read before claiming: Lv.10 Invading Zombies X:516
  Y:394, medal x10, green crate x1, iron 268.0K, food 268.0K,
  coin 268.0K, hero EXP 263.0K.
- Claim All (plain blue, no price tag) at 498,765 tapped once;
  panel closed. Coin HUD 105.9M to 106.1M, food 644.3M to
  644.6M, iron 967.4M to 967.7M - each +0.3M displayed move
  consistent with the single 268,000 row (HUD rounds to 0.1M).
  Gift badge gone after the claim.
- Stamina 44 at the march, 45 at the LOOT read (regen tick) -
  one more plus-stamina read for the open question in the
  activity metadata.
- Store not visited in this unit (pass budget): the medal
  balance was not re-read live and no Coin Chest redemption was
  attempted. Unit 001's live Store read was 3950 medals; this
  unit's kill adds a card-stated medal x10, unverified as a
  balance. The Store coin-chest identification from unit 001's
  follow-up stays open for the successor.

## Result

- zombies_killed 1 (verified: Victory implied by Returning
  march, stamina 54 to 44, March Queues 1/4 to 0/4, LOOT row
  X:516 Y:394 claimed).
- cleared false: the wave is live, more Lv.10 piles visible on
  the map, next wave arrives about 22:54.
- coin_before 105.9M HUD, coin_after 106.1M HUD,
  coins_collected 268,000 (row read before Claim All).
- medals_before not re-read, medals_after not re-read.
- chests_opened 0. squads_parallel 1 (see above).
- Target: kill wave zombies and claim LOOT; achieved: 1 Lv.10
  kill and its LOOT row claimed. Verified yes (same-unit live
  reads: row coin line, HUD deltas, stamina, queue state).
  Blocker category h (by-design partial - chain continuation).
- Follow-up: successor enqueued to start now (chain rule,
  cleared false). It should run parallel dispatches with
  freshly grounded map taps, visit the Store to identify this
  event's Coin Chest rows by tooltip and re-read the medal
  balance, and check the Lv.28 Ironhead LOOT coin line if it
  dispatches on one.
