---
title: Barracks queue read 2214
created: 2026-11-23T22:19:00Z
modified: 2026-11-23T22:19:00Z
version: 1.0.0
description: Unit training-2026-11-23-1403 - Barracks Lv.24, Lv.20 and Lv.27 idle and blocked by 'Drill Ground Full: Unable to add more units.'; Lv.30 busy with a Lv.10 batch of 793 ending 2026-11-24T11:18:24Z; slots_idle 3, slots_blocked_by_capacity 3
status: done
grounded_in:
  - source: cu_bridge run 20261123T221446Z-38d9fa, final report read by the operator, 2026-11-23T22:14Z to 22:17Z
  - source: unit brief training-2026-11-23-1403 and the troop-training rule digest
---

# Barracks queue read 2214

Rows in [2214-queue-run.csv](2214-queue-run.csv). Claimed 22:14:45Z; no different-device dialog.

- **Blocked.** Barracks **Lv.24, Lv.20 and Lv.27** are idle and each raised 'Drill Ground Full: Unable to add more units.' with no panel: blocked by capacity: Drill Ground Full. The Lv.27 batch of 726 is still waiting; no collect retry was made.
- **Busy.** Barracks **Lv.30**: Lv.10 batch of 793, Training in progress 13:01:56 at 22:16:28.3Z, ends **2026-11-24T11:18:24Z**.
- **Slots.** slots_idle 3, slots_blocked_by_capacity 3, capacity_blocker 'Drill Ground Full'.
- **Pressed.** WORLD, BASE, the tent taps, the four pistols and the panel X; no Train, Speed Up or Upgrade.
- **Run.** One run, 13 steps, 54 actions, 0.186231 USD, cap 0.5; 0 refused; foreground stayed LastWar.
- **Closing state.** The base, no panel; token released 22:16:56Z.
