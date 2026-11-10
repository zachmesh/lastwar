---
unit: scout-scout-discovery-2026-11-09-008
regular: scout
activity: total-power-149217331
segment: 1
priority: 2
created_at: 2026-11-09T14:50:26Z
expires_at:
planned_for:
not_before:
window: scout 2026-11-09 - exploration - total-power-149217331 - Total Power 149217331 - read-only learning, red lines learn-only
est_minutes: 8
chain_id: scout-discovery-2026-11-09
chain_seq: 8
attempts: 1
max_attempts: 3
claimed_by: ticker-0804
claimed_at: 2026-11-09T16:33:37Z
lease_until: 2026-11-09T16:53:37Z
result:
  status: done
  started_at: 2026-11-09T16:33:37Z
  finished_at: 2026-11-09T16:33:37Z
  duration_seconds: 0
  executor: ticker-0804
  summary: Total Power is a live HUD total, not a task: read 149,117,331 on this pass base screens (08:12, 08:29, 08:32); no reward/cost/deadline/scoring; candidate rejected as a task, same misclassification the 0606 scout already flagged
  claimed: [none]
  claimed_count: 1
  evidence: _records_/2026-11-09/perception-scout/0606-queue-run.md
  follow_up: none
  stats:
    target: explain-total-power-read
    achieved: 1
    resources_gained: none
    costs: no game time, read from this pass screens
    verified: yes
    blocker_category: none
  stats_missing: []
  stats_warnings: []
---

# scout

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.
