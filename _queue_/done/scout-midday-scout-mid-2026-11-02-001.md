---
unit: scout-midday-scout-mid-2026-11-02-001
regular: scout-midday
activity: perception-scout
segment:
priority: 2
created_at: 2026-11-02T21:53:41Z
expires_at:
planned_for:
not_before:
window:
est_minutes: 10
chain_id: scout-mid-2026-11-02
chain_seq: 1
attempts: 1
max_attempts: 3
claimed_by: ticker-0104
claimed_at: 2026-11-05T09:05:15Z
lease_until: 2026-11-05T09:25:15Z
result:
  status: failed
  started_at: 2026-11-05T09:05:15Z
  finished_at: 2026-11-05T09:06:07Z
  duration_seconds: 52
  executor: ticker-0104
  summary: Mac screen capture failure (Issue 284), 25th consecutive pass; no game screen read, no input dispatched
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-05/perception-scout/0104-queue-run.md
  follow_up: none
  stats:
    target: 1
    achieved: 0
    resources_gained: none
    costs: about-3-minutes-executor-time-no-stamina-or-items
    verified: no
    blocker_category: f
  stats_missing: []
  stats_warnings: []
---

# scout-midday

Produced by tools/queue.py. The executor reads the activity metadata and the standing rules before acting.
