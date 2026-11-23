---
title: 6. Queue genesis on this Mac
created: 2026-11-23T07:20:36Z
modified: 2026-11-23T07:20:36Z
version: 0.1.0
sequence: 11
description: The 766-unit snapshot is queue debt, not a work plan, and it is not the old
---
## 6. Queue genesis on this Mac

The 766-unit snapshot is queue debt, not a work plan, and it is not the
old live pool. The first planner passes apply this genesis protocol, in
order:

1. **Freeze** - stop staging new units except the current and next
   window. Record the inbox, claimed and done counts before any move.
   On 2026-11-22 the measured state was inbox 766, claimed 0, done 2,310.
2. **Retire** - every inbox unit whose window ended before the
   current reset is closed `expired`, with the count and the oldest
   date in the planner record. A unit is not executed merely because
   it is old. Units whose window is current or future are kept.
3. **Reset** - the regular schedule restarts at the next slot after
   the current time. Missed cycles are not backfilled; the ledger
   records them as missed with the reason. The genesis timestamp is
   the current reset, not the snapshot date.
4. **Reconcile** - the live tree and the delivered records branch
   are compared for the same day before any new close. A split is
   recorded and repaired on the branch side, never by force.
5. **Prove** - `queue.py validate`, `sync`, `slot_coverage.py` and
   `sweep-status` run at the end of the pass, and their outputs are
   in the planner record.

