---
title: Badge probe 60 minutes after the last foreground loss 1804
created: 2026-11-24T18:05:02Z
modified: 2026-11-24T18:05:02Z
version: 1.0.0
description: Unit scout-midday-badge-probe-2026-11-24-002 - probe: none. The last foreground loss known: the game restart at 17:04:31Z (System Settings 17:04:14Z, LastWar 17:04:24Z, Chrome 17:04:27Z for 3 s, a new LastWar process 17:04:32Z), about 60 minutes earlier; my own front checks read LastWar at 17:50:29Z, 17:53:35Z, 17:55:20Z, 17:58:59Z and 18:04:33Z and 18:05:06Z. The SR of cycle A's dispatch (pressed 14:23:31.9Z, shown 03:36:58) is derived back at 18:00:30Z. Six frames from 18:04:35Z to 18:04:59Z: the tram badge NONE in every frame, the pickup none, the radar dish 3 (a 4x crop of the saved last frame confirms); a dark dot 4.5 minutes after the derived return is data; nothing tapped; drags 0
status: done
grounded_in:
  - source: cu_bridge run 20261124T180434Z-9179f6, final report read by the operator, 2026-11-24T18:04Z to 18:05Z
  - source: unit brief scout-midday-badge-probe-2026-11-24-002 and the perception-scout rule digest
---

# Badge probe 60 minutes after the last foreground loss 1804

Rows in [1804-queue-run.csv](1804-queue-run.csv). Claimed 18:04:33Z; no different-device dialog.

- **probe: none.** The tram badge is dark in six frames from 18:04:35Z to 18:04:59Z, 4 to 4.5 minutes after the SR's derived return (18:00:30Z), about 60 minutes after the last known foreground loss (17:04:31Z).
- **Left column.** Tram none, pickup none, radar dish 3 (a crop of the saved frame confirms).
- **Data.** The first SR lit its badge 27 to 49 minutes after its derived return and 49 s after LastWar returned from the alert; nothing tapped; drags 0.
- **Run.** One run, 6 steps, 0 actions, 0.082305 USD, cap 0.5; 0 refused; foreground stayed LastWar.
- **Closing state.** The base, no panel; token released 18:05:06Z.
