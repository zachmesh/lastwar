---
title: Changelog part 1
created: 2026-11-23T09:02:35Z
modified: 2026-11-23T09:02:35Z
version: 0.1.0
sequence: 16
description: 2.3.0, 2026-11-01 - records merge cadence, on the owner's decision of 2026-11-01 given in chat.
---
## Changelog

- 2.3.0, 2026-11-01 - records merge cadence, on the owner's
  decision of 2026-11-01 given in chat. Records PRs no
  longer merge on every integrator pass; they merge in
  batches every 4 hours, at the first integrator pass at or
  after 19:00, 23:00, 03:00, 07:00, 11:00 and 15:00
  America/Los_Angeles, superseding cadence A of 2.0.0. The
  boundary set puts a batch right after the 19:00 trade-day
  reset so the 20:39 daily retro reads a complete trade day
  in main. Rationale recorded the same day: the integrator
  merged more than 16 PRs on 2026-11-01, nearly all routine
  records merges with zero review value. Opening records
  PRs is unchanged - a PR exists as soon as a branch carries
  commits - and knowledge and code PRs still merge promptly
  on every pass. This amendment changes the PR policy
  itself and is therefore owner-gated; it lands on the
  owner's recorded in-chat approval of 2026-11-01, the same
  precedent as PR #3 and PR #4.
- 2.2.1, 2026-11-01 - factual correction only, no rule
  change, on the owner's instruction of 2026-10-31 at 23:25
  PDT. The repository was transferred from its previous
  home under the dtadpole account to zachmesh/lastwar and
  made public on 2026-10-31. The
  platform-facts statements that described this repository as
  private are corrected to past tense, and the
  branch-protection measurement taken while the repository
  was private is marked stale pending re-measurement for the
  public repository. The living-doc references to the old
  repository name are updated in the same change.
