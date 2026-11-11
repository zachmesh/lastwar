---
unit: zombie-invasion-zombie-2026-11-10-006
regular: zombie-invasion
activity: zombie-invasion
segment:
priority: 4
created_at: 2026-11-11T10:38:27Z
expires_at:
planned_for:
not_before:
window:
est_minutes: 12
chain_id: zombie-2026-11-10
chain_seq: 6
attempts: 1
max_attempts: 3
claimed_by: ticker-0313
claimed_at: 2026-11-11T11:23:45Z
lease_until: 2026-11-11T11:43:45Z
result:
  status: partial
  started_at: 2026-11-11T11:23:45Z
  finished_at: 2026-11-11T11:29:59Z
  duration_seconds: 374
  executor: ticker-0313
  summary: 1 Lv.10 kill X:414 Y:344, 1 LOOT row claimed 268,000 coins; Free Claim +75 stamina; parallel dispatch failed on a mistargeted batch (Ironhead card, no second march); cleared false, successor enqueued
  claimed: [coins-268000, iron-268000, food-268000, medals-10, hero-exp-263000]
  claimed_count: 5
  evidence: _records_/2026-11-11/zombie-invasion/0324-queue-run.md
  follow_up: none
  stats:
    zombies_killed: 1
    cleared: false
    coin_before: 118200000
    coin_after: 118500000
    coins_collected: 268000
    medals_before: 4010
    medals_after: unverified
    chests_opened: 0
    squads_parallel: 1
    target: kill wave zombies and claim LOOT
    achieved: 1 kill, 1 LOOT row claimed (268,000 coins)
    resources_gained: coins 268000, iron 268000, food 268000, medals 10, hero EXP 263000
    costs: about 6 minutes, stamina 13 to 79
    verified: yes
    blocker_category: c
  stats_missing: []
  stats_warnings: []
---

# zombie-invasion

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.
