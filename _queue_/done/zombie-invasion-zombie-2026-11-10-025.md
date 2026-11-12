---
unit: zombie-invasion-zombie-2026-11-10-025
regular: zombie-invasion
activity: zombie-invasion
segment:
priority: 4
created_at: 2026-11-12T09:16:19Z
expires_at:
planned_for:
not_before:
window:
est_minutes: 12
chain_id: zombie-2026-11-10
chain_seq: 25
attempts: 1
max_attempts: 3
claimed_by: ticker-0304
claimed_at: 2026-11-12T11:17:28Z
lease_until: 2026-11-12T11:37:28Z
result:
  status: failed
  started_at: 2026-11-12T11:17:28Z
  finished_at: 2026-11-12T11:19:16Z
  duration_seconds: 108
  executor: ticker-0304
  summary: Device input blocked (Issue 689): 3 fresh computer sessions cc-703 cc-704 cc-705 all failed at first input with outcome_unknown, new local user submission required; game verified live on base screen via read-only snap (power 149218973, coin 145.7M HUD, stamina 84, unchanged since 0134); no kills, no claims; control-lock blocker recorded (R9); successor 026 enqueued
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-12/zombie-invasion/0320-queue-run.md
  follow_up: none
  stats:
    zombies_killed: 0
    cleared: false
    coins_collected: 0
    squads_parallel: 0
    chests_opened: 0
    control_attempts: 3
    target: 2 Lv.10 kills and LOOT claim chain 025
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
