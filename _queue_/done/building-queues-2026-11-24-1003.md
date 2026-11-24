---
unit: building-queues-2026-11-24-1003
regular: building-queues
activity: building-queues
segment: 1
priority: 3
created_at: 2026-11-24T14:29:10Z
expires_at: 2026-11-24T21:58:00Z
planned_for: 2026-11-24T18:03:00Z
not_before: 2026-11-24T18:03:00Z
window:
est_minutes: 4
serves: PL-08
chain_id:
chain_seq:
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-24T18:06:21Z
lease_until: 2026-11-24T18:26:21Z
result:
  status: done
  started_at: 2026-11-24T18:06:21Z
  finished_at: 2026-11-24T18:07:27Z
  duration_seconds: 66
  executor: operator
  summary: Builders read: Lv.26 Drill Ground ends 2026-11-26T11:08:36.6Z, Lv.27 ends 11-30T01:31:01.6Z, Lv.28 ends 12-03T23:50:13.6Z, Oil Well Lv.24 ends 11-25T07:11:19.6Z (as expected); no help indicator drawn; tram badge none. state_change: no. state_read: Building Queue: Lv.26 Drill Ground 1d 17:01:55; Lv.27 5d 07:24:20; Lv.23 Oil Well 13:04:38; Lv.28 9d 05:43:32; all in progress, Speed Up only | step 3 | 18:06:41Z
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/building-queues/1606-queue-run.md and 1606-queue-run.csv; run 20261124T180622Z-931b83
  state_read: Building Queue: Lv.26 Drill Ground 1d 17:01:55; Lv.27 5d 07:24:20; Lv.23 Oil Well 13:04:38; Lv.28 9d 05:43:32; all in progress, Speed Up only | step 3 | 18:06:41Z
  state_change: no
  follow_up: the Drill Ground ends are 10 to 36 hours earlier than the 14:48Z read (another actor); the Oil Well Lv.24 completes about 07:11:20Z on 11-25
  stats:
    target: read every builder's timer and end
    achieved: all four read to the second
    resources_gained: none
    points: 0
    costs: none spent; model 0.09006 USD
    verified: yes
    run_id: 20261124T180622Z-931b83
    run_steps: 7
    actions_done: 2
    actions_refused: 0
    cost_usd: 0.09006
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

## Brief (planner, the specifics)

Idle-slot read: a FINISHED item waiting for its Complete tap (a wrapped gift box) is FINISHED WAITING, not idle: record its name and the minutes since it finished; tap the gift box only if this unit's task is Complete. Close with `--stat slots_idle=<N>` and, for slots blocked by a full Drill Ground, `--stat slots_blocked_by_capacity=<N> --stat capacity_blocker="Drill Ground Full"`. Read only: never Train, Collect, Upgrade or Research here. The four builders run the ground and Oil Well upgrades; the Oil Well hand-offs are named units: this read presses nothing. On each builder row NOTE ANY HELP INDICATOR (a count of helps received) if the panel draws one; open the Alliance Help screen only if this unit already does; press nothing. WRITE EVERY BUILDER'S TIMER AND END TO THE SECOND, above all the three Drill Grounds' ends (the Lv.26 ground read 11-26T21:10:37Z; another actor moved it to about 11-26T11:08Z on 11-24): the 11-26 units are timed from your read.

Safe tap: the bare spot (310,660), not (400,640) after a camera shift (WORLD then BASE first). Verify each HUD icon by its label or glyph in a frame before the tap.
