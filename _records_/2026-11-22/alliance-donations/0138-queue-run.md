---
title: Alliance donation fix-up 3 taps, after a slip 0138
created: 2026-11-25T01:42:16Z
modified: 2026-11-25T01:42:16Z
version: 1.0.0
description: Unit donations-2026-11-25-0113 (the final sweep's fix-up; front at the start 01:38:24Z LastWar; two runs) - A SLIP OF MINE: the first run (01:38:25Z to 01:39:50Z) read the entry count 3/30 at 01:39:02.4Z and tapped no Donate, because my task text carried the donation PASS rule 'under 6: do not tap' that this unit's own brief does not have (its brief: donate with the coin button whenever today coin donations remain); nothing was spent; the second run (01:40:19Z, the text without that rule) read the entry count 3/30 at 01:40:55.2Z (the refill clock: 1/30 remaining after pass 009's last tap, plus the grid points 01:17:57 and 01:37:57), 3 coin Donate taps at 01:41:01.1Z, 01:41:18.1Z and the last at 01:41:23.871Z; the live count 1/30 in the frame at 01:41:19.3Z, before the last tap; the Donate turned grey with a cooldown 00:16:23 read at 01:41:34.6Z: the timer ends 01:57:57.6Z, on the grid point 01:57:57 within 0.7 s: DONE; the diamond Donate never pressed; the donation dialog, the Techs page and the Alliance hub closed one click each; tram icon not drawn; drags 0
status: done
grounded_in:
  - source: cu_bridge run 20261125T014018Z-bf858a, final report read by the operator, 2026-11-25T01:38Z to 01:42Z
  - source: unit brief donations-2026-11-25-0113 and the alliance-donations rule digest
---

# Alliance donation fix-up 3 taps, after a slip 0138

Rows in [0138-queue-run.csv](0138-queue-run.csv). Claimed 01:38:24Z; no different-device dialog.

- **Slip.** The first run tapped nothing (my text carried the pass rule 'under 6'); the unit's own brief says donate whenever coin donations remain; disclosed.
- **Entry.** **3/30** at 01:40:55.2Z (1/30 left at 00:43Z plus two grid points).
- **Taps.** **3** coin taps, the last at **01:41:23.871Z**; the live count 1/30 before it; the diamond Donate never pressed.
- **Timer.** Grey Donate **00:16:23** at 01:41:34.6Z: ends **01:57:57.6Z**, on the grid within 0.7 s: DONE; tram icon not drawn; drags 0.
- **Run.** One run, 24 steps, 15 actions, 0.316188 USD, cap 0.5; 0 refused; foreground stayed LastWar.
- **Closing state.** The base, no panel; token released 01:42:22Z.
