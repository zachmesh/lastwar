---
unit: zombie-invasion-zombie-2026-10-28-010
regular: zombie-invasion
activity: zombie-invasion
segment:
priority: 4
created_at: 2026-10-28T12:44:54Z
expires_at:
planned_for:
not_before:
window:
est_minutes: 12
chain_id: zombie-2026-10-28
chain_seq: 10
attempts: 1
max_attempts: 3
claimed_by: ticker-0534
claimed_at: 2026-10-28T12:45:10Z
lease_until: 2026-10-28T13:05:10Z
result:
  status: partial
  started_at: 2026-10-28T12:45:10Z
  finished_at: 2026-10-28T12:49:12Z
  duration_seconds: 242
  executor: ticker-0534
  summary: Parallel dispatch achieved - Squads 1 and 2 marched simultaneously (March Queues 2 of 4), two Lv.10 kills X982 Y934 and X984 Y933, LOOT Claim All collected 536000 coins (36292573 to 36828573), medals 100 to 120 by row evidence
  claimed: [loot-row-x984-y933, loot-row-x982-y934]
  claimed_count: 2
  evidence: _records_/2026-10-28/zombie-invasion/0545-queue-run.md
  follow_up: none
  stats:
    zombies_killed: 2
    cleared: false
    coin_before: 36292573
    coin_after: 36828573
    coins_collected: 536000
    medals_before: 100
    medals_after: 120
    chests_opened: 0
    squads_parallel: 2
    tasks_badge: 2
---

# zombie-invasion

Produced by tools/queue.py. The executor reads the activity metadata and the standing rules before acting.
