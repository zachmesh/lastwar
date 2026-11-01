---
title: Retro Review
created: 2026-11-01T05:38:00Z
modified: 2026-11-01T05:38:00Z
level: L1
version: 1.0.0
description: The daily retro pass - measuring the past 7 days of executions, naming the top leaks, and filing the improvement tasks the loop then works
status: active
grounded_in:
  - source: owner direction of 2026-10-31 - a daily retro with improvement tasks, and the loop activities recorded as executions
  - source: task unit queue design section 14, the retro review mechanism
  - source: ops execution records standard in the local conventions
---

# Retro review

## What this activity is

The loop's measuring and judging pass. Once a day it reads the
past 7 days of executions - game units and ops runs alike -
computes the evaluation metrics, names the top leaks, checks
the loop's own health, and files every improvement as a
tracked task in the improvements backlog for the tool developer
and the knowledge organiser to work. It operates nothing in
the game.

## Cadence

Daily, after the 19:00 local reset round (about 20:39 local),
as the standing job `lastwar-daily-retro`.

## Inputs

- The done pool and the execution records of the window,
  through `tools/retro_report.py`.
- The ops execution records of the loop activities
  (tool-development, knowledge-organization, pr-integration,
  and its own previous runs).
- The improvements backlog, the evaluation metrics
  specification, and the previous retro file.

## Outputs

- The dated retro file, its data appendix and the rolling
  file under `_records_/retro/`.
- Improvement tasks filed, re-prioritised, verified or closed
  in `_records_/retro/improvements.md`.
- Execution-knowledge corrections written back into activity
  profiles, through the PR flow.
- Its own execution record at
  `_records_/<date>/retro-review/<HHMM>-run.md`, per the
  [ops execution records](../../_conventions_/local-conventions/ops-execution-records.md)
  standard.

## Red lines

- Never closes an improvement on an edit alone - the target
  metric moved, or the stated verification passed.
- Never presents an incomplete aggregation as complete; a
  failed read is recorded as failed, with the gap named.
- Never operates the game, edits a cron definition, or merges
  its own tier-2 changes outside the PR flow.
