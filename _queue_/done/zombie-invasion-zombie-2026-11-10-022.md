---
unit: zombie-invasion-zombie-2026-11-10-022
regular: zombie-invasion
activity: zombie-invasion
segment:
priority: 4
created_at: 2026-11-12T06:31:01Z
expires_at:
planned_for:
not_before:
window:
est_minutes: 12
chain_id: zombie-2026-11-10
chain_seq: 22
attempts: 1
max_attempts: 3
claimed_by: ticker-2333
claimed_at: 2026-11-12T07:34:18Z
lease_until: 2026-11-12T07:54:18Z
result:
  status: partial
  started_at: 2026-11-12T07:34:18Z
  finished_at: 2026-11-12T07:43:58Z
  duration_seconds: 580
  executor: ticker-2333
  summary: 2 Lv.10 kills in parallel, both LOOT rows claimed, 536000 coins; cleared false, chain continues
  claimed: [coins-536000]
  claimed_count: 1
  evidence: _records_/2026-11-11/zombie-invasion/2342-queue-run.md
  follow_up: none
  stats:
    zombies_killed: 2
    cleared: false
    coin_before: 142900000
    coin_after: 143400000
    coins_collected: 536000
    medals_before: 5160
    medals_after: 5180
    chests_opened: 0
    squads_parallel: 2
    target: kill wave zombies and claim LOOT
    achieved: 2 Lv.10 kills dispatched in parallel, both LOOT rows claimed (536000 coins)
    resources_gained: coins 536000, iron 536000, food 536000, medals 20, hero EXP 526000
    costs: about 8 minutes, stamina 20 to 1
    verified: yes
    blocker_category: h
  stats_missing: []
  stats_warnings: []
---

# zombie-invasion

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.
