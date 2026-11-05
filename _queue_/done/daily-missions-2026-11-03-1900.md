---
unit: daily-missions-2026-11-03-1900
regular: daily-missions
activity: daily-missions
segment: 3
priority: 3
created_at: 2026-11-03T15:41:38Z
expires_at: 2026-11-05T03:00:00Z
planned_for: 2026-11-04T03:00:00Z
not_before: 2026-11-04T03:00:00Z
window:
est_minutes: 5
chain_id:
chain_seq:
attempts: 1
max_attempts: 3
claimed_by: ticker-0904
claimed_at: 2026-11-04T17:06:32Z
lease_until: 2026-11-04T17:26:32Z
result:
  status: partial
  started_at: 2026-11-04T17:06:32Z
  finished_at: 2026-11-04T17:10:40Z
  duration_seconds: 248
  executor: ticker-0904
  summary: Claimed 3 gather tasks (activity 180 to 210) and the 200-point chest with receipt; 8 tasks remain incomplete, tracker untouched
  claimed: [gather-food, gather-iron, gather-coin, activity-chest-200]
  claimed_count: 4
  evidence: _records_/2026-11-04/daily-missions/0914-queue-run.md
  follow_up: none
  stats:
    target: 4
    achieved: 4
    points: 30
    resources_gained: activity +30; chest: gold bar x1, red gem x50, wrench x1, flower x1, crate x1, Crystal Ore 2.0K, 5m speed-up x4
    costs: no stamina, no items
    verified: yes
    blocker_category: h
---

# daily-missions

Produced by tools/queue.py. The executor reads the activity metadata and the standing rules before acting.
