---
unit: zombie-invasion-zombie-2026-11-10-021
regular: zombie-invasion
activity: zombie-invasion
segment:
priority: 4
created_at: 2026-11-12T04:15:22Z
expires_at:
planned_for:
not_before:
window:
est_minutes: 12
chain_id: zombie-2026-11-10
chain_seq: 21
attempts: 1
max_attempts: 3
claimed_by: ticker-2211
claimed_at: 2026-11-12T06:14:22Z
lease_until: 2026-11-12T06:34:22Z
result:
  status: partial
  started_at: 2026-11-12T06:14:22Z
  finished_at: 2026-11-12T06:30:11Z
  duration_seconds: 949
  executor: ticker-2211
  summary: 2 Lv.10 kills in parallel (X:481 Y:397, X:488 Y:392), squads_parallel 2; both LOOT rows claimed 536000 coins; coin 142.3M to 142.9M HUD; stamina 25 to 6; cleared false, successor enqueued
  claimed: [loot-rows-x2, zombie-kills-x2]
  claimed_count: 2
  evidence: _records_/2026-11-11/zombie-invasion/2229-queue-run.md
  follow_up: none
  stats:
    zombies_killed: 2
    cleared: false
    coin_before: 142300000
    coin_after: 142900000
    coins_collected: 536000
    medals_before: 5140
    medals_after: 5160
    chests_opened: 0
    squads_parallel: 2
    target: kill wave zombies and claim LOOT
    achieved: 2 Lv.10 kills dispatched in parallel, both LOOT rows claimed (536000 coins)
    resources_gained: coins 536000, iron 536000, food 536000, medals 20, hero EXP 526000
    costs: about 15 minutes, stamina 25 to 6
    verified: yes (coin, food and stamina figures live-read; medals_after derived, flagged)
    blocker_category: h
    blocker: blind-batch-misfire-teleporter-popup
  stats_missing: []
  stats_warnings: []
---

# zombie-invasion

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.
