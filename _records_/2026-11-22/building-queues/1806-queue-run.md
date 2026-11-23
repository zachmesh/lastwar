---
title: Building queues read 1806
created: 2026-11-23T18:09:00Z
modified: 2026-11-23T18:09:00Z
version: 1.0.0
description: Unit building-queues-2026-11-23-1003 - four builders busy on Training Base Lv.25 with 05:13:04 to 05:13:15 left, ending about 23:20Z today (not 09:20Z tomorrow); 0 idle
status: done
grounded_in:
  - source: cu_bridge run 20261123T180648Z-442c14, final report and observation timestamps read by the operator, 2026-11-23T18:06Z to 18:07Z
  - source: unit brief building-queues-2026-11-23-1003 and the 1650 record
---

# Building queues read

Rows in [1806-queue-run.csv](1806-queue-run.csv). Claimed 18:06:48Z; no different-device dialog; nothing pressed in the panel.

- **Builders.** 4/4 busy, **0 idle**: four Training Base upgrades to Lv.25, Time Left **05:13:04, 05:13:08, 05:13:11, 05:13:15** at 18:07:08.651Z, so they end between **23:20:12Z and 23:20:24Z today**.
- **Correction.** The handover and the tag index say 'builders free 2026-11-24T09:20Z'; that 09:20 is the Oil Well upgrade's duration (09:20:18), not a clock time. The 1650 guess of '16:29' for the 06:29:20 read was also wrong: the first digit is 0, and 17:51Z plus 06:29 gives the same 23:20Z.
- **Stats.** `slots_idle=0`, no capacity blocker; the labs belong to the research unit and the barracks to the training unit of this batch.
- **Run.** One run, 6 steps, 10 actions, 0.077401 USD, cap 0.4; 0 refused; foreground stayed LastWar.
- **Closing state.** The base, panel closed with its X; token released 18:07:38Z.
