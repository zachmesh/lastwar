---
unit: zombie-invasion-zombie-2026-10-28-022
regular: zombie-invasion
activity: zombie-invasion
segment:
priority: 4
created_at: 2026-10-28T23:50:19Z
expires_at:
planned_for:
not_before:
window:
est_minutes: 12
chain_id: zombie-2026-10-28
chain_seq: 22
attempts: 1
max_attempts: 3
claimed_by: ticker-1636
claimed_at: 2026-10-28T23:50:38Z
lease_until: 2026-10-29T00:10:38Z
result:
  status: partial
  started_at: 2026-10-28T23:50:38Z
  finished_at: 2026-10-29T00:03:23Z
  duration_seconds: 765
  executor: ticker-1636
  summary: Parallel squads 2: handover kill plus new pair claimed 804,000 coins, chain continues, successor starts now
  claimed: [loot-row-x800-y755, loot-row-x959-y896, loot-row-x999-y897]
  claimed_count: 3
  evidence: _records_/2026-10-28/zombie-invasion/1701-queue-run.md
  follow_up: none
  stats:
    zombies_killed: 3
    cleared: false
    coin_before: 54407536
    coin_after: 55211536
    coins_collected: 804000
    medals_before: 80
    medals_after: 110
    chests_opened: 0
    squads_parallel: 2
---

# zombie-invasion

Produced by tools/queue.py. The executor reads the activity metadata and the standing rules before acting.
