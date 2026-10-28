---
title: Task Unit Queue
created: 2026-10-28T10:22:00Z
modified: 2026-10-28T10:22:00Z
version: 0.1.0
description: The pending, claimed and done task units of the play routine
status: live
grounded_in:
  - source: owner request 2026-10-28 to design a task unit pool with short bounded executions
---

# Task unit queue

Instance folder. Holds the task units produced from the regulars list
and worked unit by unit by the executor loop, as designed in
[task unit queue design](../_conventions_/local-conventions/task-unit-queue-design.md).

State lives in the subfolder a unit file sits in.

- `inbox` - pending units waiting to be claimed.
- `claimed` - units under execution, plus the device token.
- `done` - finished units carrying their structured result sections.

`unit-template.md` is the shape every unit file follows. Units are
managed with `tools/queue.py`. The queue went live on 2026-10-28 -
the ticker `lastwar-queue-ticker` produces and executes units, and
the segment schedules are retired.
