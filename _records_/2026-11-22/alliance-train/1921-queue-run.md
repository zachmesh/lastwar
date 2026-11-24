---
title: Train countdown skipped, tram icon absent 1921
created: 2026-11-24T19:21:23Z
modified: 2026-11-24T19:21:23Z
version: 1.0.0
description: Unit train-2026-11-24-1030 - the tram icon at (107,580) was NOT DRAWN in all four frames (19:21:21.9Z to 19:21:37.7Z, only ground there): the station countdown needs the icon DRAWN with no badge, so it was skipped and nothing was tapped; no 'Boarding closes in' banner and no locomotive icon; pickup none, radar dish none; hammer 4/4, flask 2/2; drags 0
status: done
grounded_in:
  - source: cu_bridge run 20261124T192116Z-0fa69b, final report read by the operator, 2026-11-24T19:21Z to 19:22Z
  - source: unit brief train-2026-11-24-1030 and the alliance-train rule digest
---

# Train countdown skipped, tram icon absent 1921

Rows in [1921-queue-run.csv](1921-queue-run.csv). Claimed 19:21:16Z; no different-device dialog.

- **Tram icon.** NOT DRAWN in four frames over 16 s: the Station Platform pan (the tram tap) is not available; the countdown skipped.
- **Other.** No train banner or locomotive icon; pickup and radar dish none; nothing pressed; drags 0.
- **Run.** One run, 5 steps, 0 actions, 0.055795 USD, cap 0.5; 0 refused; foreground stayed LastWar.
- **Closing state.** The base, no panel; token released 19:21:48Z.
