---
unit: daily-missions-2026-11-24-0015
regular: daily-missions
activity:
segment:
priority: 1
created_at: 2026-11-24T00:15:29Z
expires_at: 2026-11-24T01:50:00Z
planned_for:
not_before: 2026-11-24T00:20:00Z
window:
est_minutes: 6
serves: upkeep
chain_id:
chain_seq:
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-24T00:37:10Z
lease_until: 2026-11-24T00:57:10Z
result:
  status: done
  started_at: 2026-11-24T00:37:10Z
  finished_at: 2026-11-24T00:39:02Z
  duration_seconds: 112
  executor: operator
  summary: The Oil Well main task Claim pressed once (5.0K food and 5.0K iron, no popup); activity points 220 with five chests whose claimed state is unreadable (the 40 chest showed a contents preview); no Go pressed
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/daily-missions/0037-queue-run.md and 0037-queue-run.csv; run 20261124T003710Z-dde890
  follow_up: chest states 80 to 200 unread; the next daily refresh in 01:22:19 (about 02:00Z)
  stats:
    target: claim completed Mission tasks one by one and the activity chests at their thresholds
    achieved: main task claimed; chests unreadable
    resources_gained: food 5.0K; iron 5.0K
    points: 0
    costs: none spent; model 0.152859 USD
    verified: yes
    run_id: 20261124T003710Z-dde890
    run_steps: 11
    actions_done: 19
    actions_refused: 0
    cost_usd: 0.152859
    device_takeovers: 0
    main_task_claims: 1
    activity_points: 220
    rules_used: 1,2
  stats_missing: []
  stats_warnings: []
---

# daily-missions

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: upkeep

## Brief (definition pointer, from the roster)

This unit is the regular `daily-missions`: Daily missions - claim completed Mission tasks one by one, re-checking after each, and claim the activity chests at their thresholds. Its definition is the activity folder `_activities_/daily-missions/` (the folder is named for the activity, not the regular id): read its `rule-digest.md` first, then its `INDEX.md`. The map of every regular to its activity folder is `_records_/2026-11-22/queue-planning/2760-regular-to-activity-map.csv`. If the digest does not cover a step, stop with 'blocked by prerequisite' and say which step; never improvise.

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (routes in `_records_/2026-11-22/queue-planning/2700-routes.csv`). Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.
