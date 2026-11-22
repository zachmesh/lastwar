---
unit: zombie-invasion-zombie-2026-11-10-035
regular: zombie-invasion
activity: zombie-invasion
segment:
priority: 4
created_at: 2026-11-14T19:09:25Z
expires_at:
planned_for:
not_before:
window:
est_minutes: 12
chain_id: zombie-2026-11-10
chain_seq: 35
attempts: 1
max_attempts: 3
claimed_by: ticker-1328
claimed_at: 2026-11-14T21:33:58Z
lease_until: 2026-11-14T21:53:58Z
result:
  status: failed
  started_at: 2026-11-14T21:33:58Z
  finished_at: 2026-11-14T21:34:18Z
  duration_seconds: 20
  executor: ticker-1328
  summary: Mac mini unreachable (node_offline, no wake-up path; last seen 2026-11-12T17:52:28Z): connection.health failed node_offline, environment.describe failed node_offline, connection.repair failed node_offline, computer.session start failed node_offline; no game state observable, no input sent, no kills, no claims; NOT the outcome_unknown control-lock (Issue 689), so no blocker_overlay recorded and the next tick will probe again; successor 036 enqueued
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-14/zombie-invasion/1333-queue-run.md
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
