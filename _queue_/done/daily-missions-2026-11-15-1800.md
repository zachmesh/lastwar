---
unit: daily-missions-2026-11-15-1800
regular: daily-missions
activity: daily-missions
segment: 3
priority: 3
created_at: 2026-11-15T14:54:54Z
expires_at: 2026-11-17T02:00:00Z
planned_for: 2026-11-16T02:00:00Z
not_before: 2026-11-16T02:00:00Z
window:
est_minutes: 12
chain_id:
chain_seq:
attempts: 1
max_attempts: 3
claimed_by: ticker-1501
claimed_at: 2026-11-16T23:01:21Z
lease_until: 2026-11-16T23:21:21Z
result:
  status: failed
  started_at: 2026-11-16T23:01:21Z
  finished_at: 2026-11-16T23:06:18Z
  duration_seconds: 297
  executor: ticker-1501
  summary: Mac mini unreachable (node_offline, no wake-up path; last seen 2026-11-15T13:19:56Z): connection.health, connection.repair, environment.describe, computer.session start all failed node_offline; no game state observable, no input sent, no claims; NOT the outcome_unknown control-lock (Issue 689), so no blocker_overlay recorded and the next tick will probe again; pass stopped after this unit
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-16/daily-missions/1501-queue-run.md
  follow_up: none
  stats:
    target: claim completed daily missions and activity chests
    achieved: no actions; Mac mini offline, no game state observable
    resources_gained: none
    costs: about 7 minutes probe, no stamina or items
    verified: no
    blocker_category: f
  stats_missing: []
  stats_warnings: []
---

# daily-missions

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.
