---
unit: zombie-invasion-zombie-2026-11-10-026
regular: zombie-invasion
activity: zombie-invasion
segment:
priority: 4
created_at: 2026-11-12T11:19:21Z
expires_at:
planned_for:
not_before:
window:
est_minutes: 12
chain_id: zombie-2026-11-10
chain_seq: 26
attempts: 1
max_attempts: 3
claimed_by: ticker-0704
claimed_at: 2026-11-12T15:20:49Z
lease_until: 2026-11-12T15:40:49Z
result:
  status: failed
  started_at: 2026-11-12T15:20:49Z
  finished_at: 2026-11-12T15:29:11Z
  duration_seconds: 502
  executor: ticker-0704
  summary: Device input blocked (Issue 689): 3 fresh computer sessions cc-708 cc-709 cc-710 all failed at first input with outcome_unknown, new local user submission required; first R9 stale-bound probe failed, no self-clear after 4h; game verified live on base screen via read-only snap (power 149218973, coin 145.7M HUD, unchanged since 0134); no kills, no claims; control-lock blocker re-recorded (R9); successor 027 enqueued
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-12/zombie-invasion/0720-queue-run.md
  follow_up: none
  stats:
    zombies_killed: 0
    cleared: false
    coins_collected: 0
    squads_parallel: 0
    chests_opened: 0
    control_attempts: 3
    target: 2 Lv.10 kills and LOOT claim chain 026
    achieved: 0
    resources_gained: none
    costs: 3 control attempts, no stamina or items spent
    verified: no
    blocker_category: e
    blocker_overlay: control-lock
  stats_missing: []
  stats_warnings: []
---

# zombie-invasion

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.
