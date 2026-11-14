---
unit: zombie-invasion-zombie-2026-11-10-031
regular: zombie-invasion
activity: zombie-invasion
segment:
priority: 4
created_at: 2026-11-14T04:49:42Z
expires_at:
planned_for:
not_before:
window:
est_minutes: 12
chain_id: zombie-2026-11-10
chain_seq: 31
attempts: 1
max_attempts: 3
claimed_by: ticker-2152
claimed_at: 2026-11-14T05:57:05Z
lease_until: 2026-11-14T06:17:05Z
result:
  status: failed
  started_at: 2026-11-14T05:57:05Z
  finished_at: 2026-11-14T05:58:45Z
  duration_seconds: 100
  executor: ticker-2152
  summary: Mac mini unreachable (node_offline, no wake-up path; last seen 2026-11-12T17:52:28Z): 2 computer.session starts failed node_offline, connection.repair on the Mac failed node_offline, connection.repair via recovery device timed out (25s); no game state observable, no input sent, no kills, no claims; NOT the outcome_unknown control-lock (Issue 689), so no blocker_overlay recorded and the next tick will probe again; successor 032 enqueued
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-13/zombie-invasion/2157-queue-run.md
  follow_up: none
  stats:
    zombies_killed: 0
    cleared: false
    coin_before: unread
    coin_after: unread
    coins_collected: 0
    medals_before: unread
    medals_after: unread
    chests_opened: 0
    squads_parallel: 0
    target: clear nearby zombies in one chain round
    achieved: no attacks; device transport down before first input
    resources_gained: none
    costs: about 6 minutes probe, no stamina or items
    verified: no
    blocker_category: f
    control_attempts: 4
  stats_missing: []
  stats_warnings: []
---

# zombie-invasion

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.
