---
unit: building-queues-oil-well-2026-11-24-005
regular: building-queues
activity: building-queues
segment: 1
priority: 1
created_at: 2026-11-23T16:00:29Z
expires_at: 2026-11-27T02:00:00Z
planned_for: 2026-11-25T10:01:28Z
not_before:
window: oil well level 24 to 25 builder b1 chain complete the previous level and start this one
est_minutes: 8
serves: PL-17
chain_id: oil-well-2026-11-24
chain_seq: 5
attempts: 3
max_attempts: 8
claimed_by: operator
claimed_at: 2026-11-26T04:41:28Z
lease_until: 2026-11-26T05:01:28Z
result:
  status: done
  started_at: 2026-11-26T04:41:28Z
  finished_at: 2026-11-26T04:42:49Z
  duration_seconds: 81
  executor: operator
  summary: Oil Well hand-off: the Oil Well is already Lv.25 in progress (another hand started it): Time Left 08:28:12 at 04:41:44.4Z, end about 13:09:56.4Z; Lv.27 Drill Ground 3d 10:49:17; Lv.28 Drill Ground 7d 09:08:30; one builder idle (Construct); nothing started or pressed; drags 0. state_change: no. state_read: Building Queue row 1 'Lv.25 Oil Well upgrade in progress' Time Left 08:28:12, end about 13:09:56.4Z; row 3 Idle | step 3 | 04:41:44Z
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/building-queues/0441-queue-run.md and 0441-queue-run.csv; run 20261126T044129Z-865084
  state_read: Building Queue row 1 'Lv.25 Oil Well upgrade in progress' Time Left 08:28:12, end about 13:09:56.4Z; row 3 Idle | step 3 | 04:41:44Z
  state_change: no
  follow_up: the Oil Well Lv.25 ends about 13:09:56Z; one builder is idle
  stats:
    target: upgrade the Oil Well Lv.24 to 25
    achieved: already Lv.25 in progress: verified nothing-to-do
    resources_gained: none
    points: 0
    costs: none spent; model 0.087965 USD
    verified: yes
    run_id: 20261126T044129Z-865084
    run_steps: 8
    actions_done: 2
    actions_refused: 0
    cost_usd: 0.087965
    device_takeovers: 0
    claims: 0
    oil_well_end_utc: 13:09:56
    slots_idle: 1
    tram_badge: not read
    drags_tried: 0
    rules_used: 1
  stats_missing: []
  stats_warnings: []
---

# building-queues

Serves: PL-17

## Brief (definition pointer, from the roster)

This unit is the regular `building-queues`: Building queues - read the four build queues, record running upgrades and idle slots; read-only, never start builds. Its definition is the activity folder `_activities_/building-queues/` (the folder is named for the activity, not the regular id): read its `rule-digest.md` first, then its `INDEX.md`. If the digest does not cover a step, stop with 'blocked by prerequisite' and say which step; never improvise.

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (routes in `_records_/2026-11-22/queue-planning/2700-routes.csv`). Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.

## Brief (planner, builder B1: Oil Well Lv.24 to 25, PL-17)

serves: PL-17

Route: `_records_/2026-11-22/queue-planning/2900-oil-well-chain.md`. Starts at the Oil Well finish, by name. FIRST read the Oil Well entry in the hammer panel: if it reads 'Oil Well Lv.25' (another hand started it) do NOT release: close a verified nothing-to-do with a `state_read:` line (the panel, its timer); if the Lv.24 job still has more than 5 minutes left, write the time and RELEASE this unit unrun (`queue.py release`). IF THE ENTRY IS ABSENT from the panel, it is finished: write what the panel shows. Then: the well completes by TAPPING THE WRAPPED GIFT BOX on the building (no Complete button; Total Power registers then; never Speed Up or Finish Now); write Total Power before and after. Go to the well by the route in the sheet (drag ONCE per frame, check after each), read the tag ('Oil Well Lv.24'; stop and report if it differs), open the Upgrade preview ('Lv.24 to 25') and write iron cost, output, power, storage, the Upgrade button clock (effective time) and the original time; keep iron above the 150M floor; press Upgrade ONCE; read the timer to the second; write the effective time, the SPEED FACTOR (original over effective), the panel's end time in UTC and the difference in seconds (expected 23,520 s).
CLOSE by `_records_/2026-11-22/queue-planning/3170-closing-rule-done-and-partial.md`: DONE for the Upgrade pressed or a verified nothing-to-do (`--state-change no`, a `state_read:` line); else PARTIAL.
FRONT: if `lsappinfo front` is not LastWar: record, run the standing front script, record; still not: stop, release, tell the Coordinator.
May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Safe tap: (310,660), not (400,640) after a camera shift.
Cost cap, stated: 0.60 USD.
