---
title: Task Intake Workflow
created: 2026-10-25T19:18:00Z
modified: 2026-11-01T07:58:31Z
level: L2
version: 1.2.1
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

1. **Check first.** Look for the activity type and its aliases in
   `_activities_`; check `_queue_` for an existing execution unit.
   A request matching an existing type under another name counts
   as present - note the alias rather than creating a duplicate.
   One-off investigation or improvement requests are checked
   against the improvements backlog instead of being registered
   as recurring game activities.
2. **If it is not in the system, create the metadata before executing.**
   Add the folder under `_activities_` in kebab-case, with frontmatter
   and the standard sections, register it in the `_activities_` index,
   add it to the daily umbrella if it belongs to the daily round, and
   track follow-up work in the improvements backlog and record the
   intake through the normal records flow. Then start executing it and
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


## One-off work and proposals

The [improvements backlog](../../_records_/retro/improvements.md) is the
single register for one-off execution-knowledge, tooling and organization
work. Each item states its evidence, target and current value (or an
explicit data gap), responsible work class, and verification. The normal
planner or executor produces a bounded queue unit when live game
observation is needed; the knowledge organizer consumes its evidence and
does not operate the game itself. Cross-reference an existing item rather
than opening a second copy. Preserve the backlog's retro-only closure rule.

An unapproved idea or owner-only choice belongs in the companion
[owner decisions register](../../_records_/retro/owner-decisions.md), not
in the execution queue. Transferring an idea there does not approve it.
Activity definitions explain how to work; they are not a to-do list.

## Standalone task-list retirement - 2026-11-01

Owner instruction - plan and implement removal of the old task-list
folder. The migration below accounts for all seven open entries and both
unconfirmed ideas. Moving an item is not evidence that its game work was
performed or completed.

| Former item | Canonical destination and disposition |
|---|---|
| Arms Race standing four-hour checks | Existing `_activities_/arms-race/` and `_tools_/regulars.json`, with concrete `_queue_` units and dated results. Preserve the phase cadence; do not restore the retired standalone cron. |
| Verify all activity profiles against the account | IMP-20261101-01 in the improvements backlog. |
| Record the three squads, heroes, levels, gear and troop types | IMP-20261101-02. |
| Observe both sides of a Mac/iPhone device switch | IMP-20261101-03. Existing Mac-side observation is retained; iPhone-side behavior remains unverified. |
| Backfill entry, cadence, scope and availability in older profiles | Consolidated into IMP-20261101-01 rather than duplicated. |
| Reconcile the six HUD resource figures with their labels | IMP-20261101-04. Existing resource definitions are inputs, not proof of the historical mapping. |
| Spot-check the counter triangle, HQ 31 requirements and radar cap behavior | IMP-20261101-05; reuse the existing radar work and its evidence. |
| Season 2 topic and event-calendar idea | Topic already exists in `_knowledge_/season-two-winter/`; OD-20261101-01 preserves the unapproved calendar proposal. |
| Record VS and alliance results after each event | OD-20261101-02 preserves the unapproved extension; existing duel reads and execution records continue. |

Completed entries remain available in the
[sanitized historical snapshot](https://github.com/zachmesh/lastwar/blob/4bdd6fa3153b6469f52b1fbe5b05859ee83dc871/_tasks_/task-list/INDEX.md)
and the original dated execution records. That pinned snapshot is history,
not a second live backlog. The two old task-list files and their live
registry/index entries are removed. No game action, schedule change, or
new spending authorization is part of this migration.
