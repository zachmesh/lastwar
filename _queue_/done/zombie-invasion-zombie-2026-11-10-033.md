---
unit: zombie-invasion-zombie-2026-11-10-033
regular: zombie-invasion
activity: zombie-invasion
segment:
priority: 4
created_at: 2026-11-14T14:07:58Z
expires_at:
planned_for:
not_before:
window:
est_minutes: 12
chain_id: zombie-2026-11-10
chain_seq: 33
attempts: 1
max_attempts: 3
claimed_by: ticker-0804
claimed_at: 2026-11-14T16:35:26Z
lease_until: 2026-11-14T16:55:26Z
result:
  status: failed
  started_at: 2026-11-14T16:35:26Z
  finished_at: 2026-11-14T16:36:32Z
  duration_seconds: 66
  executor: ticker-0804
  summary: Mac mini unreachable (node_offline, no wake-up path; last seen 2026-11-12T17:52:28Z): connection.health, environment.describe and computer.session start failed node_offline, connection.repair via recovery device timed out (25s); no game state observable, no input sent, no kills, no claims; NOT the outcome_unknown control-lock (Issue 689), so no blocker_overlay recorded and the next tick will probe again; successor 034 enqueued
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-14/zombie-invasion/0804-queue-run.md
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
    costs: about 6 minutes probing, no stamina or items
    verified: no
    blocker_category: f
  stats_missing: []
  stats_warnings: []
---

# zombie-invasion

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.
