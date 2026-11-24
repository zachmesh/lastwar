---
title: Barracks queues read 0351
created: 2026-11-24T03:55:00Z
modified: 2026-11-24T03:55:00Z
version: 1.0.0
description: Unit training-2026-11-23-1803 - the four barracks read: the first pistol press on Barracks Lv.24 COLLECTED a finished batch of 274 Lv.8 units (Total Power 149,755,698 to 150,046,960, +291,262) as a side effect; Lv.20 blocked 'Drill Ground Full'; Lv.27 idle (Lv.9 slider maximum 726); Lv.30 training Lv.10 x793 07:25:14 left; no Train pressed
status: done
grounded_in:
  - source: cu_bridge run 20261124T035107Z-b79bd9, final report read by the operator, 2026-11-24T03:51Z to 03:53Z
  - source: unit brief training-2026-11-23-1803 and the troop-training rule digest
---

# Barracks queues read 0351

Rows in [0351-queue-run.csv](0351-queue-run.csv). Claimed 03:51:07Z; no different-device dialog.

- **Barracks Lv.24.** The pistol press **collected a finished batch of 274 Lv.8 units** (toast 'Training complete: 274 Lv. 8 units are ready', POWER +291,262): Total Power **149,755,698 to 150,046,960**; the queue is idle. This was not intended in a read-only unit.
- **Barracks Lv.20.** Blocked: 'Drill Ground Full: Unable to add more units.' The 274 units just collected took the room that was free.
- **Barracks Lv.27.** Idle: TRAIN UNITS, Lv.9 selected, slider maximum 726, Train 1d 10:19:35 (not pressed); stats Power 1352 per unit.
- **Barracks Lv.30.** Training Lv.10 x793, 07:25:14 left (ends about 11:18:30Z).
- **Pressed.** Pistols only to read; no Train, Speed Up or Finish Now.
- **Run.** One run, 13 steps, 52 actions, 0.184649 USD, cap 0.5; 0 refused; foreground stayed LastWar.
- **Closing state.** The base, no panel; token released 03:53:36Z.
