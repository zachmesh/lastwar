---
unit: building-queues-oil-well-2026-11-24-004
regular: building-queues
activity: building-queues
segment: 1
priority: 1
created_at: 2026-11-23T16:00:28Z
expires_at: 2026-11-24T19:30:00Z
planned_for:
not_before: 2026-11-24T17:26:00Z
window: oil well level 23 to 24 builder b1 chain complete the previous level and start this one
est_minutes: 8
serves: PL-17
chain_id: oil-well-2026-11-24
chain_seq: 4
attempts: 1
max_attempts: 8
claimed_by: operator
claimed_at: 2026-11-24T17:28:26Z
lease_until: 2026-11-24T17:48:26Z
result:
  status: done
  started_at: 2026-11-24T17:28:26Z
  finished_at: 2026-11-24T17:33:35Z
  duration_seconds: 309
  executor: operator
  summary: Oil Well Lv.24 started once by a plain Upgrade at 17:31:42.0Z (the Lv.23 had already completed: builder 3 idle, no gift box): iron 17.8M (783.4M to 765.6M), original time 1d 22:57:01, effective 20:11:38, the builders panel's real end 2026-11-25T07:11:20Z (23,520 s under the effective time); other state changes seen: coin down 11.7M and Total Power up 51,432 since 15:56Z, the drill-ground ends earlier, food down 6.0M and coin down 3.9M during the run (not this upgrade's cost); tram badge none. state_change: yes
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/building-queues/1731-queue-run.md and 1731-queue-run.csv; run 20261124T173103Z-b1af64
  follow_up: the Oil Well Lv.24 ends 2026-11-25T07:11:20Z; the three Drill Ground ends moved earlier (planner to re-read); the research Complete (Food Output V, ended 17:29:54Z) is its own unit; builder 3 is busy again
  stats:
    target: complete the Lv.23 and start the Oil Well Lv.24
    achieved: Lv.24 started (the Lv.23 was already complete)
    resources_gained: none
    points: 0
    costs: none spent; model 0.332237 USD
    verified: yes
    run_id: 20261124T173103Z-b1af64
    run_steps: 23
    actions_done: 32
    actions_refused: 0
    cost_usd: 0.332237
    device_takeovers: 0
    claims: 0
    upgrade_started: Oil Well Lv.24
    real_end_utc: 2026-11-25T07:11:20Z
    iron_cost: 17.8M
    tram_badge: none
    drags_tried: 2
    drags_cancelled: 0
    rules_used: 1,2,4
  stats_missing: []
  stats_warnings: []
---

# building-queues

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: PL-17

## Brief (definition pointer, from the roster)

This unit is the regular `building-queues`: Building queues - read the four build queues, record running upgrades and idle slots; read-only, never start builds. Its definition is the activity folder `_activities_/building-queues/` (the folder is named for the activity, not the regular id): read its `rule-digest.md` first, then its `INDEX.md`. The map of every regular to its activity folder is `_records_/2026-11-22/queue-planning/2760-regular-to-activity-map.csv`. If the digest does not cover a step, stop with 'blocked by prerequisite' and say which step; never improvise.

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (routes in `_records_/2026-11-22/queue-planning/2700-routes.csv`). Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.

## Brief (planner, builder B1: Oil Well Lv.23 to 24, chain unit 4 of 10, PL-17)

serves: PL-17

Facts, route and procedure: `_records_/2026-11-22/queue-planning/2900-oil-well-chain.md`. This unit starts when the Oil Well Lv.23 upgrade finishes; the coordinator dispatches it by name at the real finish: Lv.23 ENDS 2026-11-24T17:27:27.5Z (measured, difference 23,520 s); research Complete follows. FIRST read the Oil Well entry in the hammer panel: if more than 5 minutes remain, write the time left and RELEASE this unit unrun (`queue.py release --unit <this unit>`). If finished: the well completes by TAPPING THE WRAPPED GIFT BOX on the building (the panel has no Complete button; Total Power registers then; never Speed Up or Finish Now); write Total Power before and after. Go to the well by the route in the sheet (drag ONCE per frame and check the frame after each drag), read the tag ('Oil Well Lv.23'; stop and report if it differs), open the Upgrade preview ('Lv.23 to 24') and write iron cost, output, power, storage, the Upgrade button clock (the effective time) and the original time; keep iron above the 150M floor; press Upgrade ONCE; read the timer to the second and write the preview's effective time, the panel's end time in UTC and their difference in seconds (expected 23,520 s). If the finish falls in the daily quiet window 08:00Z to 08:25Z, act at 08:25:30Z, or ask the coordinator for a one-line exception if the builder would idle over 15 minutes.
Safe tap: the bare spot (310,660), not (400,640) after a camera shift.
HUD taps: verify each HUD icon by its label or glyph in a frame before the tap.
Cost cap, stated: 0.60 USD.
