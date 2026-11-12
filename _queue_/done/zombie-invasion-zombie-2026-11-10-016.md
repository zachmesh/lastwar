---
unit: zombie-invasion-zombie-2026-11-10-016
regular: zombie-invasion
activity: zombie-invasion
segment:
priority: 4
created_at: 2026-11-11T20:32:24Z
expires_at:
planned_for:
not_before:
window:
est_minutes: 12
chain_id: zombie-2026-11-10
chain_seq: 16
attempts: 1
max_attempts: 3
claimed_by: ticker-1439
claimed_at: 2026-11-11T22:41:48Z
lease_until: 2026-11-11T23:01:48Z
result:
  status: partial
  started_at: 2026-11-11T22:41:48Z
  finished_at: 2026-11-11T22:56:02Z
  duration_seconds: 854
  executor: ticker-1439
  summary: 2 squads dispatched in parallel (X:586 Y:340, X:454 Y:281, both Lv.10); mail Intel Rewards claimed at entry (unverified total); LOOT unclaimed - both squads still in flight at close, successor must check gift badge; mail-detail back arrow unresponsive to background input, recovered by menu Quit + relaunch
  claimed: [zombie-dispatch-x2]
  claimed_count: 1
  evidence: _records_/2026-11-11/zombie-invasion/1456-queue-run.md
  follow_up: none
  stats:
    zombies_killed: 0
    cleared: false
    coin_before: 135600000
    coin_after: 135600000
    coins_collected: 0
    medals_before: 4150
    medals_after: 4150
    chests_opened: 0
    squads_parallel: 2
    target: kill wave zombies and claim LOOT
    achieved: 2 Lv.10 squads dispatched in parallel, 0 LOOT rows claimed in-unit
    resources_gained: none in-unit
    costs: about 20 minutes, stamina 85 to 66
    verified: yes
    blocker_category: c
  stats_missing: []
  stats_warnings: []
---

# zombie-invasion

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.
