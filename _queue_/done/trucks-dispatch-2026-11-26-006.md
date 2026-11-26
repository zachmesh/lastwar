---
unit: trucks-dispatch-2026-11-26-006
regular: trucks
activity: truck-plunder
segment: 1
priority: 1
created_at: 2026-11-26T13:26:14Z
expires_at: 2026-11-27T02:00:00Z
planned_for:
not_before: 2026-11-26T13:35:00Z
window: trade cycle i, the 13:33z dot, settle and up to two plunders (coordinator 13:27z)
est_minutes: 15
serves: PL-18
chain_id: dispatch-2026-11-26
chain_seq: 6
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-26T13:41:38Z
lease_until: 2026-11-26T14:01:38Z
result:
  status: done
  started_at: 2026-11-26T13:41:38Z
  finished_at: 2026-11-26T13:52:42Z
  duration_seconds: 664
  executor: operator
  summary: Cycle I on the 13:43Z dot: count 5/5 (no dispatch); two plunders by the final rule (gold UR guard 14.0M: iron 931.5K, bread 931.5K, coin 587.5K and items; purple SSR guard 22.6M: steel 761.5K, bread 761.5K, coin 486.2K), plunder count 2/4 to 4/4; two earlier cards failed the 30-minute check; the Hospital free room 1,531 before and after (no casualties); the returned UR truck settled (iron 3.8M, food 3.8M, coin 2.4M, 500-badge x6); stocks food 35.2M to 40.7M, iron 631.8M to 637.3M, coin 4.0M to 7.6M; tram bare after; drags 0. state_change: yes
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/truck-plunder/1341-queue-run.md and 1341-queue-run.csv; run 20261126T134342Z-918cf4
  state_change: yes
  follow_up: slot 1 and slot 2 empty (5/5 today: no dispatch); the teal truck in slot 3 is out; plunder count 4/4
  stats:
    target: enter on the dot, plunder by the final rule (at most 2), settle every returned truck
    achieved: two plunders; one truck settled
    resources_gained: iron 5.5M, food 5.5M, coin 3.6M
    points: 0
    costs: none spent; model 0.86113 USD
    verified: yes
    run_id: 20261126T134342Z-918cf4
    run_steps: 65
    actions_done: 32
    actions_refused: 0
    cost_usd: 0.86113
    device_takeovers: 0
    claims: 3
    plunders: 2
    plunder_count_after: 4
    trade_count: 5
    hospital_room_before: 1531
    hospital_room_after: 1531
    tram_badge: red dot
    drags_tried: 0
    rules_used: 1,2
  stats_missing: []
  stats_warnings: []
---

# trucks

Serves: PL-18

## Brief (definition pointer, from the roster)

This unit is the regular `trucks`: Trucks - settle returned trucks via Truck Details, claim trade Reward Recovery, dispatch to fill (duel UR days Mega + UR only, other days SR/SSR/UR), plunder to the cap by the UR shard rule. Its definition is the activity folder `_activities_/truck-plunder/` (the folder is named for the activity, not the regular id): read its `rule-digest.md` first, then its `INDEX.md`. If the digest does not cover a step, stop with 'blocked by prerequisite' and say which step; never improvise.

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (routes in `_records_/2026-11-22/queue-planning/2700-routes.csv`). Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.

## Brief (planner, TRADE CYCLE I, the 13:33Z dot, Coordinator 13:27Z)

serves: PL-18

DISPATCH ONLY WHEN NAMED, on a DOT (the 09:07Z truck returns about 13:33:27Z, a red dot). A BARE icon after ONE WORLD then BASE is a verified nothing-to-do: no tap on it.
Do the TRADE CYCLE as `_records_/2026-11-22/queue-planning/3110-trade-cycle.md` and RULES `_records_/2026-11-22/queue-planning/2544-trade-day-rules.md`: follow both. The day's dispatch count is 5 of 5: NO dispatch. ORDER: (0) the Hospital free room: reuse a read made within the last hour, else read it BEFORE the tram tap; NEVER leave the trade screen between the entry and the Others' tab. (1) Enter on the dot; write the icon state, both tab badges, the count x of 5 and each slot's state. (2) Read the Others' tab FIRST: PLUNDER by Steer A's final rule in sheet 2544 (guard under Squad 1 as read, arrival MORE THAN 30 MINUTES, not an alliance mate, free room at least 1,000, UR then SSR then SR, no stack filter; record each card's stack and frame colour): 2 of 4 are done today, so AT MOST 2 MORE; stop after a fight that wounds more than 50; none after 22:00Z. (3) Then the Your Truck tab: settle every returned truck (each truck's iron, food and coin).
Write the icon state and its UTC time at EVERY read. FRONT: if `lsappinfo front` is not LastWar: record, run the standing front script, record; still not: stop, release, tell the Coordinator.
CLOSE by `_records_/2026-11-22/queue-planning/3170-closing-rule-done-and-partial.md`: DONE for a taken action or a verified nothing-to-do (`--state-change no`, a `state_read:` line); else PARTIAL.
May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Cost cap, stated: 1.50 USD.
