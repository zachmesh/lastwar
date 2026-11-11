---
unit: zombie-invasion-zombie-2026-11-10-008
regular: zombie-invasion
activity: zombie-invasion
segment:
priority: 4
created_at: 2026-11-11T11:53:10Z
expires_at:
planned_for:
not_before:
window:
est_minutes: 12
chain_id: zombie-2026-11-10
chain_seq: 8
attempts: 1
max_attempts: 3
claimed_by: ticker-0404
claimed_at: 2026-11-11T12:05:41Z
lease_until: 2026-11-11T12:25:41Z
result:
  status: partial
  started_at: 2026-11-11T12:05:41Z
  finished_at: 2026-11-11T12:12:22Z
  duration_seconds: 401
  executor: ticker-0404
  summary: 2 Lv.10 kills in parallel (X:434 Y:404, X:430 Y:425); 2 LOOT rows claimed 536,000 coins; Store Coin Chest (SSR) row below fold, scroll did not move the list, no redemption; cleared false, successor enqueued
  claimed: [coins-536000, iron-536000, food-536000, medals-20, hero-exp-526000]
  claimed_count: 5
  evidence: _records_/2026-11-11/zombie-invasion/0412-queue-run.md
  follow_up: none
  stats:
    zombies_killed: 2
    cleared: false
    coin_before: 119000000
    coin_after: 119500000
    coins_collected: 536000
    medals_before: 4060
    medals_after: 4080
    chests_opened: 0
    squads_parallel: 2
    target: kill wave zombies and claim LOOT
    achieved: 2 Lv.10 kills in parallel, 2 LOOT rows claimed (536,000 coins)
    resources_gained: coins 536000, iron 536000, food 536000, medals 20, hero EXP 526000
    costs: about 7 minutes, stamina 67 to 48
    verified: coin HUD 119.0M->119.5M, both LOOT rows read before Claim All, Store header 4080 live
    blocker_category: h
  stats_missing: []
  stats_warnings: []
---

# zombie-invasion

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.
