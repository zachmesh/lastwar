---
unit: scout-midday-time-grant-read-2026-11-23-001
regular: scout-midday
activity: perception-scout
segment: 2
priority: 2
created_at: 2026-11-23T23:38:14Z
expires_at: 2026-11-24T06:00:00Z
planned_for:
not_before: 2026-11-24T00:10:00Z
window: read only the event and buff pages for a flat upgrade time reduction
est_minutes: 12
serves: PL-08
chain_id: time-grant-read-2026-11-23
chain_seq: 1
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-24T00:17:18Z
lease_until: 2026-11-24T00:37:18Z
result:
  status: partial
  started_at: 2026-11-24T00:17:18Z
  finished_at: 2026-11-24T00:19:22Z
  duration_seconds: 124
  executor: operator
  summary: The flat 6h 32m time grant not found: HUD icons, Events hub, Building Queue, profile and VIP page read; VIP13 Construction Speed 50.00 percent and Research Speed 20.00 percent are percentages; The Age of Oil page not reached
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/perception-scout/0017-queue-run.md and 0017-queue-run.csv; run 20261124T001718Z-a597f5
  follow_up: read The Age of Oil rules icon after a tab-bar drag; read the last VIP privilege line; the Builder's Hut is unlocated
  stats:
    target: find the text that names the flat 6h 32m upgrade time grant
    achieved: not found; five pages read, listed
    resources_gained: none
    points: 0
    costs: none spent; model 0.139712 USD
    verified: yes
    run_id: 20261124T001718Z-a597f5
    run_steps: 10
    actions_done: 19
    actions_refused: 0
    cost_usd: 0.139712
    device_takeovers: 0
    blocker_category: f missing precondition (the Age of Oil tab off the left edge, no grant text on the pages read)
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

## Brief (planner, READ-ONLY: look for the source of the flat 6 h 32 min upgrade time grant)

serves: PL-08

Steer A's test 1: every build tonight ended 23,520 s (6 h 32 min) before its preview (Oil Well, and the Lv.26 and Lv.27 grounds), and research 15,120 s before the Research button: a flat grant, probably an event or a status. Find the text that says so. READ ONLY, one run, 12 steps, one frame per page.

1. Events hub: open the Age of Oil tab and any event page that names construction, upgrade or speed; read its rules or details text.
2. The HUD status or buff icons (near the avatar or the top bar), if any: open ONE per frame and read the text.
3. The Builders hut panel (hammer icon) and the VIP panel: read any line about build or research time.
Write every text that contains 'reduce', 'time', 'speed' or 'build' with the page name and the UTC time; if none, say 'not found' and list the pages read, so the next unit starts from them.

Press NOTHING that buys, claims, goes, shares or links. May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if one opens, STOP and touch nothing. Tag text beside every number; none means [G].
Cost cap, stated: 0.50 USD.
