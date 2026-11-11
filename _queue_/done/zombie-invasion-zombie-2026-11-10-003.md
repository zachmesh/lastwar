---
unit: zombie-invasion-zombie-2026-11-10-003
regular: zombie-invasion
activity: zombie-invasion
segment:
priority: 4
created_at: 2026-11-11T06:20:37Z
expires_at:
planned_for:
not_before:
window:
est_minutes: 12
chain_id: zombie-2026-11-10
chain_seq: 3
attempts: 1
max_attempts: 3
claimed_by: ticker-2334
claimed_at: 2026-11-11T07:40:39Z
lease_until: 2026-11-11T08:00:39Z
result:
  status: partial
  started_at: 2026-11-11T07:40:39Z
  finished_at: 2026-11-11T07:54:05Z
  duration_seconds: 806
  executor: ticker-2334
  summary: Server maintenance blocked the first half of the unit; game recovered via login retry; 1 Lv.10 kill X:471 Y:355, LOOT row claimed for 268,000 coins; wave still live, successor enqueued
  claimed: [loot-row-268000-coins]
  claimed_count: 1
  evidence: _records_/2026-11-10/zombie-invasion/2340-queue-run.md
  follow_up: none
  stats:
    zombies_killed: 1
    cleared: false
    coin_before: 109.9M
    coin_after: 110.2M
    coins_collected: 268000
    medals_before: not-re-read
    medals_after: not-re-read
    chests_opened: 0
    squads_parallel: 1
    target: 1 Lv.10 kill and LOOT claim
    achieved: 1 Lv.10 kill and LOOT row claimed
    resources_gained: 268000 coin, 268000 iron, 268000 food, 10 medals, 263000 hero EXP
    costs: 10 stamina
    verified: yes
    blocker_category: h
  stats_missing: []
  stats_warnings: []
---

# zombie-invasion

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.
