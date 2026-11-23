---
title: Records flow - date branches
created: 2026-11-23T09:02:35Z
modified: 2026-11-23T09:02:35Z
version: 0.1.0
sequence: 3
description: Append-only trajectories and live state keep their continuity without touching main directly -
---
## Records flow - date branches

Append-only trajectories and live state keep their continuity
without touching main directly:

- `_records_` - play records and ops execution records,
  append-only under C1.
- `_queue_` - the task unit pool and its state transitions.
- `_logs_` - the input and action logs.
- `_tools_/state/` - runtime state written by the tools
  themselves (for example the regulars tracker state).

Writers commit these paths to a date branch named
`records/<YYYY-MM-DD>`, the local date of the records being
committed. The branch is created from current main on its
first use that day, is pushed through the standard VPS route
(bundle to the IONOS VPS, fetch in `~/lastwar-push`,
`git push github records/<date>`), and is never deleted: it
keeps receiving that day's appends, before and after each
merge, and the next day starts a fresh date branch. The
pathspec discipline of
[recording rules](recording-rules.md) is unchanged - records
commits stage only the four records paths, by explicit
pathspec, never a blanket add, and a load-bearing change found
sitting in the working tree is left exactly as it is, noted in
the run record, and left for its own pull request. A writer
never waits for its records to reach main; the branch is its
record, and main catches up on the integrator's cadence.

