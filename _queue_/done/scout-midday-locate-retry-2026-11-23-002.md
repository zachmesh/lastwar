---
unit: scout-midday-locate-retry-2026-11-23-002
regular: scout-midday
activity: perception-scout
segment: 2
priority: 3
created_at: 2026-11-23T19:32:26Z
expires_at: 2026-11-24T03:30:00Z
planned_for:
not_before: 2026-11-23T19:40:00Z
window: locate the builders hut second attempt unseen areas only
est_minutes: 8
serves: PL-08
chain_id: locate-retry-2026-11-23
chain_seq: 2
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-23T20:23:00Z
lease_until: 2026-11-23T20:43:00Z
result:
  status: partial
  started_at: 2026-11-23T20:23:00Z
  finished_at: 2026-11-23T20:27:06Z
  duration_seconds: 246
  executor: operator
  summary: Builder's Hut not found in the centre, west and east of the HQ: Hospital Lv.25 and Lv.20, Gear Factory Lv.20, Alliance Support Hub Lv.30 and an accidental Barracks Lv.30 tag read; one tag row added
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/perception-scout/2023-queue-run.md and 2023-queue-run.csv; run 20261123T202301Z-943076
  follow_up: remaining: the far north and other pans; the quest line may be the only route; planner may close PL-08 as blocked by route
  stats:
    target: find the Builder's Hut and read its tag
    achieved: not found; Alliance Support Hub Lv.30 recorded
    resources_gained: none
    points: 0
    costs: none spent; model 0.178443 USD
    verified: yes
    run_id: 20261123T202301Z-943076
    run_steps: 12
    actions_done: 23
    actions_refused: 0
    cost_usd: 0.178443
    device_takeovers: 0
    blocker_category: f missing precondition (the Builder's Hut is not in the covered frames)
    rules_used: 1
  stats_missing: []
  stats_warnings: []
---

# scout-midday

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: PL-08

## Brief (definition pointer, from the roster)

This unit is the regular `scout-midday`: Scout - midday perception pass (floor anchor); re-walk the interface for state-dependent availability (trains, phase rotations, market refreshes); full passes also fire on detected state change between anchors. Its definition is the activity folder `_activities_/perception-scout/` (the folder is named for the activity, not the regular id): read its `rule-digest.md` first, then its `INDEX.md`. The map of every regular to its activity folder is `_records_/2026-11-22/queue-planning/2760-regular-to-activity-map.csv`. If the digest does not cover a step, stop with 'blocked by prerequisite' and say which step; never improvise.

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (routes in `_records_/2026-11-22/queue-planning/2700-routes.csv`). Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.

## Brief (planner, LOCATE AND RECORD the Builder's Hut, second attempt)

serves: PL-08

One job: read the tag; no preview, no costs.

Covered, do NOT repeat: the south-east and core base (record 1541, `_records_/2026-11-22/resource-collection/`), the whole north-west (1547), the north-east and east edge (1553: Oil Well Lv.20 at about (1090,340)) and the south-west corner (1921, `_records_/2026-11-22/perception-scout/`). Skip every building whose tag is already in `tag-index.csv`.

NOT yet seen: the west and the middle, and the centre around the HQ (about (565,405)). The Hut is a small building near the HQ and the builders; the HUD quest bar line names it ('Upgrade Builder's Hut to Lv.26'), so READ that line for the name only.

Tap ONE building per fresh frame (WORLD then BASE first; the bare spot (310,660)); read its tag text (name, level) and record the position (pan offset and tap point) as a row in `_records_/2026-11-22/growth/tag-index.csv`. The HQ radial menu or Tech hub icon only if in-game; the HUD quest bar line may be READ, its Go is NOT pressed. NEVER tap the SALE stall at (135,525): it opens the Black Market panel. Not found after 8 steps: stop 'blocked by route' and write the frames covered. Start only when the idle counter (read-only) reads 300 s or more (the owner may be at the Mac); a foreground switch to another app stops the run: touch nothing. May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if one opens, STOP.

Up to two runs, 8 steps each.
Cost cap, stated: 0.40 USD per run (the harness stops near 0.36 of it).
