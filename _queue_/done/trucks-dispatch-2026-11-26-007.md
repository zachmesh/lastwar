---
unit: trucks-dispatch-2026-11-26-007
regular: trucks
activity: truck-plunder
segment: 1
priority: 1
created_at: 2026-11-26T13:57:50Z
expires_at: 2026-11-27T02:00:00Z
planned_for:
not_before: 2026-11-26T14:18:00Z
window: trade cycle j, settle only, the 14:16z dot (coin floor)
est_minutes: 8
serves: PL-18
chain_id: dispatch-2026-11-26
chain_seq: 7
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-26T14:41:05Z
lease_until: 2026-11-26T15:01:05Z
result:
  status: done
  started_at: 2026-11-26T14:41:05Z
  finished_at: 2026-11-26T14:43:16Z
  duration_seconds: 131
  executor: operator
  summary: Cycle J on the tram count badge 1 (14:41:13.1Z): count 5/5, no dispatch or plunder; the returned SR truck in slot 3 settled (iron 2.5M, food 2.5M, coin 1.6M, three blue crates of 20, a purple 500-badge item, a green item); coin 7.6M to 9.2M (0.8M under the 10M floor), food 40.7M to 43.3M, iron 637.3M to 639.9M; the tram icon not drawn after the settle; drags 0. state_change: yes
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/truck-plunder/1441-queue-run.md and 1441-queue-run.csv; run 20261126T144106Z-e12089
  state_change: yes
  follow_up: coin 9.2M is 0.8M under the 10M floor; slots 1 to 3 empty (5 of 5 dispatched today)
  stats:
    target: enter on the badge and settle every returned truck
    achieved: one truck settled
    resources_gained: iron 2.5M, food 2.5M, coin 1.6M
    points: 0
    costs: none spent; model 0.158996 USD
    verified: yes
    run_id: 20261126T144106Z-e12089
    run_steps: 12
    actions_done: 6
    actions_refused: 0
    cost_usd: 0.158996
    device_takeovers: 0
    claims: 1
    trade_count: 5
    tram_badge: count 1
    coin_before: 7.6M
    coin_after: 9.2M
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

## Brief (planner, TRADE CYCLE J, settle only, the 14:16Z dot)

serves: PL-18

DISPATCH ONLY WHEN NAMED, on a DOT (the SR truck dispatched 09:50Z returns about 14:16:20Z; the phone's truck is unread). A BARE icon after ONE WORLD then BASE is a verified nothing-to-do: no tap on it.
Do the TRADE CYCLE as `_records_/2026-11-22/queue-planning/3110-trade-cycle.md` and RULES `_records_/2026-11-22/queue-planning/2544-trade-day-rules.md`. Plunders are 4 of 4 today and dispatch is 5 of 5: NO plunder and NO dispatch; do not leave the Your Truck tab for another screen. Enter on the dot; write the icon state, both tab badges, the count x of 5 and each slot's state. Open the Your Truck tab and settle every returned truck (a returned truck settles when its Truck Details open; claim Reward Recovery at the red dot): write each truck's iron, food and coin and the HUD coin before and after (coin was 7.6M at 13:51Z, 2.4M under its 10M floor).
Write the icon state and its UTC time at EVERY read. FRONT: if `lsappinfo front` is not LastWar: record, run the standing front script, record; still not: stop, release, tell the Coordinator.
CLOSE by `_records_/2026-11-22/queue-planning/3170-closing-rule-done-and-partial.md`: DONE for a taken settle or a verified nothing-to-do (`--state-change no`, a `state_read:` line); else PARTIAL.
May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Cost cap, stated: 0.80 USD.
