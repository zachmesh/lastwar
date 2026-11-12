---
unit: zombie-invasion-zombie-2026-11-10-018
regular: zombie-invasion
activity: zombie-invasion
segment:
priority: 4
created_at: 2026-11-12T00:14:54Z
expires_at:
planned_for:
not_before:
window:
est_minutes: 12
chain_id: zombie-2026-11-10
chain_seq: 18
attempts: 1
max_attempts: 3
claimed_by: ticker-1822
claimed_at: 2026-11-12T02:22:49Z
lease_until: 2026-11-12T02:42:49Z
result:
  status: partial
  started_at: 2026-11-12T02:22:49Z
  finished_at: 2026-11-12T02:35:21Z
  duration_seconds: 752
  executor: ticker-1822
  summary: 3 Lv.10 kills sequential (X:502 Y:406, X:497 Y:396, X:505 Y:394), squads_parallel 1 (short round trips); 3 LOOT rows claimed 804000 coins; coin 136.7M to 137.5M HUD; stamina 88 to 59; cleared false, successor enqueued
  claimed: [loot-rows-x3, zombie-kills-x3]
  claimed_count: 2
  evidence: _records_/2026-11-11/zombie-invasion/1834-queue-run.md
  follow_up: none
  stats:
    zombies_killed: 3
    cleared: false
    coin_before: 136700000
    coin_after: 137500000
    coins_collected: 804000
    medals_before: 5070
    medals_after: 5100
    chests_opened: 0
    squads_parallel: 1
    target: kill wave zombies and claim LOOT
    achieved: 3 Lv.10 kills dispatched, 3 LOOT rows claimed (804000 coins)
    resources_gained: coins 804000, iron 804000, food 804000, medals 30, hero EXP 789000
    costs: about 12 minutes, stamina 88 to 59
    verified: yes
    blocker_category: h
  stats_missing: []
  stats_warnings: []
---

# zombie-invasion

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.
