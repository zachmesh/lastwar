---
title: Zombie invasion queue run
created: 2026-10-30T04:55:00Z
modified: 2026-10-30T04:55:00Z
version: 1.0.0
description: Queue unit zombie-invasion-zombie-2026-10-28-050 execution
status: partial
---

# Zombie invasion - 2026-10-29 21:50 to 21:55 PDT queue run

Unit: zombie-invasion-zombie-2026-10-28-050, executor
ticker-2134, chain zombie-2026-10-28 seq 50.

## Two Lv.10 kills, loot claimed in-unit

- Events page verified by title Zombie Invasion (event
  timer 21:09:18 left, next wave in 00:50:45 at entry).
- Kill 1: batched Search, crossed-swords, March.
  Deploy panel Squad 1, 25.05M vs 670.00K, Easy Win,
  Unit Count 2,231/2,231, stamina 63, cost 10.
  March verified 1/4, Go X:990 Y:938, stamina 63 to 53.
- Kill 2: immediate batched second dispatch while Squad 1
  was out. Its deploy panel again read Squad 1, 25.05M,
  Easy Win, so Squad 1 had already returned on the short
  round trip - parallel dispatch failed again for short
  round trips, as in units 043 and 049, not for the march
  cap of 4. Marched anyway: 1/4, Go X:986 Y:936,
  stamina 53 to 44 observed.
- Computer session cc-393 dropped mid-unit (observe
  returned observation_unavailable); session cc-397 was
  started, LastWar re-selected, no game state lost.
  Squad home verified 0/4 on return.
- LOOT panel held exactly this unit's 2 rows, each
  coin 268.0K, medal x10: X:990 Y:938 and X:986 Y:936.
  Claim All (plain blue, no price tag) tapped in-unit;
  panel closed, 536,000 coins collected by row lines.
- Coin panel exact readings were not taken in this unit;
  HUD coin read 121.5M at entry and after the claim, so
  no exact coin_before/coin_after is reported. Medal
  balance was not live-measured in the Store, so no
  derived medal total is reported (only plus 20 medals
  by row evidence).
- Stamina 44 remains, so no stamina item was opened and
  no backpack stamina inventory check was needed. The
  event Store was not visited in this unit (pass budget);
  the SSR row re-check and Buy-step retry from unit 047
  and the owned Coin Chest location stay open for the
  successor. No chest opened, nothing bought, no diamonds
  spent.

## Outcome

Partial (pass budget): 2 kills, loot claimed in-unit,
squads_parallel 1 for the stated short-round-trip reason.
Nearby zombies not verified cleared, so cleared is false
and the successor starts now.
