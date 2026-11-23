---
title: Queue Planning Hospital All Or Nothing And Cost Caps 2450 2026-11-23
created: 2026-11-23T00:38:00-08:00
modified: 2026-11-23T00:38:00-08:00
level: L0
version: 1.0.0
description: Planner pass after the operator's 0030 hospital read - retries of the 5,306 Collect removed from every staged brief, the ledger keeps the hospital as stuck stock with a threshold, capacity ranked by training slots, and operator cost caps stated
status: done
activity: queue-planning
run_id: queue-planning-2026-11-23-0038-hospital-and-caps
trigger: coordinator message after the serves conformance pass
started_at: 2026-11-23T00:35:00-08:00
finished_at: 2026-11-23T00:38:00-08:00
verified: a search of every inbox brief for the Hospital Collect wording; word counts of staged units; validate exit 0
grounded_in:
  - source: coordinator relay of the operator's 0030 hospital read
  - source: _records_/2026-11-22/growth/2357-troop-read.md and 0009-inventory-read.md for the per-step costs
---

# Hospital all or nothing, and cost caps, 2450

## 1. Retries removed

The Hospital Collect is all-or-nothing: it needs free capacity of at least 5,306 at once, and a retry only repeats the toast. Edited, all unclaimed: the 13 fill briefs (the TRAIN line now says never retry it; the 2026-11-24 fills no longer collect the Hospital), the two power units, and the 19:55Z collect unit. Slot B makes the one Hospital read per day; slot A does not. The 19:55Z to 21:55Z unit is kept: it collects the Lv.27 T9 x726 batch and logs the exact Total Power change, which tells whether a batch collect works under Drill Ground Full. A search finds no brief that instructs a retry.

## 2. Ledger

The hospital row is now stuck stock: ceiling about 8M power, threshold free capacity of at least 5,306 at once, one read a day. A new row, 200 T10 troops into freed training slots, gives +329,400 for about 1.4M food and 1.4M iron (5.5M per 793 is about 6,936 each). The capacity table carries a `filled_slot_value` column, and its Drill Ground rows read 200 T10 filled: +329,400. The Strategist's table governs from here.

## 3. Cost caps

The operator's records show 0.013 to 0.020 USD a step: 0.141 USD for 7 steps, 0.099 for 6 and 0.077 for 6 in the 2357 read, and 0.530 USD for 37 steps in the inventory read. With the harness stopping near 0.36 of the stated figure, I stated 0.60 USD on read-only, fill, power and collect units (it stops near 0.22 USD, enough for 10 steps) and 0.90 USD on the four conversion units (near 0.32 USD, for 10 steps plus chest opens). The line was added to 37 unclaimed units; the longest brief is 440 words. These are my estimates from two records.
