---
title: Task Unit Queue
created: 2026-10-28T10:22:00Z
modified: 2026-10-28T10:22:00Z
version: 0.1.0
description: The pending, claimed and done task units of the play routine
status: proposal
grounded_in:
  - source: owner request 2026-10-28 to design a task unit pool with short bounded executions
---

# Task unit queue

Instance folder. Holds the task units produced from the regulars list
and worked by short executor batches, as designed in
[task unit queue design](../_conventions_/local-conventions/task-unit-queue-design.md).

State lives in the subfolder a unit file sits in.

- `inbox` - pending units waiting to be claimed.
- `claimed` - units under execution, plus the device token.
- `done` - finished units carrying their structured result sections.

`unit-template.md` is the shape every unit file follows. Units are
managed with `tools/queue.py`. The design is a proposal under owner
review - the live routine still runs on the segment schedules until
the owner approves the migration.
