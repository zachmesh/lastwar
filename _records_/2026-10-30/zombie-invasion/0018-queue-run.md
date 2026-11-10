---
title: Zombie invasion queue run
created: 2026-10-30T07:18:00Z
modified: 2026-10-30T07:18:00Z
version: 1.0.0
description: Queue unit zombie-invasion-zombie-2026-10-28-051 execution
status: partial
---

# Zombie invasion - 2026-10-30 00:09 to 00:18 PDT queue run

Unit: zombie-invasion-zombie-2026-10-28-051, executor
ticker-0004, chain zombie-2026-10-28 seq 51.

## Two Lv.10 kills in parallel, loot claimed in-unit

- Events page verified by title Zombie Invasion (event
  timer 18:49:18 left, next wave in 00:30:48 at entry).
  The tab bar had shifted again between openings: the
  leftmost partial tab read only "sion", and dragging the
  bar right revealed the Zombie Invasion tab at 647,131,
  which was then tapped and verified by title before
  Search. On the second dispatch the Events button
  reopened directly on the Zombie Invasion page, so no
  tab navigation was needed there.
- Kill 1: batched Search, crossed-swords, March (grounded
  points 358,941, 499,753, 500,759). March Queues 1/4,
  Go X:897 Y:995, stamina 71 to 61 proving the 10-cost
  march. Deploy panel details were not read in the
  batched sequence, per the standing batched method.
- Kill 2: immediate batched second dispatch while Squad 1
  was still out (its timer read 00:00:54 at the second
  screenshot, outbound leg still running). March Queues
  2/4, Go X:889 Y:977, stamina 61 to 51 proving the
  second 10-cost march. squads_parallel is therefore 2,
  the first true parallel overlap in this chain since
  unit 047 - the longer 90-second-class march to
  X:897 Y:995, not a home-cluster 10-second trip, is
  what made the overlap possible.
- Computer session cc-417 dropped mid-unit (observe
  returned observation_unavailable); session cc-418 was
  started, LastWar re-selected, no game state lost.
- Both squads verified Returning (00:00:25 and 00:01:23)
  and then home (0/4). The gift-box badge read 2 while
  both squads were still Returning, so LOOT rows
  materialize on victory, before the squads reach home.
- LOOT panel held exactly this unit's 2 rows, each
  coin 268.0K, medal x10, iron 268.0K, food 268.0K,
  hero EXP 263.0K: X:897 Y:995 and X:889 Y:977.
  Claim All (plain blue, no price tag) tapped in-unit;
  panel closed, badge cleared, 536,000 coins collected
  by row lines.
- Coin HUD read 122.0M at base entry and 122.5M after
  the claim, consistent with plus 536,000 (food
  263.9M to 264.4M and iron 447.5M to 448.1M moved by
  the same two rows). No exact coin-panel reading was
  taken, so no exact coin_before/coin_after is reported.
  Medal balance was not live-measured in the Store, so
  no derived medal total is reported (only plus 20
  medals by row evidence).
- Stamina closed at 52 (regen plus 1 after the two
  marches), so no stamina item was opened and no
  backpack stamina inventory check was needed. The
  event Store was not visited in this unit (unit cap);
  the SSR row re-check and Buy-step retry from unit
  047 and the owned Coin Chest location stay open for
  the successor. No chest opened, nothing bought, no
  diamonds spent.

## Outcome

Partial (unit cap): 2 kills, parallel dispatch achieved
(squads_parallel 2), loot claimed in-unit. Nearby
zombies not verified cleared (Search found targets in
this wave, next wave due in about 30 minutes at entry),
so cleared is false and the successor starts now.
