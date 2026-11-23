---
title: Queue Planning Drill Ground F1 Values In The Builder Units 2455 2026-11-23
created: 2026-11-23T00:41:00-08:00
modified: 2026-11-23T00:41:00-08:00
level: L0
version: 1.0.0
description: Planner update after the F1 panel read - the builder conversion units now carry the measured Drill Ground Lv.28 to 29 cost and time, the ledger and tables hold the measured row, and the guide's factors are checked against two buildings
status: done
activity: queue-planning
run_id: queue-planning-2026-11-23-0041-drill-ground-f1
trigger: coordinator message with the F1 values and cost caps confirmed
started_at: 2026-11-23T00:39:00-08:00
finished_at: 2026-11-23T00:41:00-08:00
verified: F1 values read in _records_/2026-11-22/perception-scout/0035-queue-run.md lines 23 to 27; minutes and chest counts recomputed; word counts under 450; validate exit 0
grounded_in:
  - source: _records_/2026-11-22/perception-scout/0035-queue-run.md
  - source: _records_/2026-11-22/queue-planning/2400-candidate-ledger-template.csv, 2420-capacity-sources.csv, 2430-sinks-by-slot-day.csv
---

# Drill Ground F1 values, 2455

## 1. Measured

Drill Ground Lv.28 to 29, from the panel at 08:35Z: coin 119.0M (short, with an Obtain button beside it that is never pressed), iron 144.5M met, prerequisite Lv.29 Headquarters met, no food row, 18d 09:21:34 which is 26,481 minutes, Unit Count +7,600 to +7,800 so +200 slots, power +30,400. Finish Now would cost 228,514 diamonds, a red line.

## 2. Builder units

`building-queues-growth-convert-2026-11-24-001` and `-002` now say: convert 119.0M, which is 49 UR Coin Chests (119.07M, of the 87 read), opened by quantity if offered, otherwise at most 10 and stop; the iron is met; the bounded speed-up is up to 10,000 minutes and never above, leaving about 11.4 days; the panel governs if it differs. Both count the Drill Grounds first and take the lowest not already upgrading; only one is confirmed, and a second may sit at the bottom right edge, label unread. The Strategist decides which ground once they are counted.

## 3. Checks against the guide

The panel's coin 119.0M and iron 144.5M are 0.85 of the guide's 140M and 170M, so cost factor 0.85 holds on a second building. The effective time ratio is 0.4706 here and 0.4764 on the Hut. The guide-based estimate of 19,315 power per builder-day for L29 against 19,565 measured is within 1.3 percent. The ledger has the measured row: 1.68 slots per million coin, 18.4 builder-days. The Hut's coin line is still unread.
