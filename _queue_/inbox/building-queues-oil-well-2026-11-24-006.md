---
unit: building-queues-oil-well-2026-11-24-006
regular: building-queues
activity: building-queues
segment: 1
priority: 9
created_at: 2026-11-23T16:00:30Z
expires_at: 2026-11-26T11:04:00Z
planned_for:
not_before: 2026-11-25T23:04:00Z
window: oil well level 25 to 26 builder b1 chain complete the previous level and start this one
est_minutes: 8
serves: PL-17
chain_id: oil-well-2026-11-24
chain_seq: 6
attempts: 0
max_attempts: 8
claimed_by:
claimed_at:
lease_until:
---

# building-queues

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: PL-17

## Brief (definition pointer, from the roster)

This unit is the regular `building-queues`: Building queues - read the four build queues, record running upgrades and idle slots; read-only, never start builds. Its definition is the activity folder `_activities_/building-queues/` (the folder is named for the activity, not the regular id): read its `rule-digest.md` first, then its `INDEX.md`. The map of every regular to its activity folder is `_records_/2026-11-22/queue-planning/2760-regular-to-activity-map.csv`. If the digest does not cover a step, stop with 'blocked by prerequisite' and say which step; never improvise.

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (routes in `_records_/2026-11-22/queue-planning/2700-routes.csv`). Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.

## Brief (planner, builder B1: Oil Well Lv.25 to 26, PL-17)

serves: PL-17

Route: `_records_/2026-11-22/queue-planning/2900-oil-well-chain.md`. Starts at the Oil Well finish, dispatched by name. FIRST read the Oil Well entry in the hammer panel: if more than 5 minutes remain, write the time left and RELEASE this unit unrun (`queue.py release`). If finished: the well completes by TAPPING THE WRAPPED GIFT BOX on the building (no Complete button; Total Power registers then; never Speed Up or Finish Now); write Total Power before and after. Go to the well by the route in the sheet (drag ONCE per frame, check after each), read the tag ('Oil Well Lv.25'; stop and report if it differs), open the Upgrade preview ('Lv.25 to 26') and write iron cost, output, power, storage, the Upgrade button clock (effective time) and the original time; keep iron above the 150M floor; press Upgrade ONCE; read the timer to the second; write the effective time, the SPEED FACTOR (original over effective), the panel's end time in UTC and the difference in seconds (expected 23,520 s). If the finish falls in the quiet window 08:00Z to 08:25Z, act at 08:25:30Z, or ask the coordinator for an exception if the builder would idle over 15 minutes.
FRONT: if `lsappinfo front` is not LastWar: record, run the standing front script, record; still not: stop, release, tell the Coordinator.
May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Safe tap: (310,660), not (400,640) after a camera shift.
HUD taps: verify each icon by its label or glyph first.
Cost cap, stated: 0.60 USD.
