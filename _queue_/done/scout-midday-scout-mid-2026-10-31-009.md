---
unit: scout-midday-scout-mid-2026-10-31-009
regular: scout-midday
activity: perception-scout
segment:
priority: 2
created_at: 2026-11-08T09:11:51Z
expires_at:
planned_for:
not_before:
window: scout-alliance remainder: station panel - check the two preparation signals first (left-column train icon, Boarding closes in banner); if neither present, close partial without panning
est_minutes: 10
chain_id: scout-mid-2026-10-31
chain_seq: 9
attempts: 1
max_attempts: 3
claimed_by: ticker-0434
claimed_at: 2026-11-08T12:36:36Z
lease_until: 2026-11-08T12:56:36Z
result:
  status: partial
  started_at: 2026-11-08T12:36:36Z
  finished_at: 2026-11-08T12:38:49Z
  duration_seconds: 133
  executor: ticker-0434
  summary: Scout station re-check partial: both train-preparation signals absent, no train preparing, no pan per window instruction; base HUD read live, red dots 11 seen 11 explained 0 unexplained; chain spent, no successor
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-08/perception-scout/0440-queue-run.md
  follow_up: none
  stats:
    target: 2
    achieved: 2
    resources_gained: none
    verified: yes
    costs: about 8 min, no items
    surfaces_walked: 1
    items_observed: 12
    red_dots_seen: 11
    red_dots_explained: 11
    unexplained_red_dots: 0
    unknown_items: 4
    blocker_category: h
  stats_missing: []
  stats_warnings: []
---

# scout-midday

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.
