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

Serves: PL-18

## Brief (definition pointer, from the roster)

This unit is the regular `trucks`: Trucks - settle returned trucks via Truck Details, claim trade Reward Recovery, dispatch to fill (duel UR days Mega + UR only, other days SR/SSR/UR), plunder to the cap by the UR shard rule. Its definition is the activity folder `_activities_/truck-plunder/` (the folder is named for the activity, not the regular id): read its `rule-digest.md` first, then its `INDEX.md`. If the digest does not cover a step, stop with 'blocked by prerequisite' and say which step; never improvise.

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (routes in `_records_/2026-11-22/queue-planning/2700-routes.csv`). Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.

## Brief (planner, TRADE CYCLE D, Steer A 10:16Z and 02:51Z)

serves: PL-18

Do the TRADE CYCLE as `_records_/2026-11-22/queue-planning/3110-trade-cycle.md` says (steps 0 to 4, Hospital first). FIRST write the tram badge state AND ITS COUNT with the UTC time, and BOTH trade tab badges at entry. THIS CYCLE [M, cycle C's record]: the returns are UR 06:19:17Z, SR 06:19:38Z, SSR 06:39:30Z (the SSR not back at 06:40Z: wait for its timer): SETTLE all three, then DISPATCH the last TWO (count to 5/5); plunder was 4 of 4: read the count, do NOT fight. It ends before 08:00Z.
DOWNGRADE TEST (Steer A 02:51Z, one of five): on the FIRST truck that reaches SR (never an SSR or UR) make ONE MORE refresh (price line first, no diamond); write quality before and after; if it downgrades, refresh until SR or better is back, within the slot's ten, the day's 60 and the floor 80.
THE FOURTH SLOT: tap the padlock on slot 4 ONCE; read it by TEXT; close it by its X; a price or purchase surface: STOP.
NO badge at the first read: WORLD then BASE (one tap each on the standing corner button, no icon), read once: lit: enter; dark: close 'badge absent: no tap'. Write the UTC times of the dark read, the WORLD tap, the BASE tap and the lit read, and the icon state at EVERY read. Up to TEN runs of 12 steps. FRONT: if `lsappinfo front` is not LastWar: record, run the standing front script, record; still not: stop, release, tell the Coordinator.
May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Cost cap, stated: 1.50 USD.
