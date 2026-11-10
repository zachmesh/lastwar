---
unit: zombie-invasion-zombie-2026-10-28-009
regular: zombie-invasion
activity: zombie-invasion
segment:
priority: 4
created_at: 2026-10-28T12:13:41Z
expires_at:
planned_for:
not_before:
window:
est_minutes: 12
chain_id: zombie-2026-10-28
chain_seq: 9
attempts: 1
max_attempts: 3
claimed_by: ticker-0534
claimed_at: 2026-10-28T12:34:46Z
lease_until: 2026-10-28T12:54:46Z
result:
  status: partial
  started_at: 2026-10-28T12:34:46Z
  finished_at: 2026-10-28T12:44:53Z
  duration_seconds: 607
  executor: ticker-0534
  summary: Waited out exhausted wave, new wave kill X986 Y950, LOOT claimed 268000 coins (36024573 to 36292573), medals 90 to 100 by row evidence, handover row from unit 007 absent from LOOT panel, squads_parallel 1 (6s march resolved before second dispatch could land)
  claimed: [loot-row-x986-y950]
  claimed_count: 1
  evidence: _records_/2026-10-28/zombie-invasion/0534-queue-run.md
  follow_up: none
  stats:
    zombies_killed: 1
    cleared: false
    coin_before: 36024573
    coin_after: 36292573
    coins_collected: 268000
    medals_before: 90
    medals_after: 100
    chests_opened: 0
    squads_parallel: 1
    tasks_badge: 1
---

# zombie-invasion

Produced by tools/queue.py. The executor reads the activity metadata and the standing rules before acting.
