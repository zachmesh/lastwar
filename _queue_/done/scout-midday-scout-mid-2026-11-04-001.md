---
unit: scout-midday-scout-mid-2026-11-04-001
regular: scout-midday
activity: perception-scout
segment:
priority: 2
created_at: 2026-11-04T17:11:49Z
expires_at:
planned_for:
not_before:
window:
est_minutes: 10
chain_id: scout-mid-2026-11-04
chain_seq: 1
attempts: 1
max_attempts: 3
claimed_by: ticker-1334
claimed_at: 2026-11-05T21:36:04Z
lease_until: 2026-11-05T21:56:04Z
result:
  status: failed
  started_at: 2026-11-05T21:36:04Z
  finished_at: 2026-11-05T21:38:46Z
  duration_seconds: 162
  executor: ticker-1334
  summary: Mac mini offline (Issue 284), 48th consecutive pass; no game screen read, no input dispatched
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-05/perception-scout/1334-queue-run.md
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
