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
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-26T08:48:03Z
lease_until: 2026-11-26T09:08:03Z
result:
  status: partial
  started_at: 2026-11-26T08:48:03Z
  finished_at: 2026-11-26T08:50:31Z
  duration_seconds: 148
  executor: operator
  summary: Cycle E entry: the tram icon drawn bare at 08:48:11.6Z; the one unconditional tap at 08:48:16.5Z only panned the camera to the train station (no Intercity Trade, no tab badges, count or slots); WORLD then BASE restored the home view and the icon stayed bare (08:49:39.5Z, 08:49:49.4Z); nothing settled, dispatched or plundered; the different-device dialog never showed; drags 0. state_change: no
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/truck-plunder/0848-queue-run.md and 0848-queue-run.csv; run 20261126T084803Z-abf548
  state_change: no
  follow_up: the trade slots stay unread: a bare icon opens no trade screen; the Coordinator re-dispatches
  stats:
    target: settle, dispatch up to the day's remaining count, plunder up to four
    achieved: entry tapped: bare icon, camera pan only
    resources_gained: none
    points: 0
    costs: none spent; model 0.150859 USD
    verified: yes
    run_id: 20261126T084803Z-abf548
    run_steps: 12
    actions_done: 3
    actions_refused: 0
    cost_usd: 0.150859
    device_takeovers: 0
    claims: 0
    blocker_category: bare tram icon: no trade screen
    tram_badge: bare at every read
    drags_tried: 0
    rules_used: 1,2
  stats_missing: []
  stats_warnings: [blocker_category not in enum a-i]
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
