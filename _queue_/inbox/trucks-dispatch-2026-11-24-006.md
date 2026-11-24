---
unit: trucks-dispatch-2026-11-24-006
regular: trucks
activity: truck-plunder
segment: 2
priority: 1
created_at: 2026-11-24T10:13:23Z
expires_at: 2026-11-25T07:55:00Z
planned_for:
not_before: 2026-11-25T06:40:00Z
window: dispatch the last two after the 02:00Z reset
est_minutes: 15
serves: PL-18
chain_id: dispatch-2026-11-24
chain_seq: 6
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

## Brief (planner, TRADE CYCLE D: settle, dispatch and plunder on one badge, Steer A 10:16Z)

serves: PL-18

Do the TRADE CYCLE exactly as `_records_/2026-11-22/queue-planning/3110-trade-cycle.md` says: read it first; its steps 0 to 4 (the Hospital before the tram tap, then settle, dispatch, plunder, close). FIRST write the tram badge state AND ITS COUNT with the UTC time, the slots out and the returned trucks due (the Coach's table). THIS CYCLE: ESTIMATE, re-timed from the real arrivals of cycle C (it ends before the 08:00Z window): SETTLE; DISPATCH the last TWO (count to 5/5); PLUNDER what remains of the count.
NO badge at the FIRST read: WORLD then BASE (one tap each on the standing corner button, no icon), then read the badge ONCE: lit: enter; still dark: close 'badge absent: no tap' (3 tries at most) (Steer A 16:02Z; the 18:21Z test lit a stale dot). Write the UTC clock time of the dark read, the WORLD tap, the BASE tap and the lit read (the Coach's series: refresh to light). Also read the badge on the WORLD frame (about 3 s after the WORLD tap) and for EVERY read write the icon state: absent (not drawn), bare or badge N. Up to TEN runs of 12 steps. May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Cost cap, stated: 1.50 USD.
