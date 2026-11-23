---
title: Training read run 1344
created: 2026-11-23T14:00:00Z
modified: 2026-11-23T14:00:00Z
version: 1.0.0
description: Unit training-2026-11-23-0203 under the READ ONLY ruling - Barracks Lv.24 and Lv.20 are idle and blocked by 'Drill Ground Full', Lv.27 and Lv.30 run their batches (19:56:30Z and 2026-11-24T11:18Z); no Train, no Speed Up
status: done
grounded_in:
  - source: cu_bridge run 20261123T134405Z-089c31, events and final result, 2026-11-23T13:44Z to 13:47Z
  - source: unit training-2026-11-23-0203 and the coordinator ruling TRAINING READ ONLY of 13:43Z
---

# Training read run 1344

Rows in [1344-queue-run.csv](1344-queue-run.csv), the tag text beside every row. Claimed 13:44:05Z; no different-device dialog at the no-click first frame; nothing spent.

- **Barracks Lv.24 and Barracks Lv.20:** idle. The pistol raised the toast **"Drill Ground Full: Unable to add more units."** at 13:44:22Z and 13:45:04Z; no TRAIN UNITS panel, so no slider maximum. Both queues are blocked
  by capacity (2).
- **Barracks Lv.27:** TRAIN UNITS, Lv.9 batch of **726**, "Training in progress **06:10:58**" at 13:45:32Z, ends about **19:56:30Z**; Power 1352, Morale 625.0, Squad Load Capacity 2000.
- **Barracks Lv.30:** TRAIN UNITS, Lv.10 batch of **793**, "Training in progress **21:32:08**" at 13:46:16Z, ends about **2026-11-24T11:18:21Z**; Power 1647, Morale 750.0, Squad Load Capacity 2200.
  Both panels showed a Speed Up button, not pressed.
- **Reading.** The timers agree with the 11:09Z and 11:12Z reads, so nobody sped them up. New training stays blocked until a Drill Ground level rises (Lv.28 to 29 needs 119.0M coin) or the batches finish.
- **Run.** `claude-gateway/claude-sonnet-5-5`, 14 steps, 0 refused, no `local_input` pause, 0.183748 USD (stated cap 0.6). HUD unchanged (food 654.7M, iron 1.0G, coin 529.2K, Total Power 150,413,046).
- Closing state: the base, no panel, token released.
