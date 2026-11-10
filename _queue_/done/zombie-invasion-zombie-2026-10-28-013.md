---
unit: zombie-invasion-zombie-2026-10-28-013
regular: zombie-invasion
activity: zombie-invasion
segment:
priority: 4
created_at: 2026-10-28T15:14:56Z
expires_at:
planned_for:
not_before:
window:
est_minutes: 12
chain_id: zombie-2026-10-28
chain_seq: 13
attempts: 1
max_attempts: 3
claimed_by: ticker-0834
claimed_at: 2026-10-28T15:35:10Z
lease_until: 2026-10-28T15:55:10Z
result:
  status: partial
  started_at: 2026-10-28T15:35:10Z
  finished_at: 2026-10-28T15:44:37Z
  duration_seconds: 567
  executor: ticker-0834
  summary: Four squads in parallel (March Queues 4 of 4, cap reached) - 1 kill verified, 3 marches in flight; two LOOT rows claimed for 536000 coins (coin 49595336 to 50131336 exact), medals 140 to 160 inferred reaching the SR chest price, cleared false
  claimed: [loot-row-x891, loot-row-x883]
  claimed_count: 2
  evidence: _records_/2026-10-28/zombie-invasion/0840-queue-run.md
  follow_up: none
  stats:
    zombies_killed: 1
    cleared: false
    coin_before: 49595336
    coin_after: 50131336
    coins_collected: 536000
    medals_before: 140
    medals_after: 160
    chests_opened: 0
    squads_parallel: 4
    tasks_badge: 1
---

# zombie-invasion

Produced by tools/queue.py. The executor reads the activity metadata and the standing rules before acting.
