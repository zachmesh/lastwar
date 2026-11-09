---
unit: scout-scout-discovery-2026-11-09-015
regular: scout
activity: total-power-149217331
segment: 1
priority: 2
created_at: 2026-11-09T16:43:44Z
expires_at:
planned_for:
not_before:
window: scout 2026-11-09 - exploration - total-power-149217331 - Total Power 149217331 - read-only learning, red lines learn-only
est_minutes: 8
chain_id: scout-discovery-2026-11-09
chain_seq: 15
attempts: 1
max_attempts: 3
claimed_by: ticker-1134
claimed_at: 2026-11-09T19:48:47Z
lease_until: 2026-11-09T20:08:47Z
result:
  status: done
  started_at: 2026-11-09T19:48:47Z
  finished_at: 2026-11-09T19:50:01Z
  duration_seconds: 74
  executor: ticker-1134
  summary: Total Power 149217331 verified live twice in this pass (11:36 and 11:46 PT, unchanged, matches observation); known HUD figure, not a candidate task; 472287 below the 2026-10-25 baseline, does not match Issue 482 641100 step-down - fresh reads commented on #482
  claimed: [none]
  claimed_count: 1
  evidence: _records_/2026-11-09/total-power-149217331/1149-queue-run.md
  follow_up: none
  stats:
    target: learn-total-power-profile-fields
    achieved: 1
    resources_gained: none
    costs: about-3-minutes-no-game-session
    verified: yes
    blocker_category: none
    points: 0
    surfaces_walked: none-reused-unit-014-live-reads
    items_observed: 1
    red_dots_seen: 0
    red_dots_explained: 0
    unexplained_red_dots: 0
    unknown_items: 0
  stats_missing: []
  stats_warnings: []
---

# scout

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.
