---
unit: zombie-invasion-zombie-2026-11-10-004
regular: zombie-invasion
activity: zombie-invasion
segment:
priority: 4
created_at: 2026-11-11T07:54:13Z
expires_at:
planned_for:
not_before:
window:
est_minutes: 12
chain_id: zombie-2026-11-10
chain_seq: 4
attempts: 1
max_attempts: 3
claimed_by: ticker-0004
claimed_at: 2026-11-11T08:30:12Z
lease_until: 2026-11-11T08:50:12Z
result:
  status: partial
  started_at: 2026-11-11T08:30:12Z
  finished_at: 2026-11-11T08:42:55Z
  duration_seconds: 763
  executor: ticker-0004
  summary: 2 Lv.10 kills in parallel (squads_parallel 2, first in Glacieradon chain), both LOOT rows claimed for 536,000 coins; Store medals 4000 live, 120-medal row is Universal Exclusive Weapon Shard not a Coin Chest; wave live, successor enqueued
  claimed: [loot-coins-536000, medals-20]
  claimed_count: 2
  evidence: _records_/2026-11-11/zombie-invasion/0030-queue-run.md
  follow_up: none
  stats:
    target: 2
    achieved: 2
    zombies_killed: 2
    cleared: false
    coin_before: 110.2M
    coin_after: 110.7M
    coins_collected: 536000
    medals_after: 4000
    chests_opened: 0
    squads_parallel: 2
    resources_gained: 536000 coin + 536000 iron + 536000 food + 526000 hero EXP + 20 medals
    costs: 20 stamina + about 12 minutes
    verified: yes
    blocker_category: h
  stats_missing: []
  stats_warnings: []
---

# zombie-invasion

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.
