---
unit: zombie-invasion-zombie-2026-10-28-021
regular: zombie-invasion
activity: zombie-invasion
segment:
priority: 4
created_at: 2026-10-28T23:31:07Z
expires_at:
planned_for:
not_before:
window:
est_minutes: 12
chain_id: zombie-2026-10-28
chain_seq: 21
attempts: 1
max_attempts: 3
claimed_by: ticker-1636
claimed_at: 2026-10-28T23:37:11Z
lease_until: 2026-10-28T23:57:11Z
result:
  status: partial
  started_at: 2026-10-28T23:37:11Z
  finished_at: 2026-10-28T23:50:19Z
  duration_seconds: 788
  executor: ticker-1636
  summary: Parallel squads 2: handover kill and new Squad 2 kill claimed 536,000 coins, Squad 1 still returning, successor starts now
  claimed: [loot-row-x800-y768, loot-row-x994-y953]
  claimed_count: 2
  evidence: _records_/2026-10-28/zombie-invasion/1649-queue-run.md
  follow_up: none
  stats:
    zombies_killed: 2
    cleared: false
    coin_before: 53871536
    coin_after: 54407536
    coins_collected: 536000
    medals_before: 60
    medals_after: 80
    chests_opened: 0
    squads_parallel: 2
---

# zombie-invasion

Produced by tools/queue.py. The executor reads the activity metadata and the standing rules before acting.
