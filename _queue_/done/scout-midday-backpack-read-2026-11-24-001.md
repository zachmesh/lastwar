---
unit: scout-midday-backpack-read-2026-11-24-001
regular: scout-midday
activity: perception-scout
segment: 2
priority: 2
created_at: 2026-11-24T15:35:53Z
expires_at: 2026-11-24T18:40:00Z
planned_for:
not_before: 2026-11-24T15:47:00Z
window: read only backpack read names and quantities of the items received held for steer a
est_minutes: 8
serves: snapshot
chain_id: backpack-read-2026-11-24
chain_seq: 1
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-24T16:01:03Z
lease_until: 2026-11-24T16:21:03Z
result:
  status: partial
  started_at: 2026-11-24T16:01:03Z
  finished_at: 2026-11-24T16:06:40Z
  duration_seconds: 337
  executor: operator
  summary: Backpack read-only: six tabs, rows 1 to 3 of five tabs and the Gift tab in full (general speed-ups 5m x32,468 and 1m x24,902, construction 5m x24,390 and 1m x19,440, red gem items 5.0K x16, Drone Parts x231, Skill Medal 17.8K); two composed pans from the margin moved the grids 0 px so the 4th rows stay cut off; nothing used; tram badge none
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/perception-scout/1601-queue-run.md and 1601-queue-run.csv; run 20261124T160103Z-5c955d
  follow_up: the 4th rows of five tabs need another scroll method (a drag from a tile gap or the wheel are untried here); two of the four allowed pans remain
  stats:
    target: read every stack's name and quantity on every tab
    achieved: rows 1 to 3 of five tabs and the Gift tab; the 4th rows unread
    resources_gained: none
    points: 0
    costs: none spent; model 0.455782 USD
    verified: yes
    run_id: 20261124T160103Z-5c955d
    run_steps: 36
    actions_done: 51
    actions_refused: 0
    cost_usd: 0.455782
    device_takeovers: 0
    tabs_read: 6
    pans: 2
    blocker_category: f missing precondition (the grid did not move under the margin pan: the 4th rows stay cut off)
    tram_badge: none
    drags_tried: 2
    rules_used: 1,2,3
  stats_missing: []
  stats_warnings: []
---

# scout-midday

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: snapshot

## Brief (definition pointer, from the roster)

This unit is the regular `scout-midday`: Scout - midday perception pass (floor anchor); re-walk the interface for state-dependent availability (trains, phase rotations, market refreshes); full passes also fire on detected state change between anchors. Its definition is the activity folder `_activities_/perception-scout/` (the folder is named for the activity, not the regular id): read its `rule-digest.md` first, then its `INDEX.md`. The map of every regular to its activity folder is `_records_/2026-11-22/queue-planning/2760-regular-to-activity-map.csv`. If the digest does not cover a step, stop with 'blocked by prerequisite' and say which step; never improvise.

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (routes in `_records_/2026-11-22/queue-planning/2700-routes.csv`). Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.

## Brief (planner, THE BACKPACK READ: names and quantities, NOTHING opened or used, approved by Steer A 15:46Z)

serves: snapshot

HAZARD (route row `backpack`): the Resources tab opens with the 5,000 Diamonds x16 tile SELECTED and a LIVE Use. Tap ONLY the tabs and the back arrow: NOTHING is opened, used, sold, merged, split or selected; no Use, Open, Sell, Merge, Quantity slider; NEVER a tile tap.
(1) Bottom bar Inventory. EACH tab (Resources, Speed-up, Chests, Others) a frame; write each stack's NAME and QUANTITY as the grid shows: the chests (Mystery Supply Box; UR, SSR, SR choice; metal-crate, gold, pass crates, Lv.4), the speed-ups BY KIND (tech, construction, general) and minutes, the red gem items (the trucks' 50, 100, 200 tiles), the oil items (5 x 6.0K), Drone Parts, gear. Name not readable from the grid: 'unreadable' and the tag only. Crop counts from the SAVED frame at 6x, no zoom action.
(2) A page needing a pan is a NEW page: the first pan names the blank right margin and what is cut off, read in a frame. ONE composed pan per screen in ONE MESSAGE: mouse_move to the start; left_mouse_down; wait 1 (second); ONE move of about 175 px; wait 1 (second); left_mouse_up; a screenshot after. At most FOUR pans in all and one correction pan; if it moves nothing or flings: stop.
(3) Any price, diamond line, dialog or other app: STOP, touch nothing. May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Cost cap, stated: 0.60 USD.
