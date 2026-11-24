---
unit: passes-s1-claim-experiment-2026-11-24-002
regular: passes
activity: shop-claims
segment: 1
priority: 2
created_at: 2026-11-24T11:54:49Z
expires_at: 2026-11-24T12:59:00Z
planned_for:
not_before: 2026-11-24T11:57:00Z
window: experiment two a short margin drag waiting for steer a held shut
est_minutes: 6
serves: PL-05
chain_id: s1-claim-experiment-2026-11-24
chain_seq: 2
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-24T11:58:42Z
lease_until: 2026-11-24T12:18:42Z
result:
  status: partial
  started_at: 2026-11-24T11:58:42Z
  finished_at: 2026-11-24T12:00:13Z
  duration_seconds: 91
  executor: operator
  summary: One short margin drag (70 px up from (685,330)) moved the Weekly Pass page 0 px; the S1 Claim stayed clipped and was not pressed: blocked by route: Claim clipped; the Iron and Coin cards never came into view; the 250 px drag at 11:51Z over-scrolled, so the drag has a distance threshold; drags 1; diamonds 11,153; tram badge none
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/shop-claims/1158-queue-run.md and 1158-queue-run.csv; run 20261124T115843Z-936891
  follow_up: an intermediate margin drag (about 120 to 150 px) from the blank right margin is the next experiment; the S1 pickup stays unclaimed
  stats:
    target: bring the S1 Claim inside the content by a 60 to 80 px margin drag and claim it once
    achieved: the 70 px drag moved nothing
    resources_gained: none
    points: 0
    costs: none spent; model 0.128181 USD
    verified: yes
    run_id: 20261124T115843Z-936891
    run_steps: 10
    actions_done: 13
    actions_refused: 0
    cost_usd: 0.128181
    device_takeovers: 0
    blocker_category: f missing precondition (blocked by route: Claim clipped; the 70 px drag moved 0 px)
    drags_tried: 1
    drags_cancelled: 0
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

## Brief (planner, THE S1 CLAIM, EXPERIMENT 2: a SHORT margin drag, approved by Steer A 11:57Z)

serves: PL-05

Record `_records_/2026-11-22/shop-claims/1150-queue-run.md`: Page Down did nothing; a drag from the blank right margin moved the page and over-scrolled; three drags that started on a card moved nothing. THE WHOLE PERMISSION, 8 steps:
(1) The Weekly Pass tab ONLY (the G tab never; never Go on the check-in banner). ONE short margin drag, 60 to 80 px UP, starting at x=685 on the blank right margin, from the TOP of the page, a frame before and after; at most ONE correction drag the other way (20 to 40 px) if it over-scrolled.
(2) S1 DRONE PARTS: tap the Claim ONCE only if its button reads a plain CLAIM with NO price, NO diamond or gem icon, NO 'Buy', 'Purchase', 'Unlock', 'Upgrade' or 'Activate', and it is fully inside the content, not at the window's bottom edge; a frame after.
(3) The Iron and Coin cards' green buttons at (573,642) and (573,879): READ ONLY: labels, any price line, any gem icon, and whether the card reads 'Purchased', 'Active' or 'Locked'; NOT PRESSED.
(4) A dialog with a price, a diamond count to spend, a real-money line or an app store sheet: STOP, press nothing. Diamonds (11,153 on screen) are never spent. No wheel test here.
Verify each HUD icon by its label or glyph before the tap. May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Cost cap, stated: 0.40 USD.
