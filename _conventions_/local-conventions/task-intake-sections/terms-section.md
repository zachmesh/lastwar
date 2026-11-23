---
title: Terms and 2 more
created: 2026-11-23T08:37:54Z
modified: 2026-11-23T08:37:54Z
version: 0.1.0
sequence: 2
description: A task type is a kind of in-game task or activity, for example radar tasks or
---
## Terms

- A **task type** is a kind of in-game task or activity, for example
  radar tasks or secret missions.
- Its **metadata** is its definition folder - what the task is, how it
  is done, its costs, caps, lessons and open questions.

## Separation of metadata and records

- Task type metadata lives in its **own top level folder**,
  `_activities_`, one folder per task type. It is a sibling of
  `_records_`, never nested inside it or inside any other type folder.
- `_records_` holds executions only, organised by date, then by the
  task type name, then one file per execution. A record subfolder that
  reuses a task type name is grouping only - it indexes and holds
  executions and links back to the metadata folder. Knowledge is never
  accumulated inside a record subfolder.

## What metadata must record

At the owner direction on 2026-10-25, every task type folder records,
as it is learned in game -

- **How to enter** - the exact entry path, screen by screen, so the
  task can be found again without rediscovery.
- **Cadence** - how often the task is expected to be executed, and
  any daily or weekly cap that paces it.
- **Scope and availability** - limits, unlock conditions, and whether
  the task is season specific or always available.

These join the standing sections - what the task is, how it is done,
what is known, limits and open questions. When an existing folder is
checked under this workflow and one of these is missing, add it from
observation where possible.

