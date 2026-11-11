---
title: Zombie invasion queue run 0030
created: 2026-11-11T00:42:00-08:00
modified: 2026-11-11T00:42:00-08:00
version: 1.0.0
description: Zombie invasion unit zombie-invasion-zombie-2026-11-10-004, Glacieradon wave, first parallel dispatch in this chain (squads_parallel 2), 2 Lv.10 kills and both LOOT rows claimed for 536,000 coins, Store medal balance 4000 and the 120-medal row identified as Universal Exclusive Weapon Shard
status: partial
grounded_in:
  - source: live game screen on the owner Mac mini, 2026-11-11 00:30-00:42 PT
---

# Zombie invasion queue run 0030

- Unit: zombie-invasion-zombie-2026-11-10-004, executor ticker-0004,
  chain zombie-2026-11-10 seq 4, sessions cc-525 and cc-526.
- Window: 00:30-00:42 PST. Status partial - the wave is still live
  and the chain continues. Successor enqueued to start now.

## Entry state

- The game was on the ALLIANCE TECHS panel at unit start (the
  donations unit left it there): closed the tech panel and the
  tree, back arrow to the base screen. Base HUD at entry: food
  655.7M, iron 978.7M, coin 110.2M (HUD-rounded), badge 13.22K,
  gold 6,287, stamina 120, Total Power 149,218,973.
- Session cc-525 dropped mid-unit (observe returned
  observation_unavailable with no session open); session cc-526
  was started, LastWar re-selected, and no game state was lost.
- No "active on a different device" dialog appeared at any point.

## The event page

- Events icon at 935,138 opened the Events hub on the Zombie
  Invasion - Glacieradon page (the hub remembered the tab).
- Page read live: event timer 2d 17:26:24 remaining, "Zombies are
  invading! Protect our City! Challenge the fearsome Beast
  Glacieradon!", Store / Ranking / Rewards buttons, Alliance
  Finding / My Findings tabs, boss clue counter 40/40 with
  "Challenge begins in: 1d 17:26:25. Your Timezone: 2026-11-12
  18:00". Alliance Finding lists Lv.80 and Lv.85 Zombie Bosses
  at 546km, 487km, 486km, 506km. "The next wave of Invading
  Zombies will arrive in 00:20:58" at the read - the current
  wave (arrived about 23:57) is live.
- A system ticker read "...ed 1000 from Zombie Boss Loot!" at
  the top during the first Search - quoted verbatim; a ticker
  line, not this account's gain, and not claimed as one.

## Kill 1

- Search at 379,946 found a Lv.10 Invading Zombies target:
  Guaranteed Reward medal x10, drone data 1.3K, hero EXP 263.0K,
  iron 268.0K, food 268.0K; Potential Reward green crate x1,
  green box x4, gold ticket x1; Suggested Power 670,000; stamina
  cost 10; despawn 11:20:17.
- The first crossed-swords tap failed with stale_observation
  (the target app's process identity was unavailable, input NOT
  dispatched, side effect none); the window was re-selected,
  the card re-observed still open, and the tap re-sent - no
  input was replayed.
- Crossed-swords at 496,736 opened the deploy panel: Squad 1,
  five Lv.150 heroes, Unit Count 2,231/2,231, 25.20M vs 670.00K,
  Easy Win, march 00:01:37, stamina 120 with -10 shown.
- March at 500,755 dispatched at once. Stamina 120 to 110,
  March Queues 1/4, Go X:534 Y:376 00:01:20.

## Kill 2 - parallel dispatch

- While Squad 1 was out, Events (935,138) back to the
  Glacieradon page and Search at 379,946 found a second Lv.10
  target with the same card values.
- Crossed-swords at 496,736 opened the deploy panel with Squad 2
  auto-selected (Unit Count 2,175/2,175, Easy Win - no squad-tab
  tap needed, per unit 024).
- March at 500,755 dispatched at once. Stamina 110 to 100,
  March Queues 2/4, Go X:525 Y:356 00:01:54.
