---
title: Forecast gate rule for the enqueue check
created: 2026-11-23T10:02:00Z
modified: 2026-11-24T10:49:00Z
version: 1.1.0
level: L3
description: The rule the toolsmith implements so that a unit's plan item has a forecast row, first as a warning and later as a refusal, and when the ledger counts as stable
status: unverified
grounded_in:
  - source: Steer A red team round 6 of 2026-11-23 10:01Z on the missing forecast criterion
  - source: _records_/2026-11-22/strategy/forecast-ledger.csv and plan-of-record.csv
---

# Forecast gate rule

For the toolsmith, via the coordinator.

## The check

A unit carries `serves: PL-nn` or `serves: upkeep`. Upkeep is exempt. For a plan item id, the check passes when `forecast-ledger.csv` has at least one row whose `plan_item` equals that id and whose `kind` is not `retired`. PL-12 (the weekly review) has no forecast row by design and is listed in the exemption list with `upkeep`.

## Phase 1: warning now

`validate` prints a warning for a unit whose plan item has no ledger row. It does not refuse.

## Phase 2: refusal

`enqueue` refuses such a unit when all three hold; I announce it in the strategy log:

1. No change to the ledger columns for 24 hours (the last change was 09:20Z on 2026-11-23, so no earlier than 2026-11-24T09:20Z).
2. Every plan item PL-01 to PL-14 except PL-12 has at least one row (true at 10:05Z).
3. The coach's first calibration report has landed.

Earliest refusal: 2026-11-24T10:00Z (the columns last changed 09:20Z; no schema change since). Until I log it, the check stays a warning.

## Notes

The ledger moves by appended rows and amendment notes, never by deleted ids, so an id that once passed keeps passing. Forecast rows for reads carry a metric instead of a power figure; they count as rows.

## As implemented and probed (2026-11-24)

The announcement is in strategy-log-1124c.md (10:23Z) and the switch is `coordination.queue.require_forecast: true` (branch `land/forecast-flip`). Steer A's probe in a scratch queue root with the real 181-row ledger: a serves of an imaginary plan item is refused, a unit with no serves line is refused, `upkeep` and `PL-17` pass, and the emergency path `--no-require-forecast` passes. The rule is strict: the serves line is split on commas and semicolons and each part must be a ledger plan item id, an exempt word or the fill-idle-slot pattern, so `PL-17, PL-08` passes and `PL-17 the Oil Well chain` is refused. All 51 inbox units classify ok.

Live since 2026-11-24T10:48:40Z (PR 959, merge b341250ac): the live TEAM.yaml 0.7.5 carries the switch and `queue.py validate` reads 'pool valid' for the planner's 51 units. A unit that serves a new plan item needs its ledger row first.

