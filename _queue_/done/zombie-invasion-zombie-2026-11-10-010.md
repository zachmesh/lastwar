---
unit: zombie-invasion-zombie-2026-11-10-010
regular: zombie-invasion
activity: zombie-invasion
segment:
priority: 4
created_at: 2026-11-11T14:23:35Z
expires_at:
planned_for:
not_before:
window:
est_minutes: 12
chain_id: zombie-2026-11-10
chain_seq: 10
attempts: 1
max_attempts: 3
claimed_by: ticker-0707
claimed_at: 2026-11-11T15:11:14Z
lease_until: 2026-11-11T15:31:14Z
result:
  status: partial
  started_at: 2026-11-11T15:11:14Z
  finished_at: 2026-11-11T15:24:09Z
  duration_seconds: 775
  executor: ticker-0707
  summary: 3 Lv.10 kills in parallel (X:475 Y:359, X:412 Y:402, X:483 Y:348); 3 LOOT rows claimed 804,000 coins; Store medals 4130 live (+20 unexplained vs kills); SSR chest row still below fold, no redemption; cleared false, successor enqueued
  claimed: [coins-804000, iron-804000, food-804000, medals-30, hero-exp-789000]
  claimed_count: 5
  evidence: _records_/2026-11-11/zombie-invasion/0724-queue-run.md
  follow_up: none
  stats:
    zombies_killed: 3
    cleared: false
    coin_before: 121400000
    coin_after: 122200000
    coins_collected: 804000
    medals_before: 4080
    medals_after: 4130
    chests_opened: 0
    squads_parallel: 3
    target: kill wave zombies and claim LOOT
    achieved: 3 Lv.10 kills in parallel, 3 LOOT rows claimed (804,000 coins)
    resources_gained: coins 804000, iron 804000, food 804000, medals 30, hero EXP 789000
    costs: about 13 minutes, stamina 64 to 36
    verified: yes
    blocker_category: h
  stats_missing: []
  stats_warnings: []
---

# zombie-invasion

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.
