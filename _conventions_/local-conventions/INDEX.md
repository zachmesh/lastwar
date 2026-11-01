---
title: Local Conventions
created: 2026-10-25T17:56:00Z
modified: 2026-11-01T05:35:00Z
version: 1.7.0
description: The local convention articles of this repository
grounded_in:
  - source: human-authored
---

# Local conventions

Instance folder. Holds the articles that state how the adopted format works
in this repository.

## Contents

- [Typed-folder adoption](typed-folder-adoption.md) — the pinned source
  conventions, the constitution clauses in force, and the local type registry.
- [Recording rules](recording-rules.md) — evidence, language, approvals and
  append-only rules for knowledge, tasks, activities and play records.
- [Task intake workflow](task-intake-workflow.md) — how a newly named task
  is checked against the task types, registered if missing, executed if
  new, and only checked and updated if it already exists.
- [Task unit queue design](task-unit-queue-design.md) — the design
  the routine runs on: short task units drawn from a file queue
  instead of long segment runs, the execution discipline rules,
  the perception layer contract, and the retro review mechanism
  of section 14.
- [Miss audit 2026-10-31](miss-audit-2026-10-31.md) — the root cause
  audit of every non-done queue unit of 2026-10-30 and 2026-10-31,
  with the owner expanded collection checklist checked line by line.
- [Reflection 2026-10-31](reflection-2026-10-31.md) — the reflection
  on that audit, with every fix mapped to the file it landed in.
- [Loop review 2026-10-31](loop-review-2026-10-31.md) — the review of
  whether the feedback and improvement loop is closed, with the four
  open links filed for the first retro.
- [Evaluation metrics](evaluation-metrics.md) — the specification for
  measuring the play system itself: execution efficiency per task
  type, perception completeness and discovery generalisation, retro
  effectiveness, the measured impact of the tool developer and the
  knowledge organiser, and loop health, with the monitoring
  thresholds the daily retro enforces.
- [Push and PR policy](push-and-pr-policy.md) — the two-tier push
  policy the owner approved on 2026-10-31: execution records,
  queue state, logs and tool state push straight to main, while
  load-bearing knowledge and code (tools, conventions, activity
  profiles, the regulars) land by pull request through the VPS
  `gh` route, enforced by discipline and the retro audit while
  the Free plan offers no branch protection.
- [Daily collection ledger](daily-collection-ledger.md) — the master
  list of everything collectible or due in one reset day, each line
  with the live read that closes it, walked by the pre-reset zero
  sweeps.
- [Perception-driven queue](perception-driven-queue.md) — the scout
  layer; daily work is determined by what the game screen actually
  offers, perceived first into structured items and scheduled by
  observation triggers rather than fixed slots, with the regulars
  kept as a capability profile library, new tasks discovered,
  profiled and scheduled under the discovery protocol, the
  scout_diff tool of Phase 2, and the learning and knowledge
  hardening protocol.
