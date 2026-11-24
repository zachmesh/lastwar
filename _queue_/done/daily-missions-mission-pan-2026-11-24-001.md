---
unit: daily-missions-mission-pan-2026-11-24-001
regular: daily-missions
activity: daily-missions
segment: 2
priority: 2
created_at: 2026-11-24T13:07:35Z
expires_at: 2026-11-24T13:55:00Z
planned_for:
not_before: 2026-11-24T13:12:00Z
window: one pan on the mission panel for the two claim rows below the fold held for steer a
est_minutes: 6
serves: upkeep
chain_id: mission-pan-2026-11-24
chain_seq: 1
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-24T13:15:49Z
lease_until: 2026-11-24T13:35:49Z
result:
  status: done
  started_at: 2026-11-24T13:15:49Z
  finished_at: 2026-11-24T13:16:56Z
  duration_seconds: 67
  executor: operator
  summary: The two Claim rows sat inside the Mission panel (not below the fold): no pan; one Claim tap claimed both (activity points 90 to 130, badge 2 to 1, no popup); the 120 chest looks highlighted and was not opened; drags 0; tram badge none
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/daily-missions/1315-queue-run.md and 1315-queue-run.csv; run 20261124T131550Z-46ce53
  follow_up: the 120 activity chest looks claimable at 130 points (a daily-missions unit); the rest of the rows are Go only
  stats:
    target: claim the two Claim rows below the fold by the composed pan
    achieved: both claimed by one tap, no pan needed
    resources_gained: none
    points: 0
    costs: none spent; model 0.083087 USD
    verified: yes
    run_id: 20261124T131550Z-46ce53
    run_steps: 5
    actions_done: 7
    actions_refused: 0
    cost_usd: 0.083087
    device_takeovers: 0
    claims: 2
    activity_points_before: 90
    activity_points_after: 130
    drags_tried: 0
    tram_badge: none
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

## Brief (planner, THE MISSION PANEL: the two Claim rows below the fold, ONE pan, approved by Steer A 13:11Z)

serves: upkeep

A NEW page: do NOT copy the shop page's numbers. THE RECIPE (13:01Z, Weekly Pass page: moved 150 px, no fling), ALL IN ONE MESSAGE: mouse_move to a start on the blank right margin; left_mouse_down; wait 1 (second); mouse_move about 175 px along the page; wait 1 (second); left_mouse_up; a screenshot after the up; nothing else between the down and the up; if refused: write the text, STOP.
(1) Open the Mission panel; a frame. BEFORE the pan write where the two Claim rows are and where the blank margin of THIS panel is (outside the cards), and the start y. ONE pan by the recipe from that margin; a frame after; write the margin x and the distance you chose, the rows' y before and after, and the page's MOVE in px. At most ONE correction pan the same way.
(2) Tap each Claim now inside the content ONCE, only if its button reads a plain CLAIM with NO price, gem or diamond icon, Buy, Purchase, Unlock, Upgrade or Activate. A chest those rows open follows the standing chest rules: read the quantity before any Use. A claim needing a second pan: write it, STOP.
(3) A price, diamond spend, real-money line or app store sheet: STOP. Any other element (tooltip, menu, highlight, dialog): touch nothing, frame, stop, tell the Coordinator. May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Cost cap, stated: 0.40 USD.
