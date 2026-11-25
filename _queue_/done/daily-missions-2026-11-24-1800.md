---
unit: daily-missions-2026-11-24-1800
regular: daily-missions
activity: daily-missions
segment: 3
priority: 3
created_at: 2026-11-24T22:01:01Z
expires_at: 2026-11-26T02:00:00Z
planned_for: 2026-11-25T02:00:00Z
not_before: 2026-11-25T02:06:00Z
window:
est_minutes: 2
serves: upkeep
chain_id:
chain_seq:
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-25T02:06:33Z
lease_until: 2026-11-25T02:26:33Z
result:
  status: done
  started_at: 2026-11-25T02:06:33Z
  finished_at: 2026-11-25T02:09:27Z
  duration_seconds: 174
  executor: operator
  summary: New-day missions: Main Tasks had no Claim (five Go rows, never pressed); Daily Tasks: one tap on the Daily Login Claim paid the login and VIP rows (points 0 to 50, diamonds 11,173 to 11,193) and the glowing 40 chest was claimed once (2 gear items, a rocket item, 2 resource crates, 2 bread crates, 6 gold crates, 600 crystal shards, a 5-minute speed-up); the 80 chest needs 30 more points; tram badge 3 and pickup badge 10 unchanged; drags 0. state_change: yes
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/daily-missions/0206-queue-run.md and 0206-queue-run.csv; run 20261125T020633Z-d33d0a
  state_change: yes
  follow_up: the remaining daily tasks need Go (not seat actions); 30 more points open the 80 chest
  stats:
    target: claim the Main Tasks and Daily Tasks rewards
    achieved: login and VIP rewards and the 40 chest claimed
    resources_gained: gems +20; 40 chest: gear items x2, rocket item x1, resource crates x2, bread crates x2, gold crates x6, crystal shards 600, 5m speed-up x1
    points: 0
    costs: none spent; model 0.247812 USD
    verified: yes
    run_id: 20261125T020633Z-d33d0a
    run_steps: 19
    actions_done: 8
    actions_refused: 0
    cost_usd: 0.247812
    device_takeovers: 0
    claims: 2
    points_before: 0
    points_after: 50
    diamonds_before: 11173
    diamonds_after: 11193
    tram_badge: 3
    pickup_badge: 10
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

MAIN TASKS (Steer A 01:21Z, folded in): the panel may open on the Main Tasks tab (read the tab labels first). Read every Main Tasks row by text; tap a plain green CLAIM once per row (no price, no gem icon, not Buy, Unlock, Upgrade or Activate), re-reading the list after each; EVERY Go stays unpressed; record the rewards. Then the Daily Tasks tab as below.
Daily missions: claim each completed Mission task's plain Claim one by one, re-checking after each; claim an activity chest at its threshold only when its button is a plain Claim (never a diamond or price line). Write the points before and after.

Safe tap: the bare spot (310,660), not (400,640) after a camera shift (WORLD then BASE first). Verify each HUD icon by its label or glyph in a frame before the tap. A TIPS dialog about another device: STOP, report, never Confirm. No purchase, diamond spend or speed-up.
FRONT (Steer A 21:11Z): at the start, if `lsappinfo front` is not LastWar, record it, run the standing front script, record again; still not LastWar: stop, release, tell the Coordinator.
May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Cost cap, stated: 0.60 USD.
