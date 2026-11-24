---
title: Train countdown skipped, tram icon absent 2241
created: 2026-11-24T22:41:43Z
modified: 2026-11-24T22:41:43Z
version: 1.0.0
description: Unit train-2026-11-24-1430 (front at the start 22:41:32Z LastWar) - the tram icon at (107,580) was NOT DRAWN in all four frames (22:41:40.2Z to 22:41:57.3Z, only ground and buildings there): the station countdown needs the icon DRAWN with no badge, so it was skipped and nothing was tapped; no 'Boarding closes in' banner and no locomotive icon; pickup none, radar dish 3; hammer 4/4, flask 2/2; drags 0
status: done
grounded_in:
  - source: cu_bridge run 20261124T224133Z-f15dc6, final report read by the operator, 2026-11-24T22:41Z to 22:42Z
  - source: unit brief train-2026-11-24-1430 and the alliance-train rule digest
---

# Train countdown skipped, tram icon absent 2241

Rows in [2241-queue-run.csv](2241-queue-run.csv). Claimed 22:41:32Z; no different-device dialog.

- **Tram icon.** NOT DRAWN in four frames over 17 s: the Station Platform pan is not available; the countdown skipped.
- **Other.** No train banner or locomotive icon; nothing pressed; drags 0.
- **Run.** One run, 5 steps, 0 actions, 0.066524 USD, cap 0.5; 0 refused; foreground stayed LastWar.
- **Closing state.** The base, no panel; token released 22:42:11Z.
