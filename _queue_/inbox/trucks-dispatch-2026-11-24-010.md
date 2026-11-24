---
unit: trucks-dispatch-2026-11-24-010
regular: trucks
activity: truck-plunder
segment: 2
priority: 1
created_at: 2026-11-24T15:59:13Z
expires_at: 2026-11-24T20:30:00Z
planned_for:
not_before: 2026-11-24T18:50:00Z
window: cycle b3 settle only the ur that returns about 18:46:07z
est_minutes: 10
serves: PL-18
chain_id: dispatch-2026-11-24
chain_seq: 10
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

## Brief (planner, TRADE CYCLE B3: settle the UR only, Steer A 15:57Z)

serves: PL-18

The UR of cycle A returns about 18:46:07Z (cargo iron 3.8M, food 3.8M, coin 2.4M). Opens about 18:50Z. FIRST write the tram badge state AND ITS COUNT with the UTC time. No badge: close 'badge absent: no tap' (3 tries at most). Badge lit: ONE tap on the tram icon opens Intercity Trade; read the HUD diamonds, iron, food and coin; SETTLE the UR by one tap on its slot; read the HUD after; on the Your Truck tab write its return stamp, deadline or timer, quality and cargo. No dispatch (5/5), no fight. Close with the back arrow. Ten minutes, up to 6 runs. May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Cost cap, stated: 1.00 USD.
