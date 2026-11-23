---
unit: scout-midday-locate-2026-11-23-002
regular: scout-midday
activity: perception-scout
segment: 2
priority: 3
created_at: 2026-11-23T16:08:39Z
expires_at: 2026-11-24T03:30:00Z
planned_for:
not_before: 2026-11-23T16:40:00Z
window: locate and record the builders hut no reading attached
est_minutes: 8
serves: PL-08
chain_id: locate-2026-11-23
chain_seq: 2
attempts: 0
max_attempts: 3
claimed_by:
claimed_at:
lease_until:
---

# scout-midday

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: snapshot

## Brief (definition pointer, from the roster)

This unit is the regular `scout-midday`: Scout - midday perception pass (floor anchor); re-walk the interface for state-dependent availability (trains, phase rotations, market refreshes); full passes also fire on detected state change between anchors. Its definition is the activity folder `_activities_/perception-scout/` (the folder is named for the activity, not the regular id): read its `rule-digest.md` first, then its `INDEX.md`. The map of every regular to its activity folder is `_records_/2026-11-22/queue-planning/2760-regular-to-activity-map.csv`. If the digest does not cover a step, stop with 'blocked by prerequisite' and say which step; never improvise.

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (routes in `_records_/2026-11-22/queue-planning/2700-routes.csv`). Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.

## Brief (planner, LOCATE AND RECORD the Builders Hut, no reading, the Coach's cause 1 of the growth partials)

serves: PL-08

The Builders Hut was never located: `tag-index.csv` row says 'not found'. Search the base by panning as in the Oil Well find (WORLD then BASE, drag (400,580) to (150,830), drag (660,470) to (390,620)) and the other quadrants, at most 8 pans; tap ONE building per fresh frame.

ONE job, done when the tag is read: find it, read the tag text (name and level above it, or the screen title) and record its position (the pan offset and the tap point on the fresh frame) or the route taps. Write it as a row in `_records_/2026-11-22/growth/tag-index.csv` (columns tag_text, level, fresh_frame_x, fresh_frame_y, note). Read NOTHING else: no preview, no costs. Not found after the pans: stop 'blocked by route' and write the frames covered, so the next unit starts from them. May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if one opens, STOP.

Up to two runs, 10 steps each.
Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (safe tap: bare spot (310,660), not (400,640) after a camera shift). A TIPS dialog about another device: STOP, report, never Confirm. Tag text beside every number; none means [G]. Press nothing that upgrades, collects, trains, researches or speeds up.
Cost cap, stated: 0.40 USD (the harness stops near 0.36 of it).
