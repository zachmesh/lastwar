---
title: Changelog part 2
created: 2026-11-23T09:02:35Z
modified: 2026-11-23T09:02:35Z
version: 0.1.0
sequence: 17
description: 2.2.0, 2026-11-01 - executor PR discipline, on the owner's instruction of 2026-10-31 at 2302 PDT that
---
- 2.2.0, 2026-11-01 - executor PR discipline, on the owner's
  instruction of 2026-10-31 at 23:02 PDT that every executor
  check the questions and issues on its own previous pull
  requests before doing anything else, and open a pull
  request every time a run finishes. Each executor run now
  starts by clearing its own PRs - answering every question
  on the PR, fixing review feedback on the same branch -
  before starting new work, and ends only when its output
  is inside a PR: work output opened as a PR in the same
  run, records output pushed to the date branch with the
  records PR confirmed to exist or opened by the executor
  itself when missing (owned by `lastwar-pr-integrator`).
  A run that cannot open or confirm its PR records itself
  partial with the reason; finished output never ends a run
  sitting on a local branch. The section is the temporal
  side of pull request ownership and leaves the
  integrator's sweep and reassignment rules unchanged; the
  retro audit gains an own-PRs-first and closing-PR check
  on run records. The seven standing executor jobs' texts
  were updated to these two rules the same evening, ahead
  of this amendment; the amendment codifies them so future
  jobs are bound automatically. This amendment changes the
  PR policy itself and is therefore owner-gated; it lands
  by bootstrap squash merge on the owner's recorded in-chat
  instruction of 2026-10-31 23:02 PDT, the same precedent
  as PR #3 and PR #4.
