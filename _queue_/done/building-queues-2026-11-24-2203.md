---
unit: building-queues-2026-11-24-2203
regular: building-queues
activity: building-queues
segment: 1
priority: 3
created_at: 2026-11-25T02:01:06Z
expires_at: 2026-11-25T09:55:00Z
planned_for: 2026-11-25T06:03:00Z
not_before: 2026-11-25T06:03:00Z
window:
est_minutes: 4
serves: PL-08
chain_id:
chain_seq:
attempts: 0
max_attempts: 3
claimed_by:
claimed_at:
lease_until:
result:
  status: expired
  started_at: 
  finished_at: 2026-11-25T10:01:00Z
  duration_seconds: 
  executor: 
  summary: window passed before execution
  claimed: []
  claimed_count: 0
  evidence: 
  follow_up: none
  stats:
  stats_missing: [target, achieved, resources_gained, costs, verified]
  stats_warnings: []
---

# building-queues

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

## Brief (definition pointer, from the roster)

This unit is the regular `building-queues`: Building queues - read the four build queues, record running upgrades and idle slots; read-only, never start builds. Its definition is the activity folder `_activities_/building-queues/` (the folder is named for the activity, not the regular id): read its `rule-digest.md` first, then its `INDEX.md`. The map of every regular to its activity folder is `_records_/2026-11-22/queue-planning/2760-regular-to-activity-map.csv`. If the digest does not cover a step, stop with 'blocked by prerequisite' and say which step; never improvise.

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (routes in `_records_/2026-11-22/queue-planning/2700-routes.csv`). Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.

## Brief (planner, the specifics)

Idle-slot read: a FINISHED item waiting for its Complete tap (a wrapped gift box) is FINISHED WAITING, not idle: record its name and the minutes since it finished; tap the gift box only if this unit's task is Complete. Close with `--stat slots_idle=<N>` and, for slots blocked by a full Drill Ground, `--stat slots_blocked_by_capacity=<N> --stat capacity_blocker="Drill Ground Full"`. Read only: never Train, Collect, Upgrade or Research here. The four builders run the ground and Oil Well upgrades; the Oil Well hand-offs are named units: this read presses nothing. On each builder row NOTE ANY HELP INDICATOR (a count of helps received) if the panel draws one; open the Alliance Help screen only if this unit already does; press nothing. WRITE EVERY BUILDER'S TIMER AND END TO THE SECOND, above all the three Drill Grounds' ends (the Lv.26 ground read 11-26T21:10:37Z; another actor moved it to about 11-26T11:08Z on 11-24): the 11-26 units are timed from your read.

May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing. Safe tap: the bare spot (310,660), not (400,640) after a camera shift (WORLD then BASE first). Verify each HUD icon by its label or glyph in a frame before the tap.
H118 (Steer A 04:10Z): also read the Oil Well Lv.24 end to the second (the help request's UTC time is in the record of `building-queues-help-test-2026-11-25-001`; the end before it was 07:11:19.6Z) and write it with the UTC time and the minutes since the request.
FRONT (Steer A 21:11Z): at the start, if `lsappinfo front` is not LastWar, record it, run the standing front script, record again; still not LastWar: stop, release, tell the Coordinator.
