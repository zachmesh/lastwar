---
unit: zombie-invasion-zombie-2026-11-10-017
regular: zombie-invasion
activity: zombie-invasion
segment:
priority: 4
created_at: 2026-11-11T22:56:16Z
expires_at:
planned_for:
not_before:
window:
est_minutes: 12
chain_id: zombie-2026-11-10
chain_seq: 17
attempts: 1
max_attempts: 3
claimed_by: ticker-1547
claimed_at: 2026-11-12T00:02:49Z
lease_until: 2026-11-12T00:22:49Z
result:
  status: partial
  started_at: 2026-11-12T00:02:49Z
  finished_at: 2026-11-12T00:14:44Z
  duration_seconds: 715
  executor: ticker-1547
  summary: 2 Lv.10 kills in parallel (X:500 Y:417, X:436 Y:435), squads_parallel 2; 4 LOOT rows claimed 1072000 coins; coin 135.6M to 136.7M HUD; Store medal balance 5070 live, no Coin Chest row on first screen; cleared false, successor enqueued
  claimed: [loot-rows-x4, zombie-kills-x2]
  claimed_count: 2
  evidence: _records_/2026-11-11/zombie-invasion/1619-queue-run.md
  follow_up: successor 018 enqueued to start now; Store below-fold rows still unread, scroll did not move the list
  stats:
    zombies_killed: 2
    cleared: false
    coin_before: 135600000
    coin_after: 136700000
    coins_collected: 1072000
    medals_before: unverified
    medals_after: 5070
    chests_opened: 0
    squads_parallel: 2
    target: kill wave zombies and claim LOOT
    achieved: 2 Lv.10 kills dispatched in parallel, 4 LOOT rows claimed (1072000 coins)
    resources_gained: coins 1072000, iron 1072000, food 1072000, medals 40, hero EXP 1052000
    costs: about 15 minutes, stamina 80 to 61
    verified: yes
    blocker_category: h
  stats_missing: []
  stats_warnings: []
---

# zombie-invasion

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.
