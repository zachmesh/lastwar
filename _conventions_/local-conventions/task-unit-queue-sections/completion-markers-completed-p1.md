---
title: Completion markers ( completed/ ) part 1
created: 2026-11-23T09:03:48Z
modified: 2026-11-23T09:03:48Z
version: 0.1.0
sequence: 6
description: A unit closed in a detached worktree leaves its done record in that worktree, so the
---
### Completion markers (`completed/`)

A unit closed in a detached worktree leaves its done record in that
worktree, so the main checkout's inbox still holds the unit and the
next pass would re-execute it (issue #438). The closing therefore
also records a small marker in the main checkout's `_queue_/completed/`
(`_tools_/queue.py` `record_completion`, called by the complete path
and by the dead-letter path; best effort - a write failure warns but
never fails the closing itself).

A marker is frontmatter only - `unit`, `status`, `finished_at`,
`executor` - because the full result lives in the done record; the
marker only has to answer "did this unit already close somewhere".
A marker suppresses the inbox copy only when it parses, names its
own unit, and carries a closing status; a file that fails any of
those suppresses nothing, so a half-written record can never hide
fresh work. `next`, `claim`, `sync` and `plan` treat a valid marker
exactly like a local done record, and sync production also blocks a
fresh unit for a slot whose closing is visible only as a marker
(issue #466).

