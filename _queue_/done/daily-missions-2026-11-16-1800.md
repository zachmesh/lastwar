---
unit: daily-missions-2026-11-16-1800
regular: daily-missions
activity: daily-missions
segment: 3
priority: 3
created_at: 2026-11-16T14:22:53Z
expires_at: 2026-11-18T02:00:00Z
planned_for: 2026-11-17T02:00:00Z
not_before: 2026-11-17T02:00:00Z
window:
est_minutes: 12
chain_id:
chain_seq:
attempts: 2
max_attempts: 3
claimed_by: ticker-1704
claimed_at: 2026-11-18T01:10:50Z
lease_until: 2026-11-18T01:30:50Z
result:
  status: failed
  started_at: 2026-11-18T01:10:50Z
  finished_at: 2026-11-18T01:20:36Z
  duration_seconds: 586
  executor: ticker-1704
  summary: Game window missing: control channel cannot bind any window (geometry_mismatch agent_display=false); LastWar windowless, 23rd consecutive ticker process failure; no game input sent
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-17/queue-ticker/1704-process-failure.md
  follow_up: none
  stats:
    target: claim completed daily missions and activity chests
    achieved: no game access; window missing
    resources_gained: none
    costs: about 15 minutes device probing, no stamina or items
    verified: yes
    blocker_category: f
  stats_missing: []
  stats_warnings: []
---

# daily-missions

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.
