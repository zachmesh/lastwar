---
unit: scout-midday-backpack-row4-2026-11-24-001
regular: scout-midday
activity: perception-scout
segment: 2
priority: 2
created_at: 2026-11-24T16:08:44Z
expires_at: 2026-11-24T16:18:23Z
planned_for:
not_before: 2026-11-24T23:58:00Z
window: backpack row four one wheel scroll at the blank right margin held for steer a
est_minutes: 8
serves: snapshot
chain_id: backpack-row4-2026-11-24
chain_seq: 1
attempts: 0
max_attempts: 3
claimed_by:
claimed_at:
lease_until:
result:
  status: expired
  started_at:
  finished_at: 2026-11-24T16:18:24Z
  duration_seconds: 
  executor:
  summary: retired by the planner: Steer A 16:17Z ruled (A) park the fourth rows; only the names unit (C) runs
  claimed: []
  claimed_count: 0
  evidence: 
  follow_up: none
  stats:
  stats_missing: [target, achieved, resources_gained, costs, verified]
  stats_warnings: []
---

# scout-midday

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: snapshot

## Brief (definition pointer, from the roster)

This unit is the regular `scout-midday`: Scout - midday perception pass (floor anchor); re-walk the interface for state-dependent availability (trains, phase rotations, market refreshes); full passes also fire on detected state change between anchors. Its definition is the activity folder `_activities_/perception-scout/` (the folder is named for the activity, not the regular id): read its `rule-digest.md` first, then its `INDEX.md`. The map of every regular to its activity folder is `_records_/2026-11-22/queue-planning/2760-regular-to-activity-map.csv`. If the digest does not cover a step, stop with 'blocked by prerequisite' and say which step; never improvise.

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (routes in `_records_/2026-11-22/queue-planning/2700-routes.csv`). Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.

## Brief (planner, THE BACKPACK ROW 4: one WHEEL at the blank margin, WAITING FOR STEER A)

serves: snapshot

DO NOT RUN until the Coordinator names this unit after Steer A's yes; else close 'blocked by prerequisite: waiting for Steer A', press nothing.
Record `_records_/2026-11-22/perception-scout/1601-queue-run.md`: two composed pans from the margin (665,600 to 665,425) moved the grids 0 px; the 4th row of Special and Resources (chests, quantities unread) is cut off. HAZARD (route row `backpack`): the Resources tab has a SELECTED Diamonds x16 tile with a LIVE Use: NEVER tap Use, Open, Sell, Merge or any tile; tap only the tabs and the back arrow. 5 steps:
(1) Bottom bar Inventory (it opens on Special): a frame; write row 3's top edge y.
(2) ONE wheel scroll (the scroll action) at the blank right margin x=665, y about 500, a few clicks down: a frame; write row 3's top edge y after and the MOVE in px. If it did not move: STOP, no second try.
(3) If it moved: write row 4's tiles (icon, quantity tag; crop the SAVED frame at 6x; names 'unreadable'). Then the Resources tab: ONE wheel scroll the same way, a frame, row 4's tiles. At most TWO wheel scrolls in all.
(4) Any dialog, price line, diamond line or other app: STOP, touch nothing. May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Cost cap, stated: 0.40 USD.
