---
title: Zombie Invasion Execution 2026-10-29 0952 Queue Run
created: 2026-10-29T16:56:00Z
unit: zombie-invasion-zombie-2026-10-28-046
executor: ticker-0934
status: partial
---

# Zombie Invasion - execution, 2026-10-29 0952 queue unit 046

A single task unit, executed by executor ticker-0934 under the
task unit queue. Unit zombie-invasion-zombie-2026-10-28-046,
chain zombie-2026-10-28, chain sequence 46, priority 4.
Session window about 09:52 to 09:56 America/Los_Angeles.
Status - partial; the chain continues while the event is
available and zombies remain nearby, so the tracker is
left untouched. The one kill dispatched in this unit was
resolved and claimed inside it, and the march queue
was empty at the close.

## What was observed

- Open - the game was on the base screen, no
  different-device dialog at any point. One computer
  session was live throughout this unit (cc-260).
- Dispatch, batched - one batched sequence (Events,
  Search, crossed-swords at 498,728, March at
  500,755) dispatched first try this time. March
  Queues read 1/4 with the squad Returning at
  00:00:08, then 0/4 after the return. The target
  coordinates read X:974 Y:946 in the LOOT row.
  Stamina 34 at the prior close, 25 at this
  close (34 minus 10 for the kill, plus about 1
  regenerated).
- Claim - the grounded gift tap 317,233 opened the
  LOOT panel with exactly one row, Lv.10 Invading
  Zombies at X:974 Y:946, coin line read directly
  as 268.0K, medal x10, iron 268.0K, food 268.0K,
  hero EXP 263.0K. Claim All at 498,760, blue
  button with no price tag.
- Coin totals - coin_before is HUD-rounded 105.6M
  at this unit's start (105.3M before unit 045's
  claim plus its 268,000, corroborating that
  claim's landing); coin_after is HUD-rounded
  105.6M after this claim as well, the 268,000
  landing inside the 0.1M rounding band.
  coins_collected 268,000 is exact from the LOOT
  row's coin line.
- Medals - medals_before 2940 is unit 045's
  derived medals_after carried forward, not a
  fresh live read; medals_after 2950 is derived
  (2940 plus this unit's 10). The Store was not
  re-opened this unit, so the Coin Chest (SSR)
  redemption stays deferred, and no owned chest
  was opened - their backpack location is still
  unknown.
- squads_parallel - 1. A single batched dispatch
  ran solo; no second squad was staged in
  parallel within this unit. Not a march cap
  (the queue cap remains 4).
- Cleared - false. Search found a target on
  demand in a live wave, and the event still has
  over a day left. Successor unit 047 enqueued
  to start now.

## Result statistics

- zombies_killed: 1
- cleared: false
- coin_before: 105.6M HUD rounded
- coin_after: 105.6M HUD rounded
- coins_collected: 268000
- medals_before: 2940 derived
- medals_after: 2950 derived
- chests_opened: 0
- squads_parallel: 1
- tasks_badge: 1
- stamina_end: 25
