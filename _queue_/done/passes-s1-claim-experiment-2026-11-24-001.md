---
unit: passes-s1-claim-experiment-2026-11-24-001
regular: passes
activity: shop-claims
segment: 1
priority: 2
created_at: 2026-11-24T11:47:16Z
expires_at: 2026-11-24T13:55:00Z
planned_for:
not_before: 2026-11-24T11:50:00Z
window: one experiment page down key for the clipped s1 drone parts claim
est_minutes: 6
serves: PL-05
chain_id: s1-claim-experiment-2026-11-24
chain_seq: 1
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-24T11:50:25Z
lease_until: 2026-11-24T12:10:25Z
result:
  status: partial
  started_at: 2026-11-24T11:50:25Z
  finished_at: 2026-11-24T11:52:23Z
  duration_seconds: 118
  executor: operator
  summary: One drag from the blank right margin (685,650 to 685,400) moved the Weekly Pass page a long way (S1 scrolled out of view, the Iron and Coin pass cards with their own Claim buttons came into view); one Page Down key moved nothing; the S1 Claim was never inside the page, no tap: blocked by route: Claim clipped; drags 1, keys 1; diamonds 11,153; tram badge none
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/shop-claims/1150-queue-run.md and 1150-queue-run.csv; run 20261124T115025Z-e01068
  follow_up: a short drag (60 to 80 px) from (685,650) may bring the S1 Claim into view; the Iron and Coin pass cards' Claim buttons unread
  stats:
    target: claim the S1 Drone Parts Daily Pickup by one drag and one Page Down key
    achieved: the page moved by the margin drag; the key did nothing; S1 not claimed
    resources_gained: none
    points: 0
    costs: none spent; model 0.15093 USD
    verified: yes
    run_id: 20261124T115025Z-e01068
    run_steps: 12
    actions_done: 16
    actions_refused: 0
    cost_usd: 0.15093
    device_takeovers: 0
    blocker_category: f missing precondition (blocked by route: Claim clipped; the drag over-scrolled and Page Down moved nothing)
    drags_tried: 1
    drags_cancelled: 0
    keys: 1
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

## Brief (planner, THE S1 DRONE PARTS CLAIM: ONE experiment, Steer A's option (b), 11:22Z and 11:45Z)

serves: PL-05

The S1 Drone Parts Claim (the shop's Weekly Pass tab) is CLIPPED at the page bottom: seven failed taps since 04:43Z; 13 scrolls in 9 runs moved nothing. ONE EXPERIMENT, 8 steps, NO second try. Reach the Weekly Pass tab by the shop-claims route; read that tab ONLY; the G tab (Gold Brick Mall) is NEVER tapped; NEVER click Go on the check-in banner (it opens the web store).
ONE drag from a blank margin, then ONE Page Down key (the key action), and a frame after. If the page MOVED: record 'Page Down works on the shop page' and tap the Claim ONCE (the claim then returns to the regular passes unit with that route). If NOT: close 'blocked by route: Claim clipped' with NO tap at the window's bottom edge (the Claim at about (572,913) is at the edge); no hold-drag; the claim stays out until a phased scroll exists. May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Safe tap: the bare spot (310,660), not (400,640) after a camera shift (WORLD then BASE first). Verify each HUD icon by its label or glyph before the tap.
Cost cap, stated: 0.40 USD.
