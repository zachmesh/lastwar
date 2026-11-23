---
title: When the owner names a task
created: 2026-11-23T08:37:54Z
modified: 2026-11-23T08:37:54Z
version: 0.1.0
sequence: 3
description: Check first.
---
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

