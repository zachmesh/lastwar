---
title: Task Unit Queue Design
created: 2026-10-28T10:22:00Z
modified: 2026-11-23T08:37:05Z
version: 0.39.0
description: Run the routine as short task units drawn from a file queue instead of long segment runs - implemented 2026-10-28
status: implemented
grounded_in:
  - source: owner request 2026-10-28 to design a task unit pool with short bounded executions
  - source: run records of 2026-10-27 and 2026-10-28 in _records_
  - source: miss audit of 2026-10-31 and the owner instruction of 2026-10-31 to reflect and fix
  - source: "PR #267 merged 2026-11-04 (Refs #147) - zero-sweep slots reset-anchored (reset_utc 02:00, offsets 90/30 minutes)"
  - source: "PR #614 merged 2026-11-11 (Refs #606) - zero-sweep slots moved from [90, 30] to [120, 60]; section 12 synced to that roster by this change"
  - source: "organizer 0432 run 2026-11-07 (Refs #147) - the four 19:00 mentions flagged as follow-up in 0.15.0 rewritten to the absolute reset instant 02:00 UTC (VIP expiry, scout anchor, quota checkpoints, deadline list)"
  - source: "Issue #689 (tooling) - outcome_unknown control lock after a session drop, implemented 2026-11-12 as the pool-level control-lock blocker and rule R9"
---

# Task Unit Queue Design

Run the routine as short task units drawn from a file queue instead of long segment runs - implemented 2026-10-28. This register stays at this path as an entry page; its text was split verbatim into 45 articles in [task-unit-queue-sections](task-unit-queue-sections/INDEX.md), unchanged and in reading order.

## Adding an entry

Add one small article file `task-unit-queue-sections/<entry-id>.md`, named by an entry id that starts with letters (for example `entry-20261123-01.md`), with the frontmatter fields title, created, modified, version and description, then add one line for it at the end of this page: `- [Title](task-unit-queue-sections/entry-20261123-01.md) one sentence`. Never edit an existing article.

## Articles

- [Catalog 01](task-unit-queue-sections/catalog-01.md) - Task unit queue design to 12-the-daily
- [Catalog 02](task-unit-queue-sections/catalog-02.md) - 12-the-daily to changelog-section

## Changelog

- 0.39.0, 2026-11-23 - Split verbatim by split_doc.py into 45 articles and 2 catalog pages; --check EQUAL, sha256 7df4ea20c516; the unsplit 0.38.0 file is commit 6d019ade
