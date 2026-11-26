---
unit: trucks-dispatch-2026-11-26-005
regular: trucks
activity: truck-plunder
segment: 1
priority: 1
created_at: 2026-11-26T09:54:07Z
expires_at: 2026-11-27T02:00:00Z
planned_for:
not_before: 2026-11-26T13:30:00Z
window: trade cycle h, the next dot, settle and plunders (coordinator 09:55z)
est_minutes: 15
serves: PL-18
chain_id: dispatch-2026-11-26
chain_seq: 5
attempts: 0
max_attempts: 3
claimed_by:
claimed_at:
lease_until:
---

# trucks

Serves: PL-18

## Brief (definition pointer, from the roster)

This unit is the regular `trucks`: Trucks - settle returned trucks via Truck Details, claim trade Reward Recovery, dispatch to fill (duel UR days Mega + UR only, other days SR/SSR/UR), plunder to the cap by the UR shard rule. Its definition is the activity folder `_activities_/truck-plunder/` (the folder is named for the activity, not the regular id): read its `rule-digest.md` first, then its `INDEX.md`. If the digest does not cover a step, stop with 'blocked by prerequisite' and say which step; never improvise.

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (routes in `_records_/2026-11-22/queue-planning/2700-routes.csv`). Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.

## Brief (planner, TRADE CYCLE H, the next dot: settle, Coordinator 09:55Z)

serves: PL-18

DISPATCH ONLY WHEN NAMED, on a DOT (a returned truck: the 09:07Z dispatch is back about 13:33Z, the phone's truck is unread, the 09:52Z dispatch about 14:16Z). A BARE icon after ONE WORLD then BASE is a verified nothing-to-do (3170 DONE): no tap on it.
Do the TRADE CYCLE as `_records_/2026-11-22/queue-planning/3110-trade-cycle.md` and RULES `_records_/2026-11-22/queue-planning/2544-trade-day-rules.md`: follow both. The day's dispatch count is 5 of 5: NO dispatch, so no downgrade test today (sheet 2544 carries it). ORDER: (0) the Hospital free room: reuse a read made within the last hour, else read it BEFORE the tram tap; NEVER leave the trade screen between the entry and the Others' tab. (1) Enter on the dot; write the icon state, both tab badges, the count x of 5 and each slot's state. (2) Read the Others' tab FIRST: PLUNDER only while the day's count is under 4 of 4 (2 of 4 done at 09:52Z), a guard under Squad 1 (26.10M), free room at least 1,000, the casualty guard of 2544, none after 22:00Z. (3) Then the Your Truck tab: settle every returned truck (write each truck's iron, food and coin).
Write the icon state and its UTC time at EVERY read. Up to TEN runs of 12 steps. FRONT: if `lsappinfo front` is not LastWar: record, run the standing front script, record; still not: stop, release, tell the Coordinator.
CLOSE by `_records_/2026-11-22/queue-planning/3170-closing-rule-done-and-partial.md`: DONE for a taken action or a verified nothing-to-do (`--state-change no`, a `state_read:` line); else PARTIAL.
May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Cost cap, stated: 1.50 USD.
