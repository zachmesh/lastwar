---
title: Commit discipline - execution commits stay on records branches
created: 2026-11-23T08:37:03Z
modified: 2026-11-23T08:37:03Z
version: 0.1.0
sequence: 5
description: Pushes run under the PR-only policy of push and PR policy (owner decision, 2026-10-31 - main
---
## Commit discipline - execution commits stay on records branches

Pushes run under the PR-only policy of
[push and PR policy](push-and-pr-policy.md) (owner decision,
2026-10-31 - main advances only by pull request merge, and
the tier-1 direct tier of the earlier two-tier policy is
abolished). An execution commit - the ticker's per-pass
record commits and any other commit an executor makes while
doing the work - is made on the date branch
`records/<YYYY-MM-DD>` for the local date of the records,
never on main, and stages only the records paths, by
explicit pathspec, never a blanket add:

- `_records_`, `_queue_`, `_logs_`, `_tools_/state/`

A change under `_tools_/`, `_conventions_` or `_activities_` is
load-bearing and must never be swept into a record commit,
however small it looks - the scout production seeds in
`_tools_/queue.py` landed exactly that way once, inside a
ticker records commit (d1fa5b9, 2026-10-31). When an executor
finds load-bearing changes sitting in the working tree, it
leaves them exactly as they are, notes them in the run
record, and leaves them for the pull request flow. The
executor does not wait for its records to reach main: the
records branch is pushed through the standard route and
reaches main through the integrator's records PR on the
policy's cadence.

Pull request branches follow the mirror rule for the logs: a
work branch never stages `_logs_` at all. The append-only
input and action logs are written on records branches, and
for pull request work the integrator adds the log lines at
merge time (or they ride the next records branch), per the
push and PR policy - during the PR's life its body and
commit messages are the record. Log appends on a PR branch
race main's records commits and conflict by construction
(PR #2, 2026-10-31).

