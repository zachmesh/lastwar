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
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-25T02:16:40Z
lease_until: 2026-11-25T02:36:40Z
result:
  status: done
  started_at: 2026-11-25T02:16:40Z
  finished_at: 2026-11-25T02:49:52Z
  duration_seconds: 1992
  executor: operator
  summary: Cycle C: the tram lit (badge 3 counted the three empty slots), Hospital free room 1,329 before and after, three trucks dispatched (SSR, SR with the downgrade test SR to SR, UR; count 3/5; Trade Contract 261 to 258), four plunders (UR 23.58M, UR 23.58M, UR 22.59M, SSR 22.50M; all Mission Completed; iron 3.57M, food 3.57M, coin 2.29M, 500-badge shards x12; no troops wounded); the base tram icon bare afterwards, unchanged by WORLD then BASE; a person used the Mac at 02:38:09Z and paused one run (stopped, clean-up run); avatar never tapped; drags 0. state_change: yes
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/truck-plunder/0216-queue-run.md and 0216-queue-run.csv; run 20261125T021640Z-8fba2c
  state_change: yes
  follow_up: the three trucks return about 06:19Z to 06:39Z; the dispatch count 3/5 leaves two for the next window; plunder 4 of 4 done today
  stats:
    target: settle, dispatch three, plunder four on one badge
    achieved: nothing waited; 3 dispatched; 4 plundered
    resources_gained: iron 3.57M; food 3.57M; coin 2.29M; 500-badge shards 12
    points: 0
    costs: none spent; model 1.345400 USD
    verified: yes
    run_id: 20261125T021640Z-8fba2c
    run_steps: 104
    actions_done: 62
    actions_refused: 0
    cost_usd: 1.345400
    device_takeovers: 0
    dispatched: 3
    plundered: 4
    hospital_free_room_before: 1329
    hospital_free_room_after: 1329
    tram_badge_first_read: 3
    trade_contracts_after: 258
    downgrade_test: SR to SR no downgrade
    runs: 10
    drags_tried: 0
    rules_used: 1,2
  stats_missing: []
  stats_warnings: [duration exceeds 15-minute unit cap]
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
