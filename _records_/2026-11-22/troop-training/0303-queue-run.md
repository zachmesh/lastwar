---
title: Four barracks read, one empty and three full 0303
created: 2026-11-25T03:08:41Z
modified: 2026-11-25T03:08:41Z
version: 1.0.0
description: Unit training-2026-11-24-1803 (front at the start 03:03:39Z LastWar; two runs; run 1 ended in a context_full error at step 17 with no final report, so I read its saved frames myself) - one pistol press per barracks, each on a fresh WORLD then BASE frame: Barracks Lv.27 (pistol (459,632) at 03:04:31.3Z): the TRAIN UNITS panel opened with no toast, a batch slider at 726 (Train button 1d 10:19:35, not pressed): EMPTY QUEUE; Barracks Lv.30 (pistol (527,680) at 03:05:44.6Z): the toast 'Drill Ground Full: Unable to add more units.': FINISHED BATCH WAITING; run 2: Barracks Lv.24 (pistol (598,615) at 03:08:00.4Z) and Barracks Lv.20 (pistol (598,584) at 03:08:32.2Z): the same toast: FINISHED BATCH WAITING each; the ready bubbles (a 6x crop of the saved frame, tiny digits, read with low confidence): Lv.30 a red-helmet portrait with about 793, Lv.24 a blue-helmet portrait with about 249, Lv.20 a blue-cap portrait with about 310, Lv.27 a white bubble with a face (no digits); slots_idle 1; slots_blocked_by_capacity 3 (Drill Ground Full); never Train, Finish Now or speed up; the Lv.26 Drill Ground upgrade ends 11-25T13:38:35.7Z; Total Power 150,103,292 before and after; tram icon without a badge, the pickup badge 10; the two question-mark bubbles beside the pickup are back at (145,649) and (98,682) in the frames from 03:03Z; drags 0
status: done
grounded_in:
  - source: cu_bridge run 20261125T030340Z-b334e7, final report read by the operator, 2026-11-25T03:03Z to 03:09Z
  - source: unit brief training-2026-11-24-1803 and the troop-training rule digest
---

# Four barracks read, one empty and three full 0303

Rows in [0303-queue-run.csv](0303-queue-run.csv). Claimed 03:03:39Z; no different-device dialog.

- **Lv.27.** EMPTY QUEUE (the TRAIN UNITS panel, slider 726, no toast); closed unpressed.
- **Lv.30, Lv.24, Lv.20.** Toast 'Drill Ground Full: Unable to add more units.': finished batches waiting (bubbles about 793, 249, 310).
- **Counts.** slots_idle 1, slots_blocked_by_capacity 3; Total Power unchanged; run 1 ended in a context_full error (saved frames read); drags 0.
- **Run.** One run, 27 steps, 17 actions, 0.346479 USD, cap 0.5; 0 refused; foreground stayed LastWar.
- **Closing state.** The base, no panel or tag; token released 03:08:52Z.
