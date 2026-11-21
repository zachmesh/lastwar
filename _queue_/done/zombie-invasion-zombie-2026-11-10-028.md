---
unit: zombie-invasion-zombie-2026-11-10-028
regular: zombie-invasion
activity: zombie-invasion
segment:
priority: 4
created_at: 2026-11-12T17:55:34Z
expires_at:
planned_for:
not_before:
window:
est_minutes: 12
chain_id: zombie-2026-11-10
chain_seq: 28
attempts: 1
max_attempts: 3
claimed_by: ticker-1408
claimed_at: 2026-11-13T22:15:17Z
lease_until: 2026-11-13T22:35:17Z
result:
  status: failed
  started_at: 2026-11-13T22:15:17Z
  finished_at: 2026-11-13T22:22:22Z
  duration_seconds: 425
  executor: ticker-1408
  summary: Mac mini unreachable (node_offline, no wake-up path; last seen 2026-11-12T17:52:28Z): 2 computer.session starts failed node_offline, connection.repair and connection.health via recovery device timed out (25s each); no game state observable, no input sent, no kills, no claims; NOT the outcome_unknown control-lock (Issue 689), so no blocker_overlay recorded and the next tick will probe again; successor 029 enqueued
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-13/zombie-invasion/1415-queue-run.md
  follow_up: none
  stats:
    zombies_killed: 0
    cleared: false
    coins_collected: 0
    squads_parallel: 0
    chests_opened: 0
    control_attempts: 4
    target: reach game and kill nearby zombies (chain 028)
    achieved: 0
    resources_gained: none
    costs: 4 device invokes, no stamina or items spent
    verified: no
    blocker_category: f
  stats_missing: []
  stats_warnings: []
---

# zombie-invasion

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.
