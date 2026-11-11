---
unit: zombie-invasion-zombie-2026-11-10-005
regular: zombie-invasion
activity: zombie-invasion
segment:
priority: 4
created_at: 2026-11-11T08:42:56Z
expires_at:
planned_for:
not_before:
window:
est_minutes: 12
chain_id: zombie-2026-11-10
chain_seq: 5
attempts: 1
max_attempts: 3
claimed_by: ticker-0212
claimed_at: 2026-11-11T10:25:21Z
lease_until: 2026-11-11T10:45:21Z
result:
  status: partial
  started_at: 2026-11-11T10:25:21Z
  finished_at: 2026-11-11T10:38:22Z
  duration_seconds: 781
  executor: ticker-0212
  summary: 4 Lv.10 kills in 2 parallel pairs; 3 LOOT rows claimed (804,000 coins); Squad 1 row lost (no row ever appeared); Store 160-medal row is Iron Chest (SSR), no Coin Chest found; cleared false, chain continues
  claimed: [coins 804000, iron 804000, food 804000, medals 10, hero EXP 789000]
  claimed_count: 5
  evidence: _records_/2026-11-11/zombie-invasion/0238-queue-run.md
  follow_up: none
  stats:
    zombies_killed: 4
    cleared: false
    coin_before: 117400000
    coin_after: 118200000
    coins_collected: 804000
    medals_before: 4000
    medals_after: 4010
    chests_opened: 0
    squads_parallel: 2
    target: kill wave zombies and claim LOOT
    achieved: 4 kills, 3 LOOT rows claimed (804,000 coins)
    resources_gained: coins 804000, iron 804000, food 804000, medals 10, hero EXP 789000
    points: 0
    costs: about 12 minutes, stamina 32->3
    verified: coin HUD 117.4M->118.2M
    blocker_category: none
  stats_missing: []
  stats_warnings: []
---

# zombie-invasion

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.
