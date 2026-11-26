---
unit: building-queues-2026-11-26-0603
regular: building-queues
activity: building-queues
segment: 1
priority: 3
created_at: 2026-11-26T10:00:51Z
expires_at: 2026-11-26T18:03:00Z
planned_for: 2026-11-26T14:03:00Z
not_before: 2026-11-26T14:03:00Z
window:
est_minutes: 4
serves: PL-08
chain_id:
chain_seq:
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-26T17:35:56Z
lease_until: 2026-11-26T17:55:56Z
result:
  status: done
  started_at: 2026-11-26T17:35:56Z
  finished_at: 2026-11-26T17:40:19Z
  duration_seconds: 263
  executor: operator
  summary: Builders read: four of four busy (Oil Well Lv.26 1d 15:13:56, ends 2026-11-28T08:50:10Z; Drill Grounds Lv.27 2d 21:54:48 (ends 2026-11-29T15:31:02Z), Lv.27 11d 15:49:21 (ends 2026-12-08T09:25:35Z) and Lv.28 6d 20:14:00 (ends 2026-12-03T13:50:14Z)); no help count; no white round helmet bubble over any build (the Oil Well carries the oil collect bubble); slots_idle 0; Speed Up never pressed; drags 4. state_change: no. state_read: Building Queue: hammer 4/4, all four rows in progress with Time Left and ends; no helmet bubble | step 3 | 17:36:14Z
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/building-queues/1736-queue-run.md and 1736-queue-run.csv; run 20261126T173556Z-dc9965
  state_read: Building Queue: hammer 4/4, all four rows in progress with Time Left and ends; no helmet bubble | step 3 | 17:36:14Z
  state_change: no
  follow_up: the Oil Well ends 2026-11-28T08:50:10Z; the 3-day ground 2026-11-29T15:31:02Z
  stats:
    target: read idle builder slots and every end time
    achieved: verified all four busy
    resources_gained: none
    points: 0
    costs: none spent; model 0.311421 USD
    verified: yes
    run_id: 20261126T173556Z-dc9965
    run_steps: 25
    actions_done: 10
    actions_refused: 0
    cost_usd: 0.311421
    device_takeovers: 0
    claims: 0
    slots_idle: 0
    hammer: 4/4
    oil_well_end: 2026-11-28T08:50:10Z
    tram_badge: not read
    drags_tried: 4
    rules_used: 1,2
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
