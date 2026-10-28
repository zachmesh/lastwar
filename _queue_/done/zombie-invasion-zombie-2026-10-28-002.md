---
unit: zombie-invasion-zombie-2026-10-28-002
regular: zombie-invasion
activity: zombie-invasion
segment:
priority: 4
created_at: 2026-10-28T10:46:31Z
expires_at:
planned_for:
not_before:
window:
est_minutes: 12
chain_id: zombie-2026-10-28
chain_seq: 2
attempts: 1
max_attempts: 3
claimed_by: ticker-0334
claimed_at: 2026-10-28T10:46:55Z
lease_until: 2026-10-28T11:06:55Z
result:
  status: failed
  started_at: 2026-10-28T10:46:55Z
  finished_at: 2026-10-28T10:48:20Z
  duration_seconds: 85
  executor: ticker-0334
  summary: Access-failed - device channel returned the known unreliable authorization error on 3 consecutive attempts after claim; no play in this unit
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-10-28/zombie-invasion/0347-queue-run.md
  follow_up: none
  stats:
    zombies_killed: 0
    cleared: false
---

# zombie-invasion

Produced by tools/queue.py. The executor reads the activity metadata and the standing rules before acting.
