---
title: A. Execution efficiency, per task type
created: 2026-11-23T08:36:55Z
modified: 2026-11-23T08:36:55Z
version: 0.1.0
sequence: 2
description: Per regular, per day and rolling 7 days.
---
## A. Execution efficiency, per task type

Per regular, per day and rolling 7 days. Source - the unit
results in `_queue_/done` (fields `result.status`,
`result.duration_seconds`, `result.attempts`,
`result.stats.target`, `result.stats.achieved`,
`result.stats.resources_gained`, `result.stats.points`,
`result.stats.costs`, `result.stats.verified`,
`result.stats.blocker_category`), read through the canonical
appendix `_records_/retro/<date>-data.json` - the per-regular
`rolling` and `by_day` summaries under `regulars.<regular>`.

- **Duration median and p90** - median and 90th percentile of
  `duration_seconds` over the window's executions. Both are
  emitted today (`duration_median_seconds` and
  `duration_p90_seconds`, nearest-rank) by
  `_tools_/retro_report.py` 1.4.0 (PR #30, merged 2026-11-01).
- **Attempts** - mean and maximum of attempts per execution, and
  the share of executions that needed more than one attempt
  (`attempts_mean`, `attempts_max`, share over 1), emitted today
  by `_tools_/retro_report.py` 1.4.0 (PR #30, merged 2026-11-01).
  Attempts are read from the unit's top-level `attempts` field,
  which queue.py increments on claim; `result.attempts` is a
  fallback only - the live pool carries attempts only at top
  level, never under result. Units without a result contribute
  no attempts figure, never an invented zero.
- **Done rate** - done over executions, from `statuses`.
- **Target attainment** - `attainment_summed` (summed achieved
  over summed target) and `attainment_mean_ratio`, over the
  units that carried both keys (`attainment_units` is the
  denominator and is always reported beside the ratio).
- **Resource yield** - `resources_gained` itemised by resource,
  per execution and per minute (`resources_per_minute`). Free
  text that does not parse is counted in
  `resources_unparsed_count`, never dropped silently.
- **Points per minute** - `points_per_minute`, for the scoring
  types that report `points`.
- **Unverified rate** - `unverified` over executions, with
  `unverified_reasons` split (verified not yes, missing
  required stats, missing result) and `missing_key_counts`
  naming which keys the pool is failing to produce.

Thresholds - no universal attainment line; attainment is read
per type against its own history. For the quota types with a
hard daily target (trucks, donations) a rolling attainment
under 0.8 is named. The unverified rate is thresholded under
Monitoring below.

Known defects - units executed before the section 14 stats
specification landed (2026-11-01) are legacy-shaped and count
as unverified almost by definition; early windows are dominated
by them, so every unverified figure is read together with the
legacy share of its window. Attainment is undefined for types
whose units carry no numeric target; those types report
attainment_units 0 and are judged on done rate and yield.

