---
unit: passes-s1-claim-experiment-2026-11-24-006
regular: passes
activity: shop-claims
segment: 1
priority: 2
created_at: 2026-11-24T12:53:29Z
expires_at: 2026-11-24T13:50:00Z
planned_for:
not_before: 2026-11-24T12:53:00Z
window: experiment six the composed pan again with waits as duration_ms
est_minutes: 6
serves: PL-05
chain_id: s1-claim-experiment-2026-11-24
chain_seq: 6
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-24T12:53:55Z
lease_until: 2026-11-24T13:13:55Z
result:
  status: partial
  started_at: 2026-11-24T12:53:55Z
  finished_at: 2026-11-24T12:55:23Z
  duration_seconds: 88
  executor: operator
  summary: Stopped before the batch: the model's wait action takes only whole seconds (duration 1 to 300) and cannot send duration_ms 300 or 100; it can send mouse_move, left_mouse_down, left_mouse_up, left_click_drag, scroll and wait in whole seconds; no batch, no pan, no Claim tap; shop closed; drags 0; tram badge none
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/shop-claims/1254-queue-run.md and 1254-queue-run.csv; run 20261124T125355Z-fac89f
  follow_up: ask Steer A whether the composed pan may use whole-second waits (about 8 s with the button down) or the harness must expose duration_ms to the model; the S1 Claim stays unclaimed
  stats:
    target: one composed pan with duration_ms waits
    achieved: not sendable by the model
    resources_gained: none
    points: 0
    costs: none spent; model 0.093335 USD
    verified: yes
    run_id: 20261124T125355Z-fac89f
    run_steps: 7
    actions_done: 9
    actions_refused: 0
    cost_usd: 0.093335
    device_takeovers: 0
    blocker_category: f missing precondition (the model's wait action takes whole seconds only: no duration_ms)
    drags_tried: 0
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

## Brief (planner, THE S1 CLAIM, EXPERIMENT 6: the COMPOSED pan again, waits as duration_ms, Steer A 12:43Z)

serves: PL-05

Experiment 5 (record 1248) was refused whole, nothing ran: whole-second waits are refused ('a wait inside a press needs a positive whole duration_ms'). THE FIX: every wait is a wait action with duration_ms 300 after the down, 100 after each move, 300 before the up. ONE pan, the LAST on this page, 8 steps:
(1) The Weekly Pass tab ONLY (never the G tab or Go), from the TOP of the page. A frame; then ALL 15 CALLS IN ONE MESSAGE: mouse_move (685,650); left_mouse_down; wait duration_ms 300; mouse_move (685,615); wait 100; (685,580); wait 100; (685,545); wait 100; (685,510); wait 100; (685,475); wait 100; wait duration_ms 300; left_mouse_up; a screenshot. NOTHING but mouse_move or wait between the down and the up; never hold a button across turns. If refused: write the refusal text; retry at most ONCE with corrected waits.
(2) In the record cite WHERE the action event can be read (composedFrom, path, holdMs: file and line). Write the page's MOVE in px (S2 title y 531 before; S1 Claim y about 915 before and after). At most ONE correction pan back (about 40 px).
(3) S1 DRONE PARTS: tap the Claim ONCE only if its button reads a plain CLAIM with NO price, NO gem or diamond icon, NO Buy, Purchase, Unlock, Upgrade or Activate, fully inside the content, not at the bottom edge. Iron/Coin cards: READ ONLY.
(4) A price, diamond spend, real-money line or app store sheet: STOP. May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Cost cap, stated: 0.40 USD.
