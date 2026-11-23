---
title: Executor PR discipline part 2
created: 2026-11-23T09:02:35Z
modified: 2026-11-23T09:02:35Z
version: 0.1.0
sequence: 10
description: Work output (knowledge, code, conventions) is opened as a PR in the same run that produces
---
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

