---
unit: building-queues-growth-convert-2026-11-24-004
regular: building-queues
activity: building-queues
segment: 1
priority: 1
created_at: 2026-11-23T22:43:46Z
expires_at: 2026-11-23T12:00:00Z
planned_for:
not_before: 2026-11-23T23:20:15Z
window: fallback the lv 28 ground start after the food conversion if the first attempt stopped on food
est_minutes: 12
serves: PL-08
chain_id: growth-convert-2026-11-24
chain_seq: 4
attempts: 0
max_attempts: 3
claimed_by:
claimed_at:
lease_until:
result:
  status: expired
  started_at:
  finished_at: 2026-11-23T23:49:56Z
  duration_seconds: 
  executor:
  summary: retired by the planner: ground 002 started the Lv.28 ground at 23:39:45.957Z (ends 2026-12-12T02:29:20Z), so this fallback start would try to upgrade a ground already upgrading
  claimed: []
  claimed_count: 0
  evidence: 
  follow_up: none
  stats:
  stats_missing: [target, achieved, resources_gained, costs, verified]
  stats_warnings: []
---

# building-queues

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: PL-08

## Brief (definition pointer, from the roster)

This unit is the regular `building-queues`: Building queues - read the four build queues, record running upgrades and idle slots; read-only, never start builds. Its definition is the activity folder `_activities_/building-queues/` (the folder is named for the activity, not the regular id): read its `rule-digest.md` first, then its `INDEX.md`. The map of every regular to its activity folder is `_records_/2026-11-22/queue-planning/2760-regular-to-activity-map.csv`. If the digest does not cover a step, stop with 'blocked by prerequisite' and say which step; never improvise.

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (routes in `_records_/2026-11-22/queue-planning/2700-routes.csv`). Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.

## Brief (planner, FALLBACK: the Lv.28 ground start (B4) after the food conversion)

serves: PL-08

DISPATCH ONLY WHEN NAMED, after `building-queues-growth-convert-2026-11-24-002` stopped on 'blocked by prerequisite: food' and `building-queues-growth-preconvert-2026-11-23-003` converted the food. Plan, tap points, previews, hazards: `_records_/2026-11-22/queue-planning/2540-drill-ground-sheet.md`. The first idle builder, the Lv.28 ground (119.0M coin, 144.5M iron, about 442M food if the row shows): read its tag and preview INCLUDING the troop capacity line (current and next), the Details figure and the free room; read EVERY cost row, scrolling to its end if it scrolls, and write each row (name, value, visible without a scroll yes or no) in the unit note as [M]; a short row stops with 'blocked by prerequisite: <resource>'; press Upgrade once, read the timer to the second and write the finish time in UTC. Never Speed Up, Finish Now or Obtain.

Tag text beside every number; none means [G]. Never Upgrade on a builder running the owner's queue.
Cost cap, stated: 0.60 USD.
