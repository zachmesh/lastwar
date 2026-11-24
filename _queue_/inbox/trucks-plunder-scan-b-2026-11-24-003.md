---
unit: trucks-plunder-scan-b-2026-11-24-003
regular: trucks
activity: truck-plunder
segment: 2
priority: 2
created_at: 2026-11-24T10:20:20Z
expires_at: 2026-11-24T17:15:00Z
planned_for:
not_before: 2026-11-24T15:04:00Z
window: one plunder fight after cycle b the badge stays lit at 5 of 5 hospital first
est_minutes: 7
serves: PL-18
chain_id: plunder-scan-b-2026-11-24
chain_seq: 3
attempts: 0
max_attempts: 3
claimed_by:
claimed_at:
lease_until:
---

# trucks

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: PL-18

## Brief (definition pointer, from the roster)

This unit is the regular `trucks`: Trucks - settle returned trucks via Truck Details, claim trade Reward Recovery, dispatch to fill (duel UR days Mega + UR only, other days SR/SSR/UR), plunder to the cap by the UR shard rule. Its definition is the activity folder `_activities_/truck-plunder/` (the folder is named for the activity, not the regular id): read its `rule-digest.md` first, then its `INDEX.md`. The map of every regular to its activity folder is `_records_/2026-11-22/queue-planning/2760-regular-to-activity-map.csv`. If the digest does not cover a step, stop with 'blocked by prerequisite' and say which step; never improvise.

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (routes in `_records_/2026-11-22/queue-planning/2700-routes.csv`). Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.

## Brief (planner, ONE plunder fight 3 of 4 after cycle B, Steer A's GO of 10:04Z)

serves: PL-18

Do `_records_/2026-11-22/queue-planning/3110-trade-cycle.md` steps 0, 1, 3 and 4 (the Hospital before the tram tap, open, plunder, close); skip step 2 (no dispatch: today's five are out) and settle only a truck that is waiting. THIS UNIT: ONE fight (Quick Plunder once, Battle once). The badge stays lit at 5 of 5 because the SR's empty slot (settled by cycle B, `trucks-dispatch-2026-11-24-003`) counts: write the badge state first. NO badge: close 'badge absent: no tap' (the Coordinator re-dispatches 15 minutes later, at most 3 tries). The screen's 'Your Plunder Count Today' decides how many fights remain (stop at 4 of 4), never arithmetic: cycle A may have done two. Record per fight the guard, quality, cargo and loot, and the Hospital free room before and after. It must END by 17:21Z (the Oil Well hand-off is 17:28Z). May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Cost cap, stated: 0.50 USD.
