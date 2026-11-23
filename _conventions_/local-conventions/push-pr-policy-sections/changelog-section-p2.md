---
title: Changelog part 2
created: 2026-11-23T08:37:00Z
modified: 2026-11-23T08:37:00Z
version: 0.1.0
sequence: 14
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
- 2.1.0, 2026-11-01 - pull request ownership, on the owner's
  instruction of 2026-10-31 at 23:00 PDT that every PR have
  an owner and that a catch-all scheduled task own any PR no
  class matches. Every PR names its owning scheduled job in
  its body at creation (an `Owner:` line); the owner fixes
  review feedback on the same branch, replies on the PR, and
  drives it to mergeable, while merging stays with the
  integrator. Assignment is by change class - `_tools_/` to
  `lastwar-tool-developer`, `_activities_` and
  `_conventions_` to `lastwar-knowledge-organizer`, records
  PRs to `lastwar-pr-integrator` - and anything no class
  matches falls to the new standing catch-all job
  `lastwar-pr-catchall-owner`. The integrator reassigns a
  missing or wrong owner at first review and an ownerless PR
  is not mergeable until it does; owner-gated PRs are owned
  by the integrator as shepherd. The retro audit gains an
  ownership-coverage check against a 100 percent target.
  This amendment changes the PR policy itself and is
  therefore owner-gated; it lands by bootstrap squash merge
  on the owner's recorded in-chat instruction of 2026-10-31
  23:00 PDT, the same precedent as PR #3.
