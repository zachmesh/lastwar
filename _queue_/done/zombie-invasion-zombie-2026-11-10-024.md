---
unit: zombie-invasion-zombie-2026-11-10-024
regular: zombie-invasion
activity: zombie-invasion
segment:
priority: 4
created_at: 2026-11-12T08:31:41Z
expires_at:
planned_for:
not_before:
window:
est_minutes: 12
chain_id: zombie-2026-11-10
chain_seq: 24
attempts: 1
max_attempts: 3
claimed_by: ticker-0234
claimed_at: 2026-11-12T10:39:22Z
lease_until: 2026-11-12T10:59:22Z
result:
  status: failed
  started_at: 2026-11-12T10:39:22Z
  finished_at: 2026-11-12T10:40:44Z
  duration_seconds: 82
  executor: ticker-0234
  summary: Device input blocked (Issue 689): 3 fresh computer sessions cc-700 cc-701 cc-702 all failed at first input with outcome_unknown, new local user submission required; game verified live on base screen via read-only snap (power 149218973, coin 145.7M HUD, unchanged since 0134); no kills, no claims; successor 025 already in inbox
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-12/zombie-invasion/0247-queue-run.md
  follow_up: next tick retries zombie 025; channel lock needs local user submission or clearing (Issue 689)
  stats:
    zombies_killed: 0
    cleared: false
    coins_collected: 0
    squads_parallel: 0
    chests_opened: 0
    control_attempts: 3
  stats_missing: [target, achieved, resources_gained, costs, verified, blocker_category]
  stats_warnings: []
---

# zombie-invasion

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.
