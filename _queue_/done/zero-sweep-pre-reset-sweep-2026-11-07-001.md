---
unit: zero-sweep-pre-reset-sweep-2026-11-07-001
regular: zero-sweep
activity: daily-activities
segment: 3
priority: 1
created_at: 2026-11-07T09:30:26Z
expires_at: 2026-11-08T03:00:00Z
planned_for:
not_before: 2026-11-08T01:30:00Z
window: pre-reset zero sweep, first pass
est_minutes: 15
chain_id: pre-reset-sweep-2026-11-07
chain_seq: 1
attempts: 0
max_attempts: 3
claimed_by:
claimed_at:
lease_until:
result:
  status: expired
  started_at: 
  finished_at: 2026-11-08T03:06:08Z
  duration_seconds: 
  executor: 
  summary: window passed before execution
  claimed: []
  claimed_count: 0
  evidence: 
  follow_up: none
  stats:
---

# zero-sweep

Produced by tools/queue.py. The executor reads the activity metadata and the standing rules before acting.

## Task - pre-reset zero sweep, first pass (17:30 local)

Read `_conventions_/local-conventions/daily-collection-ledger.md`
first. This is the first of the two zero sweeps before the 19:00
local reset that ends the 2026-11-07 trade and reset day (queue
design section 12).

Walk the ledger item by item - all 23 lines. For each line, read
its state live and record one of three outcomes in the sweep
record - at zero, not at zero, or unreadable.

- A line not at zero - enqueue a priority 1 unit of that line own
  type before this sweep closes, and name it in the record. Do
  not do another type work inside this unit - one unit, one task
  type. The fix-up units run between this sweep and the final
  sweep at 18:30.
- A line unreadable - close it as unverified under rule R1 and
  name it in the record; the final sweep reads it again.
- Lines with no producing unit and the owner-named open items
  (crystal, Glittering Market) are reported by name and age, not
  skipped - rule R5.

Record the execution under `_records_` for the daily-activities
activity as the sweep record of this pass, listing every line
outcome and every fix-up unit enqueued.
