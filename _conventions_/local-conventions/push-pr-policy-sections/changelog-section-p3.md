---
title: Changelog part 3
created: 2026-11-23T09:02:35Z
modified: 2026-11-23T09:02:35Z
version: 0.1.0
sequence: 18
description: 2.1.0, 2026-11-01 - pull request ownership, on the owner's instruction of 2026-10-31 at 2300 PDT that
---
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
