---
title: Planner seat duties
created: 2026-11-22T19:11:00-08:00
modified: 2026-11-22T19:11:00-08:00
level: L2
version: 0.1.0
description: The per-firing checklist for this seat
status: unverified
grounded_in:
  - source: TEAM.yaml 0.1.0 and continuous-play-team.md 0.1.0
---

# Duties - planner

## Each pass

1. Snapshot inbox, claimed and done counts and the oldest inbox unit.
2. Run `reap`, then `sync`; record reaped and expired counts by reason.
3. Apply the recovery protocol while the establishment is open: retire every
   unit whose window ended before the current reset, and do not backfill
   missed cycles.
4. Stage the next window only; no catch-up flood.
5. Run `validate`, `slot_coverage.py check` and `sweep-status`; record their
   exit codes.
6. Write the planner record and update the queue state.

## Record

Write the run at `_records_/<date>/<activity>/<HHMM>-run.md` and append the
day index. The record carries inputs, outputs, stats and follow-up.
