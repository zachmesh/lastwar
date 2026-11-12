---
unit: zombie-invasion-zombie-2026-11-10-022
regular: zombie-invasion
activity: zombie-invasion
segment:
priority: 4
created_at: 2026-11-12T06:31:01Z
expires_at:
planned_for:
not_before:
window:
est_minutes: 12
chain_id: zombie-2026-11-10
chain_seq: 22
attempts: 1
max_attempts: 3
claimed_by: ticker-0100
claimed_at: 2026-11-12T09:03:34Z
lease_until: 2026-11-12T09:23:34Z
result:
  status: partial
  started_at: 2026-11-12T09:03:34Z
  finished_at: 2026-11-12T09:16:10Z
  duration_seconds: 756
  executor: ticker-0100
  summary: 2 Lv.10 kills sequential X:489 Y:441 and X:504 Y:410, squads_parallel 1 (short round trips); 1 LOOT row claimed 268000 coins, coin 143.4M to 143.7M HUD; X:489 row never materialized (4th handover loss); stamina 68 to 59; cleared false, successor 025 enqueued
  claimed: [loot-row-x504-y410-268000-coins]
  claimed_count: 1
  evidence: _records_/2026-11-12/zombie-invasion/0114-queue-run.md
  follow_up: none
  stats:
    zombies_killed: 2
    cleared: false
    coin_before: 143.4M
    coin_after: 143.7M
    coins_collected: 268000
    medals_before: unmeasured
    medals_after: unmeasured
    chests_opened: 0
    squads_parallel: 1
    tasks_badge: 1
    stamina_before: 68
    stamina_after: 59
    target: 2
    achieved: 1
    resources_gained: coin_268000_iron_268000_food_268000_exp_263000_medals_20_crate_1
    costs: 20_stamina_12_minutes
    verified: yes
    blocker_category: h
  stats_missing: []
  stats_warnings: []
---

# zombie-invasion

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.
