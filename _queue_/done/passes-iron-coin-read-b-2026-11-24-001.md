---
unit: passes-iron-coin-read-b-2026-11-24-001
regular: passes
activity: shop-claims
segment: 2
priority: 2
created_at: 2026-11-24T13:30:47Z
expires_at: 2026-11-24T13:35:27Z
planned_for:
not_before: 2026-11-24T13:54:00Z
window: read the iron and coin pass cards up to four composed pans from the top held for steer a
est_minutes: 12
serves: PL-05
chain_id: iron-coin-read-b-2026-11-24
chain_seq: 1
attempts: 0
max_attempts: 3
claimed_by:
claimed_at:
lease_until:
result:
  status: expired
  started_at:
  finished_at: 2026-11-24T13:35:27Z
  duration_seconds: 
  executor:
  summary: retired by the planner: Steer A 13:33Z ruled no separate read-only unit; the Iron and Coin cards are pans 3 and 4 of the 14:57Z regular (sheet 3130)
  claimed: []
  claimed_count: 0
  evidence: 
  follow_up: none
  stats:
  stats_missing: [target, achieved, resources_gained, costs, verified]
  stats_warnings: []
---

# passes

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: PL-05

## Brief (definition pointer, from the roster)

This unit is the regular `passes`: Passes - weekly/monthly daily pickups and Free Supply in the shop. Its definition is the activity folder `_activities_/shop-claims/` (the folder is named for the activity, not the regular id): read its `rule-digest.md` first, then its `INDEX.md`. The map of every regular to its activity folder is `_records_/2026-11-22/queue-planning/2760-regular-to-activity-map.csv`. If the digest does not cover a step, stop with 'blocked by prerequisite' and say which step; never improvise.

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (routes in `_records_/2026-11-22/queue-planning/2700-routes.csv`). Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.

## Brief (planner, THE IRON AND COIN PASS CARDS: up to FOUR composed pans from the top, READ ONLY, WAITING FOR STEER A)

serves: PL-05

DO NOT RUN until the Coordinator names this unit after Steer A's yes; else close 'blocked by prerequisite: waiting for Steer A', press nothing.
Record `_records_/2026-11-22/shop-claims/1327-queue-run.md`: two composed pans (175 px, x=685) each moved the Weekly Pass page about 150 px; S1 and S2 read 'Already claimed today'; the EXP card showed a green Claim at y about 855; the Iron and Coin cards lie about TWO pans further. The page RESETS to the top each visit: start from the top. THE RECIPE (13:01Z), ALL IN ONE MESSAGE: mouse_move (685,650); left_mouse_down; wait 1 (second); mouse_move (685,475); wait 1 (second); left_mouse_up; a screenshot after the up; nothing else between the down and the up; if refused: write the text, STOP.
(1) The Weekly Pass tab ONLY (never the G tab or Go). A frame; up to FOUR pans by the recipe, a frame after each, ONE pan per message; STOP panning when both the Iron and the Coin card are in view; write each pan's MOVE.
(2) READ ONLY, press NOTHING: the EXP card's Claim (label, price line, gem or diamond icon), and the Iron and Coin cards: label, price line, gem or diamond icon, 'Purchased', 'Active', 'Locked' or 'Claim'. Diamonds are never spent.
(3) A price line, diamond spend, real-money line or app store sheet: STOP. Any other element: touch nothing, frame, stop, tell the Coordinator. May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Cost cap, stated: 0.60 USD.
