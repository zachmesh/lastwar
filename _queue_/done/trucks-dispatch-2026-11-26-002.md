---
unit: trucks-dispatch-2026-11-26-002
regular: trucks
activity: truck-plunder
segment: 2
priority: 1
created_at: 2026-11-25T22:17:43Z
expires_at: 2026-11-27T02:00:00Z
planned_for:
not_before: 2026-11-26T07:25:00Z
window: trade cycle f settle cycle e returns and dispatch the last two
est_minutes: 15
serves: PL-18
chain_id: dispatch-2026-11-26
chain_seq: 2
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-26T09:07:47Z
lease_until: 2026-11-26T09:27:47Z
result:
  status: partial
  started_at: 2026-11-26T09:07:47Z
  finished_at: 2026-11-26T09:15:47Z
  duration_seconds: 480
  executor: operator
  summary: Cycle F: entry by a red-dot tram icon (09:07:53.5Z; tab badges Others' 4, Your Truck 1; count 3/5); settled the UR truck of slot 2 (iron 3.8M, food 3.8M, coin 2.4M, blue tablet x1, 500-badge x6, orange scroll x1, puzzle piece x1, gem item 100 x1, gold bar x1); dispatched one truck (R, free dice SR, one more contract refresh 255 to 254 gave UR: no downgrade; Let's Go 09:12:34.6Z; back about 13:33:27Z; count 4/5); Hospital free room 1,531; plunders not done: after the dispatch the tram icon is bare and the trade screen cannot be re-entered; sequencing error disclosed; drags 0. state_change: yes
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/truck-plunder/0907-queue-run.md and 0907-queue-run.csv; run 20261126T090748Z-770d8a
  state_change: yes
  follow_up: re-enter on the red dot when slot 1 or 3 returns or a slot empties: then dispatch the 5th truck and plunder up to four (Hospital room 1,531)
  stats:
    target: settle, dispatch up to the day's remaining count, plunder up to four
    achieved: one truck settled, one dispatched (4/5), no plunder
    resources_gained: iron 3.8M, food 3.8M, coin 2.4M (the settled truck)
    points: 0
    costs: none spent; model 0.465463 USD
    verified: yes
    run_id: 20261126T090748Z-770d8a
    run_steps: 37
    actions_done: 16
    actions_refused: 0
    cost_usd: 0.465463
    device_takeovers: 0
    claims: 1
    dispatches: 1
    trade_count: 4/5
    downgrade_test: SR to UR, no downgrade
    hospital_free_room: 1531
    blocker_category: entry: bare tram icon after dispatch, plunders not reached
    tram_badge: red dot at entry, bare after
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

## Brief (planner, TRADE CYCLE F, the 11-26 day, Steer A 22:15Z)

serves: PL-18

DISPATCH ONLY WHEN NAMED, after cycle E's trucks are back (about 07:25Z if E ran at 02:15Z): read each truck's timer on the Your Truck tab; a timer over 20 minutes: leave it and write it.
Do the TRADE CYCLE as `_records_/2026-11-22/queue-planning/3110-trade-cycle.md` (steps 0 to 4, Hospital first) and RULES `_records_/2026-11-22/queue-planning/2544-trade-day-rules.md`: follow both. FIRST write the tram badge state AND ITS COUNT, and BOTH tab badges. SETTLE every returned truck (claim Reward Recovery), then DISPATCH the last TWO into EMPTY slots (count to 5/5) before 22:00Z on 11-26; the downgrade test only if E did not run it; PLUNDER only if under 4 of 4 and before 22:00Z: per the sheet. Avoid 08:00Z-08:25Z and 09:58Z-10:05Z.
BADGE FIRST: a BARE icon is the Alliance Train shortcut by glyph (a tap only pans the camera: 11-04, 11-24, 11-26 at 04:45Z and 08:48Z): no tap on it. NO badge at the first read: WORLD then BASE (one tap each on the standing corner button, no icon), read ONCE: lit: enter; still bare or dark: close a verified nothing-to-do ('badge absent: no tap') with a `state_read:` line. Write the icon state (absent, bare or badge N) and its UTC time at EVERY read. Up to TEN runs of 12 steps. FRONT: if `lsappinfo front` is not LastWar: record, run the standing front script, record; still not: stop, release, tell the Coordinator.
CLOSE by `_records_/2026-11-22/queue-planning/3170-closing-rule-done-and-partial.md`: DONE for a taken action or a verified nothing-to-do (`--state-change no`, a `state_read:` line); else PARTIAL.
May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Cost cap, stated: 1.50 USD.
