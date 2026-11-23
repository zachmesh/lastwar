---
title: Changelog part 8
created: 2026-11-23T09:03:48Z
modified: 2026-11-23T09:03:48Z
version: 0.1.0
sequence: 62
description: 0.10.0, 2026-11-01 - Phase 2 of the perception layer landed in section 13 - _tools_/scout_diff.py implemented
---
- 0.10.0, 2026-11-01 - Phase 2 of the perception layer landed
  in section 13 - `_tools_/scout_diff.py` implemented (dry run by
  default, `--apply` only against an explicitly named pool
  root, scratch-pool validated), the scout and scout-midday
  production priorities and estimate seeds recorded as landed
  in `_tools_/queue.py`, and the learning and knowledge hardening
  protocol of the perception document (its section 10)
  referenced, with radar-tasks as the first retrospective
  hardening target. Section 14 added under the owner direction
  of 2026-10-31 - the retro review mechanism: the repository as
  the single source of truth for this game line, the required
  per-unit result stats keys (target, achieved,
  resources_gained, points, costs, verified, blocker_category
  in the miss audit classes), the aggregation specification
  for a later `_tools_/retro_report.py` writing only into
  `_records_/retro/`, and the daily rolling retro whose
  improvement actions split into execution knowledge and meta
  knowledge, each carrying a verification method and a next-day
  recheck.
- 0.9.0, 2026-11-01 - section 13 extended under the owner
  refinement of 2026-10-31 - scheduling is trigger-based rather
  than fixed-slot, the regulars repositioned as a capability
  profile library, the planner evolution from slot staging to
  consuming observations plus profile triggers, perception
  points as a floor under rolling and change-triggered passes,
  and the new task discovery protocol with its candidate state
  machine and unmatched labels coverage; the perception-driven
  queue design rises to version 1.1.0 alongside.
- 0.8.0, 2026-11-01 - section 13 added under the owner direction
  of 2026-10-31 for perception-driven daily tasks - the scout
  unit type, its chain splitting, the observation output and its
  result contract, referencing the new perception-driven queue
  design document.
