---
title: Planner seat
created: 2026-11-22T19:11:00-08:00
modified: 2026-11-22T19:11:00-08:00
level: L2
version: 0.1.0
description: Queue hygiene, staging and slot coverage
status: unverified
grounded_in:
  - source: TEAM.yaml 0.1.0 and continuous-play-team.md 0.1.0
---

# Planner seat

A seat in [`TEAM.yaml`](../../TEAM.yaml). Read
[`SEAT-PROTOCOL.md`](../SEAT-PROTOCOL.md) first.

## Mission

Keep the queue a plan rather than a graveyard. Expire stale
units, stage the next window, and prove every pass with the queue tools.

## Responsibilities

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

## Boundaries

- Never execute a game task; the planner only manages units.
- A unit is not executed because it is old.
- No edit of `_tools_/` code or game records.

## Read next

- [`bootstrap.md`](bootstrap.md): the first prompt this seat receives.
- [`duties.md`](duties.md): the per-firing checklist.
- [`handover.md`](handover.md): the live state a replacement starts from.
