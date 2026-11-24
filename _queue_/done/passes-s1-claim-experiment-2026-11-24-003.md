---
unit: passes-s1-claim-experiment-2026-11-24-003
regular: passes
activity: shop-claims
segment: 1
priority: 2
created_at: 2026-11-24T12:01:00Z
expires_at: 2026-11-24T13:11:00Z
planned_for:
not_before: 2026-11-24T12:09:00Z
window: experiment three an intermediate margin drag waiting for steer a held shut
est_minutes: 6
serves: PL-05
chain_id: s1-claim-experiment-2026-11-24
chain_seq: 3
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-24T12:11:12Z
lease_until: 2026-11-24T12:31:12Z
result:
  status: partial
  started_at: 2026-11-24T12:11:12Z
  finished_at: 2026-11-24T12:13:16Z
  duration_seconds: 124
  executor: operator
  summary: One 135 px margin drag (685,400 to 685,265) moved the Weekly Pass page 0 px (S2 title y 531 before and after; the S1 Claim y about 915 before and after): clipped, not pressed: blocked by route: Claim clipped; with 70 px 0 and 250 px far (S1 out of view) the threshold lies between 135 and 250 px; the Iron and Coin cards never visible; drags 1; tram badge none
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/shop-claims/1211-queue-run.md and 1211-queue-run.csv; run 20261124T121112Z-cf30f9
  follow_up: the distance table: 70 px moved 0, 135 px moved 0, 250 px over-scrolled; the S1 Claim stays unclaimed until a drag between 135 and 250 px is allowed
  stats:
    target: claim the S1 Drone Parts Daily Pickup by one 120 to 150 px margin drag
    achieved: the 135 px drag moved 0 px
    resources_gained: none
    points: 0
    costs: none spent; model 0.130438 USD
    verified: yes
    run_id: 20261124T121112Z-cf30f9
    run_steps: 10
    actions_done: 13
    actions_refused: 0
    cost_usd: 0.130438
    device_takeovers: 0
    blocker_category: f missing precondition (blocked by route: Claim clipped; the 135 px drag moved 0 px)
    drags_tried: 1
    drags_cancelled: 0
    drag_distance_px: 135
    page_move_px: 0
    tram_badge: none
    rules_used: 1,2,3,6
  stats_missing: []
  stats_warnings: []
---

# passes

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: PL-05

## Brief (definition pointer, from the roster)

This unit is the regular `passes`: Passes - weekly/monthly daily pickups and Free Supply in the shop. Its definition is the activity folder `_activities_/shop-claims/` (the folder is named for the activity, not the regular id): read its `rule-digest.md` first, then its `INDEX.md`. The map of every regular to its activity folder is `_records_/2026-11-22/queue-planning/2760-regular-to-activity-map.csv`. If the digest does not cover a step, stop with 'blocked by prerequisite' and say which step; never improvise.

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (routes in `_records_/2026-11-22/queue-planning/2700-routes.csv`). Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.

## Brief (planner, THE S1 CLAIM, EXPERIMENT 3: an INTERMEDIATE margin drag, approved by Steer A 12:08Z)

serves: PL-05

Records 1150 and 1158 (shop-claims): 250 px from the margin flung the page and over-scrolled it; 70 px moved it 0 px; card-start drags moved nothing. THE WHOLE PERMISSION, 8 steps, the LAST drag experiment on this page:
(1) The Weekly Pass tab ONLY (the G tab never; never Go on the check-in banner). ONE margin drag, 120 to 150 px UP, from (685, start) to (685, start minus 135) on the blank right margin, from the TOP of the page, a frame after; at most ONE correction drag the other way (20 to 40 px) if it moved too far. FOR EVERY DRAG write the start (x,y), the end, the distance in px, card or blank margin, and the page's measured MOVE in px (from a fixed feature in both frames: the first card's top edge or a text line), plus where the S1 Claim was before and after.
(2) S1 DRONE PARTS: tap the Claim ONCE only if its button reads a plain CLAIM with NO price, NO diamond or gem icon, NO 'Buy', 'Purchase', 'Unlock', 'Upgrade' or 'Activate', and it is fully inside the content, not at the window's bottom edge; a frame after.
(3) The Iron and Coin cards' green buttons: READ ONLY (labels, price line, gem icon, 'Purchased', 'Active' or 'Locked'); NOT PRESSED.
(4) A price, a diamond spend, a real-money line or an app store sheet: STOP, press nothing. No wheel test; no further drag.
May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Cost cap, stated: 0.40 USD.
