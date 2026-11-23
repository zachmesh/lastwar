---
unit: building-queues-oil-well-2026-11-24-003
regular: building-queues
activity: building-queues
segment: 1
priority: 1
created_at: 2026-11-23T16:00:27Z
expires_at: 2026-11-26T10:01:00Z
planned_for:
not_before: 2026-11-24T18:01:00Z
window: oil well level 22 to 23 builder b1 chain complete the previous level and start this one
est_minutes: 8
serves: PL-17
chain_id: oil-well-2026-11-24
chain_seq: 3
attempts: 0
max_attempts: 3
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

## Brief (planner, builder B1: Oil Well Lv.22 to 23, chain unit 3 of 10, PL-17)

serves: PL-17

Facts, route and procedure: `_records_/2026-11-22/queue-planning/2900-oil-well-chain.md`. This unit starts when the Oil Well Lv.22 upgrade finishes; the window opens at the earliest possible finish and the coordinator dispatches it by name at the real one. FIRST read the Oil Well entry in the hammer panel: if more than 5 minutes remain, write the time left and RELEASE this unit unrun (`queue.py release --unit <this unit>`), never complete it. If finished: press Complete (never Speed Up or Finish Now); Total Power before and after. Then go to the well by the route in the sheet, read the tag ('Oil Well Lv.22'; stop and report if it differs), open the Upgrade preview ('Lv.22 to 23') and write iron cost, output, power, storage, the Upgrade button clock (the effective time) and the original time; keep iron above the 150M floor; press Upgrade ONCE; read the timer to the second and write the finish time in UTC. If the finish falls in the daily quiet window 08:00Z to 08:25Z, act at the nearest edge, or ask the coordinator for a one-line exception if the builder would idle over 15 minutes.

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (safe tap: bare spot (310,660), not (400,640) after a camera shift). A TIPS dialog about another device: STOP, report, never Confirm. Iron only: no coin, food or oil, no speed-up, never Finish Now. Tag text beside every number; none means [G].
Cost cap, stated: 0.60 USD (the harness stops near 0.36 of it).
