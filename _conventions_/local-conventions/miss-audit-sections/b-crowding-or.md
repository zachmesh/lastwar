---
title: B. Crowding or starvation of a subtask - 6 units
created: 2026-11-23T08:37:03Z
modified: 2026-11-23T08:37:03Z
version: 0.1.0
sequence: 6
description: Instances -
---
### B. Crowding or starvation of a subtask - 6 units

Instances:

- Four radar units on the 2026-10-30 release day ran Quick Execute
  and Claim All to completion and left the special map pins
  unattempted every time - 0220, 0623, 1040 and 1418 queue runs
  (`_records_/2026-10-30/radar-tasks/0220-queue-run.md`,
  `_records_/2026-10-30/radar-tasks/0623-queue-run.md`,
  `_records_/2026-10-30/radar-tasks/1040-queue-run.md`,
  `_records_/2026-10-30/radar-tasks/1418-queue-run.md`). No radar unit
  that day attempted a single pin.
- Two truck units filled dispatch and left plunder untouched inside
  the same unit - trucks-2026-10-30-1057 (Trade Count 1 of 5 to 3 of
  5, plunder 0 of 4 untouched) and trucks-2026-10-30-1857 (settled
  and dispatched, plunder untouched)
  (`_records_/2026-10-30/truck-plunder/1305-queue-run.md`,
  `_records_/2026-10-30/truck-plunder/2017-queue-run.md`).

Prevention rule B - a subtask deferred twice in one day is promoted.
Pins after dispatch work, plunder after dispatch work, and the store
step after combat work each become the first action of the next unit
of that type, or a unit of their own, instead of the last action of a
unit that has already spent its budget.

