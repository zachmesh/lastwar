---
unit: building-queues-oil-well-2026-11-24-003
regular: building-queues
activity: building-queues
segment: 1
priority: 1
created_at: 2026-11-23T16:00:27Z
expires_at: 2026-11-24T10:30:00Z
planned_for:
not_before: 2026-11-24T08:07:00Z
window: oil well level 22 to 23 builder b1 chain complete the previous level and start this one
est_minutes: 8
serves: PL-17
chain_id: oil-well-2026-11-24
chain_seq: 3
attempts: 1
max_attempts: 8
claimed_by: operator
claimed_at: 2026-11-24T08:08:46Z
lease_until: 2026-11-24T08:28:46Z
result:
  status: done
  started_at: 2026-11-24T08:08:46Z
  finished_at: 2026-11-24T08:13:50Z
  duration_seconds: 304
  executor: operator
  summary: Oil Well Lv.22 completed by one tap on the gift box at 08:11:06.986Z (Total Power +4,900) and Lv.22 to 23 started once at 08:12:33.334Z (iron 14.4M, effective time 15:46:54); the builders panel ends it 2026-11-24T17:27:27.5Z, 23,520 s under the effective time; drags 3, cancelled 0
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/building-queues/0808-queue-run.md and 0808-queue-run.csv; run 20261124T081154Z-f63c35
  follow_up: the Oil Well Lv.23 ends 2026-11-24T17:27:27.5Z; the next hand-off then
  stats:
    target: complete the finished Oil Well and start Lv.22 to 23
    achieved: completed and started; end 17:27:27.5Z
    resources_gained: none
    points: 0
    costs: none spent; model 0.285 USD
    verified: yes
    run_id: 20261124T081154Z-f63c35
    run_steps: 22
    actions_done: 32
    actions_refused: 0
    cost_usd: 0.285
    device_takeovers: 0
    slots_idle: 0
    complete_utc: 08:11:06.986
    upgrade_utc: 08:12:33.334
    end_utc: 2026-11-24T17:27:27.5Z
    drags_tried: 3
    drags_cancelled: 0
    rules_used: 1,2
  stats_missing: []
  stats_warnings: []
---

# building-queues

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: PL-17

## Brief (definition pointer, from the roster)

This unit is the regular `building-queues`: Building queues - read the four build queues, record running upgrades and idle slots; read-only, never start builds. Its definition is the activity folder `_activities_/building-queues/` (the folder is named for the activity, not the regular id): read its `rule-digest.md` first, then its `INDEX.md`. The map of every regular to its activity folder is `_records_/2026-11-22/queue-planning/2760-regular-to-activity-map.csv`. If the digest does not cover a step, stop with 'blocked by prerequisite' and say which step; never improvise.

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (routes in `_records_/2026-11-22/queue-planning/2700-routes.csv`). Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.

## Brief (planner, builder B1: Oil Well Lv.22 to 23, chain unit 3 of 10, PL-17)

serves: PL-17

Facts, route and procedure: `_records_/2026-11-22/queue-planning/2900-oil-well-chain.md`. This unit starts when the Oil Well Lv.22 upgrade finishes; the coordinator dispatches it by name at the real finish. FIRST read the Oil Well entry in the hammer panel: if more than 5 minutes remain, write the time left and RELEASE this unit unrun (`queue.py release --unit <this unit>`). If finished: the well completes by TAPPING THE WRAPPED GIFT BOX on the building (the panel has no Complete button; Total Power registers then; never Speed Up or Finish Now); write Total Power before and after. Go to the well by the route in the sheet (drag ONCE per frame and check the frame after each drag), read the tag ('Oil Well Lv.22'; stop and report if it differs), open the Upgrade preview ('Lv.22 to 23') and write iron cost, output, power, storage, the Upgrade button clock (the effective time) and the original time; keep iron above the 150M floor; press Upgrade ONCE; read the timer to the second and write the preview's effective time, the panel's end time in UTC and their difference in seconds (expected 23,520 s).
Lv.22 ENDED 08:01:46Z (measured). The cu team released the window: claim now; the hand-off must END BY 08:24Z (the cu window ends 08:25Z) and in any case before 09:45Z.
Safe tap: the bare spot (310,660), not (400,640) after a camera shift.
Cost cap, stated: 0.60 USD.
