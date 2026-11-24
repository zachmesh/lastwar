---
unit: trucks-dispatch-2026-11-24-003
regular: trucks
activity: truck-plunder
segment: 2
priority: 1
created_at: 2026-11-24T10:03:40Z
expires_at: 2026-11-24T17:30:00Z
planned_for:
not_before: 2026-11-24T15:03:00Z
window: dispatch cycle 3 settle then dispatch estimate to be re-timed from the real arrival
est_minutes: 15
serves: PL-18
chain_id: dispatch-2026-11-24
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

## Brief (planner, TRADE CYCLE B: settle, dispatch and plunder on one badge, Steer A 10:16Z)

serves: PL-18

Do the TRADE CYCLE exactly as `_records_/2026-11-22/queue-planning/3110-trade-cycle.md` says: read it first; its steps 0 to 4 (the Hospital before the tram tap, then settle, dispatch, plunder, close). THIS CYCLE: about 15:05Z: the SR returned 14:59:21Z: SETTLE it; no dispatch (5/5); read the LOCKED slot 4's unlock text (one tap on the lock only if it shows plain text; never an Unlock, Buy or price). NO plunder in this unit: the separate scans `trucks-plunder-scan-b-2026-11-24-001` to `-004` follow it; the SR's slot stays empty at 5/5 so the badge stays lit.
NO badge: close 'badge absent: no tap' (the Coordinator re-dispatches 15 minutes later, at most 3 tries). Up to 3 runs of 12 steps. May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Cost cap, stated: 0.90 USD.
