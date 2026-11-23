---
unit: scout-midday-locate-2026-11-23-001
regular: scout-midday
activity: perception-scout
segment: 2
priority: 3
created_at: 2026-11-23T16:08:38Z
expires_at: 2026-11-24T03:30:00Z
planned_for:
not_before: 2026-11-23T16:40:00Z
window: locate and record the tech center no reading attached
est_minutes: 8
serves: PL-04
chain_id: locate-2026-11-23
chain_seq: 1
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-23T18:01:07Z
lease_until: 2026-11-23T18:21:07Z
result:
  status: partial
  started_at: 2026-11-23T18:01:07Z
  finished_at: 2026-11-23T18:03:12Z
  duration_seconds: 125
  executor: operator
  summary: Tech Center not found on the fresh frame: four tags read (Arena Lv.1, Hospital Lv.25, Drone Center Lv.1, Eternal Pyramid Lv.3), one building showed no tag; no pans made; three tag rows added
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/perception-scout/1801-queue-run.md and 1801-queue-run.csv; run 20261123T180107Z-2f61d4
  follow_up: second run with pans (south and west, then the far left); Tech Center unlocated
  stats:
    target: find the Tech Center and read its tag
    achieved: not found; 4 other tags read
    resources_gained: none
    points: 0
    costs: none spent; model 0.131713 USD
    verified: yes
    run_id: 20261123T180107Z-2f61d4
    run_steps: 11
    actions_done: 28
    actions_refused: 0
    cost_usd: 0.131713
    device_takeovers: 0
    blocker_category: f missing precondition (the Tech Center is unlocated; no pan made)
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

## Brief (planner, LOCATE AND RECORD the Tech Center, no reading, the Coach's cause 1 of the growth partials)

serves: PL-04

The Tech Center is not on the base frame (the flask opens the research list without it) and the HQ 31 read gave only 'Lv.30 Any Tech Center' green. Its tag was never read. Last known: not found; `tag-index.csv` row 'Tech Center' says unlocated. Likely a large building: search the base by panning as in the Oil Well find (WORLD then BASE, drag (400,580) to (150,830), drag (660,470) to (390,620)) and the other quadrants, at most 8 pans.

ONE job, done when the tag is read: find it, read the tag text (name and level above it, or the screen title) and record its position (the pan offset and the tap point on the fresh frame) or the route taps. Write it as a row in `_records_/2026-11-22/growth/tag-index.csv` (columns tag_text, level, fresh_frame_x, fresh_frame_y, note). Read NOTHING else: no preview, no costs. Not found after the pans: stop 'blocked by route' and write the frames covered, so the next unit starts from them. May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if one opens, STOP.

Up to two runs, 10 steps each.
Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (safe tap: bare spot (310,660), not (400,640) after a camera shift). A TIPS dialog about another device: STOP, report, never Confirm. Tag text beside every number; none means [G]. Press nothing that upgrades, collects, trains, researches or speeds up.
Cost cap, stated: 0.40 USD (the harness stops near 0.36 of it).
