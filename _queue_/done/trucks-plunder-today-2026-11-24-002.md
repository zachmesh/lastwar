---
unit: trucks-plunder-today-2026-11-24-002
regular: trucks
activity: truck-plunder
segment: 2
priority: 1
created_at: 2026-11-24T07:01:37Z
expires_at: 2026-11-24T07:11:47Z
planned_for:
not_before: 2026-11-24T08:40:00Z
window: plunder scan 2 of 4 today count 0 of 4 hospital first
est_minutes: 6
serves: PL-18
chain_id: plunder-today-2026-11-24
chain_seq: 2
attempts: 0
max_attempts: 3
claimed_by:
claimed_at:
lease_until:
result:
  status: expired
  started_at:
  finished_at: 2026-11-24T07:11:47Z
  duration_seconds: 
  executor:
  summary: retired by the planner: the supervised first tap at 07:09:16Z showed that (107,580) is the Alliance Train shortcut, not the Intercity Trade entry; every scan starts from it; restaged after trucks-plunder-locate-2026-11-24-001 finds the entry
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

## Brief (planner, ONE plunder scan 2 of 4 today, Steer A lifted the icon hold)

serves: PL-18

OD-20261123-20: TRADE TRUCKS ONLY; no other PvP. Look ONCE, never loop. HOSPITAL FIRST: read the Hospital Lv.25 figures behind its tag's orange middle button (free room = 7,999 minus wounded minus 'Completed'; 1,329 at 02:07Z): STOP the whole session under 1,000, 'blocked by capacity: hospital room'. Then the Plunder Count: STOP at 4 of 4. The first tap unit `trucks-plunder-first-tap-2026-11-24-001` must have written 'icon safe': if it did not, stop 'blocked by route'.

1. Intercity Trade, Others' Trucks: read the list once, no refresh unless its button reads Free. If the trade icon is absent, close 'blocked by route: trade icon absent'.
2. TARGET: a gold (UR) or purple (SSR) truck, a UR 500-badge stack in EITHER half, guard under Squad 1 (25.61M), arrival over 30 minutes away; PREFER the card with the MOST shards.
3. Quick Plunder once, Battle once: ONE fight per unit. Never Collect, Heal or Speed Up.
4. Per fight record: shards won; per item the share of the cargo taken; the card's shard count and stack slots; troops wounded; the count; Total Power. Two fights in a row each wounding over 100: write a stop.

May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing. Safe tap: the bare spot (310,660), not (400,640) after a camera shift (WORLD then BASE first). A TIPS dialog about another device: STOP, report.
Cost cap, stated: 0.40 USD.
