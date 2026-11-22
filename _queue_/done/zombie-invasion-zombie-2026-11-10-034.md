---
unit: zombie-invasion-zombie-2026-11-10-034
regular: zombie-invasion
activity: zombie-invasion
segment:
priority: 4
created_at: 2026-11-14T16:36:45Z
expires_at:
planned_for:
not_before:
window:
est_minutes: 12
chain_id: zombie-2026-11-10
chain_seq: 34
attempts: 1
max_attempts: 3
claimed_by: ticker-1100
claimed_at: 2026-11-14T19:04:59Z
lease_until: 2026-11-14T19:24:59Z
result:
  status: failed
  started_at: 2026-11-14T19:04:59Z
  finished_at: 2026-11-14T19:09:24Z
  duration_seconds: 265
  executor: ticker-1100
  summary: Mac mini unreachable (node_offline, no wake-up path; last seen 2026-11-12T17:52:28Z): 2 computer.session starts failed node_offline, connection.health failed node_offline, connection.repair via recovery device timed out (25s); no game state observable, no input sent, no kills, no claims; NOT the outcome_unknown control-lock (Issue 689), so no blocker_overlay recorded and the next tick will probe again; successor 035 enqueued
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-14/zombie-invasion/1100-queue-run.md
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
    costs: about 8 minutes probe, no stamina or items
    verified: no
    blocker_category: f
    control_attempts: 4
  stats_missing: []
  stats_warnings: []
---

# zombie-invasion

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.
