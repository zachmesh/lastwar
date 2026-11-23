---
title: Calibration report 1 - five closed forecasts, five misses
created: 2026-11-23T13:03:00Z
modified: 2026-11-23T13:03:00Z
version: 1.0.0
description: Coach calibration of the five closed forecast ledger rows - interval hit rate, Brier score and reliability for the binaries, bias by lever and by evidence tag, the in-sample test of Steer A's shading rule and the retired-lever check
status: done
activity: coach
run_id: coach-2026-11-23-0501
trigger: Steer A round 14, item 2
started_at: 2026-11-23T12:57:00Z
finished_at: 2026-11-23T13:03:00Z
duration_seconds: 360
verified: no
grounded_in:
  - source: _records_/2026-11-22/strategy/forecast-ledger.csv, rows F-001, F-005, F-006, F-007 and F-048 (106 rows, 5 closed)
  - source: _records_/2026-11-22/strategy/lever-ranking-v3.md and 0446-strategy-v3.md
---

# Calibration report 1

Values in [forecast-calibration.csv](forecast-calibration.csv). The ledger is the Strategist's file, so I did not edit it: `in_range`, `error_pct` and `brier` are in my CSV for the Strategist to enter.

- **Interval hit rate: 0 of 2** against 80 percent ranges. F-001 actual 0 against 1 / 5 / 20 (error -100 percent of the point); F-005 actual 3,900 against 4,000 / 8,000 / 12,000 (-51.3 percent; 100 under the low). If the ranges really covered 80 percent, two misses in a row has a chance of 4 percent.
- **Binaries (3):** Brier 0.3025, 0.1225 and 0.36, mean 0.262, no better than a flat 50 percent (0.25). Mean forecast 0.50, observed 0 of 3. By themselves three false outcomes at these odds are 12 percent likely, so chance cannot be ruled out; with the intervals the five together are about 0.5 percent likely if calibrated and independent. Reliability bins hold one to two rows each, too few to draw a curve.
- **Bias by lever:** materials -100 percent (a box can pay nothing); research -51 percent on the range and p 0.55 on the node, both missed; new ground p 0.35, false; events p 0.60, false. All five are optimistic, none pessimistic.
- **Bias by evidence tag:** G rows 0 of 4 resolved in favour (F-001, F-006, F-007, F-048); the single-source row F-005 missed by 2.5 percent below its low; no closed [M] forecast yet.

## The shading rule, tested in-sample

Shading G and single-source probabilities by 0.15 gives 0.40, 0.20 and 0.45, mean Brier 0.134 against 0.262. Widening the ranges by 25 percent each side rescues F-005 (3,000 to 15,000 holds 3,900) but not F-001: an outcome of 0 is below any multiple of a low of 1, so a yield that may pay nothing needs a low of 0. Five rows, in-sample: indicative, not proof.

## Retired lever

Confirmed: ranking v3 retires the Extra Drill Ground and new-ground lever (`lever-ranking-v3.md:35`, `0446-strategy-v3.md:30`) and its CSV has no such row. Stale: `_knowledge_/growth-plan/lever-table.csv` still lists Extra Drill Ground research, 61M coin and 700 Valor, tag S1.

## F-048 learning, a draft for the ledger owner

Forecast p 0.60 that the two Age of Oil stage-3 cards had a free claimable reward; actual: none available. The assumption that failed was a guide-text expectation (tag G). Rule: shade G rows by 0.15; test: read the card's claim state before forecasting.
