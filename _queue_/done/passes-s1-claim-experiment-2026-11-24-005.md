---
unit: passes-s1-claim-experiment-2026-11-24-005
regular: passes
activity: shop-claims
segment: 1
priority: 2
created_at: 2026-11-24T12:43:29Z
expires_at: 2026-11-24T13:50:00Z
planned_for:
not_before: 2026-11-24T12:44:00Z
window: experiment five a composed momentum free pan in one turn waiting for steer a held shut
est_minutes: 6
serves: PL-05
chain_id: s1-claim-experiment-2026-11-24
chain_seq: 5
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-24T12:48:41Z
lease_until: 2026-11-24T13:08:41Z
result:
  status: partial
  started_at: 2026-11-24T12:48:41Z
  finished_at: 2026-11-24T12:50:54Z
  duration_seconds: 133
  executor: operator
  summary: The first composed press was refused whole at 12:49:25.6Z ('batch_refused: nothing ran: action 2 was refused (malformed)': 'a wait inside a press needs a positive whole duration_ms': the model sent a whole-second wait of 0 instead of duration_ms); nothing ran, the page unmoved, no Claim tap; the events are lines 28 to 42 of the run's events.jsonl; drags 0; tram badge none
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/shop-claims/1248-queue-run.md and 1248-queue-run.csv; run 20261124T124841Z-948b80
  follow_up: retry once with every wait sent as duration_ms (300, 100) if Steer A allows; the S1 Claim stays unclaimed
  stats:
    target: one composed pan on the Weekly Pass page
    achieved: the batch was refused: nothing ran
    resources_gained: none
    points: 0
    costs: none spent; model 0.17 USD
    verified: yes
    run_id: 20261124T124841Z-948b80
    run_steps: 8
    actions_done: 7
    actions_refused: 0
    cost_usd: 0.17
    device_takeovers: 0
    blocker_category: f missing precondition (the composed batch was refused: a wait needs duration_ms)
    drags_tried: 0
    batch_calls: 15
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

## Brief (planner, THE S1 CLAIM, EXPERIMENT 5: a COMPOSED pan in ONE turn, approved by Steer A 12:43Z)

serves: PL-05

The drag action takes two points only (record 1235); cu (CU-64) composes a pan from mouse actions sent in ONE turn (several tool calls in one message). ONE pan, the LAST on this page, 8 steps:
(1) The Weekly Pass tab ONLY (never the G tab or Go), from the TOP of the page. A frame; then ALL IN ONE TURN: mouse_move (685,650); left_mouse_down; wait 300; mouse_move (685,615); wait 100; (685,580); wait 100; (685,545); wait 100; (685,510); wait 100; (685,475); wait 100; wait 300; left_mouse_up; a screenshot. NOTHING but mouse_move or wait between the down and the up; never a down without its up in that turn; never hold a button across turns. Cannot send them in ONE turn: STOP, 'composition unavailable', press nothing.
(2) In the record cite WHERE the action event can be read (composedFrom and the path with holdMs: file and line). Write the page's MOVE in px (S2 title y 531 before; S1 Claim y about 915 before and after). At most ONE correction pan the other way (about 40 px, three points).
(3) S1 DRONE PARTS: tap the Claim ONCE only if it reads a plain CLAIM with NO price, NO gem or diamond icon, NO Buy, Purchase, Unlock, Upgrade or Activate, fully inside the content, not at the bottom edge. Iron and Coin cards: READ ONLY.
(4) A price, diamond spend, real-money line or app store sheet: STOP. May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Cost cap, stated: 0.40 USD.
