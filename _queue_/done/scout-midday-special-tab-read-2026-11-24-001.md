---
unit: scout-midday-special-tab-read-2026-11-24-001
regular: scout-midday
activity: perception-scout
segment: 2
priority: 2
created_at: 2026-11-24T23:08:11Z
expires_at: 2026-11-24T23:58:00Z
planned_for:
not_before: 2026-11-24T23:15:00Z
window: one read only frame of the special tab count tags held for steer a
est_minutes: 5
serves: snapshot
chain_id: special-tab-read-2026-11-24
chain_seq: 1
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-24T23:15:23Z
lease_until: 2026-11-24T23:35:23Z
result:
  status: done
  started_at: 2026-11-24T23:15:23Z
  finished_at: 2026-11-24T23:17:29Z
  duration_seconds: 126
  executor: operator
  summary: Backpack Special tab: the Mystery Supply Box is ABSENT from rows 1 to 5 (its slot gone: stock 0; 376 at 16:46Z); Violet's Loot 58 (350 at 16:01Z); pink crystal 18,442 (4,442); rows 4 and 5 hold new chest stacks (row 5 tags clipped); one composed pan from a gap between tiles inside the grid (274,448 to 274,273) moved the grid about 143 px with no selection; the tram icon not drawn; drags 1. state_change: no. state_read: Special tab: Mystery Supply Box absent from rows 1 to 5; Violet's Loot 58; pink crystal 18,442; rows 4 and 5 new chests | step 6 | 23:16:00Z
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/perception-scout/2315-queue-run.md and 2315-queue-run.csv; run 20261124T231523Z-ba08a2
  state_read: Special tab: Mystery Supply Box absent from rows 1 to 5; Violet's Loot 58; pink crystal 18,442; rows 4 and 5 new chests | step 6 | 23:16:00Z
  state_change: no
  follow_up: rows beyond 5 unread (a second pan would reach them); the gap-start pan works on the Backpack grid
  stats:
    target: read rows 1 to 3 and row 4 of the Special tab by one gap-start pan
    achieved: rows 1 to 5 read; the pan moved 143 px
    resources_gained: none
    points: 0
    costs: none spent; model 0.172576 USD
    verified: yes
    run_id: 20261124T231523Z-ba08a2
    run_steps: 12
    actions_done: 3
    actions_refused: 0
    cost_usd: 0.172576
    device_takeovers: 0
    claims: 0
    mystery_supply_box: absent
    violets_loot: 58
    pink_crystal: 18442
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

This unit is the regular `scout-midday`: Scout - midday perception pass (floor anchor); re-walk the interface for state-dependent availability (trains, phase rotations, market refreshes); full passes also fire on detected state change between anchors. Its definition is the activity folder `_activities_/perception-scout/` (the folder is named for the activity, not the regular id): read its `rule-digest.md` first, then its `INDEX.md`. The map of every regular to its activity folder is `_records_/2026-11-22/queue-planning/2760-regular-to-activity-map.csv`. If the digest does not cover a step, stop with 'blocked by prerequisite' and say which step; never improvise.

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (routes in `_records_/2026-11-22/queue-planning/2700-routes.csv`). Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.

## Brief (planner, THE SPECIAL TAB READ and ONE gap pan to row 4, approved by Steer A 23:09Z)

serves: snapshot

Facts [M] (22:57Z to 23:03Z): Violet's Loot 58 (350 at 16:21Z), the pink crystal 18,442; the purple question-mark chest (Mystery Supply Box, 376 at 16:46Z) was NOT in rows 1 to 3; row 4 is clipped; the margin start moved nothing.
(1) Bottom bar Inventory (opens on Special): a frame with the UTC time of rows 1 to 3 and every count tag (icon described, digits cropped at 6x). NEVER the Resources tab.
(2) Name in a frame the START POINT: a GAP BETWEEN TILES inside the grid (not the margin).
(3) ONE composed pan in ONE MESSAGE: mouse_move to the start; left_mouse_down; wait 1 (second); ONE move of about 175 px; wait 1 (second); left_mouse_up; a frame after. AT MOST TWO pans: the second only if the first selected a tile.
(4) A tile SELECTED: read its panel name, then clear it by the back arrow or the panel's close. NEVER Use, Open, Sell, Merge, Split or the quantity slider.
(5) Write the Mystery Supply Box count (or its absence), Violet's Loot, the pink crystal and any new row 4 stack by icon and count tag.
(6) Any dialog or price line: STOP. `--state-change no`, `state_read:` line. FRONT: if `lsappinfo front` is not LastWar: record, run the standing front script, record; still not: stop, release, tell the Coordinator.
May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Cost cap, stated: 0.30 USD.
