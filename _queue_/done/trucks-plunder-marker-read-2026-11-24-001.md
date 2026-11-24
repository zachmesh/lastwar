---
unit: trucks-plunder-marker-read-2026-11-24-001
regular: trucks
activity: truck-plunder
segment: 2
priority: 2
created_at: 2026-11-24T09:07:54Z
expires_at: 2026-11-24T12:00:00Z
planned_for:
not_before: 2026-11-24T09:30:00Z
window: read only the green truck marker with a countdown on the world map
est_minutes: 8
serves: PL-18
chain_id: plunder-marker-read-2026-11-24
chain_seq: 1
attempts: 2
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-24T09:30:23Z
lease_until: 2026-11-24T09:50:23Z
result:
  status: partial
  started_at: 2026-11-24T09:30:23Z
  finished_at: 2026-11-24T09:31:48Z
  duration_seconds: 85
  executor: operator
  summary: Closed 'marker not verified': the world map shows no green truck marker with a countdown and no other truck marker; nothing tapped; the first run stopped on the leftover Secret Command Post panel; no alert after the 09:26:39Z restore; drags 0
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/truck-plunder/0930-queue-run.md and 0930-queue-run.csv; run 20261124T093023Z-9cafc7
  follow_up: the marker seen at 07:14Z was probably a timed object that is gone; the dispatch unit goes through the yard bubble route; the Oil Well Lv.23 quest line shows a green check
  stats:
    target: read the green truck marker on the world map by one tap
    achieved: marker not found, nothing tapped
    resources_gained: none
    points: 0
    costs: none spent; model 0.133 USD
    verified: yes
    run_id: 20261124T093023Z-9cafc7
    run_steps: 8
    actions_done: 7
    actions_refused: 0
    cost_usd: 0.133
    device_takeovers: 0
    blocker_category: f missing precondition (the green truck marker is not on the world map now: marker not verified)
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

## Brief (planner, READ-ONLY: the green truck marker with a countdown on the world map, Steer A)

serves: PL-18

WORLD; take a frame; verify BY GLYPH the GREEN TRUCK MARKER WITH A COUNTDOWN at about (607,463) on the world map; a frame before and after ONE tap on it and `lsappinfo front` in the same turn. OPEN AND READ ONLY: write the TITLE, TABS, BUTTONS and PRICES. FORBIDDEN: Plunder, Battle, Quick Plunder, Send, Dispatch, Let's Go, Mega Mode, Start Trade, Refresh, Speed Up, any price or diamond, any purchase, any 'Free' not read first. Close with X or back, or ONE tap on a dimmed margin 40+ px outside the dialog over no HUD button. Record the PATH; if it is the Plunder list, stop there. 8 steps; window 09:30Z to 12:00Z, after the train boarding (09:45Z to 10:00Z).
Any other app, alert or dialog: STOP, answer nothing, name `lsappinfo front`, tell the Coordinator. TIPS 'Enable notifications': Cancel only, by its text. Verify each HUD icon by its glyph before the tap. May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Cost cap, stated: 0.40 USD.
