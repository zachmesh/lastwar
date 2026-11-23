---
title: The integrator
created: 2026-11-23T09:02:35Z
modified: 2026-11-23T09:02:35Z
version: 0.1.0
sequence: 12
description: The standing PR integrator job (every 15 minutes) owns the merge point of main.
---
## The integrator

The standing PR integrator job (every 15 minutes) owns the
merge point of main. Its duties under this policy:

1. **Records PRs.** Open when missing, merge by merge commit
   on the batch cadence (the first pass at or after 19:00,
   23:00, 03:00, 07:00, 11:00 and 15:00 America/Los_Angeles)
   when new commits exist, comment and report on conflict,
   never force-merge, never delete a records branch. At each
   merge, add the log lines the change is owed (previous
   section).
2. **Knowledge and code PRs.** Review against the PR body
   requirements and the repository's standing rules; merge
   clean PRs by squash; leave numbered criticism comments on
   PRs that are fixable but not clean, and do not repeat a
   comment when no new commit has arrived since it.
3. **Owner-gated classes are never merged by the
   integrator** - a change that loosens a red line, widens an
   authorization, changes a cron definition, or changes this
   policy itself is commented, escalated to the owner in
   chat, and merged only on the owner's recorded approval.
4. **Sync and records.** After merges, sync main back to the
   local clone through the VPS bundle route; and leave an
   ops execution record for every pass, including no-op
   passes, per the ops execution records standard - the
   loop's own activity is recorded as executions like
   everything else.

