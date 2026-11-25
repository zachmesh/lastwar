---
unit: building-queues-2026-11-24-1803
regular: building-queues
activity: building-queues
segment: 1
priority: 3
created_at: 2026-11-24T22:01:05Z
expires_at: 2026-11-25T06:03:00Z
planned_for: 2026-11-25T02:03:00Z
not_before: 2026-11-25T02:03:00Z
window:
est_minutes: 4
serves: PL-08
chain_id:
chain_seq:
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-25T02:53:55Z
lease_until: 2026-11-25T03:13:55Z
result:
  status: done
  started_at: 2026-11-25T02:53:55Z
  finished_at: 2026-11-25T02:55:24Z
  duration_seconds: 89
  executor: operator
  summary: Builders read twice: all four busy, ends within 0.3 s of the known ends (Lv.26 Drill Ground 11-25T13:38:35.7Z, Oil Well 07:11:19.7Z, Lv.27 11-30T01:31:01.7Z, Lv.28 12-03T23:50:13.7Z); slots idle 0, blocked by capacity 0, no help indicator; pressed the hammer and the X only; tram icon drawn without a badge; drags 0. state_change: no. state_read: four builder rows in progress with Time Left read twice; ends match the known ends; no idle slot | step 3 | 02:54:20Z
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/building-queues/0253-queue-run.md and 0253-queue-run.csv; run 20261125T025356Z-1d5f2c
  state_read: four builder rows in progress with Time Left read twice; ends match the known ends; no idle slot | step 3 | 02:54:20Z
  state_change: no
  follow_up: the Oil Well completes about 07:11Z (a named hand-off); the Lv.26 Drill Ground about 13:38Z
  stats:
    target: read every builder's timer and end against the known ends
    achieved: 4 rows read, 0 idle
    resources_gained: none
    points: 0
    costs: none spent; model 0.094448 USD
    verified: yes
    run_id: 20261125T025356Z-1d5f2c
    run_steps: 7
    actions_done: 2
    actions_refused: 0
    cost_usd: 0.094448
    device_takeovers: 0
    slots_idle: 0
    slots_blocked_by_capacity: 0
    tram_badge: icon drawn without a badge
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

## Brief (planner, the specifics)

Idle-slot read: a FINISHED item waiting for its Complete tap (a wrapped gift box) is FINISHED WAITING, not idle: record its name and the minutes since it finished; tap the gift box only if this unit's task is Complete. Close with `--stat slots_idle=<N>` and, for slots blocked by a full Drill Ground, `--stat slots_blocked_by_capacity=<N> --stat capacity_blocker="Drill Ground Full"`. Read only: never Train, Collect, Upgrade or Research here. The four builders run the ground and Oil Well upgrades; the Oil Well hand-offs are named units: this read presses nothing. On each builder row NOTE ANY HELP INDICATOR (a count of helps received) if the panel draws one; open the Alliance Help screen only if this unit already does; press nothing. WRITE EVERY BUILDER'S TIMER AND END TO THE SECOND, above all the three Drill Grounds' ends (the Lv.26 ground read 11-26T21:10:37Z; another actor moved it to about 11-26T11:08Z on 11-24): the 11-26 units are timed from your read.

May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing. Safe tap: the bare spot (310,660), not (400,640) after a camera shift (WORLD then BASE first). Verify each HUD icon by its label or glyph in a frame before the tap.
FRONT (Steer A 21:11Z): at the start, if `lsappinfo front` is not LastWar, record it, run the standing front script, record again; still not LastWar: stop, release, tell the Coordinator.
