---
title: Executor PR discipline part 1
created: 2026-11-23T09:02:35Z
modified: 2026-11-23T09:02:35Z
version: 0.1.0
sequence: 9
description: Owner instruction, 2026-10-31 at 2302 PDT - an executor's pull requests are part of its run,
---
## Executor PR discipline

Owner instruction, 2026-10-31 at 23:02 PDT: an executor's
pull requests are part of its run, at both ends. This
section is the temporal side of the ownership section
above - ownership says whose a PR is; this section says
when its owner must attend to it. The integrator's
full-sweep review and reassignment rules are unchanged by
it.

**Own PRs first.** Before an executor job does any new
work in a run, it checks the pull requests it opened or
owns - the PRs whose body `Owner:` line names the job,
plus the records PRs it opened itself. It reads the latest
comments on each one. Every question on one of its PRs is
answered on the PR, whether or not the answer needs a code
change; every piece of review feedback is fixed on the
same branch first and replied to on the PR. A job does not
start new work while one of its own PRs still carries an
unanswered question or unaddressed feedback it can act on.

**A run ends by opening a PR.** A run is not finished
until its output is inside a pull request:

