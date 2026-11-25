---
title: Help test void, no Oil Well row, a builder idle 0525
created: 2026-11-25T05:27:35Z
modified: 2026-11-25T05:27:35Z
version: 1.0.0
description: Unit building-queues-help-test-2026-11-25-001 (the clean test of H118; front LastWar at the start 05:25:04Z; the owner idle 644 s, over the gate; the unit held from 04:50Z while the owner played) - BLOCKED BY ROUTE: the builders panel (the hammer (108,200), closed by the X (612,237)) at 05:25:25.8Z has NO OIL WELL ROW: row 1 Lv.26 Drill Ground 08:13:10 left (ends 2026-11-25T13:38:35.8Z), row 2 Lv.27 Drill Ground 4d 20:05:36 (ends 2026-11-30T01:31:01.8Z), row 3 IDLE with a Construct button (a free builder), row 4 Lv.28 Drill Ground 8d 18:24:48 (ends 2026-12-03T23:50:13.8Z); the hammer counter 3/4; no help control, hand glyph or helps count ('n of 30') drawn on any row; the Oil Well Lv.24 upgrade (expected end 07:11:19.6Z) is gone: it finished before 05:25Z (the base HUD at 05:22Z: oil 600.0K, Total Power 150,701,116, builders 3/4: the owner's play between 03:47Z and 05:22Z): the test cannot run: no help request tapped; the rows read at 05:27:01.5Z and 05:27:09.0Z (08:11:34, 4d 20:04:00, 8d 18:23:12) consistent with the first read; nothing pressed but the hammer and the X; the tram icon without a badge; drags 0
status: partial
grounded_in:
  - source: cu_bridge run 20261125T052504Z-53fcc0, final report read by the operator, 2026-11-25T05:25Z to 05:28Z
  - source: unit brief building-queues-help-test-2026-11-25-001 and the building-queues rule digest
---

# Help test void, no Oil Well row, a builder idle 0525

Rows in [0525-queue-run.csv](0525-queue-run.csv). Claimed 05:25:04Z; no different-device dialog.

- **Blocked by route.** The builders panel has no Oil Well row: the Oil Well Lv.24 upgrade (expected end 07:11:19.6Z) finished before 05:25Z; no help control on any row; the test is void.
- **Builders.** Lv.26 Drill Ground ends 13:38:35.8Z; Lv.27 11-30T01:31:01.8Z; Lv.28 12-03T23:50:13.8Z; ONE builder idle (Construct).
- **Counts.** Nothing pressed but the hammer and the X; drags 0.
- **Run.** One run, 13 steps, 2 actions, 0.149623 USD, cap 0.5; 0 refused; foreground stayed LastWar.
- **Closing state.** The base, no panel; token released 05:27:49Z.
