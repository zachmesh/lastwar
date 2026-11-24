---
unit: trucks-dispatch-2026-11-24-002
regular: trucks
activity: truck-plunder
segment: 2
priority: 1
created_at: 2026-11-24T10:03:38Z
expires_at: 2026-11-24T16:30:00Z
planned_for:
not_before: 2026-11-24T14:15:00Z
window: dispatch cycle 2 settle then dispatch estimate to be re-timed from the real arrival
est_minutes: 15
serves: PL-18
chain_id: dispatch-2026-11-24
chain_seq: 2
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

## Brief (planner, TRADE CYCLE A: settle, dispatch and plunder on one badge, Steer A 10:16Z)

serves: PL-18

Do the TRADE CYCLE exactly as `_records_/2026-11-22/queue-planning/3110-trade-cycle.md` says: read it first; its steps 0 to 4 (the Hospital before the tram tap, then settle, dispatch, plunder, close). THIS CYCLE: about 14:15Z: the UR (back 14:07:11Z) and the SSR (14:13:31Z) have returned: SETTLE both; DISPATCH the last TWO of today's five (count to 5/5); then, on Others' Trucks, PLUNDER up to TWO fights (the screen's 'Your Plunder Count Today' decides, never arithmetic).
NO badge: close 'badge absent: no tap' (the Coordinator re-dispatches 15 minutes later, at most 3 tries). Up to THREE runs, 25 minutes in all, ENDING BY 15:00Z (the SR returns 14:59Z: cycle B's entry). THE TRADE SCREEN STAYS OPEN across the runs of this unit: do NOT go to the base between runs; each continuation run's first frame names the screen. Record per fight the guard, the quality, the cargo and the loot; after closing, read the Hospital free room again. May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Cost cap, stated: 0.90 USD.
