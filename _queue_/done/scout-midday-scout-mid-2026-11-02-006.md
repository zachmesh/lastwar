---
unit: scout-midday-scout-mid-2026-11-02-006
regular: scout-midday
activity: perception-scout
segment:
priority: 2
created_at: 2026-11-04T17:18:45Z
expires_at:
planned_for:
not_before:
window: scout-alliance remainder: station panel, loot box re-check
est_minutes: 10
chain_id: scout-mid-2026-11-02
chain_seq: 6
attempts: 1
max_attempts: 3
claimed_by: ticker-1404
claimed_at: 2026-11-05T22:07:32Z
lease_until: 2026-11-05T22:27:32Z
result:
  status: failed
  started_at: 2026-11-05T22:07:32Z
  finished_at: 2026-11-05T22:09:53Z
  duration_seconds: 141
  executor: ticker-1404
  summary: Mac mini offline, no wake-up path; no game screen read, no input dispatched (Issue 284, 49th consecutive pass)
  claimed: [none]
  claimed_count: 1
  evidence: _records_/2026-11-05/perception-scout/1404-queue-run.md
  follow_up: none
  stats:
    target: 1
    achieved: 0
    resources_gained: none
    costs: no_game_input
    verified: no
    blocker_category: e
    device_takeovers: 0
    capture_attempts: 4
    issue: 284
  stats_missing: []
  stats_warnings: []
---

# scout-midday

Produced by tools/queue.py. The executor reads the activity metadata and the standing rules before acting.
