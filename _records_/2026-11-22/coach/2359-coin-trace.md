---
title: Coin trace - where the coin went, 2026-11-10 to 2026-11-23
created: 2026-11-23T08:06:00Z
modified: 2026-11-23T08:06:00Z
version: 1.0.0
description: Coach record tracing the coin balance from 80.6M on 2026-11-10 to 9.6M, the three spend windows between reads, and what the records show about each
status: done
activity: coach
run_id: coach-2026-11-22-2359
trigger: coordinator request to find where the coin went and the corrected coin series
started_at: 2026-11-23T08:00:00Z
finished_at: 2026-11-23T08:06:00Z
duration_seconds: 360
verified: no
grounded_in:
  - source: HUD coin readings in the run records listed in coin-series.csv
  - source: _tools_/state/resources.jsonl rows 14 and 15
---

# Coin trace

Coin is a flow: the owner spends it by hand and income refills it. The corrected series ([series](coin-series.csv)): 33.9M on 10-28, 44.2M on 11-09, 80.6M on 11-10, 145.7M on 11-12, 153.7M on 11-14, 27.7M on 11-16, 103.9M on 11-22 at 01:34, 109.2M at 14:00, 35.3M at 19:55, 45.2M at 21:40, 9.6M at 22:48 and 23:49. The 9.6M is 0.4M under the 10M floor.

## Three spend windows between reads ([windows](coin-windows.csv))

- **A, 11-14 18:33 to 11-16 21:04 PT: -126.0M.** 48 team game records fall inside; none mentions coin or gold, and none states builder or lab status. The first builder read afterwards, 11-21 00:02, shows 1 of 4 busy. Nothing records what was started.
- **B, 11-22 14:00 to 19:55 PT: -73.9M.** No team record inside: the executor was stopped. At 19:55 builders read 0 of 4 and labs 2 of 2, so no build runs from this spend. Power rose from 147,972,169 (11:41) to 150,080,120. The labs held Unlock Oil Well and Defense Training VIII Lv.7 at 20:22 (`research-queue/2022-queue-run.md`), but the 10:10 and 13:10 reads showed Advanced Armor VIII Lv.3 and Defense Training VIII Lv.6; the record leaves that contradiction unreconciled, so a start by hand is unverified.
- **C, 11-22 22:05 to 22:48 PT: -35.6M.** Builders 0 of 4 to 4 of 4, food 750.8M to 638.0M: four Lv.25 Training Base builds, about 8.9M coin and 28.2M food each by arithmetic. Three records show them: `secret-missions/2248-queue-run-detail.md`, `building-queues/2335-queue-run-detail.md`, `growth/2344-fill-run.md`. Other device, likely; unverified.

## Totals

Spend found: 126.0 + 73.9 + 35.6 = 235.5M. The net from 80.6M (11-10) to 9.6M is -71.0M, so income between was about 164.5M over 12.9 days. Measured income between spends: +76.2M from 11-17 02:29 to 11-22 01:34, 15.5M a day.

## Reading for the plan

The team started nothing by rule before 07:43Z on 11-23, so every spend above is the owner's, unrecorded. A coin-costing start by the team competes with that hand spend for a balance that is near zero now; the 3x rule will block coin starts until it recovers.
