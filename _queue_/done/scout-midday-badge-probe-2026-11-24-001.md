---
unit: scout-midday-badge-probe-2026-11-24-001
regular: scout-midday
activity: perception-scout
segment: 2
priority: 2
created_at: 2026-11-24T15:29:52Z
expires_at: 2026-11-24T15:55:16Z
planned_for:
not_before: 2026-11-24T17:00:00Z
window: no tap tram badge probe one before the second truck returns at 18:00:30z
est_minutes: 2
serves: PL-18
chain_id: badge-probe-2026-11-24
chain_seq: 1
attempts: 0
max_attempts: 3
claimed_by:
claimed_at:
lease_until:
result:
  status: expired
  started_at:
  finished_at: 2026-11-24T15:55:17Z
  duration_seconds: 
  executor:
  summary: retired by the planner: the Coach's 15:50Z reading superseded the 17:00Z probe (the SR is being settled, so no lone returned truck would remain); the test moves to a no-tap read about 18:05Z with the game in front
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

## Brief (planner, THE TRAM BADGE PROBE ONE: a no-tap read, the Coach's test of 15:29Z)

serves: PL-18

The SR of the first dispatch was due back about 14:59:21Z; three tries found NO badge (records 1503, 1516, 1525). The second truck returns about 18:00:30Z (cycle A's SR), the UR about 18:46:07Z. Until then a LONE returned SR either lights the badge (the SR is back: count 1) or does not (a lone truck lights nothing). This probe separates the two. TAP NOTHING: no tram tap, no drag, no scroll, no pan. 3 steps:
(1) Take one frame of the base screen. If another screen is in front, close it by its back arrow; open nothing.
(2) CROP the left column from the SAVED frame at 6x (never a zoom action): write the tram icon's badge (present or none) AND ITS COUNT, the pickup badge, the radar dish count, the HUD (diamonds, iron, food, coin) and the UTC time.
(3) Close 'probe: badge N' or 'probe: none': a no-badge read is a COMPLETE, not a partial. Any dialog: touch nothing, take the frame, stop, tell the Coordinator. Verify each HUD icon by its label or glyph before any tap (none is expected). May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Cost cap, stated: 0.20 USD.
