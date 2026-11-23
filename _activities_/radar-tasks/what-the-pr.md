---
title: What the PR 237 merge settled - 1450 re-read as a stack-day unit
created: 2026-11-23T06:25:33Z
modified: 2026-11-23T06:25:33Z
version: 0.1.0
sequence: 95
description: PR 237 (lastwar-tool-developer, Refs 235) merged 2026-11-03 1638 local, during this organizer run, after the run's
---
## What the PR 237 merge settled - 1450 re-read as a stack-day unit

- PR 237 (lastwar-tool-developer, Refs #235) merged
  2026-11-03 16:38 local, during this organizer run,
  after the run's first three folds were already
  committed. It changes only _tools_/duel.py: the duel
  day is now computed in the timezone the schedule
  declares (America/Los_Angeles), with day boundaries
  at 19:00 local wall times, instead of a naive
  datetime.now().
- Re-read of the 1450 unit: the unit ran on duel day 2
  (Base Expansion, stack), not day 3 (Age of Science,
  release). The 1532 fold's classification of 1450 as
  a release-day unit is corrected here, not left
  standing. The claims themselves are unaffected as
  resources: 27 rewards claimed, radar points 139 to
  166 (radar points, not duel points - consistent
  with the dialog that no duel points were granted
  that day). The claim-anyway rationale (resources
  certain, holding the stack risks task expiry) still
  stands; the "release standard governs" justification
  is superseded, since the unit was a stack-day unit.
  Its partial status stands on the same grounds as
  before (6 pins left unattempted, Quick Execute 4
  tasks left for the next unit).
- Standing rule going forward: the next radar release
  decision uses the corrected tool, and any future
  tool-versus-stamp disagreement is settled against
  the VS panel itself plus the tool's clock basis,
  never by assuming the schedule is stale or the
  stamp lags. The stored-versus-completable open
  question (Claim All 8 after Quick Execute batches
  of 3 and of 2, returning marches the leading
  hypothesis) is untouched by this resolution.
- Issue #235 commented by this run with this
  resolution; the issue is NOT closed here - closure
  belongs to the daily retro once the next radar unit
  after merge reports the PT day.


