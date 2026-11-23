---
title: 2. Concepts part 1
created: 2026-11-23T08:37:05Z
modified: 2026-11-23T08:37:05Z
version: 0.1.0
sequence: 3
description: Task unit - one regular from _tools_/regulars.json, sized to finish in a few minutes.
---
## 2. Concepts

- **Task unit** - one regular from `_tools_/regulars.json`, sized to
  finish in a few minutes. A unit is a Markdown file whose frontmatter
  is one structured YAML document describing the task, its queue state
  and, once executed, its result and result statistics (sections 4
  and 5). The prose body is instructions for the executor; tools read
  only the YAML. Units are the only thing executors run.
- **One unit, one task type** - owner rule of 2026-10-28. A unit
  names exactly one regular and one activity, an executor never
  merges two types into one unit or one result, and a chain is
  homogeneous - every unit in it shares the same regular (the queue
  tool refuses to extend a chain with a different regular). Work
  that belongs to another type, even when a screen flow touches it
  on the way, is executed and counted under that type's own unit.
  This is what keeps the per-type statistics - durations, failures,
  late finishes - clean enough to judge execution quality by type.
- **Pool** - the `_queue_` type folder with three state subfolders.
  `inbox` holds pending units, `claimed` holds units under execution,
  `done` holds finished units. Moving a file is the state transition.
- **Producer** - a short job that reads the due list from
  `_tools_/regulars.py` and writes one unit file per due regular into
  `inbox`. It never touches the device.
- **Executor loop** - the main agent's standing job under this
  design. It keeps executing where work is needed - take the device
  token, pick the best unit, run it, write its result, pick the next
  one. The loop is driven by one periodic ticker (section 6), not by
  the three segment schedules, which this design retires.
- **The 15 minute unit** - owner rule of 2026-10-28 - **each unit
  runs at most 15 minutes**. The unit is the scheduling quantum -
  when a unit ends, the loop re-reads the pool, so work that became
  due or urgent in the meantime is picked up at the next boundary,
  at most 15 minutes later. A task that cannot fit in 15 minutes is
  split into units at intake, never stretched.
