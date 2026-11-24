---
unit: building-queues-oil-well-2026-11-24-001
regular: building-queues
activity: building-queues
segment: 1
priority: 1
created_at: 2026-11-23T16:00:26Z
expires_at: 2026-11-24T01:21:00Z
planned_for:
not_before: 2026-11-23T23:20:15Z
window: oil well level 20 to 21 builder b1 chain complete the previous level and start this one
est_minutes: 8
serves: PL-17
chain_id: oil-well-2026-11-24
chain_seq: 1
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-23T23:28:21Z
lease_until: 2026-11-23T23:48:21Z
result:
  status: done
  started_at: 2026-11-23T23:28:21Z
  finished_at: 2026-11-23T23:30:56Z
  duration_seconds: 155
  executor: operator
  summary: Oil Well Lv.20 to 21 started once at 23:29:34.806Z: preview rows iron 8.5M only, no food row, power +4,200; builders panel ends 2026-11-24T02:17:53Z; builder 4 idle
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/building-queues/2328-queue-run.md and 2328-queue-run.csv; run 20261123T232821Z-80ddf5
  follow_up: the Oil Well timer is 6.5 hours under the preview (unexplained); food and coin fell by 2.9M and 1.9M without a row; next the food unit for the third ground
  stats:
    target: Oil Well Lv.20 to 21 start, every cost row read
    achieved: start pressed once, all rows read, no food row
    resources_gained: iron -8.5M
    points: 0
    costs: none spent; model 0.197218 USD
    verified: yes
    run_id: 20261123T232821Z-80ddf5
    run_steps: 14
    actions_done: 25
    actions_refused: 0
    cost_usd: 0.197218
    device_takeovers: 0
    slots_idle: 1
    iron_before: 909.3M
    iron_after: 900.8M
    food_row_shown: no
    rules_used: 1
  stats_missing: []
  stats_warnings: []
---

# building-queues

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: PL-17

## Brief (definition pointer, from the roster)

This unit is the regular `building-queues`: Building queues - read the four build queues, record running upgrades and idle slots; read-only, never start builds. Its definition is the activity folder `_activities_/building-queues/` (the folder is named for the activity, not the regular id): read its `rule-digest.md` first, then its `INDEX.md`. The map of every regular to its activity folder is `_records_/2026-11-22/queue-planning/2760-regular-to-activity-map.csv`. If the digest does not cover a step, stop with 'blocked by prerequisite' and say which step; never improvise.

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (routes in `_records_/2026-11-22/queue-planning/2700-routes.csv`). Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.

## Brief (planner, builder B1: Oil Well Lv.20 to 21 at 09:21Z, the first of ten chain units, PL-17)

serves: PL-17

Facts, route and procedure: `_records_/2026-11-22/queue-planning/2900-oil-well-chain.md`. TIME CHECK: the four Training Base builders finish at 23:20:13Z on 2026-11-23 (corrected from 09:20Z, which was the upgrade's duration, not a clock time) and this unit opens at 23:20:15Z (claimable at the 23:20:20Z dispatch; the operator is idle from 23:10Z); be ready before it. Today's quiet windows end at 18:50Z, so none interferes. Run 1: 1. Hammer icon: press the button each finished Training Base entry shows, Complete or Collect (record its text; never Speed Up or Finish Now); Total Power before and after, since power registers only on Complete; skip: unit `building-queues-growth-convert-2026-11-24-001` runs FIRST and does it. 2. Go to the Oil Well by the route in the sheet; read the tag, which must read 'Oil Well Lv.20' (else stop and report). 3. Open the Upgrade preview ('Lv.20 to 21'): expect output 1,200 to 1,260 an hour, power +4,200, iron 8.5M only, effective time 09:20:18; write every row. 4. Press Upgrade ONCE on the first idle builder; read the timer to the second and write the finish time in UTC (about 08:41Z on 2026-11-24): the coordinator sets the trigger for unit 002. Never Speed Up or Finish Now.

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (safe tap: bare spot (310,660), not (400,640) after a camera shift). A TIPS dialog about another device: STOP, report, never Confirm. Iron only: no coin, food or oil, no speed-up, never Finish Now. Tag text beside every number; none means [G].
Cost cap, stated: 0.60 USD (the harness stops near 0.36 of it).
