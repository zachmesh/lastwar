---
title: Zombie invasion queue run
created: 2026-10-30T08:05:00Z
modified: 2026-11-01T07:26:52Z
version: 1.0.1
description: Queue unit zombie-invasion-zombie-2026-10-28-053 execution
status: done
---

# Zombie invasion - 2026-10-30 01:04 to 01:17 PDT queue run

Unit: zombie-invasion-zombie-2026-10-28-053, executor
ticker-0104, chain zombie-2026-10-28 seq 53, computer
sessions cc-421 then cc-422 (cc-421 dropped mid-unit with
observation_unavailable; cc-422 re-selected LastWar, no game
state lost).

## Two Lv.10 kills, both LOOT rows claimed in-unit

- Events page verified by title Zombie Invasion on first
  opening (event timer 17:54:38 left, next wave in
  00:36:06 at entry). Coin HUD 123.6M at entry.
- Kill 1, single-step dispatch (Search 358,941,
  crossed-swords 467,729, March 500,759, with a screen
  read between steps): X:979 Y:956, March Queues 1/4,
  stamina 22 to 12. Its LOOT row claimed in-unit:
  X:979 Y:956, coin 268.0K, medals x10, iron 268.0K,
  food 268.0K, hero EXP 263.0K. Claim All (plain blue,
  no price tag) tapped; coin HUD moved to 123.9M and
  food 265.5M to 265.7M, iron 449.2M to 449.4M,
  consistent with one 268.0K row.
- A batched second dispatch (Search, crossed-swords
  499,753, March 500,759 in one 1.5 second batch, no
  reads in between) FAILED silently: stamina stayed
  at 13 and March Queues stayed 0/4. Lesson: a batch
  this fast outruns the Search jump animation, so the
  later clicks land before the card or deploy panel
  exists. Batched dispatches need a pause after Search,
  or single-step dispatches as in kill 1 and kill 2.
- Kill 2, single-step dispatch again: X:982 Y:965,
  March Queues 1/4, stamina 13 to 3. squads_parallel
  is therefore 1: both kills ran alone because the
  first squad had already returned (11 second class
  round trips) before the second dispatch landed,
  the same short-round-trip binding limit as units
  043 and 049, not the march cap of 4.
- Second LOOT row, gift-box hunting: the first two
  taps at the grounded gift point (317,233, then
  312,225) opened ally another commander's base profile
  instead, because the map was centred on that base
  and the base sat under the gift icon. After a map
  drag moved the base clear, a tap at 319,247 opened
  the LOOT panel. Lesson: the gift-box point is only
  valid when the map view matches the screenshot it
  was grounded on; when an ally base sits under it,
  drag the map clear first and re-ground, never
  re-tap the same point blindly.
- Second row claimed in-unit: X:982 Y:965, from a
  LOOT panel whose row line was NOT screenshot-read
  before tapping Claim All, under the unit cap, so
  its individual coin line is unverified; the
  536,000 total below counts it at the chain's
  standard Lv.10 row value of 268.0K (read on kill
  1 and on every row in units 047, 049 and 052).
  Coin HUD about 124.1M after the claim, consistent
  with that total at HUD rounding. Stamina closed
  at 4 (3 after kill 2 plus regen).
- Store NOT visited in this unit: the gift-box
  hunting and the session drop consumed the cap,
  so no medal balance was live-measured and no
  derived medal total is reported. The SSR Coin
  Chest redemption and the owned-chest location
  stay open for the successor, as in units 048
  and 049. No diamonds and no money spent.

## Outcome

Done (unit work completed inside the cap): 2 kills at
squads_parallel 1, loot 536,000 coins claimed
in-unit, cleared false - nearby zombies not
exhausted (Search found a target twice, next wave
still incoming), so the successor starts now.
Stamina 4 at close, no stamina item opened; stamina
was not exhausted, so no 1 hour delay applies.
