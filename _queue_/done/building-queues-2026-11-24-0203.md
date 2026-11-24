---
unit: building-queues-2026-11-24-0203
regular: building-queues
activity: building-queues
segment: 1
priority: 3
created_at: 2026-11-24T06:40:27Z
expires_at: 2026-11-24T14:03:00Z
planned_for: 2026-11-24T10:03:00Z
not_before: 2026-11-24T10:03:00Z
window:
est_minutes: 4
serves: PL-08
chain_id:
chain_seq:
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-24T10:15:16Z
lease_until: 2026-11-24T10:35:16Z
result:
  status: done
  started_at: 2026-11-24T10:15:16Z
  finished_at: 2026-11-24T10:17:54Z
  duration_seconds: 158
  executor: operator
  summary: All four builders and both labs busy with ends as predicted, no finished item waiting, Hospital unchanged at 1,364 wounded, 5,306 completed, free room 1,329; slots_idle 0; tram badge none; Total Power 150,051,860
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/building-queues/1015-queue-run.md and 1015-queue-run.csv; run 20261124T101517Z-ea9f9f
  follow_up: the Oil Well Lv.23 ends 17:27:28Z; the next free builder at 2026-11-24T17:27:28Z
  stats:
    target: idle-slot read: builders, labs and the hospital
    achieved: all read, none idle
    resources_gained: none
    points: 0
    costs: none spent; model 0.190772 USD
    verified: yes
    run_id: 20261124T101517Z-ea9f9f
    run_steps: 15
    actions_done: 14
    actions_refused: 0
    cost_usd: 0.190772
    device_takeovers: 0
    slots_idle: 0
    tram_badge: none
    drags_tried: 0
    rules_used: 1
  stats_missing: []
  stats_warnings: []
---

# building-queues

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

## Brief (definition pointer, from the roster)

This unit is the regular `building-queues`: Building queues - read the four build queues, record running upgrades and idle slots; read-only, never start builds. Its definition is the activity folder `_activities_/building-queues/` (the folder is named for the activity, not the regular id): read its `rule-digest.md` first, then its `INDEX.md`. The map of every regular to its activity folder is `_records_/2026-11-22/queue-planning/2760-regular-to-activity-map.csv`. If the digest does not cover a step, stop with 'blocked by prerequisite' and say which step; never improvise.

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (routes in `_records_/2026-11-22/queue-planning/2700-routes.csv`). Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.

## Brief (planner, the 10:03Z wave specifics)

Idle-slot read: a FINISHED item waiting for its Complete tap (a wrapped gift box) is FINISHED WAITING, not idle: record its name and the minutes since it finished; tap the gift box only if this unit's task is Complete. Close with `--stat slots_idle=<N>` and, for slots blocked by a full Drill Ground, `--stat slots_blocked_by_capacity=<N> --stat capacity_blocker="Drill Ground Full"`. Read only: never Train, Collect, Upgrade or Research here. The four builders run the ground and Oil Well upgrades; the Oil Well hand-offs are named units: this read presses nothing.

Safe tap: the bare spot (310,660), not (400,640) after a camera shift (WORLD then BASE first).
HUD taps: verify each HUD icon by its label or glyph in a frame before the tap.
