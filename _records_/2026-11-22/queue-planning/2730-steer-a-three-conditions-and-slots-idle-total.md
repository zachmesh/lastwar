---
title: Queue Planning Steer A Three Conditions And The Slots Idle Total 2730 2026-11-23
created: 2026-11-23T05:59:00-08:00
modified: 2026-11-23T05:59:00-08:00
level: L0
version: 1.0.0
description: Planner pass applying Steer A's approval of PL-04 with three conditions to the two speed-up units, and the corrected meaning of slots_idle in the three slot-read units
status: done
activity: queue-planning
run_id: queue-planning-2026-11-23-0559-three-conditions
trigger: coordinator message 13:50Z
started_at: 2026-11-23T05:51:00-08:00
finished_at: 2026-11-23T05:59:00-08:00
verified: unit states read before each edit; word counts; validate exit 0
grounded_in:
  - source: coordinator message 13:50Z relaying Steer A and the toolsmith's branch 92b9ba30
---

# Steer A's conditions and the slots idle total, 2730

## 1. The order in the units

The full order is in [2720](2720-coin-output-v-chain-order.md): read both labs; FIRST convert the coin Iron Output V needs (plan on 6.2M, N = ceil((6.2M + 10M - coin now) / 2.4364M) UR chests, stop above 40); THEN the tech speed-up on Coin Output V (tech items only, item name and quantity read before each press, inventory counts before and after); THEN Complete; THEN read Iron Output V's panel before Start (effective time with no speed-up, original time, coin, iron, food, oil, power: the first clean read of the research speed, written at once); THEN Start it in lab 2 in the same run chain, never leaving the lab idle. `research-speedup-coin-v-2026-11-23-002` (the fallback, 358 words) carries the compact outline. `-001` was claimed by the operator while I was editing; its file holds the same order in a longer 517-word form, which is over the 450-word gate; I do not edit a claimed unit, so the coordinator may need to trim it on completion if the commit gate objects. The second spend on Iron Output V (about 2,000 tech minutes to match Food Output V at 2026-11-24T17:30Z, shown in the preview before confirming) is a separate unit, staged when the operator reports the start and the timer.

## 2. slots_idle

The toolsmith's branch treats `slots_idle` as every open slot including the blocked ones and subtracts `slots_blocked_by_capacity`. The three slot-read units and the route card (now 1.2.0) say so: `slots_idle` is the TOTAL open slots, and the blocked count is a subset of it. The operator's training read wrote `slots_blocked_by_capacity=2`.
