---
unit: daily-missions-2026-11-21-1800
regular: daily-missions
activity: daily-missions
segment: 3
priority: 3
created_at: 2026-11-21T14:34:23Z
expires_at: 2026-11-23T02:00:00Z
planned_for: 2026-11-22T02:00:00Z
not_before: 2026-11-22T02:00:00Z
window:
est_minutes: 12
chain_id:
chain_seq:
attempts: 1
max_attempts: 3
claimed_by: ticker-1504
claimed_at: 2026-11-22T23:14:28Z
lease_until: 2026-11-22T23:34:28Z
result:
  status: partial
  started_at: 2026-11-22T23:14:28Z
  finished_at: 2026-11-22T23:20:52Z
  duration_seconds: 384
  executor: ticker-1504
  summary: 6 completed rows claimed on one tap, activity 0 to 90, 40 and 80 chests claimed; remaining tasks belong to other regulars
  claimed: [activity 90, 40-chest receipt, 80-chest contents]
  claimed_count: 3
  evidence: _records_/2026-11-22/daily-missions/1504-queue-run.md
  follow_up: none
  stats:
    target: claim all completed daily tasks and every reachable activity chest
    achieved: 6 completed rows claimed on one tap, activity 0 to 90, 40 and 80 chests claimed
    resources_gained: 40-chest receipt gear x6 rocket x1 wrench x2 blue crate x10 food crate x10 gold x6 Crystal Ore 1.6K 5m speedup x5 plus 80-chest contents by cascade
    costs: about 5 minutes device time, no spend, no items
    activity_before: 0
    activity_after: 90
    rows_claimed: 6
    chests_claimed: 2
    verified: yes
    blocker_category: h
---

# daily-missions

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.
