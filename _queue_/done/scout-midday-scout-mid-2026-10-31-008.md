---
unit: scout-midday-scout-mid-2026-10-31-008
regular: scout-midday
activity: perception-scout
segment:
priority: 2
created_at: 2026-11-08T05:41:13Z
expires_at:
planned_for:
not_before:
window: scout-alliance remainder: station panel - check the two preparation signals first (left-column train icon, Boarding closes in banner); if neither present, close partial without panning; R2 metadata change landed 2026-11-07
est_minutes: 10
chain_id: scout-mid-2026-10-31
chain_seq: 8
attempts: 1
max_attempts: 3
claimed_by: ticker-2304
claimed_at: 2026-11-08T07:13:12Z
lease_until: 2026-11-08T07:33:12Z
result:
  status: partial
  started_at: 2026-11-08T07:13:12Z
  finished_at: 2026-11-08T07:14:10Z
  duration_seconds: 58
  executor: ticker-2304
  summary: Station panel re-check: both train-preparation signals absent (no train icon, no boarding banner), fifth confirmation this pass; closed without panning, no successor
  claimed: [none]
  claimed_count: 1
  evidence: _records_/2026-11-07/perception-scout/2317-queue-run.md
  follow_up: none
  stats:
    target: 2
    achieved: 2
    resources_gained: none-observe-only
    costs: about-2-minutes-device-time
    verified: yes
    blocker_category: h
    surfaces_walked: 1
    items_observed: 3
    red_dots_seen: 5
    red_dots_explained: 0
    unexplained_red_dots: 5
    unknown_items: 1
  stats_missing: []
  stats_warnings: []
---

# scout-midday

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.
