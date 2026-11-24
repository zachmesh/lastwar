---
unit: passes-coin-claim-2026-11-24-001
regular: passes
activity: shop-claims
segment: 2
priority: 2
created_at: 2026-11-24T15:11:48Z
expires_at: 2026-11-24T17:15:00Z
planned_for:
not_before: 2026-11-24T15:30:00Z
window: one off five pans from the top to reach the coin card held for steer a
est_minutes: 12
serves: PL-05
chain_id: coin-claim-2026-11-24
chain_seq: 1
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-24T15:30:07Z
lease_until: 2026-11-24T15:50:07Z
result:
  status: done
  started_at: 2026-11-24T15:30:07Z
  finished_at: 2026-11-24T15:33:38Z
  duration_seconds: 211
  executor: operator
  summary: Five composed pans (150 px each, none refused) reached the Coin Weekly Pass card; S1, EXP and Iron already claimed today; the Coin Claim tapped once paid a gold coin chest x3; the four Weekly Pass pickups are all done today; diamonds 11,173; tram badge none
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/shop-claims/1530-queue-run.md and 1530-queue-run.csv; run 20261124T153153Z-fb7cb9
  follow_up: the Weekly Pass pickups reset after 18:00 server time; five pans from the top reach the Coin card
  stats:
    target: claim the Coin Weekly Pass pickup by the fifth pan
    achieved: claimed: a gold coin chest x3
    resources_gained: none
    points: 0
    costs: none spent; model 0.295956 USD
    verified: yes
    run_id: 20261124T153153Z-fb7cb9
    run_steps: 22
    actions_done: 55
    actions_refused: 0
    cost_usd: 0.295956
    device_takeovers: 0
    claims: 1
    pans: 5
    tram_badge: none
    drags_tried: 5
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

## Brief (planner, THE COIN CARD: ONE read-and-claim with FIVE pans, WAITING FOR STEER A)

serves: PL-05

Steer A approved this unit 15:20Z: run it in the gap before cycle B2, ending by 17:15Z (before the Oil Well hand-off at 17:28Z).
Record `_records_/2026-11-22/shop-claims/1306-queue-run.md`: four composed pans (about 150 px each, none refused) reached S1, EXP and Iron; EXP and Iron paid chests x3 at 15:07Z; the Coin card showed only its title after pan 4. Do `_records_/2026-11-22/queue-planning/3130-weekly-pass-page-sequence.md` with ONE CHANGE for this unit: FIVE composed pans from the top (S1, EXP, Iron, the Coin title, the Coin Claim in view), each its own message with a frame after it, at most ONE correction pan, no sixth pan; the cap is 12 minutes.
(1) Weekly Pass tab ONLY (never the G tab or Go). S1, EXP and Iron are expected 'Already claimed today': read each, tap nothing on a card that reads it.
(2) The Coin card: READ its label, price line, gem icon and state BEFORE any tap; tap its Claim ONCE only if a plain CLAIM, no price, gem or diamond icon, no Buy, Purchase, Unlock, Upgrade or Activate, an OWNED state (a Remaining time or Active), fully inside the content, not at the bottom edge. Else record label and state and press nothing.
(3) Record each pan's measured move, the Coin claim's reward and whether it was already claimed on arrival. A price line, diamond spend, real-money line or app store sheet: STOP. Any other element: touch nothing, frame, stop, tell the Coordinator. May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Cost cap, stated: 0.60 USD.
