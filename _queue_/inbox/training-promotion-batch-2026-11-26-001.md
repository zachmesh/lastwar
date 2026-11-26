---
unit: training-promotion-batch-2026-11-26-001
regular: training
activity: troop-training
segment: 1
priority: 1
created_at: 2026-11-26T16:50:36Z
expires_at: 2026-11-26T22:30:00Z
planned_for:
not_before: 2026-11-26T20:16:00Z
window: promotion batch 2 after the 20:13z completion (steer a 16:27z standing)
est_minutes: 8
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

## Brief (planner, PROMOTION BATCH 2: Steer A's pipeline rule 17:39Z; plan reason: the 2.75M power lever)

serves: PL-09

ONE PROMOTION ONLY. Route: the `barracks` row of `_records_/2026-11-22/queue-planning/2700-routes.csv`, the Lv.27 barracks (tag 'Barracks Lv.27', read first): the pistol ONCE (verify the pistol glyph in a frame first).
FIRST read in ONE frame: Total Power, the Lv.7, Lv.8, Lv.9 and Lv.10 counts, the HUD food, iron and coin, the queue row. THE RETURN of batch 1 (the Lv.9 count decides, the Total confirms): FITTED = Lv.9 3,330 (Total 153,094,991 if no other power moved); BLOCKED = Lv.9 2,604 (Total 152,113,439: 'Drill Ground Full'): write which. START BATCH 2 EITHER WAY. Conditions: the queue row IDLE, food at least 35M, iron at least 150M, Lv.8 still has troops: if any fails: promote NOTHING, write the frame, STOP.
Select Lv.8, do NOT touch the quantity (726 expected, else write the max), press the green up-arrow beside the cost row ONCE (Steer A's exception for this arrow only). The dialog 'Unit Upgrading' Lv.8 to Lv.9 has TWO buttons: CONFIRM ONLY THE Promote BUTTON ONCE, NEVER PRESS Finish Now (the sibling button; its presence is not a reason to cancel). Cancel by the X only if a row shows a coin, gem or diamond price or a food or iron cost above 1.0M.
Read the frame at +10 s and +60 s (HUD, Total Power, counts, queue row; a drop of about 772K is the promotion in progress). STOP if food or iron falls by more than 1.0M each. NO second Promote.
IF BATCH 1 WAS BLOCKED: right after the +60 s frame press the pistol ONCE at the Lv.27 tent (tag read first) to collect its 726 Lv.9 into the places the new batch freed; write Total Power and the Lv.7, Lv.8, Lv.9 and Lv.10 counts BEFORE and AFTER. Nothing else.
CLOSE by `_records_/2026-11-22/queue-planning/3170-closing-rule-done-and-partial.md`: DONE for the Promote pressed or a verified nothing-to-do (`--state-change yes` if pressed, a `state_read:` line); else PARTIAL.
FRONT: if `lsappinfo front` is not LastWar: record, run the standing front script, record; still not: stop, release, tell the Coordinator.
May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Cost cap, stated: 0.60 USD.
