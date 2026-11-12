---
unit: zombie-invasion-zombie-2026-11-10-020
regular: zombie-invasion
activity: zombie-invasion
segment:
priority: 4
created_at: 2026-11-12T03:32:33Z
expires_at:
planned_for:
not_before:
window:
est_minutes: 12
chain_id: zombie-2026-11-10
chain_seq: 20
attempts: 1
max_attempts: 3
claimed_by: ticker-2001
claimed_at: 2026-11-12T04:04:04Z
lease_until: 2026-11-12T04:24:04Z
result:
  status: partial
  started_at: 2026-11-12T04:04:04Z
  finished_at: 2026-11-12T04:15:14Z
  duration_seconds: 670
  executor: ticker-2001
  summary: 2 Lv.10 kills in parallel (X:443 Y:436, X:505 Y:383), squads_parallel 2; 1 LOOT row claimed 268000 coins, Squad 1 row missing; coin 138.0M to 138.3M HUD; stamina 58 to 49; cleared false, successor enqueued
  claimed: [loot-row-x1, zombie-kills-x2]
  claimed_count: 2
  evidence: _records_/2026-11-11/zombie-invasion/2020-queue-run.md
  follow_up: none
  stats:
    zombies_killed: 2
    cleared: false
    coin_before: 138000000
    coin_after: 138300000
    coins_collected: 268000
    medals_before: 5120
    medals_after: 5140
    chests_opened: 0
    squads_parallel: 2
    target: kill wave zombies and claim LOOT
    achieved: 2 Lv.10 kills dispatched in parallel, 1 LOOT row claimed (268000 coins)
    resources_gained: coins 268000, iron 268000, food 268000, medals 20, hero EXP 263000
    costs: about 17 minutes, stamina 58 to 49
    verified: yes (coin, food and stamina figures live-read; medals_after derived, flagged)
    blocker_category: h
    blocker: missing-loot-row-squad-1
  stats_missing: []
  stats_warnings: []
---

# zombie-invasion

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.
