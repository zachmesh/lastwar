---
unit: daily-missions-2026-11-05-1800
regular: daily-missions
activity: daily-missions
segment: 3
priority: 3
created_at: 2026-11-06T02:43:02Z
expires_at: 2026-11-07T02:00:00Z
planned_for: 2026-11-06T02:00:00Z
not_before:
window:
est_minutes: 5
chain_id:
chain_seq:
attempts: 1
max_attempts: 3
claimed_by: ticker-1604
claimed_at: 2026-11-07T00:07:46Z
lease_until: 2026-11-07T00:27:46Z
result:
  status: failed
  started_at: 2026-11-07T00:07:46Z
  finished_at: 2026-11-07T00:12:10Z
  duration_seconds: 264
  executor: ticker-1604
  summary: Mac mini offline, no wake-up path, node_offline on 3 session attempts plus recovery timeouts; no game screen read, no mission claimed; same blocker as Issue 284
  claimed: [none]
  claimed_count: 1
  evidence: _records_/2026-11-06/daily-missions/1612-queue-run.md
  follow_up: none
  stats:
    target: 1
    achieved: 0
    resources_gained: none
    costs: no_game_input
    verified: no
    blocker_category: e
    device_takeovers: 0
    capture_attempts: 7
    issue: 284
  stats_missing: []
  stats_warnings: []
---

# daily-missions

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.
