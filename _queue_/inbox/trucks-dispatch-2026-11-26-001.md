---
unit: trucks-dispatch-2026-11-26-001
regular: trucks
activity: truck-plunder
segment: 1
priority: 1
created_at: 2026-11-25T22:17:41Z
expires_at: 2026-11-27T02:00:00Z
planned_for:
not_before: 2026-11-26T02:15:00Z
window: trade cycle e first window of the 11-26 day settle and dispatch three and plunder
est_minutes: 15
serves: PL-18
chain_id: dispatch-2026-11-26
chain_seq: 1
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

## Brief (planner, TRADE CYCLE E, the 11-26 day, Steer A 22:15Z)

serves: PL-18

Do the TRADE CYCLE as `_records_/2026-11-22/queue-planning/3110-trade-cycle.md` (steps 0 to 4, Hospital first) and RULES `_records_/2026-11-22/queue-planning/2544-trade-day-rules.md`: follow both. FIRST write the tram badge state AND ITS COUNT with the UTC time, and BOTH tab badges. First window of the 11-26 day: SETTLE every returned truck (cycle C's may still wait: claim Reward Recovery), then DISPATCH into each EMPTY slot, up to THREE (count to 3/5), the downgrade test on the first SR, and PLUNDER up to FOUR with the siege rule (none after 22:00Z): all per the sheet.
NO badge at the first read: WORLD then BASE (one tap each on the standing corner button, no icon), read ONCE: lit: enter; dark: close 'badge absent: no tap'. Write the icon state (absent, bare or badge N) and its UTC time at EVERY read. Up to TEN runs of 12 steps. FRONT: if `lsappinfo front` is not LastWar: record, run the standing front script, record; still not: stop, release, tell the Coordinator.
May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Cost cap, stated: 1.50 USD.
