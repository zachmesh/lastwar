---
unit: zombie-invasion-zombie-2026-11-10-009
regular: zombie-invasion
activity: zombie-invasion
segment:
priority: 4
created_at: 2026-11-11T12:12:27Z
expires_at:
planned_for:
not_before:
window:
est_minutes: 12
chain_id: zombie-2026-11-10
chain_seq: 9
attempts: 1
max_attempts: 3
claimed_by: ticker-0604
claimed_at: 2026-11-11T14:12:42Z
lease_until: 2026-11-11T14:32:42Z
result:
  status: partial
  started_at: 2026-11-11T14:12:42Z
  finished_at: 2026-11-11T14:23:25Z
  duration_seconds: 643
  executor: ticker-0604
  summary: 2 Lv.10 kills in parallel (X:560 Y:399, X:555 Y:389); 2 LOOT rows claimed 536,000 coins; coin exact 120927972 to 121463972; medals 4080 to 4100 live; Store scroll did not move, Coin Chest SSR row unverified, no redemption; cleared false, successor enqueued
  claimed: [coins-536000, iron-536000, food-536000, medals-20, hero-exp-526000]
  claimed_count: 5
  evidence: _records_/2026-11-11/zombie-invasion/0622-queue-run.md
  follow_up: none
  stats:
    zombies_killed: 2
    cleared: false
    coin_before: 120927972
    coin_after: 121463972
    coins_collected: 536000
    medals_before: 4080
    medals_after: 4100
    chests_opened: 0
    squads_parallel: 2
    target: kill wave zombies and claim LOOT
    achieved: 2 Lv.10 kills in parallel, 2 LOOT rows claimed (536,000 coins)
    resources_gained: coins 536000, iron 536000, food 536000, medals 20, hero EXP 526000
    costs: about 10 minutes, stamina 73 to 54
    verified: coin panel exact 120927972 to 121463972, both LOOT rows read before Claim All, Store header 4100 live
    blocker_category: h
  stats_missing: []
  stats_warnings: []
---

# zombie-invasion

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.
