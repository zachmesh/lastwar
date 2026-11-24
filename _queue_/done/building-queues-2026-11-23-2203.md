---
unit: building-queues-2026-11-23-2203
regular: building-queues
activity: building-queues
segment: 1
priority: 3
created_at: 2026-11-24T03:40:03Z
expires_at: 2026-11-24T10:03:00Z
planned_for: 2026-11-24T06:03:00Z
not_before: 2026-11-24T06:03:00Z
window:
est_minutes: 4
serves: PL-08
chain_id:
chain_seq:
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-24T06:15:04Z
lease_until: 2026-11-24T06:35:04Z
result:
  status: done
  started_at: 2026-11-24T06:15:04Z
  finished_at: 2026-11-24T06:18:12Z
  duration_seconds: 188
  executor: operator
  summary: All four builders and both labs busy with ends as predicted, no finished item waiting, Hospital unchanged at 1,364 wounded, 5,306 completed, free room 1,329; slots_idle 0; Total Power 150,046,960
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/building-queues/0615-queue-run.md and 0615-queue-run.csv; run 20261124T061504Z-c84204
  follow_up: the Oil Well Lv.22 ends 08:01:46Z inside the quiet window; the next free builder at 2026-11-26T21:10:37Z
  stats:
    target: idle-slot read: builders, labs and the hospital
    achieved: all read, none idle
    resources_gained: none
    points: 0
    costs: none spent; model 0.216087 USD
    verified: yes
    run_id: 20261124T061504Z-c84204
    run_steps: 17
    actions_done: 16
    actions_refused: 0
    cost_usd: 0.216087
    device_takeovers: 0
    slots_idle: 0
    drags_tried: 0
    drags_cancelled: 0
    rules_used: 1
  stats_missing: []
  stats_warnings: []
---

# building-queues

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

## Brief (definition pointer, from the roster)

This unit is the regular `building-queues`: Building queues - read the four build queues, record running upgrades and idle slots; read-only, never start builds. Its definition is the activity folder `_activities_/building-queues/` (the folder is named for the activity, not the regular id): read its `rule-digest.md` first, then its `INDEX.md`. The map of every regular to its activity folder is `_records_/2026-11-22/queue-planning/2760-regular-to-activity-map.csv`. If the digest does not cover a step, stop with 'blocked by prerequisite' and say which step; never improvise.

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (routes in `_records_/2026-11-22/queue-planning/2700-routes.csv`). Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.

## Brief (planner, the 06:03Z wave specifics)

Idle-slot read: a FINISHED item waiting for its Complete tap (a wrapped gift box) is FINISHED WAITING, not idle: record its name and the minutes since it finished; tap the gift box only if this unit's task is Complete. Close with `--stat slots_idle=<N>` (the TOTAL open slots) and, for slots blocked by a full Drill Ground, `--stat slots_blocked_by_capacity=<N> --stat capacity_blocker="Drill Ground Full"`. Read only: never Train, Collect, Upgrade or Research here.

Safe tap: the bare spot (310,660), not (400,640) after a camera shift (WORLD then BASE first).
