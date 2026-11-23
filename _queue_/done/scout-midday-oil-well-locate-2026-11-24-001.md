---
unit: scout-midday-oil-well-locate-2026-11-24-001
regular: scout-midday
activity: perception-scout
segment: 2
priority: 2
created_at: 2026-11-23T15:39:43Z
expires_at: 2026-11-23T12:00:00Z
planned_for:
not_before: 2026-11-24T02:05:00Z
window: oil well locate read tag position storage and level preview read only
est_minutes: 12
serves: PL-17
chain_id: oil-well-locate-2026-11-24
chain_seq: 1
attempts: 0
max_attempts: 3
claimed_by:
claimed_at:
lease_until:
result:
  status: expired
  started_at:
  finished_at: 2026-11-23T16:00:45Z
  duration_seconds: 
  executor:
  summary: retired by the planner: the Oil Well was found at Lv.20 by the operator (record 1553-oil-well-found), so the locate read is moot
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

Serves: PL-17

## Brief (definition pointer, from the roster)

This unit is the regular `scout-midday`: Scout - midday perception pass (floor anchor); re-walk the interface for state-dependent availability (trains, phase rotations, market refreshes); full passes also fire on detected state change between anchors. Its definition is the activity folder `_activities_/perception-scout/` (the folder is named for the activity, not the regular id): read its `rule-digest.md` first, then its `INDEX.md`. The map of every regular to its activity folder is `_records_/2026-11-22/queue-planning/2760-regular-to-activity-map.csv`. If the digest does not cover a step, stop with 'blocked by prerequisite' and say which step; never improvise.

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (routes in `_records_/2026-11-22/queue-planning/2700-routes.csv`). Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.

## Brief (planner, OIL WELL LOCATE read, fallback for today's assignment, PL-17)

serves: PL-17

The first collection (`_queue_/done/harvest-oil-well-2026-11-23-001.md`) used the top-bar barrel panel (1.2K an hour) but never found the Oil Well BUILDING. If a 2026-11-23 record already gives its tag, position and preview, read only what is missing.

1. Fresh base frame. Look for an oil derrick or pump, or a bubble with an oil barrel. Pan as in the Drill Ground route (drag (540,700) to (290,450); fresh is the panned frame plus (250,250)), at most 8 pans; tap ONE building per fresh frame and read its tag text. Not found: stop 'blocked by route' and write the frames covered.
2. Found: write the tag text (name, level), position, storage (stored oil and capacity or time to full), output per hour, and the Upgrade preview Lv.N to N+1: coin, iron, food, oil, the FINISH NOW clock as the effective time, original time, power, prerequisites.
3. Press NOTHING that upgrades, collects or speeds up. Do NOT press the OIL panel's Details button: its effect is unrecorded, so it needs Steer A's approval first. Any banner, Go, Buy, link, web or share button may open another app: if one opens, STOP and touch nothing.

Up to two runs, 10 steps each. Tag text beside every number; none means [G]. Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (safe tap: bare spot (310,660)). A TIPS dialog about another device: STOP, report.
Cost cap, stated: 0.60 USD per run (the harness stops near 0.36 of it).
