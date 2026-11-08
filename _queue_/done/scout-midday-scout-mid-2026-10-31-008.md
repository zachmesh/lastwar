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
claimed_by: ticker-0104
claimed_at: 2026-11-08T09:08:03Z
lease_until: 2026-11-08T09:28:03Z
result:
  status: partial
  started_at: 2026-11-08T09:08:03Z
  finished_at: 2026-11-08T09:11:50Z
  duration_seconds: 227
  executor: ticker-0104
  summary: Station check: no train preparing (no left-column train icon, no Boarding closes in banner); sixth no-train confirmation in chain; closed partial without panning; successor seq 009 enqueued
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-08/perception-scout/0118-queue-run.md
  follow_up: successor scout-midday-scout-mid-2026-10-31-009 enqueued for station panel re-check
  stats:
    surfaces_walked: 1
    items_observed: 12
    red_dots_seen: 8
    red_dots_explained: 6
    unexplained_red_dots: 2
    unknown_items: 2
    target: 1
    achieved: 0
    resources_gained: none
    costs: duration about 5 minutes, no items spent
    verified: yes
    blocker_category: h
  stats_missing: []
  stats_warnings: []
---

# scout-midday

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.
