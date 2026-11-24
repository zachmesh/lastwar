---
unit: building-queues-2026-11-24-0603
regular: building-queues
activity: building-queues
segment: 1
priority: 3
created_at: 2026-11-24T10:02:30Z
expires_at: 2026-11-24T18:03:00Z
planned_for: 2026-11-24T14:03:00Z
not_before: 2026-11-24T14:03:00Z
window:
est_minutes: 4
serves: PL-08
chain_id:
chain_seq:
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-24T14:48:13Z
lease_until: 2026-11-24T15:08:13Z
result:
  status: done
  started_at: 2026-11-24T14:48:13Z
  finished_at: 2026-11-24T14:51:04Z
  duration_seconds: 171
  executor: operator
  summary: All four builders and both labs busy with ends as predicted (Oil Well Lv.23 ends 17:27:28.5Z), no finished item waiting, Hospital unchanged at 1,364 wounded, 5,306 completed, free room 1,329; slots_idle 0; tram badge none
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/building-queues/1448-queue-run.md and 1448-queue-run.csv; run 20261124T144813Z-2a4325
  follow_up: the Oil Well Lv.23 ends 17:27:28.5Z
  stats:
    target: idle-slot read: builders, labs and the hospital
    achieved: all read, none idle
    resources_gained: none
    points: 0
    costs: none spent; model 0.202021 USD
    verified: yes
    run_id: 20261124T144813Z-2a4325
    run_steps: 16
    actions_done: 21
    actions_refused: 0
    cost_usd: 0.202021
    device_takeovers: 0
    slots_idle: 0
    tram_badge: none
    rules_used: 1
  stats_missing: []
  stats_warnings: []
---

# building-queues

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

## Brief (definition pointer, from the roster)

This unit is the regular `building-queues`: Building queues - read the four build queues, record running upgrades and idle slots; read-only, never start builds. Its definition is the activity folder `_activities_/building-queues/` (the folder is named for the activity, not the regular id): read its `rule-digest.md` first, then its `INDEX.md`. The map of every regular to its activity folder is `_records_/2026-11-22/queue-planning/2760-regular-to-activity-map.csv`. If the digest does not cover a step, stop with 'blocked by prerequisite' and say which step; never improvise.

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (routes in `_records_/2026-11-22/queue-planning/2700-routes.csv`). Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.

## Brief (planner, the specifics)

Idle-slot read: a FINISHED item waiting for its Complete tap (a wrapped gift box) is FINISHED WAITING, not idle: record its name and the minutes since it finished; tap the gift box only if this unit's task is Complete. Close with `--stat slots_idle=<N>` and, for slots blocked by a full Drill Ground, `--stat slots_blocked_by_capacity=<N> --stat capacity_blocker="Drill Ground Full"`. Read only: never Train, Collect, Upgrade or Research here. The four builders run the ground and Oil Well upgrades; the Oil Well hand-offs are named units: this read presses nothing.

Safe tap: the bare spot (310,660), not (400,640) after a camera shift (WORLD then BASE first). Verify each HUD icon by its label or glyph in a frame before the tap.
