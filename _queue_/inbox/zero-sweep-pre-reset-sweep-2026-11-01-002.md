---
unit: zero-sweep-pre-reset-sweep-2026-11-01-002
regular: zero-sweep
activity: daily-activities
segment: 3
priority: 1
created_at: 2026-11-01T05:01:56Z
expires_at: 2026-11-02T03:00:00Z
planned_for:
not_before: 2026-11-02T02:30:00Z
window: pre-reset zero sweep, final pass
est_minutes: 15
chain_id: pre-reset-sweep-2026-11-01
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
first, and the record of the first sweep pass (unit
zero-sweep-pre-reset-sweep-2026-11-01-001) before starting. This
is the final zero sweep before the 19:00 local reset that ends
the 2026-11-01 trade and reset day (queue design section 12).

Walk the ledger item by item again - all 23 lines - verifying
live that each line is now at zero, including every line the
first pass found short and every fix-up unit it enqueued.

- A line still not at zero - work out why in the record, enqueue
  a priority 1 unit of its own type expiring at the reset where
  the window still allows one, and name the shortfall for the
  round summary. A quota line short at this pass is a miss in
  the making and is reported as such tonight, not tomorrow.
- A line still unreadable - it closes the day as unverified and
  is named in the round summary as unverified, under rule R1.
- The owner-named open items (crystal, Glittering Market) are
  named with their ages whether or not they moved - rule R5.

Record the execution under `_records_` for the daily-activities
activity as the final sweep record, with the closing state of
every ledger line for the day.
