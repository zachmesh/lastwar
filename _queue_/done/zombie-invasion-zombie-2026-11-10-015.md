---
unit: zombie-invasion-zombie-2026-11-10-015
regular: zombie-invasion
activity: zombie-invasion
segment:
priority: 4
created_at: 2026-11-11T19:15:16Z
expires_at:
planned_for:
not_before:
window:
est_minutes: 12
chain_id: zombie-2026-11-10
chain_seq: 15
attempts: 1
max_attempts: 3
claimed_by: ticker-1204
claimed_at: 2026-11-11T20:19:09Z
lease_until: 2026-11-11T20:39:09Z
result:
  status: partial
  started_at: 2026-11-11T20:19:09Z
  finished_at: 2026-11-11T20:32:15Z
  duration_seconds: 786
  executor: ticker-1204
  summary: 1 Lv.10 kill at X:517 Y:417, 1 LOOT row claimed 268,000 coins; squad 2 March failed (stale target), squads_parallel 1; cleared false, successor enqueued
  claimed: [coins-268000, iron-268000, food-268000, medals-10, hero-exp-263000]
  claimed_count: 5
  evidence: _records_/2026-11-11/zombie-invasion/1222-queue-run.md
  follow_up: none
  stats:
    zombies_killed: 1
    cleared: false
    coin_before: 131900000
    coin_after: 132100000
    coins_collected: 268000
    medals_before: 4140
    medals_after: 4150
    chests_opened: 0
    squads_parallel: 1
    target: kill wave zombies and claim LOOT
    achieved: 1 Lv.10 kill dispatched, 1 LOOT row claimed (268,000 coins)
    resources_gained: coins 268000, iron 268000, food 268000, medals 10, hero EXP 263000
    costs: about 10 minutes, stamina 95 to 87
    verified: yes
    blocker_category: c
  stats_missing: []
  stats_warnings: []
---

# zombie-invasion

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.
