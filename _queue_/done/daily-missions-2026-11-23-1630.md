---
unit: daily-missions-2026-11-23-1630
regular: daily-missions
activity: daily-missions
segment: 3
priority: 1
created_at: 2026-11-23T06:12:45Z
expires_at: 2026-11-24T02:00:00Z
planned_for: 2026-11-24T00:30:00Z
not_before: 2026-11-24T00:30:00Z
window: pre-reset fix-up for 2026-11-23 sweep
est_minutes: 11
serves: upkeep
chain_id:
chain_seq:
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-24T00:49:33Z
lease_until: 2026-11-24T01:09:33Z
result:
  status: done
  started_at: 2026-11-24T00:49:33Z
  finished_at: 2026-11-24T00:51:33Z
  duration_seconds: 120
  executor: operator
  summary: Nothing left to claim: the Oil Well row gone, all five activity chests (220 points) opened as contents previews only (read as claimed), the remaining rows are Go rows; no Go pressed
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/daily-missions/0049-queue-run.md and 0049-queue-run.csv; run 20261124T004933Z-d8e27d
  follow_up: daily refresh about 02:00Z; ledger line 14 at zero on this read
  stats:
    target: claim completed Mission tasks one by one and the activity chests at their thresholds
    achieved: nothing claimable; the five chests read as claimed
    resources_gained: none
    points: 0
    costs: none spent; model 0.143577 USD
    verified: yes
    run_id: 20261124T004933Z-d8e27d
    run_steps: 11
    actions_done: 30
    actions_refused: 0
    cost_usd: 0.143577
    device_takeovers: 0
    activity_points: 220
    chests_read: 5
    rules_used: 1,2
  stats_missing: []
  stats_warnings: []
---

# daily-missions

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

## Brief (planner, definition pointer, the unit had none)

This unit is the regular `daily-missions`: Daily missions - claim completed Mission tasks one by one, re-checking after each, and claim the activity chests at their thresholds. Its definition is the activity folder `_activities_/daily-missions/` (the folder is named for the activity, not the regular id): read its `rule-digest.md` first, then its `INDEX.md`. The map of every regular to its activity folder is `_records_/2026-11-22/queue-planning/2760-regular-to-activity-map.csv`. If the digest does not cover a step, stop with 'blocked by prerequisite' and say which step; never improvise.

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (routes in `2700-routes.csv`); the safe empty-ground tap is the bare spot (310,660), not (400,640) after a camera shift. A TIPS dialog about another device: STOP, report, never Confirm. Tag text beside every number from a building panel. No purchase, diamond spend or speed-up. Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.
May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Cost cap, stated: 0.60 USD (the harness stops near 0.36 of it).
