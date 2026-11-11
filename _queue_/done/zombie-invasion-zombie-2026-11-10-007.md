---
unit: zombie-invasion-zombie-2026-11-10-007
regular: zombie-invasion
activity: zombie-invasion
segment:
priority: 4
created_at: 2026-11-11T11:30:01Z
expires_at:
planned_for:
not_before:
window:
est_minutes: 12
chain_id: zombie-2026-11-10
chain_seq: 7
attempts: 1
max_attempts: 3
claimed_by: ticker-0336
claimed_at: 2026-11-11T11:41:41Z
lease_until: 2026-11-11T12:01:41Z
result:
  status: partial
  started_at: 2026-11-11T11:41:41Z
  finished_at: 2026-11-11T11:53:04Z
  duration_seconds: 683
  executor: ticker-0336
  summary: 2 Lv.10 kills in parallel (X:414 Y:324, X:337 Y:420); 2 LOOT rows claimed 536,000 coins; Store Coin Chest (SSR) identified, Owned 153; cleared false, successor enqueued
  claimed: [coins-536000, iron-536000, food-536000, medals-20, hero-exp-526000]
  claimed_count: 5
  evidence: _records_/2026-11-11/zombie-invasion/0341-queue-run.md
  follow_up: none
  stats:
    zombies_killed: 2
    cleared: false
    coin_before: 118500000
    coin_after: 119000000
    coins_collected: 536000
    medals_before: 4010
    medals_after: 4060
    chests_opened: 0
    squads_parallel: 2
    target: kill wave zombies and claim LOOT
    achieved: 2 Lv.10 kills in parallel, 2 LOOT rows claimed (536,000 coins); Store Coin Chest (SSR) row identified (160 medals, Limit 100, Owned 153, 812.16K coins)
    resources_gained: coins 536000, iron 536000, food 536000, medals 20, hero EXP 526000
    costs: about 10 minutes, stamina 82 to 63
    verified: coin HUD 118.5M to 119.0M, food and iron each plus 536K, both LOOT rows read before Claim All, Store header 4060 and SSR tooltip read live
    blocker_category: h
    tasks_badge: 2
    stamina_inventory_10: 647
    stamina_inventory_50: 669
    stamina_free_claim: 0
    device_takeovers: 0
  stats_missing: []
  stats_warnings: []
---

# zombie-invasion

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.
