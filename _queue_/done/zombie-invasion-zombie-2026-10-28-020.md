---
unit: zombie-invasion-zombie-2026-10-28-020
regular: zombie-invasion
activity: zombie-invasion
segment:
priority: 4
created_at: 2026-10-28T20:49:24Z
expires_at:
planned_for:
not_before:
window:
est_minutes: 12
chain_id: zombie-2026-10-28
chain_seq: 20
attempts: 1
max_attempts: 3
claimed_by: ticker-1604
claimed_at: 2026-10-28T23:16:12Z
lease_until: 2026-10-28T23:36:12Z
result:
  status: partial
  started_at: 2026-10-28T23:16:12Z
  finished_at: 2026-10-28T23:30:19Z
  duration_seconds: 847
  executor: ticker-1604
  summary: Parallel squads 2: Squad 1 kill claimed 268,000 coins, Squad 2 still in flight, successor starts now
  claimed: [loot-row-x794-y956]
  claimed_count: 1
  evidence: _records_/2026-10-28/zombie-invasion/1629-queue-run.md
  follow_up: none
  stats:
    zombies_killed: 1
    cleared: false
    coin_before: 53603536
    coin_after: 53871536
    coins_collected: 268000
    medals_before: 50
    medals_after: 60
    chests_opened: 0
    squads_parallel: 2
---

# zombie-invasion

Produced by tools/queue.py. The executor reads the activity metadata and the standing rules before acting.
