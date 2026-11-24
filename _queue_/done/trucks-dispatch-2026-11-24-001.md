---
unit: trucks-dispatch-2026-11-24-001
regular: trucks
activity: truck-plunder
segment: 2
priority: 1
created_at: 2026-11-24T09:07:55Z
expires_at: 2026-11-24T12:00:00Z
planned_for:
not_before: 2026-11-24T10:00:00Z
window: own truck dispatch the owner daily quota by the verified route
est_minutes: 10
serves: PL-18
chain_id: dispatch-2026-11-24
chain_seq: 1
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-24T10:00:01Z
lease_until: 2026-11-24T10:20:01Z
result:
  status: done
  started_at: 2026-11-24T10:00:01Z
  finished_at: 2026-11-24T10:09:45Z
  duration_seconds: 584
  executor: operator
  summary: Three own trucks dispatched by rule 2 (SR arrives in 04:53:35, SSR 04:07:28, UR 04:00:10; count 3/5; Trade Contracts 261 to 258; no diamond; no Mega Mode); nothing to settle; path: tram icon (107,580) with badge 3 opens Intercity Trade on Others' Trucks (plunder list, untouched), the Your Truck tab holds the slots; drags 0
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/truck-plunder/1000-queue-run.md and 1000-queue-run.csv; run 20261124T100510Z-ad2994
  follow_up: the first truck returns about 14:07Z (UR), then about 14:13Z and 14:59Z; the fifth slot opens when one returns; the plunder units use the Others' Trucks tab only on Steer A's authorization
  stats:
    target: settle returned trucks, dispatch by rule 2
    achieved: nothing to settle; three trucks dispatched
    resources_gained: none
    points: 0
    costs: none spent; model 0.392 USD
    verified: yes
    run_id: 20261124T100510Z-ad2994
    run_steps: 43
    actions_done: 38
    actions_refused: 0
    cost_usd: 0.392
    device_takeovers: 0
    trucks_dispatched: 3
    trade_count: 3/5
    contracts_before: 261
    contracts_after: 258
    drags_tried: 0
    drags_cancelled: 0
    rules_used: 2,3,4,6
  stats_missing: []
  stats_warnings: []
---

# trucks

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: PL-18

## Brief (definition pointer, from the roster)

This unit is the regular `trucks`: Trucks - settle returned trucks via Truck Details, claim trade Reward Recovery, dispatch to fill (duel UR days Mega + UR only, other days SR/SSR/UR), plunder to the cap by the UR shard rule. Its definition is the activity folder `_activities_/truck-plunder/` (the folder is named for the activity, not the regular id): read its `rule-digest.md` first, then its `INDEX.md`. The map of every regular to its activity folder is `_records_/2026-11-22/queue-planning/2760-regular-to-activity-map.csv`. If the digest does not cover a step, stop with 'blocked by prerequisite' and say which step; never improvise.

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (routes in `_records_/2026-11-22/queue-planning/2700-routes.csv`). Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.

## Brief (planner, THE DISPATCH: own trucks, the owner's daily quota)

serves: PL-18

ROUTE (verified): WORLD then BASE; first write the vehicle-front icon's BADGE state (none, red dot or a count) with the UTC time; the tram icon (107,580), glyph verified, ONE tap; on the station frame ONE tap on the white truck-glyph bubble over the TRUCK AND CONTAINER YARD ((165,408) or (120,438), glyph verified): the 'INTERCITY TRADE - TRUCK' dialog (no tabs).
(a) READ FIRST: quality, arrival, rewards, Squad 1, the count (0/5).
(b) SR OR ABOVE as rolled: 'Let's Go' ONCE. BELOW SR: the FREE dice refresh once, then a Trade Contract refresh only after reading the item panel's name and quantity; NEVER a refresh with a diamond. No Mega Mode today.
(c) AFTER THE FIRST DISPATCH READ THE SCREEN THAT FOLLOWS: an Intercity Trade screen with bottom tabs (Others' Trucks, Your Truck) means Others' Trucks is the plunder list: record the PATH (taps, frames); press nothing on it.
(d) Then per dispatch: a frame, arrival, count; up to 4 now, the fifth when one returns. Close by ONE tap on the dimmed margin (40 px outside, no HUD button); write the badge state and trade count again with the UTC time.
After the train boarding (deadline 10:06:44Z); window 10:00Z to 12:00Z; past 10:50Z only if the Coordinator names it. No Plunder or Battle. Another app, alert or dialog: STOP, name `lsappinfo front`; TIPS Cancel only. May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Cost cap, stated: 0.60 USD.
