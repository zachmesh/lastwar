---
unit: training-train-preview-2026-11-24-001
regular: training
activity: troop-training
segment: 2
priority: 2
created_at: 2026-11-24T03:39:31Z
expires_at: 2026-11-23T12:00:00Z
planned_for:
not_before: 2026-11-24T04:00:00Z
window: read only the train preview for the free drill ground room never train
est_minutes: 12
serves: PL-09
chain_id: train-preview-2026-11-24
chain_seq: 1
attempts: 0
max_attempts: 3
claimed_by:
claimed_at:
lease_until:
result:
  status: expired
  started_at:
  finished_at: 2026-11-24T03:59:31Z
  duration_seconds: 
  executor:
  summary: retired by the planner: at 03:51Z the pistol on Barracks Lv.24 collected a finished batch of 274 Lv.8 troops (+291,262 power), so the free Drill Ground room is about 0 again; restaged for the next room (the Lv.26 ground completes 2026-11-26T21:10:37Z, +200)
  claimed: []
  claimed_count: 0
  evidence: 
  follow_up: none
  stats:
  stats_missing: [target, achieved, resources_gained, costs, verified]
  stats_warnings: []
---

# training

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: PL-09

## Brief (definition pointer, from the roster)

This unit is the regular `training`: Troop training - requeue any finished barracks at its highest tier. Its definition is the activity folder `_activities_/troop-training/` (the folder is named for the activity, not the regular id): read its `rule-digest.md` first, then its `INDEX.md`. The map of every regular to its activity folder is `_records_/2026-11-22/queue-planning/2760-regular-to-activity-map.csv`. If the digest does not cover a step, stop with 'blocked by prerequisite' and say which step; never improvise.

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (routes in `_records_/2026-11-22/queue-planning/2700-routes.csv`). Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.

## Brief (planner, READ-ONLY: the Train preview for the free Drill Ground room, the Strategist's call)

serves: PL-09

Why: at 03:30:53Z the Lv.27 batch of 726 collected with no refusal because the 1,000 troops the siege wounded left the army: about 274 room is left (record `_records_/2026-11-22/perception-scout/0330-queue-run.md`). An idle barracks could train up to 274 troops (T8 1,063 to T10 1,647 power each). The Strategist decides; this unit only READS the preview.

EXIT PLAN. PRESSED: the barracks tag taps (tap points and tag text in `_records_/2026-11-22/growth/tag-index.csv`: Lv.24 about (628,562), Lv.20 about (668,535), Lv.27 about (462,585) on the fresh frame, one barracks per frame), the pistol (the middle button under the tag), the quantity field or slider, and the panel's X. NEVER PRESSED: Train, Confirm, Speed Up, Buy, Use, Collect. May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if one opens, STOP and touch nothing.

For each IDLE barracks: write the tag text; in the Train panel write every tier offered (T8, T9, T10), and per tier the cost per troop (each resource), the time, the power per troop if shown, and the slider maximum with any 'Drill Ground Full' text. Then set the quantity to 274 (or the slider maximum if lower) and write the Total cost and Total time lines in a frame BEFORE closing; close with X, never Train. Done when one idle barracks is read; the others are optional extras.

Up to two runs, 10 steps each. Tag text beside every number; none means [G]. Safe tap: the bare spot (310,660), not (400,640) after a camera shift.
Cost cap, stated: 0.50 USD per run.
