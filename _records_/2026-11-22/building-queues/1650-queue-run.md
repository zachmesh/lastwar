---
title: Building queues idle-slot read 1650
created: 2026-11-23T16:58:00Z
modified: 2026-11-23T16:58:00Z
version: 1.0.0
description: Unit building-queues-2026-11-23-0603 - builders 4/4 and labs 2/2 all busy (0 idle); the two idle barracks were not re-read (the pistol tap showed no toast), the 13:44Z Drill Ground Full read stands
status: partial
grounded_in:
  - source: cu_bridge runs 20261123T165032Z-127154 (builders, labs) and 20261123T165211Z-a16d45 (barracks retry), final reports read by the operator, 2026-11-23T16:50Z to 16:53Z
  - source: unit brief building-queues-2026-11-23-0603 and the 1344 training record
---

# Building queues idle-slot read

Rows in [1650-queue-run.csv](1650-queue-run.csv). Claimed 16:50:31Z; no different-device dialog.

- **Builders.** 4/4 busy, 0 idle: four Lv.25 Training Base upgrades, timers read 06:29:20 to 06:29:31. Unverified: that probably is 16:29:20, which ends 2026-11-24T09:20Z as in the handover; the model may have misread the first digit.
- **Labs.** 2/2 busy, 0 idle: Food Output V 1d 00:38:43 and Iron Output V 1d 09:47:45, as in the handover.
- **Barracks.** The first run's tap at (628,562) hit bare ground (the camera had shifted); after WORLD then BASE both tags read (Barracks Lv.24 and Lv.20), but the pistol tap showed neither panel nor toast within 2 s, so idle state and the toast were not read. The 13:44Z read (idle, blocked by capacity: Drill Ground Full, 2 slots) stands unconfirmed.
- **Why partial.** Total open slots not confirmed; no Train, Collect, Upgrade, Research or priced control was pressed.
- **Runs.** Two runs, 0.112105 and 0.127427 USD (0.239532 in all), cap 0.5 each; 0 refused; foreground stayed LastWar.
- **Closing state.** The base, no panel, no building selected; token released 16:53:52Z.
