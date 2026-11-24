---
unit: trucks-dispatch-2026-11-24-010
regular: trucks
activity: truck-plunder
segment: 2
priority: 1
created_at: 2026-11-24T15:59:13Z
expires_at: 2026-11-24T20:30:00Z
planned_for:
not_before: 2026-11-24T18:50:00Z
window: cycle b3 settle only the ur that returns about 18:46:07z
est_minutes: 14
serves: PL-18
chain_id: dispatch-2026-11-24
chain_seq: 10
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-24T18:50:34Z
lease_until: 2026-11-24T19:10:34Z
result:
  status: done
  started_at: 2026-11-24T18:50:34Z
  finished_at: 2026-11-24T18:56:45Z
  duration_seconds: 371
  executor: operator
  summary: Cycle B3: the tram icon was absent at 18:50:39.968Z and drawn with a badge 1 at 18:51:02.149Z after WORLD (18:50:46.814Z) then BASE (18:50:54.300Z); Hospital free room 1,329; settled the UR (iron 2.8M, food 2.8M, coin 1.8M against the nominal 3.8M, 3.8M, 2.4M: a plunder at 07:40:21 PT took a gold crate x10, a 500 item x3, an Extra x1, iron 951.8K, food 951.8K, coin 607.5K); the History Dispatch pan moved the list 150 px (oldest row 02:05:46 PT, no 11-12 to 11-22 dispatch visible); the Defense Failed row is that plunder (state 2095, no loot text); HUD iron +2.9M, food +2.8M, coin +1.8M; no fight, no dispatch; drags 1. state_change: yes
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/truck-plunder/1850-queue-run.md and 1850-queue-run.csv; run 20261124T185034Z-21bef9
  state_change: yes
  follow_up: all five dispatches of today are settled; the next dispatch day resets at the server day change; older Dispatch rows lie below the fold
  stats:
    target: settle the UR; read slot 3, its cargo, the History Dispatch tab and the Defense Failed row
    achieved: all done
    resources_gained: iron 2.8M; food 2.8M; coin 1.8M; speed-up tiles
    points: 0
    costs: none spent; model 0.479523 USD
    verified: yes
    run_id: 20261124T185034Z-21bef9
    run_steps: 37
    actions_done: 59
    actions_refused: 0
    cost_usd: 0.479523
    device_takeovers: 0
    claims: 1
    hospital_free_room: 1329
    stale_dot_series: n=2: absent, WORLD, BASE, lit
    tram_badge: 1 then none
    drags_tried: 1
    drags_cancelled: 0
    rules_used: 2,3,4,6,9,10
  stats_missing: []
  stats_warnings: []
---

# trucks

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: PL-18

## Brief (definition pointer, from the roster)

This unit is the regular `trucks`: Trucks - settle returned trucks via Truck Details, claim trade Reward Recovery, dispatch to fill (duel UR days Mega + UR only, other days SR/SSR/UR), plunder to the cap by the UR shard rule. Its definition is the activity folder `_activities_/truck-plunder/` (the folder is named for the activity, not the regular id): read its `rule-digest.md` first, then its `INDEX.md`. The map of every regular to its activity folder is `_records_/2026-11-22/queue-planning/2760-regular-to-activity-map.csv`. If the digest does not cover a step, stop with 'blocked by prerequisite' and say which step; never improvise.

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (routes in `_records_/2026-11-22/queue-planning/2700-routes.csv`). Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.

## Brief (planner, TRADE CYCLE B3: settle the UR, then the History read, Steer A 15:57Z and 18:45Z)

serves: PL-18

The UR of cycle A returns about 18:46:07Z (nominal 3.8M, 3.8M, 2.4M); probably plundered in transit (a Defense Failed about 16:35Z). Opens about 18:50Z. FIRST write the tram badge state AND ITS COUNT with the UTC time. NO badge at the first read: WORLD then BASE (one tap each on the standing corner button, no icon), then read ONCE: lit: enter; still dark: close 'badge absent: no tap'. Write the UTC time of the dark read, WORLD tap, BASE tap and lit read. Badge lit: ONE tap on the tram icon opens Intercity Trade; read the HUD (diamonds, iron, food, coin).
(1) BEFORE the settle tap write slot 3's look (any flame, any red X on a reward slot) and, when Truck Details open, the CARGO LIST: every item and quantity, each reward slot filled or empty. SETTLE the UR by one tap on its slot; read the HUD after; write its return stamp, timer, quality and what it paid against the nominal.
(2) THEN, in the same visit, the History screen by `_records_/2026-11-22/queue-planning/3150-history-screen-read.md` (its Dispatch tab pan: margin read first, ONE composed pan) and the Defense Failed row of about 16:35Z: WHO plundered and WHAT was lost, from visible text; NEVER tap inside a history row.
No dispatch (5/5), no fight. Close with the back arrows. May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Cost cap, stated: 1.20 USD.
