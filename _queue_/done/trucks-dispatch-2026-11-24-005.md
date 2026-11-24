---
unit: trucks-dispatch-2026-11-24-005
regular: trucks
activity: truck-plunder
segment: 2
priority: 1
created_at: 2026-11-24T10:13:23Z
expires_at: 2026-11-24T19:30:00Z
planned_for:
not_before: 2026-11-24T18:05:00Z
window: settle the second wave
est_minutes: 15
serves: PL-18
chain_id: dispatch-2026-11-24
chain_seq: 5
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-24T18:20:26Z
lease_until: 2026-11-24T18:40:26Z
result:
  status: done
  started_at: 2026-11-24T18:20:26Z
  finished_at: 2026-11-24T18:38:38Z
  duration_seconds: 1092
  executor: operator
  summary: Cycle B2: the tram badge was dark at 18:20:31Z and 18:21:07.8Z and lit (1) at 18:21:28.6Z after one WORLD tap and one BASE tap; settled the SR (iron 2.5M, food 2.5M, coin 1.6M, a red gem item 50, two 500 medal items, a blue crate x20); two plunder fights both Mission Completed (UR Lv.29: iron 782.5K, food 782.5K, coin 493.4K, four Extra speed-up stacks; SSR Lv.25: iron 505.5K, food 505.5K, coin 324.0K, 100-badge shard x2, 500-badge shard x3), count 2/4 to 4/4, Hospital free room 1,329 before and after; slot 4's padlock showed no text; History Dispatch and Plunder tabs read, a composed pan moved the list 150 px; tram badge none after the settle; drags 1. state_change: yes
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/truck-plunder/1820-queue-run.md and 1820-queue-run.csv; run 20261124T182101Z-05f4c2
  state_change: yes
  follow_up: the badge probe: WORLD then BASE lights the badge for a returned truck; the UR (14:24:10Z) is back about 18:46:07Z: the next visit; plunder count 4/4
  stats:
    target: settle the SR, two plunder fights, slot 4 text and the History read
    achieved: all done
    resources_gained: iron 3.8M; food 3.8M; coin 2.5M; shards: 100-badge x2, 500-badge x3
    points: 0
    costs: none spent; model 1.358225 USD
    verified: yes
    run_id: 20261124T182101Z-05f4c2
    run_steps: 102
    actions_done: 150
    actions_refused: 0
    cost_usd: 1.358225
    device_takeovers: 0
    claims: 1
    fights: 2
    plunder_count: 4/4
    hospital_free_room_before: 1329
    hospital_free_room_after: 1329
    tram_badge: 1 then none
    drags_tried: 1
    drags_cancelled: 0
    rules_used: 2,3,4,6,9,10
  stats_missing: []
  stats_warnings: [duration exceeds 15-minute unit cap]
---

# trucks

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: PL-18

## Brief (definition pointer, from the roster)

This unit is the regular `trucks`: Trucks - settle returned trucks via Truck Details, claim trade Reward Recovery, dispatch to fill (duel UR days Mega + UR only, other days SR/SSR/UR), plunder to the cap by the UR shard rule. Its definition is the activity folder `_activities_/truck-plunder/` (the folder is named for the activity, not the regular id): read its `rule-digest.md` first, then its `INDEX.md`. The map of every regular to its activity folder is `_records_/2026-11-22/queue-planning/2760-regular-to-activity-map.csv`. If the digest does not cover a step, stop with 'blocked by prerequisite' and say which step; never improvise.

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (routes in `_records_/2026-11-22/queue-planning/2700-routes.csv`). Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.

## Brief (planner, TRADE CYCLE B2: settle the SR first, then two fights, then the History screen, Steer A 15:57Z)

serves: PL-18

Do `_records_/2026-11-22/queue-planning/3110-trade-cycle.md` (steps 0 to 4) and the History screen of `_records_/2026-11-22/queue-planning/3150-history-screen-read.md`. Opens 18:05Z, only if the badge is LIT: FIRST write the badge state AND ITS COUNT with the UTC time. No badge, or the screen not open: close 'badge absent: no tap'; re-reads at 18:20Z and 18:35Z (3 tries at most); B3 settles the UR at about 18:50Z. AT THE 18:20Z RE-READ (the SR derived back 18:00:30Z): first WORLD then BASE (the camera moves; NO tap on any icon), then read the badge ONCE and write whether it lit (the Coach's test: lit = a stale dot refreshed). Badge lit:
(1) Hospital first (free room 1,000 or more; stop after a fight wounding over 50).
(2) SETTLE THE SR of cycle A FIRST (cargo 2.5M, 2.5M, 1.6M): the settle ends the badge; the screen stays open. HUD before and after; the Your Truck tab's return stamp, deadline, quality, cargo.
(3) TWO plunder fights (count 2/4 to 4/4), OD-20 guards: one scan, Quick Plunder once and Battle once; guard under 25.61M; arrival over 30 minutes; UR or SSR with a UR 500-badge stack in either half; no alliance mate.
(4) In the SAME visit the slot 4 text (plain text only) and the History screen by 3150 (read only; never tap inside a row). No dispatch (5/5). Up to TEN runs. May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Cost cap, stated: 1.50 USD.
