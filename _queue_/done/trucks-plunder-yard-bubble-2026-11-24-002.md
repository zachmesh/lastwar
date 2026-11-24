---
unit: trucks-plunder-yard-bubble-2026-11-24-002
regular: trucks
activity: truck-plunder
segment: 2
priority: 1
created_at: 2026-11-24T07:30:06Z
expires_at: 2026-11-24T09:45:00Z
planned_for:
not_before: 2026-11-24T08:50:00Z
window: one tap on one truck glyph bubble over the truck and container yard read only option a waiting for steer a
est_minutes: 8
serves: PL-18
chain_id: plunder-yard-bubble-2026-11-24
chain_seq: 2
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-24T08:51:39Z
lease_until: 2026-11-24T09:11:39Z
result:
  status: partial
  started_at: 2026-11-24T08:51:39Z
  finished_at: 2026-11-24T08:54:15Z
  duration_seconds: 156
  executor: operator
  summary: Path found: tram icon (107,580) then the yard bubble (165,408) opens INTERCITY TRADE - TRUCK, the own truck dispatch dialog (Trade Count 0/5, a free dice, arrives in 04:00:46, Let's Go and Mega Mode, no tabs, no price); the dialog has no X or back arrow and was left open, nothing pressed; no alert; drags 0
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/truck-plunder/0851-queue-run.md and 0851-queue-run.csv; run 20261124T085140Z-4e7e94
  follow_up: close the dialog by a tap outside it if the coordinator allows; the plunder list (Others' Trucks) needs another entry; the own dispatch uses Let's Go (not authorized here)
  stats:
    target: find the Intercity Trade entry by one tram tap and one yard bubble tap, read only
    achieved: entry found; dialog left open (no close control)
    resources_gained: none
    points: 0
    costs: none spent; model 0.10769 USD
    verified: yes
    run_id: 20261124T085140Z-4e7e94
    run_steps: 8
    actions_done: 12
    actions_refused: 0
    cost_usd: 0.10769
    device_takeovers: 0
    blocker_category: f missing precondition (the Intercity Trade - Truck dialog has no X or back arrow and was left open)
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

## Brief (planner, ONE TAP on ONE white truck-glyph bubble over the TRUCK AND CONTAINER YARD, read only, OPTION A)

serves: PL-18

Steer A said YES to option A (two taps) at 07:31Z; the supervised read `scout-midday-bridge-supervised-read-2026-11-24-001` after the bridge restart comes BEFORE this one.

Navigation: WORLD then BASE; tap the TRAM ICON (107,580) ONCE (verified by its label: the Alliance Train shortcut, safe at 07:09Z) to pan to the station camera; a frame; then ONE tap on ONE white truck-glyph bubble over the TRUCK AND CONTAINER YARD (about (165,408) or (120,438) on that frame; verify the glyph; NOT the station's bubbles, NOT the green world-map marker). A frame before and after each tap and `lsappinfo front` in the SAME TURN; 8 steps.

OPEN AND READ ONLY: the screen's TITLE, TABS, BUTTONS and PRICES. FORBIDDEN: Plunder, Battle, Quick Plunder, Send, Dispatch, Start Trade, REFRESH, Speed Up, any price or diamond button, any purchase, any 'Free' button not read first. Close with X or back. Own trade truck panel: read, never use, write what it offers. Intercity Trade or a plunder list: record the PATH (point, title, tab) and STOP.
Any other app, alert or dialog: STOP, answer nothing, name `lsappinfo front`, tell the Coordinator. TIPS 'Enable notifications': Cancel only, by its text. May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Cost cap, stated: 0.40 USD.
