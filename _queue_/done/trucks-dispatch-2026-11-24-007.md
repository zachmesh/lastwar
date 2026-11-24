---
unit: trucks-dispatch-2026-11-24-007
regular: trucks
activity: truck-plunder
segment: 2
priority: 1
created_at: 2026-11-24T15:07:13Z
expires_at: 2026-11-24T17:15:00Z
planned_for:
not_before: 2026-11-24T15:07:00Z
window: cycle b try two settle the sr read slot 4 and the history screen after the badge was absent at 15:04:46Z
est_minutes: 15
serves: PL-18
chain_id: dispatch-2026-11-24
chain_seq: 7
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-24T15:16:02Z
lease_until: 2026-11-24T15:36:02Z
result:
  status: partial
  started_at: 2026-11-24T15:16:02Z
  finished_at: 2026-11-24T15:17:47Z
  duration_seconds: 105
  executor: operator
  summary: Closed 'badge absent: no tap' for the second time: the tram icon showed no badge at 15:17:05Z although the SR was due back about 14:59:21Z (a crop of the saved frame confirms); not tapped; Hospital free room 1,329; HUD unchanged (diamonds 11,173, iron 780.1M, food 146.5M, coin 33.4M); settle, slot 4 text and the History read not reached; drags 0
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/truck-plunder/1516-queue-run.md and 1516-queue-run.csv; run 20261124T151603Z-1b693d
  follow_up: the SR may have a longer travel (3:36 to 4:53 varied); try 3 after about 16:00Z or a tram visit by Steer A's word
  stats:
    target: settle the SR, read slot 4's text, the History Dispatch tab and the Defense Failed pan
    achieved: badge absent: nothing reached
    resources_gained: none
    points: 0
    costs: none spent; model 0.113828 USD
    verified: yes
    run_id: 20261124T151603Z-1b693d
    run_steps: 9
    actions_done: 8
    actions_refused: 0
    cost_usd: 0.113828
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

## Brief (planner, TRADE CYCLE B, try 2: settle, dispatch and plunder on one badge, Steer A 10:16Z)

serves: PL-18

Do the TRADE CYCLE exactly as `_records_/2026-11-22/queue-planning/3110-trade-cycle.md` says: read it first; steps 0 to 4. THIS CYCLE is try 2 of at most 3 (try 1 at 15:04:46Z found NO badge, record 1503): write the tram badge state FIRST. The SR of the first dispatch was due about 14:59:21Z (its travel varies 3:36 to 4:53). If a badge shows: SETTLE it, and read the HUD diamonds, iron, food and coin BEFORE and AFTER the settle (as shown); no dispatch (5/5); On the Your Truck tab READ whether an unsettled returned truck shows a deadline or timer, and write it. read the LOCKED slot 4's unlock text (a tap on the lock only if plain text; never Unlock, Buy or price). THEN THE HISTORY SCREEN (Steer A 14:42Z), before the back arrow and the scans: do `_records_/2026-11-22/queue-planning/3150-history-screen-read.md` exactly (Dispatch tab, then ONE composed pan for the 'Defense Failed' row: read only; NEVER tap inside a history row: RED LINE, no PvP). NO plunder in this unit: the separate scans `trucks-plunder-scan-b-2026-11-24-001` to `-004` follow it; the SR's slot stays empty at 5/5 so the badge stays lit.
NO badge: close 'badge absent: no tap' (3 tries at most). Up to TEN runs of 12 steps. May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Cost cap, stated: 1.50 USD.
