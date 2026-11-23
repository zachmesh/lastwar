---
title: Contents part 2
created: 2026-11-23T09:05:48Z
modified: 2026-11-23T09:05:48Z
version: 0.1.0
sequence: 3
description: Ops execution records a mental-model convention for the whole repository, not only a record format -
---
- [Ops execution records](ops-execution-records.md) — a
  mental-model convention for the whole repository, not only a
  record format: what is recorded is always an execution,
  never a session, and every activity of the loop (game
  execution, perception, planning, retro, tool development,
  knowledge organisation, PR integration) is itself an
  execution that leaves a structured record the retro measures
  with one ruler. It operationalises, for the loop's own work,
  the single-source-of-truth statement of the task unit queue
  design's section 14, and is cross-referenced with it rather
  than redefining it.
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
- [Held patches register](held-patches.md) — the in-repo record of tool
  patches held outside the repository, consulted by the tool-developer
  step-2 in-flight check before re-implementing an issue (issue #809).
