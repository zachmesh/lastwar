---
unit: zombie-invasion-zombie-2026-10-28-004
regular: zombie-invasion
activity: zombie-invasion
segment:
priority: 4
created_at: 2026-10-28T11:03:54Z
expires_at:
planned_for:
not_before:
window:
est_minutes: 12
chain_id: zombie-2026-10-28
chain_seq: 4
attempts: 1
max_attempts: 3
claimed_by: ticker-0407
claimed_at: 2026-10-28T11:07:43Z
lease_until: 2026-10-28T11:27:43Z
result:
  status: failed
  started_at: 2026-10-28T11:07:43Z
  finished_at: 2026-10-28T11:10:27Z
  duration_seconds: 164
  executor: ticker-0407
  summary: Access failed after opening coin read 35488573 - 3 reopen attempts blocked, no input landed, no kill
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-10-28/zombie-invasion/0407-queue-run.md
  follow_up: none
  stats:
    zombies_killed: 0
    cleared: false
    coin_before: 35488573
    coin_after: 35488573
    coins_collected: 0
---

# zombie-invasion

Produced by tools/queue.py. The executor reads the activity metadata and the standing rules before acting.
