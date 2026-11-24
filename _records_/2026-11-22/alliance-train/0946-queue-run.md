---
title: Alliance Train boarding 0946
created: 2026-11-24T09:58:00Z
modified: 2026-11-24T09:58:00Z
version: 1.0.0
description: Unit train-alliance-train-board-2026-11-24-001 - boarded once: carriage 2 (the 7/7 one), quantity 3, Gift Contract pressed once at 09:57:23.168Z with the Trade Contract stock 264 read before (the 266 was an expectation; the coordinator approved at 09:56Z); the platform timer read 00:09:18 at 09:57:26.0Z (departure about 10:06:44.0Z); the plus of carriage 2 became an avatar, occupancy 8/7; the stock after was not shown on the platform; drags 0
status: done
grounded_in:
  - source: cu_bridge run 20261124T095652Z-c8f5a2, final report read by the operator, 2026-11-24T09:46Z to 09:58Z
  - source: unit brief train-alliance-train-board-2026-11-24-001 and the alliance-train rule digest
---

# Alliance Train boarding 0946

Rows in [0946-queue-run.csv](0946-queue-run.csv). Claimed 09:46:04Z; no different-device dialog.

- **Boarded once.** Carriage 2, quantity **3**, Gift Contract once at **09:57:23.168Z**; stock **264** before (the 266 expected was not a limit; approved 09:56Z); the green button and no price or diamond read just before.
- **Result.** The plus of carriage 2 became an avatar, occupancy **7/7 to 8/7**; the platform timer read **00:09:18 at 09:57:26.0Z**: the train departs about **10:06:44.0Z**; the stock after is not shown on the platform (261 expected).
- **Cinematic.** A tap on a carriage plus bubble in the station-camera view plays the entry cinematic into the Station Platform view; it ended by itself.
- **Waits.** 0 s in all three runs (0.8 to 1.1 s lock admission); drags 0.
- **Run.** One run, 17 steps, 14 actions, 0.239 USD, cap 0.5; 0 refused; foreground stayed LastWar.
- **Closing state.** The Station Platform screen, no dialog; token released 09:57:49Z.
