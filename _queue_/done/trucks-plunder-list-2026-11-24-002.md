---
unit: trucks-plunder-list-2026-11-24-002
regular: trucks
activity: truck-plunder
segment: 2
priority: 2
created_at: 2026-11-24T10:13:20Z
expires_at: 2026-11-24T10:18:42Z
planned_for:
not_before: 2026-11-24T14:08:00Z
window: plunder scan 2 of 4 needs a tram badge hospital first
est_minutes: 6
serves: PL-18
chain_id: plunder-list-2026-11-24
chain_seq: 2
attempts: 0
max_attempts: 3
claimed_by:
claimed_at:
lease_until:
result:
  status: expired
  started_at:
  finished_at: 2026-11-24T10:18:43Z
  duration_seconds: 
  executor:
  summary: retired by the planner: Steer A 10:16Z - the plunder rides on the trade cycle (one visit per tram badge: settle, dispatch, plunder); the plunder step is now inside trucks-dispatch units per 3110-trade-cycle.md
  claimed: []
  claimed_count: 0
  evidence: 
  follow_up: none
  stats:
  stats_missing: [target, achieved, resources_gained, costs, verified]
  stats_warnings: []
---

# trucks

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: PL-18

## Brief (definition pointer, from the roster)

This unit is the regular `trucks`: Trucks - settle returned trucks via Truck Details, claim trade Reward Recovery, dispatch to fill (duel UR days Mega + UR only, other days SR/SSR/UR), plunder to the cap by the UR shard rule. Its definition is the activity folder `_activities_/truck-plunder/` (the folder is named for the activity, not the regular id): read its `rule-digest.md` first, then its `INDEX.md`. The map of every regular to its activity folder is `_records_/2026-11-22/queue-planning/2760-regular-to-activity-map.csv`. If the digest does not cover a step, stop with 'blocked by prerequisite' and say which step; never improvise.

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (routes in `_records_/2026-11-22/queue-planning/2700-routes.csv`). Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.

## Brief (planner, ONE plunder scan 2 of 4, Steer A's GO of 10:04Z, count 0/4)

serves: PL-18

TRADE TRUCKS ONLY. HOSPITAL FIRST: read the Hospital Lv.25 figures behind its tag's orange middle button (free room = 7,999 minus wounded minus 'Completed'; 1,329 at 10:00Z): STOP the whole session under 1,000, 'blocked by capacity: hospital room'; STOP after any fight wounding more than 50 troops.
ROUTE (record `_records_/2026-11-22/truck-plunder/1000-queue-run.md`): WORLD then BASE; write the tram icon's (107,580) BADGE state and the UTC time. WITH a badge ONE tap opens INTERCITY TRADE on Others' Trucks (the plunder list: count 0/4, filter 'out trucks from your Warzone' ticked, about 17 rows, buttons History, refresh, Recover). NO badge (it needs a free slot or a returned truck): do not tap; close 'blocked by route: no badge'.
1. Read the count; STOP at 4 of 4. Read the list once; refresh only if its button reads Free.
2. TARGET: a gold (UR) or purple (SSR) truck with a UR 500-badge stack in EITHER half, guard under Squad 1 (25.61M), arrival over 30 minutes; PREFER the most shards; the opened card decides.
3. Quick Plunder once, Battle once: ONE fight per unit. Never Collect, Heal, Recover, History or Speed Up.
4. Record per fight: shards won; share of each item taken; the card's shard count; troops wounded; the count; Total Power. Close with the blue back arrow.
May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Cost cap, stated: 0.40 USD.
