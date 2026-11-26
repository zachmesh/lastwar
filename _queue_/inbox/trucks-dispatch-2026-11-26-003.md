---
unit: trucks-dispatch-2026-11-26-003
regular: trucks
activity: truck-plunder
segment: 1
priority: 1
created_at: 2026-11-26T05:37:55Z
expires_at: 2026-11-27T02:00:00Z
planned_for:
not_before: 2026-11-26T05:45:00Z
window: trade cycle e re-staged, the day's first window, entry unconditional (steer a 05:37z)
est_minutes: 15
serves: PL-18
chain_id: dispatch-2026-11-26
chain_seq: 3
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

## Brief (planner, TRADE CYCLE E re-staged, the day's first window, Steer A 05:37Z)

serves: PL-18

Do the TRADE CYCLE as `_records_/2026-11-22/queue-planning/3110-trade-cycle.md` (steps 0 to 4, Hospital first) and RULES `_records_/2026-11-22/queue-planning/2544-trade-day-rules.md`: follow both. ENTRY IS UNCONDITIONAL (the 04:45Z partial dispatched nothing): ONE tap on the tram icon whatever it shows, bare or with a badge; if it is NOT DRAWN: WORLD then BASE once and tap where it was last drawn only if it appears, else report. At entry write the icon state with the UTC time, the Your Truck tab badge, the Others' Trucks tab badge, the dispatch count x of 5 and each slot's state (empty, out with a return time, returned waiting): the badge-at-entry sample.
Then SETTLE every returned truck (claim Reward Recovery; write each truck's iron, food and coin; the phone may have settled them), DISPATCH into each EMPTY slot up to the day's remaining count, the downgrade test on the first SR, and PLUNDER up to FOUR (the Hospital free room first: 1,531 at 04:44Z; none after 22:00Z, the siege rule): all per the sheet. The badge-first rule (WORLD then BASE for a dark icon) still applies to LATER settle checks.
Write the icon state (absent, bare or badge N) and its UTC time at EVERY read. Up to TEN runs of 12 steps. FRONT: if `lsappinfo front` is not LastWar: record, run the standing front script, record; still not: stop, release, tell the Coordinator.
CLOSE by `_records_/2026-11-22/queue-planning/3170-closing-rule-done-and-partial.md`: DONE for a taken action or a verified nothing-to-do (`--state-change no`, a `state_read:` line); else PARTIAL.
May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Cost cap, stated: 1.50 USD.
