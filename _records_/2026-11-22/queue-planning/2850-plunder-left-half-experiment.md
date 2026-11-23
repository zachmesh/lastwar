---
title: Plunder Left Half Stack Experiment Under Scan 002 2850 2026-11-23
created: 2026-11-23T07:20:00-08:00
modified: 2026-11-23T07:50:00-08:00
level: L0
version: 1.1.0
description: The coordinator's one-fight experiment on whether UR shard stacks in the left half of a trade truck's cargo pay shards, the exception it adds to scan 002 only, what is recorded, and the dated open question for the plunder digest
status: done
activity: queue-planning
run_id: queue-planning-2026-11-23-0720-left-half-experiment
trigger: coordinator message 15:10Z
started_at: 2026-11-23T07:12:00-08:00
finished_at: 2026-11-23T07:20:00-08:00
verified: the digest rule 9 text read from _activities_/truck-plunder/rule-digest.md; the scan 002 file read before and after the edit
grounded_in:
  - source: coordinator message 15:10Z (operator find at about 15:00Z)
  - source: _activities_/truck-plunder/rule-digest.md rule 9
---

# Left-half stack experiment, 2850

## The ruling

The operator found a UR Lv.30 trade truck with a guard of 18.9M and two 500-badge x3 UR shard stacks in slots 3 and 4, the LEFT half of the cargo row, arriving at about 16:00Z. The coordinator ruled that a stack in either half qualifies for ONE fight, under `trucks-plunder-scan-2026-11-23-002` (opens 15:20Z, expires 15:50Z). Nothing else changes: the guard must be below Squad 1 (25.61M), the hospital rule stands (free room at least 1,000; stop after two fights in a row each wounding over 100), the count is 1 of 4 before the fight, and the truck must still be more than 30 minutes out, so the fight must start by 15:30Z for a 16:00Z arrival. Only `-002` carries the exception; `-001` and `-003` to `-009` keep the right-half rule.

## What is recorded

Before the fight, each slot's cargo (the slot number, the stack size, the left or right half); after it, the loot item by item (coin, iron, food, shards and their size), the troops wounded, the count and Total Power. The question: do left-half stacks pay shards?

## The result (operator record 1523, scan 002, fight at 15:23:13Z)

A LEFT-HALF UR shard stack PAYS shards [M]. Target: SSR Lv.24, guard 8.2M against Squad 1 25.61M, arrival 04:33; slot 1 a gold bar, slots 2 and 3 each a UR 500-badge shard x3 (all shards in the left half), slots 4 to 6 iron 1.4M, food 1.4M, coin 933.7K. Loot: UR shard x3 (3 of the 6 shown), iron and food +492.5K each, coin +311.2K, about a third of each resource stack; hospital unchanged (0 wounded, free room 2,329); count 2 of 4. Fight 1, for comparison, stacks in the right half: shard x9, iron and food +951.8K, coin +607.5K. One trial each, so [D]: the 'preferably on the right' rule is relaxed. Scans 003 to 009 and the 18:00Z session now accept a UR 500-badge stack in either half; the other checks stand. Hazard found at 15:2xZ: (400,640) is not safe after a camera shift (it selected a Barracks and hid the left column); use the bare spot (310,660), or WORLD then BASE first.

## The open question for the digest (settled by the result above)

Dated 2026-11-23, for `_activities_/truck-plunder/rule-digest.md` rule 9, which says shards 'preferably on the right': OPEN, do left-half UR shard stacks pay shards on plunder? An experiment of one fight is under way (scan 002); the record of that run settles the word 'preferably'. The scribe adds it; I do not edit the digest.