- squads_parallel 2 - the first parallel run in the Glacieradon
  chain (units 001-003 all ran 1). The binding limit was the
  short round trips, not the march cap of 4; the second dispatch
  landed inside Squad 1's outbound window.

## LOOT claim

- Gift badge read 2 at the right end of the March Queues bar
  after both arrivals; the gift box re-grounded fresh on the
  current screenshot at 322,226 opened the LOOT panel at once.
- Two rows, read before claiming: Lv.10 Invading Zombies
  X:525 Y:356, medal x10, green box x4, iron 268.0K, food
  268.0K, coin 268.0K, hero EXP 263.0K; Lv.10 Invading Zombies
  X:534 Y:376, same values. Each row pays exactly 268,000
  coins, fourth confirmation for this variant.
- Claim All (plain blue, no price tag) at 499,765 tapped once;
  toast "Alliance Gifts received!" and the panel closed. Coin
  HUD 110.2M to 110.7M, food 655.7M to 656.2M, iron 978.7M to
  979.3M - each displayed move consistent with 2 x 268,000
  (HUD rounds to 0.1M). Gift badge gone after the claim.
  Squad 2 was still Returning 00:00:17 at the claim - rows are
  claimable before homecoming, per unit 054.

## Store - medal balance and chest-row identification

- Store opened from the event page at 846,210 on the first try.
  Medal balance read live in the header: 4000. Unit 001 read
  3950 before its kill; five Lv.10 kills since (001, 2219, 2340,
  plus these two) at medal x10 each reconcile exactly to 4000 -
  the +10 medals per Lv.10 kill is confirmed across five kills.
- First-screen rows: gold chest x1 120 medals Limit 10; gold
  bar x1 80 medals Limit 10; gold bar x1 80 medals Limit 30;
  50 Stamina x1 10 medals Limit 3 (available - NOT sold out in
  this variant, unlike the October event); crate x1 160 medals
  Limit 50; one more row below the fold, unscrolled.
- Tooltip on the 120-medal row (icon tap at 230,300): the row is
  "Universal Exclusive Weapon Shard", Owned 417 - it is NOT a
  Coin Chest, correcting unit 001's appearance-based "gold
  chest" label. No Coin Chest row is established in this variant
  yet: the 160-medal crate row and the below-fold rows are still
  unidentified, and no redemption was made. The Store X tap to
  close left no change (tooltip still up); the game was left on
  the Store screen - harmless state for the successor.
- Stamina 100 at close, no refill needed. No stamina item was
  opened and the inventory stamina count was not read (stamina
  never bound this unit).

## Result

- zombies_killed 2 (verified: stamina 120 to 110 to 100, March
  Queues 0/4 to 1/4 to 2/4 to 0/4, two LOOT rows X:534 Y:376
  and X:525 Y:356 claimed).
- cleared false: the wave is live, next wave arrives in about
  00:13:47 at the Store read, more targets may appear.
- coin_before 110.2M HUD, coin_after 110.7M HUD,
  coins_collected 536,000 (two rows read before Claim All).
- medals_before not re-read live at unit start, medals_after
  4000 (Store header read live after the kills).
- chests_opened 0. squads_parallel 2 (see above).
- Target: kill wave zombies and claim LOOT; achieved: 2 Lv.10
  kills in parallel and both LOOT rows claimed. Verified yes
  (same-unit live reads: row coin lines, HUD deltas, stamina,
  queue state, Store header).
  Blocker category h (by-design partial - chain continuation).
- Follow-up: successor enqueued to start now (chain rule,
  cleared false). It should run parallel dispatches while the
  wave lasts, finish identifying the Store chest rows (the
  160-medal crate tooltip and the below-fold rows) and, once a
  Coin Chest row is established, redeem per the maximize-coin
  rule, and check the Lv.28 Ironhead LOOT coin line if it
  dispatches on one.
