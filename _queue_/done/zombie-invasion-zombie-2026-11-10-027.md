---
unit: zombie-invasion-zombie-2026-11-10-027
regular: zombie-invasion
activity: zombie-invasion
segment:
priority: 4
created_at: 2026-11-12T15:29:17Z
expires_at:
planned_for:
not_before:
window:
est_minutes: 12
chain_id: zombie-2026-11-10
chain_seq: 27
attempts: 1
max_attempts: 3
claimed_by: ticker-0941
claimed_at: 2026-11-12T17:43:06Z
lease_until: 2026-11-12T18:03:06Z
result:
  status: failed
  started_at: 2026-11-12T17:43:06Z
  finished_at: 2026-11-12T17:55:18Z
  duration_seconds: 732
  executor: ticker-0941
  summary: Device input blocked (Issue 689): 3 fresh computer sessions cc-713 cc-714 cc-715 all failed at first input with outcome_unknown, new local user submission required; game verified live on base screen via read-only observe; no kills, no claims; control-lock blocker refreshed (R9); successor 028 enqueued; stale-tool handout (Issue 694)
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-12/zombie-invasion/0943-queue-run.md
  follow_up: successor zombie-invasion-zombie-2026-11-10-028 enqueued (chain zombie-2026-11-10); next tick probes again after the blocker ages out at 19:47Z - see Issues #689, #694
  stats:
    zombies_killed: 0
    cleared: false
    coins_collected: 0
    squads_parallel: 0
    chests_opened: 0
    control_attempts: 3
    target: 2 Lv.10 kills and LOOT claim chain 027
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
