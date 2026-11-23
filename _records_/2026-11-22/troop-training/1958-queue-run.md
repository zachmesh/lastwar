---
title: Lv.27 batch collect test 1958
created: 2026-11-23T20:01:00Z
modified: 2026-11-23T20:01:00Z
version: 1.0.0
description: Unit training-growth-collect-2026-11-23-001 - the finished Lv.27 batch of 726 could not be collected: the ready bubble tap and the pistol both raised 'Drill Ground Full: Unable to add more units.'; Total Power 150,416,946 unchanged; blocked by capacity
status: partial
grounded_in:
  - source: cu_bridge run 20261123T195824Z-93f69a, final report read by the operator, 2026-11-23T19:58Z to 20:00Z
  - source: unit brief training-growth-collect-2026-11-23-001 and the troop-training rule digest
---

# Lv.27 batch collect test 1958

Rows in [1958-queue-run.csv](1958-queue-run.csv). Claimed 19:58:24Z; no different-device dialog.

- **The test.** With the Drill Ground full, the Lv.27 batch of 726 is **not collected**: the tap on the ready bubble gave 'Drill Ground Full: Unable to add more units.' (19:59:22Z), the same text as the pistol (19:58:58Z and 19:59:39Z); Total Power stayed **150,416,946**; no animation.
- **Reading.** The Hospital collect says 'Unable to add 5306 units' with a count; this toast has none, like the idle-barracks pistol toast, so the bubble tap may have acted as a Train press rather than a collect (unverified): the batch needs room, not necessarily all at once.
- **Not read.** Troop counts per tier before and after (no panel opened).
- **Queue.** The Lv.27 barracks is still blocked: slots_idle 1, slots_blocked_by_capacity 1, capacity_blocker 'Drill Ground Full'; with Lv.24 and Lv.20 that is three blocked barracks.
- **Owner.** Local input at about 20:00:00Z (idle 13 s at 20:00:15Z), after the run ended 20:00:03Z.
- **Run.** One run, 12 steps, 24 actions, 0.163387 USD, cap 0.5; 0 refused; foreground stayed LastWar.
- **Closing state.** The base, no tag, no panel; token released 20:00:03Z.
