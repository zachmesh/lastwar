---
title: Alignment of the existing activities
created: 2026-11-23T08:38:24Z
modified: 2026-11-23T08:38:24Z
version: 0.1.0
sequence: 7
description: Ticker - already aligned - its executions are the task units and their per-unit record files.
---
## Alignment of the existing activities

- **Ticker** - already aligned: its executions are the task
  units and their per-unit record files.
- **Planner** - not yet aligned: its run log lives outside the
  repository, in the goal workspace, so its run rate is
  proxied by the units it produces (evaluation metrics family
  G states this defect). Mirroring the planner log into
  `_records_/<date>/planner/` in this shape is the migration
  item; it is deliberately not forced in the change that
  introduces this standard, because the planner job's own
  instructions must change with it and that change is
  scheduled work, not a document edit.
- **Knowledge organiser** - partially aligned: its dated note
  under `_records_/knowledge-organizer/` carries most of the
  counts but not the field shape. New runs record under
  `_records_/<date>/knowledge-organization/` in this shape;
  the note series stays as history.
- **Retro, tool developer, PR integrator** - aligned from this
  standard forward; their earlier runs are reconstructed where
  evidence survives, marked `verified: reconstructed`, with
  unrecoverable fields written `unknown` - never invented.

