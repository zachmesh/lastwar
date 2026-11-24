---
unit: trucks-dispatch-2026-11-24-004
regular: trucks
activity: truck-plunder
segment: 2
priority: 1
created_at: 2026-11-24T10:03:41Z
expires_at: 2026-11-25T04:25:00Z
planned_for:
not_before: 2026-11-25T02:15:00Z
window: dispatch cycle 4 settle then dispatch estimate to be re-timed from the real arrival
est_minutes: 15
serves: PL-18
chain_id: dispatch-2026-11-24
chain_seq: 4
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

## Brief (planner, TRADE CYCLE C: settle, dispatch and plunder on one badge, Steer A 10:16Z)

serves: PL-18

Do the TRADE CYCLE exactly as `_records_/2026-11-22/queue-planning/3110-trade-cycle.md` says: read it first; steps 0 to 4 (Hospital first). FIRST write the tram badge state AND ITS COUNT with the UTC time, the slots out and the returned trucks due (the Coach's table). THIS CYCLE: the first window after the 02:00Z reset (count 0/5 and 0/4): today's trucks are settled by B2 and B3; SETTLE only what still waits (probably nothing). NO LIT BADGE AT 02:30Z (Steer A 15:57Z; a stale dot may hide a truck): do WORLD then BASE (the camera moves; NO tap on any icon), then re-read the badge ONCE and write whether it lit (the Coach's probe); enter if lit. DISPATCH THREE (3 out at once). THE DOWNGRADE TEST (Steer A 14:42Z, ONE): on the FIRST truck that reaches SR (not SSR or UR) make ONE MORE refresh (price line read first, no diamond); if it downgrades, refresh until SR or better is back (within ten a slot, 60 a day); write the quality before and after each; one test only, then stop at the first SR or better; PLUNDER up to FOUR.
NO badge: close 'badge absent: no tap' (the Coordinator re-dispatches 15 minutes later, at most 3 tries). Up to TEN runs of 12 steps. May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Cost cap, stated: 1.50 USD.
