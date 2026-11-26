---
unit: training-promotion-batch-2026-11-26-001
regular: training
activity: troop-training
segment: 1
priority: 1
created_at: 2026-11-26T16:50:36Z
expires_at: 2026-11-27T00:40:00Z
planned_for:
not_before: 2026-11-26T20:16:00Z
window: promotion batch 2 after the 20:13z completion (steer a 16:27z standing)
est_minutes: 15
serves: PL-09
chain_id: promotion-batch-2026-11-26
chain_seq: 1
attempts: 0
max_attempts: 3
claimed_by:
claimed_at:
lease_until:
---

# training

Serves: PL-09

## Brief (definition pointer, from the roster)

One-off promotion batch, NOT a training run. Definition `_activities_/troop-training/`; routes `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md`.

## Brief (planner, PROMOTION BATCH 2 AND THE CONVEYOR: Steer A 17:39Z and 17:51Z; plan reason: the room)

serves: PL-09

ONE PROMOTION, then the collects. Route: the `barracks` row of `_records_/2026-11-22/queue-planning/2700-routes.csv`; the Lv.27 barracks (tag read first): the pistol ONCE (verify the pistol glyph first).
FIRST read in ONE frame: Total Power, the Lv.7, Lv.8, Lv.9 and Lv.10 counts, the HUD food, iron and coin, the queue row. Batch 1's RETURN: Lv.9 3,330 = FITTED, 2,604 = BLOCKED: write which. START BATCH 2 EITHER WAY. Conditions: the queue row IDLE, food at least 35M, iron at least 150M, Lv.8 still has troops: else promote NOTHING and STOP (no start, no collects).
Select Lv.8, do NOT touch the quantity (726 expected, else write the max), press the green up-arrow beside the cost row ONCE (his exception, this arrow only). The dialog 'Unit Upgrading' has TWO buttons: CONFIRM ONLY THE Promote BUTTON ONCE, NEVER PRESS Finish Now (its presence is not a reason to cancel). Cancel by the X only on a coin, gem or diamond price or a food or iron cost above 1.0M. Read +10 s and +60 s frames; STOP if food or iron falls by more than 1.0M each. NO second Promote.
THE CONVEYOR: plain collects, ONE press each, the tag read first, in this order: (i) the Lv.30 barracks pistol (67 Lv.10); (ii) the Hospital's green Collect (the 'Hospital Lv.25' tag, the orange middle button, then Collect; write its free room before and after); (iii) the Lv.27 tent's pistol (batch 1's 726 Lv.9 if blocked); (iv) the Lv.24 pistol (248 Lv.8); (v) the Lv.20 pistol (110). Before and after each step write Total Power and the Lv.7, Lv.8, Lv.9 and Lv.10 counts. STOP when a toast says 'Drill Ground Full: Unable to add more units.' NEVER Train, Heal or Finish Now.
CLOSE by `_records_/2026-11-22/queue-planning/3170-closing-rule-done-and-partial.md`: DONE for the Promote pressed or a verified nothing-to-do (`--state-change yes` if pressed, a `state_read:` line); else PARTIAL.
FRONT: if `lsappinfo front` is not LastWar: record, run the standing front script, record; still not: stop, release, tell the Coordinator.
May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Cost cap, stated: 1.00 USD.
