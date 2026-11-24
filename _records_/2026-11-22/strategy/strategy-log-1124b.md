---
title: Strategy log 2026-11-24 part b
created: 2026-11-24T03:39:00Z
modified: 2026-11-24T04:02:00Z
version: 1.0.0
level: L3
description: Second log of 2026-11-24, covering the speed-ups, the collected T9 batch and the food row settlement
status: unverified
grounded_in:
  - source: operator records 0301 and 0330 and 2320 as relayed at 03:36Z
---

# Strategy log 2026-11-24 part b

- 2026-11-24 03:36Z. Speed-ups: 29,440 minutes on the three grounds, ends 11-26 21:10:37Z, 11-30 22:21:48Z, 12-05 11:59:18Z; duel points exactly 150 a minute (F-070 true). A bubble tap collected the Lv.27 T9 batch of 726 whole (+981,552) with room about 1,000; 274 left. My order of use named the T10 batch, which ends 11:18Z: my error, rows re-timed. F-064 missed low (the flat was known and not applied); F-036 scored true with a learning entry (I lowered p on absence of a panel row). The food rows are real (221.0M and 314.5M, food 674.4M to 138.9M). Decision 2026-11-24-02 sets the ladder against the long line.
- 2026-11-24 03:47Z. Steer A has the free 274 slots trained now (T9 at the Lv.27 barracks, about 264, +356,928) in the order whole batch, new training, healing last. My trade: the T10 batch then fits after four levels, not three, a 2-day delay if B2's next level starts at 11-26 21:10Z, two weeks if not. F-176 prior set to 0.25; F-177 re-derived; F-178 and F-179 added.
- 2026-11-24 03:57Z. The pistol press on the Lv.24 barracks collected a finished batch of 274 T8 (+291,262): the 1,000 freed slots are used, room is 0, the T9 training rows F-178 and F-179 are retired, and the partial Collect test moves to the first room at 11-26 21:10Z. Both collects were free power from room the siege freed (+1,272,814). Lesson: an idle-looking barracks may hold a finished batch (timing lesson 7); my base-case T8 fill assumed idle barracks.
- 2026-11-24 04:05Z. Decided early for the planner: B2's next job at 11-26 21:15Z is the same ground's Lv.27 to 28 with one 10,000-minute speed-up, the only builder job that makes army room; pre-conversion 20:00Z to 21:00Z (about 60M coin, 265M food); fallback Gold Mine or Farmland if the 1.0G floor binds (decision 2026-11-24-03).
- 2026-11-24 04:02Z watchdog. Closed with sources: H122 and H123 (partly), H125 (the flat is measured, the cause is new H128), H76 (speed-ups score 150 points a minute); H90 DEFERRED to the owner's answer; the by-tag range rule re-tests after 10 closed rows (H101); overdue reads H31, H65, H120, H121 carry proposed dates for the planner to confirm; PL-05's Monday window passed, so F-012 is re-timed to an idle slot. The troop-training read must separate an empty queue, a finished batch waiting (size) and a block recorded in the same read (timing lesson 7).
