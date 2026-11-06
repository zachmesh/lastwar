---
unit: daily-missions-2026-11-04-1800
regular: daily-missions
activity: daily-missions
segment: 3
priority: 3
created_at: 2026-11-05T09:05:05Z
expires_at: 2026-11-06T02:00:00Z
planned_for: 2026-11-05T02:00:00Z
not_before:
window:
est_minutes: 5
chain_id:
chain_seq:
attempts: 1
max_attempts: 3
claimed_by: ticker-1734
claimed_at: 2026-11-06T01:38:58Z
lease_until: 2026-11-06T01:58:58Z
result:
  status: failed
  started_at: 2026-11-06T01:38:58Z
  finished_at: 2026-11-06T01:41:34Z
  duration_seconds: 156
  executor: ticker-1734
  summary: Mac mini offline, no wake-up path; no screen read, no mission claimed (56th consecutive access-blocked pass, Issue 284)
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-05/daily-missions/1734-queue-run.md
  follow_up: none
  stats:
    target: 1
    achieved: 0
    resources_gained: none
    costs: duration_about_9m
    verified: no
    blocker_category: e
    follow_up: Issue_284
  stats_missing: []
  stats_warnings: []
---

# daily-missions

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.
