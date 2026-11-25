---
unit: scout-midday-resources-tab-read-2026-11-24-001
regular: scout-midday
activity: perception-scout
segment: 2
priority: 2
created_at: 2026-11-24T23:24:35Z
expires_at: 2026-11-24T23:58:00Z
planned_for:
not_before: 2026-11-24T23:28:00Z
window: read the resources tab counts by a gap pan nothing in the selected panel touched steer a 23:24z
est_minutes: 5
serves: snapshot
chain_id: resources-tab-read-2026-11-24
chain_seq: 1
attempts: 1
max_attempts: 1
claimed_by: operator
claimed_at: 2026-11-24T23:28:12Z
lease_until: 2026-11-24T23:48:12Z
result:
  status: done
  started_at: 2026-11-24T23:28:12Z
  finished_at: 2026-11-24T23:30:13Z
  duration_seconds: 121
  executor: operator
  summary: Backpack Resources tab read (the pre-selected 5,000 Diamonds x16 panel never touched; diamonds 11,173 before and after): choice chests UR 552, SSR 587, SR 1,713 (1,523 on 11-23), the plain Resource Chest 22,179 (20,753 on 11-23), food chests 68, 1,428, 8,227, 67 and a 50.0K bread tile 1,339 (row 5 tags clipped); one gap-start pan (274,448 to 274,273) moved the grid 150 px with no selection; the tram icon not drawn; drags 1. state_change: no. state_read: Resources tab: UR 552, SSR 587, SR 1,713, plain Resource Chest 22,179; the 5,000 Diamonds x16 panel untouched | step 7 | 23:28:57Z
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/perception-scout/2328-queue-run.md and 2328-queue-run.csv; run 20261124T232812Z-eb3274
  state_read: Resources tab: UR 552, SSR 587, SR 1,713, plain Resource Chest 22,179; the 5,000 Diamonds x16 panel untouched | step 7 | 23:28:57Z
  state_change: no
  follow_up: SR 1,713 against the Coach's about 1,840; rows beyond 5 unread
  stats:
    target: read the Resources tab stacks by a gap-start pan
    achieved: rows 1 to 5 read; nothing used
    resources_gained: none
    points: 0
    costs: none spent; model 0.162878 USD
    verified: yes
    run_id: 20261124T232812Z-eb3274
    run_steps: 12
    actions_done: 3
    actions_refused: 0
    cost_usd: 0.162878
    device_takeovers: 0
    claims: 0
    ur_chest: 552
    ssr_chest: 587
    sr_chest: 1713
    resource_chest: 22179
    diamonds: 11173
    tram_badge: icon not drawn
    drags_tried: 1
    drags_cancelled: 0
    rules_used: 1
  stats_missing: []
  stats_warnings: []
---

# scout-midday

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: snapshot

## Brief (definition pointer, from the roster)

This unit is the regular `scout-midday`: Scout - midday perception pass (floor anchor); re-walk the interface for state-dependent availability (trains, phase rotations, market refreshes); full passes also fire on detected state change between anchors. Its definition is the activity folder `_activities_/perception-scout/` (the folder is named for the activity, not the regular id): read its `rule-digest.md` first, then its `INDEX.md`. If the digest does not cover a step, stop with 'blocked by prerequisite' and say which step; never improvise.

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (routes in `_records_/2026-11-22/queue-planning/2700-routes.csv`). Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.

## Brief (planner, THE RESOURCES TAB READ, Steer A 23:24Z)

serves: snapshot

Facts [M]: the Resources tab opens with the '5,000 Diamonds x16' tile pre-selected and a LIVE Use: its panel is NEVER touched. 11-23 08:25Z: UR choice chest 552, SSR 587, SR 1,523, plain Resource Chest 20,753.
(1) Inventory, then the Resources tab only: READ the first frame; touch NOTHING in the panel (no Use, quantity slider or Statistics). Never a tile tap.
(2) Name the START POINT in a frame first: a plain GAP between tiles, at least 60 px from any tile's edge and from the selected tile's panel. ONE composed pan in ONE MESSAGE: mouse_move; left_mouse_down; wait 1 (second); ONE move of about 175 px; wait 1 (second); left_mouse_up; a frame after. AT MOST TWO pans. A tile SELECTED by a pan: read its panel text, clear it by the back arrow or the panel's close: NEVER Use, Open, Sell, Merge or Split.
(3) Read each stack's icon and count tag in rows 1 to 5, the blue-silver choice chests especially (UR, SSR, SR), the plain Resource Chest and the iron, food and coin chests: counts only, names only if a tile is selected; the UTC time of each frame.
(4) Any price line, diamond spend, dialog, app or banner: STOP. `--state-change no`, a `state_read:` line. FRONT: if `lsappinfo front` is not LastWar: record, run the standing front script, record; still not: stop, release, tell the Coordinator.
May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Cost cap, stated: 0.30 USD.
