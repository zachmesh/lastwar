---
unit: passes-iron-coin-read-2026-11-24-001
regular: passes
activity: shop-claims
segment: 2
priority: 2
created_at: 2026-11-24T13:07:37Z
expires_at: 2026-11-24T13:56:00Z
planned_for:
not_before: 2026-11-24T13:25:00Z
window: one more pan on the weekly pass page to read the iron and coin cards read only held for steer a
est_minutes: 6
serves: PL-05
chain_id: iron-coin-read-2026-11-24
chain_seq: 1
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-24T13:26:46Z
lease_until: 2026-11-24T13:46:46Z
result:
  status: partial
  started_at: 2026-11-24T13:26:46Z
  finished_at: 2026-11-24T13:28:57Z
  duration_seconds: 131
  executor: operator
  summary: Two composed pans (175 px each, both accepted) moved the Weekly Pass page about 150 px each; the Iron and Coin cards were never in view (unread); S1 and S2 'Already claimed today'; the EXP Weekly Pass card shows a green Claim at y about 855 (not pressed); events.jsonl lines 36 and 48; drags 2; tram badge none; diamonds 11,153
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/shop-claims/1327-queue-run.md and 1327-queue-run.csv; run 20261124T132646Z-9ad644
  follow_up: the EXP Weekly Pass card's green Claim (about y 855 after two pans) needs a plain-Claim check; the Iron and Coin cards need about two more pans (a separate unit)
  stats:
    target: read the Iron and Coin pass cards' labels, prices, gem icons and states
    achieved: not reached in two pans
    resources_gained: none
    points: 0
    costs: none spent; model 0.16561 USD
    verified: yes
    run_id: 20261124T132646Z-9ad644
    run_steps: 12
    actions_done: 35
    actions_refused: 0
    cost_usd: 0.16561
    device_takeovers: 0
    blocker_category: f missing precondition (the Iron and Coin cards were not in view after two pans)
    drags_tried: 2
    drags_cancelled: 0
    page_move_px: 150
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

## Brief (planner, THE IRON AND COIN PASS CARDS: ONE more composed pan, READ ONLY, approved by Steer A 13:11Z)

serves: PL-05

The S1 pan of 13:01Z moved the Weekly Pass page 150 px; the Iron and Coin cards' green buttons lie below S1. THE RECIPE (13:01Z), ALL IN ONE MESSAGE: mouse_move (685,650); left_mouse_down; wait 1 (second); mouse_move (685,475); wait 1 (second); left_mouse_up; a screenshot after the up; nothing else between the down and the up; if refused: write the refusal text, STOP.
(1) The Weekly Pass tab ONLY (never the G tab or Go). A frame; ONE pan by the recipe; a frame after; write the page's MOVE in px (the S1 title y before and after). At most ONE correction pan the same way.
(2) READ ONLY, press NOTHING: each card's label, price line, gem or diamond icon, and whether it reads 'Purchased', 'Active', 'Locked' or 'Claim'. Diamonds are never spent.
(3) A price line, diamond spend, real-money line or app store sheet: STOP. Any other element: touch nothing, frame, stop, tell the Coordinator. May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Cost cap, stated: 0.30 USD.
