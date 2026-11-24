---
unit: trucks-dispatch-2026-11-24-003
regular: trucks
activity: truck-plunder
segment: 2
priority: 1
created_at: 2026-11-24T10:03:40Z
expires_at: 2026-11-24T17:30:00Z
planned_for:
not_before: 2026-11-24T15:03:00Z
window: dispatch cycle 3 settle then dispatch estimate to be re-timed from the real arrival
est_minutes: 15
serves: PL-18
chain_id: dispatch-2026-11-24
chain_seq: 3
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-24T15:03:54Z
lease_until: 2026-11-24T15:23:54Z
result:
  status: partial
  started_at: 2026-11-24T15:03:54Z
  finished_at: 2026-11-24T15:05:30Z
  duration_seconds: 96
  executor: operator
  summary: Closed 'badge absent: no tap': the tram icon showed no badge at 15:04:46Z although the SR was due back at 14:59:21Z; not tapped; Hospital free room 1,329; HUD diamonds 11,173, iron 780.1M, food 146.5M, coin 33.4M; settle, slot 4 text and the History read not reached; drags 0
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/truck-plunder/1503-queue-run.md and 1503-queue-run.csv; run 20261124T150354Z-8c0963
  follow_up: re-dispatch about 15:20Z; the SR badge may need more time or a trade screen visit
  stats:
    target: settle the SR, read slot 4's text, the History Dispatch tab and the Defense Failed pan
    achieved: badge absent: nothing reached
    resources_gained: none
    points: 0
    costs: none spent; model 0.11452 USD
    verified: yes
    run_id: 20261124T150354Z-8c0963
    run_steps: 9
    actions_done: 11
    actions_refused: 0
    cost_usd: 0.11452
    device_takeovers: 0
    blocker_category: f missing precondition (badge absent: no tap)
    tram_badge: none
    hospital_free_room: 1329
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

## Brief (planner, TRADE CYCLE B: settle, dispatch and plunder on one badge, Steer A 10:16Z)

serves: PL-18

Do the TRADE CYCLE exactly as `_records_/2026-11-22/queue-planning/3110-trade-cycle.md` says: read it first; its steps 0 to 4 (the Hospital before the tram tap, then settle, dispatch, plunder, close). THIS CYCLE: about 15:05Z: the SR returned 14:59:21Z: SETTLE it, and read the HUD diamonds, iron, food and coin BEFORE and AFTER the settle (write exactly what the HUD shows; no expected value); no dispatch (5/5); read the LOCKED slot 4's unlock text (one tap on the lock only if it shows plain text; never an Unlock, Buy or price). THEN THE HISTORY SCREEN (Steer A 14:42Z), before the back arrow and the scans: do `_records_/2026-11-22/queue-planning/3150-history-screen-read.md` exactly (the Dispatch tab read, then ONE composed pan for the 'Defense Failed' row on a NEW page: read only; NEVER tap inside a history row: RED LINE, no PvP; no second try). NO plunder in this unit: the separate scans `trucks-plunder-scan-b-2026-11-24-001` to `-004` follow it; the SR's slot stays empty at 5/5 so the badge stays lit.
NO badge: close 'badge absent: no tap' (the Coordinator re-dispatches 15 minutes later, at most 3 tries). Up to TEN runs of 12 steps. May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Cost cap, stated: 1.50 USD.
