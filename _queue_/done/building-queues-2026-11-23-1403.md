---
unit: building-queues-2026-11-23-1403
regular: building-queues
activity: building-queues
segment: 1
priority: 3
created_at: 2026-11-23T19:08:20Z
expires_at: 2026-11-24T02:03:00Z
planned_for: 2026-11-23T22:03:00Z
not_before: 2026-11-23T22:03:00Z
window:
est_minutes: 2
serves: PL-08
chain_id:
chain_seq:
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-23T22:12:33Z
lease_until: 2026-11-23T22:32:33Z
result:
  status: done
  started_at: 2026-11-23T22:12:33Z
  finished_at: 2026-11-23T22:13:43Z
  duration_seconds: 70
  executor: operator
  summary: Four builders busy on Training Base to Lv.25, ending 23:20:12.5Z to 23:20:23.5Z today; slots_idle 0, nothing blocked by capacity
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/building-queues/2212-queue-run.md and 2212-queue-run.csv; run 20261123T221234Z-8b688f
  follow_up: builders free from 23:20:12.5Z; the first builder unit is sent 23:20:20Z
  stats:
    target: read the builder queue, slots_idle
    achieved: 4 of 4 timers read to the second, slots_idle 0
    resources_gained: none
    points: 0
    costs: none spent; model 0.075295 USD
    verified: yes
    run_id: 20261123T221234Z-8b688f
    run_steps: 6
    actions_done: 9
    actions_refused: 0
    cost_usd: 0.075295
    device_takeovers: 0
    slots_idle: 0
    slots_blocked_by_capacity: 0
    rules_used: 1
  stats_missing: []
  stats_warnings: []
---

# building-queues

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

## Brief (definition pointer, from the roster)

This unit is the regular `building-queues`: Building queues - read the four build queues, record running upgrades and idle slots; read-only, never start builds. Its definition is the activity folder `_activities_/building-queues/` (the folder is named for the activity, not the regular id): read its `rule-digest.md` first, then its `INDEX.md`. The map of every regular to its activity folder is `_records_/2026-11-22/queue-planning/2760-regular-to-activity-map.csv`. If the digest does not cover a step, stop with 'blocked by prerequisite' and say which step; never improvise.

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (routes in `_records_/2026-11-22/queue-planning/2700-routes.csv`). Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.

## Brief (planner, the 22:03Z wave specifics)

Idle-slot read: close with `--stat slots_idle=<N>`, the TOTAL open slots including the blocked ones, and for slots blocked by a full Drill Ground `--stat slots_blocked_by_capacity=<N> --stat capacity_blocker="Drill Ground Full"` (blocker at most 40 characters); name it 'blocked by capacity: Drill Ground Full' with the building tag text. Read only: never Train, Collect, Upgrade or Research here. The four builders are freed at 23:20Z today: the Oil Well chain unit `building-queues-oil-well-2026-11-24-001` and the ground units start them; this read presses nothing.

Safe tap: the bare spot (310,660), not (400,640) after a camera shift (WORLD then BASE first).
