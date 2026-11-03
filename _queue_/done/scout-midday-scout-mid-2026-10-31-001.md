---
unit: scout-midday-scout-mid-2026-10-31-001
regular: scout-midday
activity: perception-scout
segment:
priority: 2
created_at: 2026-11-01T10:17:29Z
expires_at:
planned_for:
not_before:
window: scout-base remainder plus scout-events, scout-store, scout-alliance groups of scout-midday-2026-10-31-0700
est_minutes: 10
chain_id: scout-mid-2026-10-31
chain_seq: 1
attempts: 1
max_attempts: 3
claimed_by: ticker-0504
claimed_at: 2026-11-02T13:09:14Z
lease_until: 2026-11-02T13:29:14Z
result:
  status: partial
  started_at: 2026-11-02T13:09:14Z
  finished_at: 2026-11-02T13:11:29Z
  duration_seconds: 135
  executor: ticker-0504
  summary: Scout events/store/base-remainder walked (12 items); alliance group unwalked - right icon column lost after base pan, 3 recovery variants failed; successor enqueued
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-02/perception-scout/observation.md
  follow_up: none
  stats:
    surfaces_walked: scout-events-scout-store-scout-base
    items_observed: 12
    red_dots_seen: 4
    red_dots_explained: 2
    unexplained_red_dots: 2
    unknown_items: 2
---

# scout-midday

Produced by tools/queue.py. The executor reads the activity metadata and the standing rules before acting.
