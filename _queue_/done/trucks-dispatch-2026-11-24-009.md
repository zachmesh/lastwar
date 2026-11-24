---
unit: trucks-dispatch-2026-11-24-009
regular: trucks
activity: truck-plunder
segment: 2
priority: 1
created_at: 2026-11-24T15:52:58Z
expires_at: 2026-11-24T15:59:27Z
planned_for:
not_before: 2026-11-24T15:52:00Z
window: the rest of cycle b slot 4 text and the history screen after the scan while the badge is lit
est_minutes: 15
serves: PL-18
chain_id: dispatch-2026-11-24
chain_seq: 9
attempts: 0
max_attempts: 3
claimed_by:
claimed_at:
lease_until:
result:
  status: expired
  started_at:
  finished_at: 2026-11-24T15:59:27Z
  duration_seconds: 
  executor:
  summary: retired by the planner: Steer A 15:57Z ruled B2 (18:05Z) carries the settle, the two fights, the slot 4 text and the History screen in one visit; B3 settles the UR; the scans and -009 are folded into B2
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

## Brief (planner, TRADE CYCLE B, THE REST: the slot 4 text and the History screen, Steer A 14:42Z)

serves: PL-18

The badge lit at 15:48Z (a red 1) after the macOS alert; the scan `trucks-plunder-scan-b-2026-11-24-001` settles the SR and fights once. THIS UNIT runs AFTER the scan, only if the tram badge is still lit (or on any later lit badge before 17:15Z): FIRST write the tram badge state AND ITS COUNT with the UTC time. NO badge: close 'badge absent: no tap'. Badge lit: ONE tap on the tram icon opens Intercity Trade; then:
(1) Read the LOCKED slot 4's unlock text (one tap on the lock only if it shows plain text; never an Unlock, Buy or price).
(2) The History screen: do `_records_/2026-11-22/queue-planning/3150-history-screen-read.md` exactly (the Dispatch tab read, then ONE composed pan for the 'Defense Failed' row on a NEW page: read only; NEVER tap inside a history row: RED LINE, no PvP; no second try).
(3) Read the HUD diamonds, iron, food and coin before and after; write the Your Truck tab's unsettled trucks with any deadline or timer.
(4) Close with the back arrows. NO settle, NO dispatch, NO fight here: the scans do them. Up to TEN runs of 12 steps. May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Cost cap, stated: 1.50 USD.
