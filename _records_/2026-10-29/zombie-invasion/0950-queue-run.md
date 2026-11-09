---
title: Zombie Invasion Execution 2026-10-29 0950 Queue Run
created: 2026-10-29T16:51:00Z
unit: zombie-invasion-zombie-2026-10-28-045
executor: ticker-0934
status: partial
---

# Zombie Invasion - execution, 2026-10-29 0950 queue unit 045

A single task unit, executed by executor ticker-0934 under the
task unit queue. Unit zombie-invasion-zombie-2026-10-28-045,
chain zombie-2026-10-28, chain sequence 45, priority 4.
Session window about 09:49 to 09:51 America/Los_Angeles.
Status - partial; the chain continues while the event is
available and zombies remain nearby, so the tracker is
left untouched. The one kill dispatched in this unit was
resolved and claimed inside it, and the march queue
was empty at the close.

## What was observed

- Open - the game was on the base screen, no
  different-device dialog at any point. One computer
  session was live throughout this unit (cc-260).
- First dispatch attempt, target changed - a batched
  sequence (Events, Search, crossed-swords at
  498,728, March at 500,755) opened a Lv.10 deploy
  panel, but the March tap answered with the toast
  "The target location has changed. Please try
  again." No stamina was charged (stamina still 43
  afterwards, matching unit 044's close), the same
  failure mode unit 006 recorded: fresh-wave targets
  move or are taken within seconds.
- Second dispatch attempt, kill 1 - the same batched
  sequence dispatched at once. March Queues read
  1/4 with the squad Returning at 00:00:08, then
  0/4 after the return. The target coordinates
  read X:999 Y:969 in the LOOT row.
- Claim - the grounded gift tap 317,233 opened the
  LOOT panel with exactly one row, Lv.10 Invading
  Zombies at X:999 Y:969, coin line read directly
  as 268.0K, medal x10, iron 268.0K, food 268.0K,
  hero EXP 263.0K. Claim All at 498,760, blue
  button with no price tag.
- Coin totals - coin_before is HUD-rounded 105.3M
  at this unit's start (unit 044's post-claim
  HUD); coin_after is HUD-rounded 105.3M after
  this claim as well, the 268,000 landing inside
  the 0.1M rounding band, so the HUD cannot
  corroborate this unit's delta the way it did
  unit 044's. coins_collected 268,000 is exact
  from the LOOT row's coin line.
- Stamina - 43 at this unit's start, 34 at the
  close (43 minus 10 for the kill, plus about 1
  regenerated). No refill was needed and no
  conclusion about exhausted refills was
  required, so the backpack stamina inventory
  was not re-read this unit.
- Medals - medals_before 2930 is unit 044's
  derived medals_after carried forward, not a
  fresh live read; medals_after 2940 is derived
  (2930 plus this unit's 10). The Store was not
  re-opened this unit, so the Coin Chest (SSR)
  redemption stays deferred, and no owned chest
  was opened - their backpack location is still
  unknown.
- squads_parallel - 1. Only one squad was ever
  out: the first dispatch failed on the
  target-changed toast, and the retry ran solo
  within the pass budget; no second squad was
  staged in parallel. Not a march cap (the
  queue cap remains 4).
- Cleared - false. Search found targets on demand
  twice in a live wave, and the event still has
  over a day left. Successor unit 046 enqueued
  to start now.

## Result statistics

- zombies_killed: 1
- cleared: false
- coin_before: 105.3M HUD rounded
- coin_after: 105.3M HUD rounded
- coins_collected: 268000
- medals_before: 2930 derived
- medals_after: 2940 derived
- chests_opened: 0
- squads_parallel: 1
- tasks_badge: 1
- stamina_end: 34
