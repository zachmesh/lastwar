---
unit: passes-s1-claim-experiment-2026-11-24-007
regular: passes
activity: shop-claims
segment: 1
priority: 2
created_at: 2026-11-24T12:56:48Z
expires_at: 2026-11-24T13:55:00Z
planned_for:
not_before: 2026-11-24T12:59:00Z
window: experiment seven the two second composed pan waiting for steer a held shut
est_minutes: 6
serves: PL-05
chain_id: s1-claim-experiment-2026-11-24
chain_seq: 7
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-24T13:01:18Z
lease_until: 2026-11-24T13:21:18Z
result:
  status: done
  started_at: 2026-11-24T13:01:18Z
  finished_at: 2026-11-24T13:03:39Z
  duration_seconds: 141
  executor: operator
  summary: The first working pan: one composed drag (down, wait 1 s, move, wait 1 s, up) from (685,650) to (685,475) moved the Weekly Pass page 150 px; the S1 Claim came inside the content (y 915 to 765) and ONE tap paid Drone Parts x15; the S1 card reads Already claimed today; the event is lines 30 and 31 of the run's events.jsonl; the Iron and Coin cards never came into view; drags 1; tram badge none; diamonds 11,153
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/shop-claims/1301-queue-run.md and 1301-queue-run.csv; run 20261124T130118Z-dbbafb
  follow_up: the pan method works (175 px with 1 s dwells moved the page 150 px); the Iron and Coin pass cards below the EXP card are unread; the next daily S1 pickup after the 18:00 reset
  stats:
    target: claim the S1 Drone Parts Daily Pickup by a momentum-free pan
    achieved: claimed: Drone Parts x15
    resources_gained: none
    points: 0
    costs: none spent; model 0.172058 USD
    verified: yes
    run_id: 20261124T130118Z-dbbafb
    run_steps: 13
    actions_done: 22
    actions_refused: 0
    cost_usd: 0.172058
    device_takeovers: 0
    drags_tried: 1
    drags_cancelled: 0
    page_move_px: 150
    paid: Drone Parts x15
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

## Brief (planner, THE S1 CLAIM, EXPERIMENT 7: the TWO-SECOND composed pan, approved by Steer A 12:57Z)

serves: PL-05

Records 1248 and 1254: the model's `wait` takes WHOLE SECONDS only (`duration`, 1 to 300). ONE pan, the LAST today, 8 steps:
(1) The Weekly Pass tab ONLY (never the G tab or Go), from the TOP of the page. A frame; then ALL IN ONE MESSAGE: mouse_move (685,650); left_mouse_down; wait 1 (second); mouse_move (685,475); wait 1 (second); left_mouse_up; a screenshot AFTER the up. NOTHING else between the down and the up (about 2.1 s with the button down). If the batch is refused: write the refusal text and STOP, no second try.
(2) If ANY other element appears (tooltip, menu, highlight, dialog): touch nothing, take the frame; close with the back arrow or the dimmed area only if plainly a tooltip; else STOP and tell the Coordinator.
(3) Cite where the action event can be read (file and line). Write the page's MOVE in px (S2 title y 531 before; S1 Claim y about 915 before and after). At most ONE correction pan the other way, composed the same way (down, wait 1 s, a move of about 40 px, wait 1 s, up).
(4) S1 DRONE PARTS: tap the Claim ONCE only if its button reads a plain CLAIM with NO price, NO gem or diamond icon, NO Buy, Purchase, Unlock, Upgrade or Activate, fully inside the content, not at the bottom edge. Iron/Coin cards: READ ONLY. A price, diamond spend, real-money line or app store sheet: STOP. May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Cost cap, stated: 0.40 USD.
