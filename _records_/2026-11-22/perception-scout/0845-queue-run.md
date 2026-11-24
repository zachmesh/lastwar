---
title: Bridge supervised read 0845
created: 2026-11-24T08:47:30Z
modified: 2026-11-24T08:47:30Z
version: 1.0.0
description: Unit scout-midday-bridge-supervised-read-2026-11-24-001 - the first run on the new bridge tree (daemon pid 1335, run build commit b52c84ba391e): owner_idle_seconds=300 (source: default); lock admission 0.7 s after the start request (wait 0); no dialog or consent request; the Oil Well Lv.22 to 23 upgrade shows 08:41:47 left (ends 17:27:27.4Z); oil 675.1K; Total Power 150,051,860; no drag
status: done
grounded_in:
  - source: cu_bridge run 20261124T084523Z-158d7c, final report read by the operator, 2026-11-24T08:45Z to 08:46Z
  - source: unit brief scout-midday-bridge-supervised-read-2026-11-24-001 and the perception-scout rule digest
---

# Bridge supervised read 0845

Rows in [0845-queue-run.csv](0845-queue-run.csv). Claimed 08:45:23Z; no different-device dialog.

- **owner_idle_seconds.** The bridge printed **owner_idle_seconds=300 (source: default)**; the lock report read 1952 s of owner idle at the start.
- **Wait.** Lock admission **0.7 s** after the request: wait **0 s** before the first click (first click 08:45:33.442Z).
- **Dialogs.** None; no consent request. New in the start output: an 'Approve the app (first use only)... control-link' line; nothing answered.
- **Oil Well.** Lv.22 to 23 in progress, **08:41:47** left at 08:45:40.4Z: ends 17:27:27.4Z; oil 675.1K, Total Power 150,051,860; run build commit b52c84ba391e, clean; drags 0.
- **Run.** One run, 6 steps, 5 actions, 0.073156 USD, cap 0.5; 0 refused; foreground stayed LastWar.
- **Closing state.** The base, no panel; token released 08:46:20Z.
