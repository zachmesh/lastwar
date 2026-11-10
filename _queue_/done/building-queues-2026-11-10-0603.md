---
unit: building-queues-2026-11-10-0603
regular: building-queues
activity: building-queues
segment: 1
priority: 3
created_at: 2026-11-10T14:38:37Z
expires_at: 2026-11-10T18:03:00Z
planned_for: 2026-11-10T14:03:00Z
not_before:
window:
est_minutes: 5
chain_id:
chain_seq:
attempts: 1
max_attempts: 3
claimed_by: ticker-0904
claimed_at: 2026-11-10T17:11:11Z
lease_until: 2026-11-10T17:31:11Z
result:
  status: done
  started_at: 2026-11-10T17:11:11Z
  finished_at: 2026-11-10T17:14:14Z
  duration_seconds: 183
  executor: ticker-0904
  summary: Building queues read live: Lv.29 Aircraft Center 1d 17:13:16 left, slots 2-4 idle, nothing started
  claimed: [none]
  claimed_count: 1
  evidence: _records_/2026-11-10/building-queues/0914-queue-run.md
  follow_up: none
  stats:
    target: queue state read live
    achieved: 4
    resources_gained: none
    costs: about 3 minutes, no items spent
    verified: yes
    blocker_category: none
  stats_missing: []
  stats_warnings: [blocker_category not in enum a-i]
---

# building-queues

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.
