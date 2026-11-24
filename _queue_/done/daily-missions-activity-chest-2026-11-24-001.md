---
unit: daily-missions-activity-chest-2026-11-24-001
regular: daily-missions
activity: daily-missions
segment: 2
priority: 2
created_at: 2026-11-24T13:18:10Z
expires_at: 2026-11-24T13:55:00Z
planned_for:
not_before: 2026-11-24T13:18:00Z
window: claim the highlighted 120 point activity chest under the standing chest rules
est_minutes: 4
serves: upkeep
chain_id: activity-chest-2026-11-24
chain_seq: 1
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-24T13:30:28Z
lease_until: 2026-11-24T13:50:28Z
result:
  status: done
  started_at: 2026-11-24T13:30:28Z
  finished_at: 2026-11-24T13:31:58Z
  duration_seconds: 90
  executor: operator
  summary: The 120-point activity chest opened once at 13:30:56.8Z: gear x2, red gem item x20 (diamonds 11,153 to 11,173), firework x1, metal-crate chest x6, gold chest x6, crystal x1.2K, 5-minute speed-up x2; no Use, choice or price; the paid chests unopened; 130 points; next milestone 160; tram badge none; drags 0
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/daily-missions/1330-queue-run.md and 1330-queue-run.csv; run 20261124T133029Z-4a6e79
  follow_up: the 160 chest needs 30 more points (the Go rows); the metal-crate and gold chests x6 each join the stock unopened
  stats:
    target: open the highlighted 120-point activity chest once
    achieved: opened, seven items paid
    resources_gained: none
    points: 0
    costs: none spent; model 0.087204 USD
    verified: yes
    run_id: 20261124T133029Z-4a6e79
    run_steps: 7
    actions_done: 6
    actions_refused: 0
    cost_usd: 0.087204
    device_takeovers: 0
    chest: 120
    activity_points: 130
    diamonds_after: 11173
    drags_tried: 0
    tram_badge: none
    rules_used: 1,2
  stats_missing: []
  stats_warnings: []
---

# daily-missions

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: upkeep

## Brief (definition pointer, from the roster)

This unit is the regular `daily-missions`: Daily missions - claim completed Mission tasks one by one, re-checking after each, and claim the activity chests at their thresholds. Its definition is the activity folder `_activities_/daily-missions/` (the folder is named for the activity, not the regular id): read its `rule-digest.md` first, then its `INDEX.md`. The map of every regular to its activity folder is `_records_/2026-11-22/queue-planning/2760-regular-to-activity-map.csv`. If the digest does not cover a step, stop with 'blocked by prerequisite' and say which step; never improvise.

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (routes in `_records_/2026-11-22/queue-planning/2700-routes.csv`). Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.

## Brief (planner, THE ACTIVITY CHEST: claim the highlighted chest, approved by Steer A 13:22Z)

serves: upkeep

Record `_records_/2026-11-22/daily-missions/1315-queue-run.md`: the two Claim rows were claimed at 13:16:09Z, the activity points went 90 to 130, and the 120-point chest looked HIGHLIGHTED, not opened. 5 steps, no drag, no pan.
(1) Open the Mission panel (title verified by a frame); in a fresh frame read the activity points and which chests of the ladder (20/40/60/80/100/120, then 160 and 200 ahead) are highlighted, opened or locked. READ THE HIGHLIGHTED CHEST'S NAME AND QUANTITY IN A FRAME BEFORE ANY TAP.
(2) Tap the highlighted chest ONCE (a free points milestone reward). Read what it paid (items, speed-ups by kind: tech, construction, general; chests; resources) and the points state after. Any chest it pays (SR, SSR, UR) is NOT opened here: it joins the stock.
(3) NEVER a diamond or gem line, a purchase or an 'upgrade the chest' surface; a dialog with a price: STOP. Never a Resource Choice Chest choice, never Finish Now.
(4) READ the next milestone (160, 200: its points, and the day's maximum if the card shows it); no extra navigation. Rows that remain 'Go' are not pressed; no paid-purchase row, no Mega, Buy or Unlock.
(5) Any other dialog or element: touch nothing, frame, stop, tell the Coordinator. Verify each HUD icon by its label before the tap. May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Cost cap, stated: 0.30 USD.
