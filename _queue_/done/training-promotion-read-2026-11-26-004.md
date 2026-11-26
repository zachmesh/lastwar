---
unit: training-promotion-read-2026-11-26-004
regular: training
activity: troop-training
segment: 1
priority: 1
created_at: 2026-11-26T16:28:32Z
expires_at: 2026-11-27T02:00:00Z
planned_for:
not_before: 2026-11-26T16:45:00Z
window: promote lv.8 to lv.9, one press (steer a 16:27z)
est_minutes: 10
serves: PL-09
chain_id: promotion-read-2026-11-26
chain_seq: 4
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-26T16:45:41Z
lease_until: 2026-11-26T17:05:41Z
result:
  status: done
  started_at: 2026-11-26T16:45:41Z
  finished_at: 2026-11-26T16:49:20Z
  duration_seconds: 219
  executor: operator
  summary: Promotion confirmed: at the Lv.27 barracks with Lv.8 selected, the green arrow opened UNIT UPGRADING Lv.8 to Lv.9 (726 troops, 887.6K food and 887.6K iron, no coin, 03:25:58); the blue Promote pressed once (Finish Now never): food 49.4M to 48.5M, iron 645.7M to 644.9M, coin 13.3M; Total Power 151,689,455 to 150,917,717 (down 771,738: the promotion in progress), steady to +74 s; a clock bubble over the barracks; drags 0. state_change: yes
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/troop-training/1646-queue-run.md and 1646-queue-run.csv; run 20261126T164542Z-227c12
  state_change: yes
  follow_up: the promotion finishes in about 3 h 26 min (about 20:13Z): Total Power should return and rise about 209,800 over the Lv.8 level; a later read of the Lv.27 barracks' Train Units shows the troop counts
  stats:
    target: one promotion Lv.8 to Lv.9 at the Lv.27 barracks
    achieved: 726 troops promoting
    resources_gained: food 887.6K, iron 887.6K spent
    points: 0
    costs: none spent; model 0.250683 USD
    verified: yes
    run_id: 20261126T164542Z-227c12
    run_steps: 18
    actions_done: 7
    actions_refused: 0
    cost_usd: 0.250683
    device_takeovers: 0
    claims: 1
    promote_food_cost: 887.6K
    promote_iron_cost: 887.6K
    total_power_before: 151689455
    total_power_after: 150917717
    power_drop: 771738
    tram_badge: not read
    drags_tried: 0
    rules_used: 1,2
  stats_missing: []
  stats_warnings: []
---

# training

Serves: PL-09

## Brief (definition pointer, from the roster)

One-off promotion, NOT a training run. Definition `_activities_/troop-training/`; routes `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md`.

## Brief (planner, PROMOTE Lv.8 TO Lv.9: Steer A 16:27Z 'confirm approved'; register H13, H15; plan reason: the 2.75M power lever)

serves: PL-09

ONE PROMOTION ONLY. Route: the `barracks` row of `_records_/2026-11-22/queue-planning/2700-routes.csv`, the Lv.27 barracks (tag 'Barracks Lv.27'): press the pistol ONCE (Train Units opens while the Lv.30 barracks is Full). BUTTON ROW HAZARD as the route says: verify the pistol glyph in a frame before the tap.
(1) Select Lv.8 (its green badge only selects the tier). Do NOT touch the quantity (726 expected). BEFORE the press read in ONE frame: the HUD food, iron and coin; Total Power; the Lv.7, Lv.8, Lv.9 and Lv.10 troop counts; the barracks' queue row.
(2) Press the green up-arrow beside the cost row ONCE (Steer A's exception for this arrow only; it is otherwise never pressed on a building tag). The dialog 'Unit Upgrading' Lv.8 to Lv.9 opens: read it BY TEXT (expected 887.6K food and 887.6K iron, no coin, no gem or price icon, time about 3:26). It carries TWO buttons: CONFIRM ONLY THE Promote BUTTON ONCE, and NEVER PRESS Finish Now (the sibling button on the same dialog; its presence is not a reason to cancel). Cancel by the X only if a row shows a coin, gem or diamond price or a food or iron cost above 1.0M.
(3) After the Promote read the same frame at +10 s and +60 s: the HUD, Total Power, the four troop counts and the queue row. A drop of about 772K in Total Power right after is the promotion in progress, not a loss. STOP at once if the HUD food or iron falls by more than 1.0M each. NO second press. Close by the X.
CLOSE by `_records_/2026-11-22/queue-planning/3170-closing-rule-done-and-partial.md`: DONE for the Promote pressed or the dialog cancelled with its rows read (`--state-change yes` if pressed, a `state_read:` line); else PARTIAL.
FRONT: if `lsappinfo front` is not LastWar: record, run the standing front script, record; still not: stop, release, tell the Coordinator.
May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Cost cap, stated: 0.80 USD.
