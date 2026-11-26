---
unit: building-queues-drill-ground-2026-11-25-001
regular: building-queues
activity: building-queues
segment: 1
priority: 1
created_at: 2026-11-25T10:13:50Z
expires_at: 2026-11-26T04:43:52Z
planned_for: 2026-11-25T18:00:59Z
not_before:
window: drill ground hand-off: the completed ground's next level 27 to 28, steer a 10:12z default
est_minutes: 15
serves: PL-08
chain_id: drill-ground-2026-11-25
chain_seq: 1
attempts: 0
max_attempts: 3
claimed_by:
claimed_at:
lease_until:
result:
  status: expired
  started_at:
  finished_at: 2026-11-26T04:43:52Z
  duration_seconds: 
  executor:
  summary: retired by the planner: the phone already started the Drill Ground upgrade (builders panel 04:41:44Z: Lv.27 Drill Ground 3d 10:49:17 left), so the hand-off and its coin preconvert are moot; no chest used
  claimed: []
  claimed_count: 0
  evidence: 
  follow_up: none
  stats:
  stats_missing: [target, achieved, resources_gained, costs, verified]
  stats_warnings: []
---

# building-queues

Serves: PL-08

## Brief (definition pointer, from the roster)

This unit is the regular `building-queues`: Building queues - read the four build queues, record running upgrades and idle slots; read-only, never start builds. Its definition is the activity folder `_activities_/building-queues/` (the folder is named for the activity, not the regular id): read its `rule-digest.md` first, then its `INDEX.md`. If the digest does not cover a step, stop with 'blocked by prerequisite' and say which step; never improvise.

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (routes in `_records_/2026-11-22/queue-planning/2700-routes.csv`). Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.

## Brief (planner, the Drill Ground's next level with a preconvert, PL-08)

serves: PL-08

The ground that completes at 2026-11-25T13:38:36Z becomes Lv.27; next: Lv.27 to 28. RULES: `_records_/2026-11-22/queue-planning/2542-drill-ground-preconvert-rules.md` and sheets 2540, 2541. Runs AFTER `training-room-collect-2026-11-25-001` closes; if it has not run, tap the ground's WRAPPED GIFT BOX yourself ONCE.
(1) FIRST the builders panel and the chest counts (2542: STOP if no idle builder or the supply is short), then the tag ('Drill Ground Lv.27', else STOP) and the Upgrade preview: every cost row. FLOORS after the cost: iron at least 100M, food at least 30M, coin at least 10M.
(2) If any resource would fall under cost plus floor: PRECONVERT FIRST, fixed chests only: UR food, then SSR food; UR coin, then SSR coin; the shortfall plus about 10 percent, highest tier first. Each Use: the Resources tab opens with the 5,000 Diamonds x16 tile SELECTED and a LIVE Use: NEVER tap that tile; select the chest tile by icon and count tag, read its NAME and the count, set the smaller of the needed quantity and the count with the plus button, read the field in a frame, Use; the HUD must rise by quantity times value within 1 percent or STOP. THE RESERVE R5 IS NEVER TOUCHED; any diamond line or price: STOP.
(3) Press Upgrade ONCE; write the timer, speed factor, end UTC.
Up to FOURTEEN runs of 12 steps. Cost cap: 1.20 USD.
CLOSE by `_records_/2026-11-22/queue-planning/3170-closing-rule-done-and-partial.md`: DONE for the Upgrade pressed or a verified nothing-to-do or stop (`state_read:` line); `--state-change yes` if pressed.
FRONT: if `lsappinfo front` is not LastWar: record, run the standing front script, record; still not: stop, release, tell the Coordinator.
May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
