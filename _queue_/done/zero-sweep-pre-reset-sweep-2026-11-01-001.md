---
unit: zero-sweep-pre-reset-sweep-2026-11-01-001
regular: zero-sweep
activity: daily-activities
segment: 3
priority: 1
created_at: 2026-11-01T05:01:56Z
expires_at: 2026-11-02T03:00:00Z
planned_for:
not_before: 2026-11-02T01:30:00Z
window: pre-reset zero sweep, first pass
est_minutes: 15
chain_id: pre-reset-sweep-2026-11-01
chain_seq: 1
attempts: 1
max_attempts: 3
claimed_by: ticker-1738
claimed_at: 2026-11-02T01:45:22Z
lease_until: 2026-11-02T02:05:22Z
result:
  status: partial
  started_at: 2026-11-02T01:45:22Z
  finished_at: 2026-11-02T01:52:57Z
  duration_seconds: 455
  executor: ticker-1738
  summary: First zero sweep partial: harvest bubbles standing, trucks 4/5 and 1/4 last live, VIP never attempted today, missions 150 with 160/200 ahead; 2 priority-1 fix-ups enqueued expiring at reset
  claimed: [none]
  claimed_count: 1
  evidence: _records_/2026-11-01/daily-activities/1757-queue-run.md
  follow_up: none
  stats:
    lines_walked: 23
    lines_not_at_zero: 11
    lines_unreadable: 6
    fixups_enqueued: 2
    target: 23
    verified: no
    blocker_category: c
---

# zero-sweep

Produced by tools/queue.py. The executor reads the activity metadata and the standing rules before acting.

## Task - pre-reset zero sweep, first pass (17:30 local)

Read `_conventions_/local-conventions/daily-collection-ledger.md`
first. This is the first of the two zero sweeps before the 19:00
local reset that ends the 2026-11-01 trade and reset day (queue
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
