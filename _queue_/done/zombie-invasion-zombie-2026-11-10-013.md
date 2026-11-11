---
unit: zombie-invasion-zombie-2026-11-10-013
regular: zombie-invasion
activity: zombie-invasion
segment:
priority: 4
created_at: 2026-11-11T16:33:54Z
expires_at:
planned_for:
not_before:
window:
est_minutes: 12
chain_id: zombie-2026-11-10
chain_seq: 13
attempts: 1
max_attempts: 3
claimed_by: ticker-1045
claimed_at: 2026-11-11T18:49:05Z
lease_until: 2026-11-11T19:09:05Z
result:
  status: partial
  started_at: 2026-11-11T18:49:05Z
  finished_at: 2026-11-11T18:59:36Z
  duration_seconds: 631
  executor: ticker-1045
  summary: 2 Lv.10 kills dispatched in parallel (X:404 Y:332, X:381 Y:319); 1 LOOT row claimed 268,000 coins; squad 2 in flight at close; cleared false, successor enqueued; Issue #642 filed
  claimed: [coins-268000, iron-268000, food-268000, medals-10, hero-exp-263000]
  claimed_count: 5
  evidence: _records_/2026-11-11/zombie-invasion/1048-queue-run.md
  follow_up: none
  stats:
    zombies_killed: 2
    cleared: false
    coin_before: 129600000
    coin_after: 129900000
    coins_collected: 268000
    medals_before: 4130
    medals_after: 4140
    chests_opened: 0
    squads_parallel: 2
    target: kill wave zombies and claim LOOT
    achieved: 2 Lv.10 kills dispatched in parallel, 1 LOOT row claimed (268,000 coins)
    resources_gained: coins 268000, iron 268000, food 268000, medals 10, hero EXP 263000
    costs: about 10 minutes, stamina 117 to 98
    verified: yes
    blocker_category: h
  stats_missing: []
  stats_warnings: []
---

# zombie-invasion

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.
