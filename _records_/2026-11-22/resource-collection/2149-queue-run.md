---
title: Oil collect 2149
created: 2026-11-23T21:56:00Z
modified: 2026-11-23T21:56:00Z
version: 1.0.0
description: Unit harvest-oil-well-2026-11-23-002 - oil panel Collect once: available 658,759 to 0, owned 658.7K to 662.9K (+4,220 in 3.5 hours since the 18:19Z collect), output 1.2K an hour; Details and Go not pressed
status: done
grounded_in:
  - source: cu_bridge run 20261123T214938Z-83f499, final report read by the operator, 2026-11-23T21:49Z to 21:51Z
  - source: unit brief harvest-oil-well-2026-11-23-002 and the resource-collection rule digest
---

# Oil collect 2149

Rows in [2149-queue-run.csv](2149-queue-run.csv). Claimed 21:49:38Z; no different-device dialog.

- **Before.** OIL panel: Available 658,759, owned 658.7K, output 1.2K an hour; Collect Resources 4,220; no capacity line.
- **Collect.** Once (21:49:58.825Z): Available **662,979**, owned 662.9K, **+4,220**; no popup.
- **Interval.** 3.51 hours since the 18:19Z collect: 1,202 oil an hour, matching 1.2K.
- **Not pressed.** Details, the two Go rows and the $19.99 pack; no bubble tapped.
- **Bridge.** `cu_bridge status` now prints a warning line before its JSON (the daemon predates the owner-idle record), which broke my poll parser: fixed in the run script.
- **Run.** One run, 7 steps, 11 actions, 0.090269 USD, cap 0.5; 0 refused; foreground stayed LastWar.
- **Closing state.** The base, no panel; token released 21:54:58Z.
