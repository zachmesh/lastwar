---
unit: training-promotion-read-2026-11-26-002
regular: training
activity: troop-training
segment: 1
priority: 1
created_at: 2026-11-26T15:53:56Z
expires_at: 2026-11-26T15:59:25Z
planned_for:
not_before: 2026-11-26T16:02:00Z
window: promotion read part two, at most two taps (steer a 15:53z)
est_minutes: 8
serves: PL-09
chain_id: promotion-read-2026-11-26
chain_seq: 2
attempts: 0
max_attempts: 3
claimed_by:
claimed_at:
lease_until:
result:
  status: expired
  started_at:
  finished_at: 2026-11-26T15:59:25Z
  duration_seconds: 
  executor:
  summary: retired by the planner: the operator ran Steer A's two taps as part two (troop-training/1554) before this unit; a part three waits for Steer A's ruling on the green arrow
  claimed: []
  claimed_count: 0
  evidence: 
  follow_up: none
  stats:
  stats_missing: [target, achieved, resources_gained, costs, verified]
  stats_warnings: []
---

# training

Serves: PL-09

## Brief (definition pointer, from the roster)

One-off promotion read, NOT a training run. Definition `_activities_/troop-training/`; routes `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md`.

## Brief (planner, PROMOTION READ PART TWO: Steer A 15:53Z, the Researcher's order 15:54Z, register H13, H14, H15; plan reason: the 2.75M power lever)

serves: PL-09

READ ONLY: AT MOST TWO taps after the panel opens. NEVER Train, Finish Now, any Confirm, or any button with a gem, diamond or price icon.
Route: the `barracks` row of `_records_/2026-11-22/queue-planning/2700-routes.csv`, the Lv.27 barracks only (tag 'Barracks Lv.27', read in a fresh frame). BUTTON ROW HAZARD as the route says: verify the pistol glyph in a frame before the tap (a stray tap once opened Building Details and another the world map: close by the back arrow or X, and write it). Press the pistol ONCE. If it only toasts 'Drill Ground Full', write it and STOP. If the Train Units panel opens, write the troop row (counts by level, which is selected, any green badge), the QUANTITY field (default and max: DO NOT change it) and the cost row.
TAP 1: the green up-arrow badge on the Lv.8 troop row (Steer A's exception: the green up arrow is otherwise never pressed on a building tag). On the training panel it only selects the tier (record growth/2357-troop-read.md). Read BY TEXT: the troop row, the arrow beside the cost row (green or grey), the cost row and the QUANTITY field (default and max). TAP 2 (the only other tap): the arrow beside the cost row (about (572,684)), green or grey. Read what opens BY TEXT. If it is only a toast or nothing, write it and STOP.
If a dialog with a cost and a Confirm opens: CANCEL and write every row: the troops promoted from which level to which, the food, iron and coin cost, the power gained, the time. Close anything else by the X. Write the layout for the route card.
Write the HUD food, iron and coin before and after: they must not move.
CLOSE by `_records_/2026-11-22/queue-planning/3170-closing-rule-done-and-partial.md`: DONE for the panels read (`--state-change no`, a `state_read:` line); else PARTIAL.
FRONT: if `lsappinfo front` is not LastWar: record, run the standing front script, record; still not: stop, release, tell the Coordinator.
May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Cost cap, stated: 0.60 USD.
