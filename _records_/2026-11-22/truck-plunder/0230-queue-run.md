---
title: Plunder scan stopped 0230
created: 2026-11-24T02:37:00Z
modified: 2026-11-24T02:37:00Z
version: 1.0.0
description: Unit trucks-plunder-scan-2026-11-24-001 - closed partial: the trade icon (107,580) is PRESENT again after the reset, the hospital guard read free room 1,329, and the run stopped at 02:34:20Z when macOS UserNotificationCenter came to the front after the trade icon tap at 02:34:16.5Z; no scan, no fight
status: partial
grounded_in:
  - source: cu_bridge run 20261124T023408Z-ddf387, final report read by the operator, 2026-11-24T02:30Z to 02:34Z
  - source: unit brief trucks-plunder-scan-2026-11-24-001 and the truck-plunder rule digest
---

# Plunder scan stopped 0230

Rows in [0230-queue-run.csv](0230-queue-run.csv). Claimed 02:30:41Z; no different-device dialog.

- **Icon.** The trade icon at (107,580) is **present** again (the 02:00Z reset returned it).
- **Guard.** Hospital Lv.25: Severely Wounded 1,364 of 7,999, Completed 5,306, free room **1,329** (not under 1,000).
- **Stop.** After the one tap at **02:34:16.5Z**, macOS UserNotificationCenter came to the front at 02:34:19Z; the run was cancelled at step 2; nothing pressed or answered; LastWar not frontmost.
- **Not done.** The Plunder Count, the four cards and any fight; the trade icon is not tapped again (coordinator order).
- **Next.** Hold until the coordinator names the alert and the restore.
- **Run.** One run, 5 steps, 10 actions, 0.188 USD, cap 0.5; 0 refused; foreground stayed LastWar.
- **Closing state.** UserNotificationCenter in front, LastWar not frontmost; token released 02:38:00Z.
