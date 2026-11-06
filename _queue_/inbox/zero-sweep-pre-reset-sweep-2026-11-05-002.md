---
unit: zero-sweep-pre-reset-sweep-2026-11-05-002
regular: zero-sweep
activity: daily-activities
segment: 3
priority: 1
created_at: 2026-11-06T00:09:28Z
expires_at: 2026-11-06T03:00:00Z
planned_for:
not_before: 2026-11-06T02:30:00Z
window: pre-reset zero sweep, final pass
est_minutes: 15
chain_id: pre-reset-sweep-2026-11-05
chain_seq: 2
attempts: 0
max_attempts: 3
claimed_by:
claimed_at:
lease_until:
---

# zero-sweep

Produced by tools/queue.py. The executor reads the activity metadata and the standing rules before acting.

## Task - pre-reset zero sweep, final pass (18:30 local)

Read `_conventions_/local-conventions/daily-collection-ledger.md`
first. This is the final zero sweep before the 19:00 local reset
that ends the 2026-11-05 trade and reset day (queue design
section 12). The first pass ran at 17:30; read its sweep record
before starting.

Walk the ledger item by item - all 23 lines. For each line, read
its state live and record one of three outcomes in the sweep
record - at zero, not at zero, or unreadable.

- A line still not at zero - do the line own work now if it fits
  this unit one task type limit by enqueuing a priority 1 fix-up
  unit that expires at the reset, and name it in the record; if
  it cannot complete before the reset, record it as a miss with
  its reason (rule R6) - it does not roll silently into the next
  day.
- A line unreadable in both passes - close it as unverified
  under rule R1 and name it in the record for the round summary.
- Lines with no producing unit and the owner-named open items
  (crystal, Glittering Market) are reported by name and age, not
  skipped - rule R5.

Record the execution under `_records_` for the daily-activities
activity as the final sweep record of the day, listing every line
outcome, every fix-up unit enqueued, and every miss with reason.
