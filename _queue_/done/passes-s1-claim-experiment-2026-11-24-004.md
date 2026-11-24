---
unit: passes-s1-claim-experiment-2026-11-24-004
regular: passes
activity: shop-claims
segment: 1
priority: 2
created_at: 2026-11-24T12:26:39Z
expires_at: 2026-11-24T13:34:00Z
planned_for:
not_before: 2026-11-24T12:32:00Z
window: experiment four a momentum free pan waiting for steer a held shut
est_minutes: 6
serves: PL-05
chain_id: s1-claim-experiment-2026-11-24
chain_seq: 4
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-24T12:35:24Z
lease_until: 2026-11-24T12:55:24Z
result:
  status: partial
  started_at: 2026-11-24T12:35:24Z
  finished_at: 2026-11-24T12:37:07Z
  duration_seconds: 103
  executor: operator
  summary: Stopped before the pan: the model's drag action accepts only start_coordinate and coordinate plus an optional modifier key, with no multi-point path or per-point holdMs (the mouse-down, mouse-move and mouse-up actions carry no hold); no drag, no S1 Claim tap (clipped), no Iron or Coin read; the shop closed with its back arrow; drags 0; tram badge none
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/shop-claims/1235-queue-run.md and 1235-queue-run.csv; run 20261124T123525Z-b4946f
  follow_up: a pan built from mouse-down, mouse-move steps, a wait and mouse-up is untried; the S1 Claim stays unclaimed
  stats:
    target: one momentum-free six-point pan on the Weekly Pass page
    achieved: not possible with the model's drag action
    resources_gained: none
    points: 0
    costs: none spent; model 0.121 USD
    verified: yes
    run_id: 20261124T123525Z-b4946f
    run_steps: 8
    actions_done: 9
    actions_refused: 0
    cost_usd: 0.121
    device_takeovers: 0
    blocker_category: f missing precondition (the drag action takes no multi-point path or holdMs)
    drags_tried: 0
    pan_count: 0
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

## Brief (planner, THE S1 CLAIM, EXPERIMENT 4: a momentum-free PAN, approved by Steer A 12:31Z)

serves: PL-05

cu (12:31Z): a drag is sent as moves at most 25 pt apart about 8 ms apart, so 250 px is a FLICK; the fling is decided by the speed of the last moves before the release. ONE PAN, the LAST pan experiment on this page, 8 steps:
(1) The Weekly Pass tab ONLY (never the G tab; never Go on the banner). ONE drag from the TOP of the page with the path [(685,650,holdMs 50),(685,615,50),(685,580,50),(685,545,50),(685,510,50),(685,475,holdMs 300)] (about 175 px, the first point on the blank right margin), a frame before and after. Write the start, end, distance, and the page's measured MOVE in px from a fixed feature (the S2 title y 531 before; the S1 Claim y about 915 before and after). At most ONE correction pan the other way: a three-point path of about 40 px with the same dwell.
(2) S1 DRONE PARTS: tap the Claim ONCE only if its button reads a plain CLAIM with NO price, NO gem or diamond icon, NO 'Buy', 'Purchase', 'Unlock', 'Upgrade' or 'Activate', fully inside the content, not at the window's bottom edge; a frame after.
(3) The Iron and Coin cards' green buttons: READ ONLY (labels, price line, gem icon, 'Purchased', 'Active' or 'Locked'); never pressed.
(4) A price line, a diamond spend, a real-money line or an app store sheet: STOP, press nothing. No wheel test. May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Cost cap, stated: 0.40 USD.
