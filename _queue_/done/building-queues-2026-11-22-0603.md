---
unit: building-queues-2026-11-22-0603
regular: building-queues
activity: building-queues
segment: 1
priority: 3
created_at: 2026-11-22T16:13:29Z
expires_at: 2026-11-22T18:03:00Z
planned_for: 2026-11-22T14:03:00Z
not_before:
window:
est_minutes: 5
chain_id:
chain_seq:
attempts: 1
max_attempts: 3
claimed_by: ticker-0957
claimed_at: 2026-11-22T18:12:02Z
lease_until: 2026-11-22T18:32:02Z
result:
  status: done
  started_at: 2026-11-22T18:12:02Z
  finished_at: 2026-11-22T18:13:15Z
  duration_seconds: 73
  executor: ticker-0957
  summary: All 4 build queues read live: Drill Ground Lv.25 upgrade 07:12:47 left, slots 2-4 idle; nothing started
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/building-queues/1012-queue-run.md
  follow_up: none
  stats:
    target: 4
    achieved: 4
    resources_gained: none
    costs: 5min
    verified: yes
    blocker_category: none
  stats_missing: []
  stats_warnings: [blocker_category not in enum a-i]
---

# building-queues

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.
