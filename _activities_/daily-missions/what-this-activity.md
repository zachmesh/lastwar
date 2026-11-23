---
title: What this activity is and 1 more
created: 2026-11-23T07:18:16Z
modified: 2026-11-23T07:18:16Z
version: 0.1.0
sequence: 2
description: Working the Mission daily task list to raise activity points and claim the activity chests.
---
## What this activity is

Working the Mission daily task list to raise activity points and claim
the activity chests. This folder accumulates mission knowledge - the task
set, point values and chest thresholds. Executions are recorded in
`_records_/<date>/daily-missions/`, one file per execution.

## How it is done

- Open Mission from the orange terminal on the base screen.
- Claim with ONE tap on a completed row's Claim button: the tap claims every completed row in view at once (verified 2026-11-09 1519, fourth observation, before/after reads), then re-check the list - claimed rows sink to the bottom with green checks and the list reorders to unclaimed rows. Do not keep tapping Claim buttons on the reordered list without a fresh read: a tap can land on a Go button after the reorder (2026-10-25 warning).
- Claim the activity chests when their thresholds are reached.
- Tasks that need PvP, stamina combat or a gathering march are reported
  as not done, not silently skipped.

