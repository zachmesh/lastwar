---
unit: daily-missions-2026-11-24-1630
regular: daily-missions
activity: daily-missions
segment: 3
priority: 1
created_at: 2026-11-24T22:01:09Z
expires_at: 2026-11-25T02:00:00Z
planned_for: 2026-11-25T00:30:00Z
not_before: 2026-11-25T00:30:00Z
window: pre-reset fix-up for 2026-11-24 sweep
est_minutes: 2
serves: upkeep
chain_id:
chain_seq:
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-25T00:46:01Z
lease_until: 2026-11-25T01:06:01Z
result:
  status: done
  started_at: 2026-11-25T00:46:01Z
  finished_at: 2026-11-25T00:48:01Z
  duration_seconds: 120
  executor: operator
  summary: Daily missions: the one completed task (Defeat any Doom Elite 1/1) claimed once: activity points 140 to 150 (a bread item 5.0K and an iron item 5.0K on the row); chests 40, 80, 120 opened, 160 and 200 closed with no claim signal (150 below 160); remaining tasks all blue Go, never pressed; tram icon not drawn; drags 0. state_change: yes
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/daily-missions/0046-queue-run.md and 0046-queue-run.csv; run 20261125T004601Z-76ff14
  state_change: yes
  follow_up: 10 more activity points open the 160 chest; the remaining tasks need Go (attacks and marches are not seat actions)
  stats:
    target: claim each completed task and each reached chest
    achieved: 1 task claimed; no chest reached
    resources_gained: activity points 10; bread item 5.0K; iron item 5.0K
    points: 0
    costs: none spent; model 0.177705 USD
    verified: yes
    run_id: 20261125T004601Z-76ff14
    run_steps: 14
    actions_done: 3
    actions_refused: 0
    cost_usd: 0.177705
    device_takeovers: 0
    claims: 1
    points_before: 140
    points_after: 150
    tram_badge: icon not drawn
    drags_tried: 0
    rules_used: 1
  stats_missing: []
  stats_warnings: []
---

# daily-missions

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

## Brief (definition pointer, from the roster)

This unit is the regular `daily-missions`: Daily missions - claim completed Mission tasks one by one, re-checking after each, and claim the activity chests at their thresholds. Its definition is the activity folder `_activities_/daily-missions/` (the folder is named for the activity, not the regular id): read its `rule-digest.md` first, then its `INDEX.md`. The map of every regular to its activity folder is `_records_/2026-11-22/queue-planning/2760-regular-to-activity-map.csv`. If the digest does not cover a step, stop with 'blocked by prerequisite' and say which step; never improvise.

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (routes in `_records_/2026-11-22/queue-planning/2700-routes.csv`). Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.

## Brief (planner, the specifics)

Daily missions: claim each completed Mission task's plain Claim one by one, re-checking after each; claim an activity chest at its threshold only when its button is a plain Claim (never a diamond or price line). Write the points before and after.

Safe tap: the bare spot (310,660), not (400,640) after a camera shift (WORLD then BASE first). Verify each HUD icon by its label or glyph in a frame before the tap. A TIPS dialog about another device: STOP, report, never Confirm. No purchase, diamond spend or speed-up.
FRONT (Steer A 21:11Z): at the start, if `lsappinfo front` is not LastWar, record it, run the standing front script, record again; still not LastWar: stop, release, tell the Coordinator.
May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Cost cap, stated: 0.60 USD.
