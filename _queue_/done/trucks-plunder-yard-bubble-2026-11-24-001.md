---
unit: trucks-plunder-yard-bubble-2026-11-24-001
regular: trucks
activity: truck-plunder
segment: 2
priority: 1
created_at: 2026-11-24T07:21:17Z
expires_at: 2026-11-24T07:28:00Z
planned_for:
not_before: 2026-11-24T07:21:30Z
window: one tap on one truck glyph bubble over the truck and container yard read only
est_minutes: 6
serves: PL-18
chain_id: plunder-yard-bubble-2026-11-24
chain_seq: 1
attempts: 0
max_attempts: 3
claimed_by:
claimed_at:
lease_until:
result:
  status: expired
  started_at: 
  finished_at: 2026-11-24T10:01:56Z
  duration_seconds: 
  executor: 
  summary: window passed before execution
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

## Brief (planner, ONE TAP on ONE white truck-glyph bubble over the TRUCK AND CONTAINER YARD, read only, Steer A's permission)

serves: PL-18

The icon at (107,580) is the Alliance Train shortcut. WORLD then BASE; take a FRESH frame; verify the bubble BY ITS GLYPH (a white truck glyph) over the TRUCK AND CONTAINER YARD, NOT the train station's and NOT the green world-map marker (earlier candidates on the station-camera frame: about (165,408) and (120,438)). A frame immediately before the tap and one after, and `lsappinfo front` in the SAME TURN. ONE tap; it must END by 07:33Z; 8 steps.

OPEN AND READ ONLY: write the screen's TITLE, its TABS, its BUTTONS and their PRICES. FORBIDDEN: Plunder, Battle, Quick Plunder, Send, Dispatch, Start Trade, REFRESH (it can cost diamonds), Speed Up, any button showing a price or a diamond, any purchase, any 'Free' button whose effect is not read first. CLOSE with the panel's X or the back arrow.
If it opens the player's OWN trade truck panel (claim or dispatch): read it, never use it, write what it offers. If it opens Intercity Trade or a plunder list: record the PATH (the point, the screen title, the tab) and STOP there.
If ANY other app, alert or dialog appears: STOP, answer nothing, name `lsappinfo front` in the record, tell the Coordinator. The TIPS 'Enable notifications' dialog: Cancel only, identified by its text. May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Cost cap, stated: 0.40 USD.
