---
unit: trucks-plunder-first-tap-2026-11-24-001
regular: trucks
activity: truck-plunder
segment: 2
priority: 1
created_at: 2026-11-24T07:01:35Z
expires_at: 2026-11-24T07:30:00Z
planned_for:
not_before: 2026-11-24T07:08:00Z
window: supervised first tap on the trade icon after the hold was lifted by steer a
est_minutes: 5
serves: PL-18
chain_id: plunder-first-tap-2026-11-24
chain_seq: 1
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-24T07:08:48Z
lease_until: 2026-11-24T07:28:48Z
result:
  status: partial
  started_at: 2026-11-24T07:08:48Z
  finished_at: 2026-11-24T07:10:32Z
  duration_seconds: 104
  executor: operator
  summary: One supervised tap on the left-column tram icon (107,580) at 07:09:16.165Z: no alert, LastWar frontmost throughout; it did not open Intercity Trade but panned to the Alliance Train station: it is the Alliance Train shortcut and the Intercity Trade entry is not on the base
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/truck-plunder/0708-queue-run.md and 0708-queue-run.csv; run 20261124T070848Z-b71373
  follow_up: the plunder scans need the Intercity Trade entry: find it (a left-column icon that appears at set times, or a building) before any scan; the 02:34Z alert was not caused by this icon
  stats:
    target: one supervised tap on the trade icon, close whatever opens
    achieved: tapped once, no alert, no Trade screen
    resources_gained: none
    points: 0
    costs: none spent; model 0.076043 USD
    verified: yes
    run_id: 20261124T070848Z-b71373
    run_steps: 6
    actions_done: 9
    actions_refused: 0
    cost_usd: 0.076043
    device_takeovers: 0
    blocker_category: f missing precondition (the Intercity Trade screen did not open: the (107,580) icon is the Alliance Train shortcut)
    drags_tried: 0
    rules_used: 6
  stats_missing: []
  stats_warnings: []
---

# trucks

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: PL-18

## Brief (definition pointer, from the roster)

This unit is the regular `trucks`: Trucks - settle returned trucks via Truck Details, claim trade Reward Recovery, dispatch to fill (duel UR days Mega + UR only, other days SR/SSR/UR), plunder to the cap by the UR shard rule. Its definition is the activity folder `_activities_/truck-plunder/` (the folder is named for the activity, not the regular id): read its `rule-digest.md` first, then its `INDEX.md`. The map of every regular to its activity folder is `_records_/2026-11-22/queue-planning/2760-regular-to-activity-map.csv`. If the digest does not cover a step, stop with 'blocked by prerequisite' and say which step; never improvise.

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (routes in `_records_/2026-11-22/queue-planning/2700-routes.csv`). Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.

## Brief (planner, THE FIRST TAP: this run's ONLY job is one tap on the trade icon, Steer A's supervised test)

serves: PL-18

Steer A lifted the trade icon hold with a supervised first tap. The trade icon (107,580) was present at 02:30:41Z. Do exactly this, nothing else:
1. WORLD then BASE; take a frame of the base with the icon; tap the TRADE ICON (107,580) ONCE; take a frame immediately after; run `lsappinfo front` IN THE SAME TURN as the tap.
2. If LastWar stays in front and the Intercity Trade screen opens: close it with its X and write 'icon safe' with both frames' times.
3. IF A macOS ALERT OR ANY OTHER APP COMES TO THE FRONT: STOP; press nothing, answer nothing; run the standing pre-start `killall -9 UserNotificationCenter NotificationCenter` (it dismisses WITHOUT answering); record the time and the app's name from `lsappinfo front`; tell the Coordinator: the hold returns until Steer A decides. Do not tap again.
Finish before 07:35Z (the depot claim). No plunder, no refresh, no other tap in this run. May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Safe tap: the bare spot (310,660), not (400,640) after a camera shift (WORLD then BASE first). A TIPS dialog about another device: STOP, report.
Cost cap, stated: 0.30 USD.
