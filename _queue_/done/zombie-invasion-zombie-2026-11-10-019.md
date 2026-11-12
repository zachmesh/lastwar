---
unit: zombie-invasion-zombie-2026-11-10-019
regular: zombie-invasion
activity: zombie-invasion
segment:
priority: 4
created_at: 2026-11-12T02:35:33Z
expires_at:
planned_for:
not_before:
window:
est_minutes: 12
chain_id: zombie-2026-11-10
chain_seq: 19
attempts: 1
max_attempts: 3
claimed_by: ticker-1919
claimed_at: 2026-11-12T03:20:48Z
lease_until: 2026-11-12T03:40:48Z
result:
  status: partial
  started_at: 2026-11-12T03:20:48Z
  finished_at: 2026-11-12T03:32:05Z
  duration_seconds: 677
  executor: ticker-1919
  summary: 2 Lv.10 kills in parallel (X:505 Y:325, X:569 Y:369), squads_parallel 2; 2 LOOT rows claimed 536000 coins; coin 137.5M to 138.0M HUD; stamina 70 to 51; cleared false, successor enqueued
  claimed: [loot-rows-x2, zombie-kills-x2]
  claimed_count: 2
  evidence: _records_/2026-11-11/zombie-invasion/1936-queue-run.md
  follow_up: none
  stats:
    zombies_killed: 2
    cleared: false
    coin_before: 137500000
    coin_after: 138000000
    coins_collected: 536000
    medals_before: 5100
    medals_after: 5120
    chests_opened: 0
    squads_parallel: 2
    target: kill wave zombies and claim LOOT
    achieved: 2 Lv.10 kills dispatched in parallel, 2 LOOT rows claimed (536000 coins)
    resources_gained: coins 536000, iron 536000, food 536000, medals 20, hero EXP 526000
    costs: about 15 minutes, stamina 70 to 51
    verified: yes
    blocker_category: h
  stats_missing: []
  stats_warnings: []
---

# zombie-invasion

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.
