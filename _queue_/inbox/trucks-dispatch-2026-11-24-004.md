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

Do the TRADE CYCLE as `_records_/2026-11-22/queue-planning/3110-trade-cycle.md` says (steps 0 to 4, Hospital first). FIRST write the tram badge state AND ITS COUNT with the UTC time. First window after the 02:00Z reset: SETTLE only what still waits; DISPATCH THREE. THE DOWNGRADE TEST (Steer A 14:42Z, ONE): on the FIRST truck that reaches SR (not SSR or UR) make ONE MORE refresh (price line first); if it downgrades, refresh until SR or better is back, within the slot's ten and the day's 60; write quality before and after each; one test only, then stop at the first SR or better; PLUNDER up to FOUR.
NO badge at the first read: WORLD then BASE (one tap each on the standing corner button, no icon), then read ONCE: lit: enter; still dark: close 'badge absent: no tap'. For EVERY read (the WORLD frame about 3 s after the WORLD tap included) write the icon state (absent, bare or badge N), its UTC time and the WORLD and BASE tap times. With every slot settled and nothing waiting, the refresh is the Coach's CONTROL (it should stay dark): write that nothing waited. Up to TEN runs. FRONT: if `lsappinfo front` is not LastWar: record, run the standing front script, record; still not: stop, release, tell the Coordinator. May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Cost cap, stated: 1.50 USD.
