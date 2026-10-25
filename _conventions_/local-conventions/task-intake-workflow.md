---
title: Task Intake Workflow
created: 2026-10-25T19:18:00Z
modified: 2026-10-25T20:12:00Z
level: L2
version: 1.1.0
description: How a newly named task is checked, registered as a task type, executed and recorded
status: unverified
grounded_in:
  - source: human-authored, owner direction 2026-10-25 on handling future task requests
builds_on:
  - _conventions_/local-conventions/recording-rules.md@1.2.0
---

# Task intake workflow

The owner will name more tasks over time. This workflow governs each one.

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

## When the owner names a task

1. **Check first.** Look for the task type in `_activities_` and in the
   `_tasks_` list. A task that maps to an existing type under another
   name counts as present - note the alias in the metadata instead of
   creating a duplicate folder.
2. **If it is not in the system, create the metadata before executing.**
   Add the folder under `_activities_` in kebab-case, with frontmatter
   and the standard sections, register it in the `_activities_` index,
   add it to the daily umbrella if it belongs to the daily round, and
   note it in the task list and the logs. Then start executing it and
   log the record under `_records_/<date>/<task type>/`, one file per
   execution, with the activity index and the day table updated.
3. **If it is already in the system, check and update only.** Verify the
   metadata against the account and the current screens, and update it
   if appropriate with a version bump. Then **skip execution** - being
   mentioned is not an execution order. Execution is left to future
   cycles, meaning the next daily round or the next explicit execution
   request. Say plainly to the owner that the metadata existed, whether
   it was updated, and that execution was skipped for this turn.

## When execution does happen

The recording rules govern it - approvals first for purchases, diamond
spending, PvP, alliance diplomacy and city moves, and every execution is
written as its own record file the same day.
