---
unit: training-room-test-2026-11-24-001
regular: training
activity: troop-training
segment: 2
priority: 2
created_at: 2026-11-24T04:16:44Z
expires_at: 2026-11-23T12:00:00Z
planned_for:
not_before: 2026-11-24T11:20:00Z
window: one pistol press on the lv 30 barracks after it finishes the free partial collect test
est_minutes: 6
serves: PL-09
chain_id: room-test-2026-11-24
chain_seq: 1
attempts: 0
max_attempts: 3
claimed_by:
claimed_at:
lease_until:
result:
  status: expired
  started_at:
  finished_at: 2026-11-24T04:17:44Z
  duration_seconds: 
  executor:
  summary: retired by the planner: with room 0 both the ramp and the all-or-nothing models refuse, so a press at 11:20Z is not informative (Coach evidence 1215); the informative test is 2026-11-26T21:10:37Z in training-room-collect-2026-11-26-001
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

## Brief (planner, ONE pistol press on the Lv.30 barracks right after it finishes: the free partial collect test, PL-09)

serves: PL-09

DISPATCH ONLY WHEN NAMED, 11:20Z. The Barracks Lv.30 batch (Lv.10 x793) finishes 2026-11-24T11:18:24Z (07:25:14 left at 03:53Z); the free room is about 0 (the Lv.24 collect filled the 274; records 0330 and 0351). Steer A's test: does a collect succeed with room BELOW the batch size?

1. Read 'Unit Count X of Y' (the free room) FIRST; write it with its tag text and the UTC time.
2. Open the Lv.30 barracks (about (530,637) on the fresh frame, `_records_/2026-11-22/growth/tag-index.csv`): the ready bubble shows a portrait for a finished batch and a clock while training. If it is still training, stop 'blocked by window' and write the time left.
3. Press the pistol (the middle button under the tag) ONCE. Record the toast EXACTLY, 'Unit Count X of Y' before and after, and Total Power before and after: a partial release shows up to the room in troops; a refusal shows 'Drill Ground Full'; a whole collect would show +1,306,071.

Never Train, Heal, a Hospital Collect, speed up or buy. Outside the cu window (08:00Z to 08:25Z) and the 09:50Z to 10:20Z probe hour. May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if one opens, STOP and touch nothing.
Safe tap: the bare spot (310,660), not (400,640) after a camera shift. Tag text beside every number; none means [G].
Cost cap, stated: 0.40 USD.
