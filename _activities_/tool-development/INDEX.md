---
title: Tool Development
created: 2026-11-01T05:38:00Z
modified: 2026-11-01T05:38:00Z
level: L1
version: 1.0.0
description: The tool developer - building and fixing the tools the loop runs on, from the improvement backlog and the review feedback the integrator leaves
status: active
grounded_in:
  - source: owner direction of 2026-10-31 - improvement tasks after the retro, a tool developer to work them, and hourly feedback fixing
  - source: ops execution records standard in the local conventions
---

# Tool development

## What this activity is

The loop's builder. It takes the tooling improvement tasks
the retro files, and the numbered review feedback the PR
integrator leaves on tool branches, and turns them into
working, validated tools in `tools/`. It does not operate the
game and never touches the live queue pool beyond reading it.

## Cadence

Hourly, as the standing job `lastwar-tool-developer`. Feedback
order each run: unaddressed integrator review points on tool
PRs first, then the tooling backlog by leak size, then the
standing tool queue in the design documents.

## Inputs

- Open PRs and their integrator reviews (through the VPS `gh`
  route).
- The tooling entries of `_records_/retro/improvements.md`.
- The tool sections of the queue design, the perception
  design and the evaluation metrics specification.

## Outputs

- Tool code and its documentation, delivered on a
  `work/<slug>` branch through a PR under the two-tier push
  policy, with the target metric and the validation result in
  the PR body.
- Backlog entries moved to implemented - never closed;
  closure belongs to the retro, on metric movement.
- Its own execution record at
  `_records_/<date>/tool-development/<HHMM>-run.md`, per the
  [ops execution records](../../_conventions_/local-conventions/ops-execution-records.md)
  standard - including the no-op record of a quiet hour.

## Red lines

- Standard library only, following the existing tools'
  conventions; validation runs on an isolated scratch pool
  under /tmp, never against the live pool.
- Never edits a cron definition, never force-pushes, never
  marks its own work closed.
