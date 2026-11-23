---
title: Executor PR discipline
created: 2026-11-23T08:37:00Z
modified: 2026-11-23T08:37:00Z
version: 0.1.0
sequence: 7
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

- Work output (knowledge, code, conventions) is opened as
  a PR in the same run that produces it, per the knowledge
  and code flow above.
- Records output is pushed to the live records date
  branch, and the run then confirms the records PR for
  that branch exists - a fresh PR for the new commits, on
  top of whatever was merged before. If none exists, the
  executor opens it itself (`gh pr create`, base main,
  head `records/<date>`, body naming the date, this
  policy, and `Owner: lastwar-pr-integrator`, which owns
  records PRs end to end); it does not wait for the
  integrator to notice the branch.
- A run that cannot open or confirm its PR records itself
  partial, with the reason, in its execution record.
  Finished output is never left sitting on a local branch
  as the run's final state.

The daily retro's loop-health check extends to this
section in the same pass as its other scans: run records
are checked for the own-PRs-first step and for the closing
PR, and a run that skipped either is named in the retro
and counted in the loop-health family.

