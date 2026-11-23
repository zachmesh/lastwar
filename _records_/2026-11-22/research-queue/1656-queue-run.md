---
title: Research idle-slot read 1656
created: 2026-11-23T16:59:00Z
modified: 2026-11-23T16:59:00Z
version: 1.0.0
description: Unit research-2026-11-23-0603 - both labs busy (Food Output V 1d 00:33:16, Iron Output V 1d 09:42:17), 0 idle; read-only
status: done
grounded_in:
  - source: cu_bridge run 20261123T165626Z-e9c9d3, final report read by the operator, 2026-11-23T16:56Z to 16:57Z
  - source: unit brief research-2026-11-23-0603 and the 1650 record (same labs at 16:51Z)
---

# Research idle-slot read

Rows in [1656-queue-run.csv](1656-queue-run.csv). Claimed 16:56:26Z after a read receipt for the stale 2234 record (issue #737); no different-device dialog.

- **Labs.** 2/2 busy, **0 idle**: Food Output V 1d 00:33:16 (ends about 2026-11-24T17:30Z) and Iron Output V 1d 09:42:17 (ends about 2026-11-25T02:39Z), as in the handover and the 1650 read.
- **Blockers.** None: nothing idle, so no slots_blocked_by_capacity and no capacity blocker.
- **Taps.** The flask icon and the panel X; nothing pressed inside the panel.
- **Run.** One run, 5 steps, 6 actions, 0.063998 USD, cap 0.5; 0 refused; foreground stayed LastWar.
- **Closing state.** The base, no panel; labs 2/2, builders 4/4, diamonds 11,113; token released 16:56:59Z.
