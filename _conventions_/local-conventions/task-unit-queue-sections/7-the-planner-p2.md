---
title: 7. The planner - a 12 hour horizon part 2
created: 2026-11-23T09:03:48Z
modified: 2026-11-23T09:03:48Z
version: 0.1.0
sequence: 17
description: A unit whose slot has fully passed unexecuted is expired into done with status expired by
---
- A unit whose slot has fully passed unexecuted is expired into
  `done` with status `expired` by the next reap - the following
  slot's unit supersedes it, and the miss stays visible in the
  statistics. Chains are not planned; they are seeded and
  continued by the ticker as before.

