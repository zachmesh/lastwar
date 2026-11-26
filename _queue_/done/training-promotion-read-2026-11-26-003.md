---
unit: training-promotion-read-2026-11-26-003
regular: training
activity: troop-training
segment: 1
priority: 1
created_at: 2026-11-26T16:05:32Z
expires_at: 2026-11-27T02:00:00Z
planned_for:
not_before: 2026-11-26T16:08:00Z
window: promotion press, one action only (steer a 16:04z)
est_minutes: 10
serves: PL-09
chain_id: promotion-read-2026-11-26
chain_seq: 3
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-26T16:13:52Z
lease_until: 2026-11-26T16:33:52Z
result:
  status: done
  started_at: 2026-11-26T16:13:52Z
  finished_at: 2026-11-26T16:19:39Z
  duration_seconds: 347
  executor: operator
  summary: Promotion press: with Lv.8 selected at the Lv.27 barracks, the green up-arrow pressed once opened UNIT UPGRADING Lv.8 to Lv.9 for 726 troops (887.6K food and 887.6K iron, no coin, 03:25:58, Power 1063 to 1352 per troop, about +209,800 in all) with Finish Now and Promote buttons; cancelled by its X because of the Finish Now button; HUD, Total Power 151,689,455 and troop counts unchanged at +10 s and +73 s; nothing promoted; drags 0. state_change: yes
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/troop-training/1613-queue-run.md and 1613-queue-run.csv; run 20261126T161353Z-5fb618
  state_change: yes
  follow_up: a Confirm of Promote at 887.6K food and 887.6K iron needs Steer A's word (the Finish Now button is a sibling, not a charge)
  stats:
    target: one promotion press at the Lv.27 barracks
    achieved: the press made; the dialog read and cancelled
    resources_gained: cost 887.6K food, 887.6K iron if confirmed
    points: 0
    costs: none spent; model 0.269367 USD
    verified: yes
    run_id: 20261126T161353Z-5fb618
    run_steps: 20
    actions_done: 8
    actions_refused: 0
    cost_usd: 0.269367
    device_takeovers: 0
    claims: 1
    promote_food_cost: 887.6K
    promote_iron_cost: 887.6K
    promote_time: 03:25:58
    power_gain_est: 209800
    tram_badge: not read
    drags_tried: 0
    rules_used: 1,2
  stats_missing: []
  stats_warnings: []
---

# training

Serves: PL-09

## Brief (definition pointer, from the roster)

One-off promotion press, NOT a training run. Definition `_activities_/troop-training/`; routes `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md`.

## Brief (planner, PROMOTION PRESS: Steer A 16:04Z, register H13, H15; plan reason: the 2.75M power lever)

serves: PL-09

ONE PROMOTION ACTION ONLY. Route: the `barracks` row of `_records_/2026-11-22/queue-planning/2700-routes.csv`, the Lv.27 barracks (tag 'Barracks Lv.27'): press the pistol ONCE (Train Units opens while the Lv.30 barracks is Full). BUTTON ROW HAZARD as the route says: verify the pistol glyph in a frame before the tap.
(1) Select Lv.8 (its green badge only selects the tier). BEFORE the press read in ONE frame: the HUD food, iron and coin; Total Power; the Lv.7, Lv.8, Lv.9 and Lv.10 troop counts; the barracks' queue row; that the arrow beside the cost row (about (572,684)) is GREEN; the quantity (default 726, max 726).
(2) Press the GREEN up-arrow beside the cost row ONCE (Steer A's exception for this arrow only: it is otherwise never pressed on a building tag). Do NOT touch Train, Finish Now or the quantity.
(3) If a dialog with a cost and a Confirm opens: read the rows BY TEXT; Confirm ONCE only if ALL hold: food at most 3.3M, iron at most 3.3M, coin at most 1.0M, no gem, diamond or price icon and no Finish Now; else CANCEL and write the rows.
(4) If it promotes at once, or after a Confirm: NO second press. Read the same frame at +10 s and +60 s: the HUD, Total Power, the four troop counts and the queue row. A drop of about 772K in Total Power right after is the promotion in progress (726 x 1,063), not a loss. STOP at once if the HUD food or iron falls by more than 3.3M each. Close by the X.
CLOSE by `_records_/2026-11-22/queue-planning/3170-closing-rule-done-and-partial.md`: DONE for the press made or the dialog cancelled with its rows read (`--state-change yes` if pressed, a `state_read:` line); else PARTIAL.
FRONT: if `lsappinfo front` is not LastWar: record, run the standing front script, record; still not: stop, release, tell the Coordinator.
May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Cost cap, stated: 0.80 USD.
