---
unit: trucks-dispatch-2026-11-26-004
regular: trucks
activity: truck-plunder
segment: 1
priority: 1
created_at: 2026-11-26T09:17:24Z
expires_at: 2026-11-27T02:00:00Z
planned_for:
not_before: 2026-11-26T09:30:00Z
window: trade cycle g, the next dot, others tab first (coordinator 09:18z)
est_minutes: 15
serves: PL-18
chain_id: dispatch-2026-11-26
chain_seq: 4
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-26T09:41:43Z
lease_until: 2026-11-26T10:01:43Z
result:
  status: done
  started_at: 2026-11-26T09:41:43Z
  finished_at: 2026-11-26T09:53:11Z
  duration_seconds: 688
  executor: operator
  summary: Cycle G on a red-dot tram icon (09:41:49.2Z; tab badges Others' 4, Your Truck 1; count 4/5): two plunders (a UR truck with a 23.2M guard: iron 951.8K, food 951.8K, coin 607.5K plus scroll, gold bar and 500-badge x3; an SSR truck with a 17.2M guard: iron 761.5K, food 761.5K, coin 486.2K plus 500-badge x3 and speed-ups) with Hospital unchanged (1,364 of 7,999 wounded, free room 1,531) after the fights; settled the slot 3 SR truck (iron 2.5M, food 2.5M, coin 1.6M, 60 blue chests, a gem item, a 500-badge item); dispatched the 5th truck (SR, back about 14:16:20Z; count 5/5); plunders 3 and 4 had no valid candidate; the 500-badge tiles were purple (UR criterion unverified); drags 0. state_change: yes
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/truck-plunder/0941-queue-run.md and 0941-queue-run.csv; run 20261126T094143Z-005064
  state_change: yes
  follow_up: the next dot when slot 1 or 2 returns; the plunder count 2/4
  stats:
    target: plunder up to four, settle, dispatch up to five
    achieved: 2 plunders, 1 settle, 5th dispatch (5/5)
    resources_gained: plunder loot: iron 1.71M, food 1.71M, coin 1.09M; settled truck: iron 2.5M, food 2.5M, coin 1.6M
    points: 0
    costs: none spent; model 0.894621 USD
    verified: yes
    run_id: 20261126T094143Z-005064
    run_steps: 63
    actions_done: 41
    actions_refused: 0
    cost_usd: 0.894621
    device_takeovers: 0
    claims: 1
    dispatches: 1
    trade_count: 5/5
    plunder_count: 2/4
    hospital_free_room: 1531
    wounded_after: 1364
    tram_badge: red dot at entry, bare after
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

## Brief (planner, TRADE CYCLE G, the next dot: Others' tab first, Coordinator 09:18Z)

serves: PL-18

DISPATCH ONLY WHEN NAMED, on a DOT (a returned truck or an empty slot: the 09:07Z cycle F dispatch is back about 13:33Z; the phone's two trucks are unread). A BARE icon after ONE WORLD then BASE is a verified nothing-to-do (3170 DONE): no tap on it.
Do the TRADE CYCLE as `_records_/2026-11-22/queue-planning/3110-trade-cycle.md` and RULES `_records_/2026-11-22/queue-planning/2544-trade-day-rules.md`: follow both. ORDER (the cycle F lesson): (0) the Hospital free room: reuse a read made within the last hour; else read it BEFORE the tram tap. NEVER leave the trade screen between the entry and the Others' tab. (1) Enter on the dot; write the icon state, both tab badges, the count x of 5 and each slot's state. (2) Read the Others' tab FIRST and PLUNDER up to the day's remaining count of 4 (free room at least 1,000, the casualty guard of 2544) BEFORE any other screen. (3) Then the Your Truck tab: settle every returned truck (write each truck's iron, food and coin), dispatch into each empty slot up to 5 a day, the downgrade test on the first SR, none after 22:00Z.
Write the icon state (absent, bare or badge N) and its UTC time at EVERY read. Up to TEN runs of 12 steps. FRONT: if `lsappinfo front` is not LastWar: record, run the standing front script, record; still not: stop, release, tell the Coordinator.
CLOSE by `_records_/2026-11-22/queue-planning/3170-closing-rule-done-and-partial.md`: DONE for a taken action or a verified nothing-to-do (`--state-change no`, a `state_read:` line); else PARTIAL.
May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Cost cap, stated: 1.50 USD.
