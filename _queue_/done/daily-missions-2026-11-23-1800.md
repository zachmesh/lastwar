---
unit: daily-missions-2026-11-23-1800
regular: daily-missions
activity: daily-missions
segment: 3
priority: 3
created_at: 2026-11-23T22:33:32Z
expires_at: 2026-11-25T02:00:00Z
planned_for: 2026-11-24T02:00:00Z
not_before: 2026-11-24T02:00:00Z
window:
est_minutes: 11
serves: upkeep
chain_id:
chain_seq:
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-24T05:08:49Z
lease_until: 2026-11-24T05:28:49Z
result:
  status: partial
  started_at: 2026-11-24T05:08:49Z
  finished_at: 2026-11-24T05:12:17Z
  duration_seconds: 208
  executor: operator
  summary: Oil Well Lv.22 side task Claim (5.0K food and 5.0K iron), one Daily Tasks Claim tap for four finished rows (activity points 0 to 90, gems +20), chests 40 and 80 opened; two Claim rows remain: a swipe was cancelled at 05:11:26Z by a foreground switch of an unnamed outside app
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/daily-missions/0509-queue-run.md and 0509-queue-run.csv; run 20261124T050849Z-7d52d4
  follow_up: two Daily Tasks Claim rows below the fold remain; the foreground switch at 05:11:26Z is unexplained
  stats:
    target: claim completed Mission tasks one by one and the chests at their thresholds
    achieved: Main Tasks claimed, four daily rows claimed, chests 40 and 80 opened, two rows left
    resources_gained: none
    points: 0
    costs: none spent; model 0.244 USD
    verified: yes
    run_id: 20261124T050849Z-7d52d4
    run_steps: 19
    actions_done: 26
    actions_refused: 0
    cost_usd: 0.244
    device_takeovers: 0
    activity_points: 90
    blocker_category: f missing precondition (a foreground switch of an unnamed outside app cancelled the swipe at 05:11:26Z)
    rules_used: 1,2
  stats_missing: []
  stats_warnings: []
---

# daily-missions

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

## Brief (definition pointer, from the roster)

This unit is the regular `daily-missions`: Daily missions - claim completed Mission tasks one by one, re-checking after each, and claim the activity chests at their thresholds. Its definition is the activity folder `_activities_/daily-missions/` (the folder is named for the activity, not the regular id): read its `rule-digest.md` first, then its `INDEX.md`. The map of every regular to its activity folder is `_records_/2026-11-22/queue-planning/2760-regular-to-activity-map.csv`. If the digest does not cover a step, stop with 'blocked by prerequisite' and say which step; never improvise.

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (routes in `_records_/2026-11-22/queue-planning/2700-routes.csv`). Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.

## Brief (planner, the 02:03Z wave specifics)

Daily missions: claim only plainly labelled Claims; no purchase, no diamond item.

May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing. Safe tap: the bare spot (310,660), not (400,640) after a camera shift (WORLD then BASE first).
