---
unit: daily-missions-2026-11-14-1800
regular: daily-missions
activity: daily-missions
segment: 3
priority: 3
created_at: 2026-11-14T14:44:59Z
expires_at: 2026-11-16T02:00:00Z
planned_for: 2026-11-15T02:00:00Z
not_before: 2026-11-15T02:00:00Z
window:
est_minutes: 12
chain_id:
chain_seq:
attempts: 1
max_attempts: 3
claimed_by: ticker-1504
claimed_at: 2026-11-15T23:14:08Z
lease_until: 2026-11-15T23:34:08Z
result:
  status: failed
  started_at: 2026-11-15T23:14:08Z
  finished_at: 2026-11-15T23:16:57Z
  duration_seconds: 169
  executor: ticker-1504
  summary: Mac mini offline, 4 device probes all node_offline, no wake-up path; no daily missions claimed
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-15/daily-missions/1504-queue-run.md
  follow_up: none
  stats:
    target: claim daily missions
    achieved: no missions claimed; device unreachable
    resources_gained: none
    costs: about 5 minutes device probing, no stamina or items
    verified: yes
    blocker_category: f
  stats_missing: []
  stats_warnings: []
---

# daily-missions

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.
