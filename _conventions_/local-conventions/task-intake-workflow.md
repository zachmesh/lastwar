---
title: Task Intake Workflow
created: 2026-10-25T19:18:00Z
modified: 2026-11-23T08:37:54Z
level: L2
version: 1.3.0
description: How a newly named task is checked, registered as a task type, executed and recorded
status: unverified
grounded_in:
  - source: human-authored, owner direction 2026-10-25 on handling future task requests
builds_on:
  - _conventions_/local-conventions/recording-rules.md@1.2.0
---

# Task Intake Workflow

How a newly named task is checked, registered as a task type, executed and recorded. This register stays at this path as an entry page; its text was split verbatim into 5 articles in [task-intake-sections](task-intake-sections/INDEX.md), unchanged and in reading order.

## Adding an entry

Add one small article file `task-intake-sections/<entry-id>.md`, named by an entry id that starts with letters (for example `entry-20261123-01.md`), with the frontmatter fields title, created, modified, version and description, then add one line for it at the end of this page: `- [Title](task-intake-sections/entry-20261123-01.md) one sentence`. Never edit an existing article.

## Articles

- [Task intake workflow](task-intake-sections/task-intake-workflow.md) - The owner will name more tasks over time.
- [Terms and 2 more](task-intake-sections/terms-section.md) - terms-section, separation-of-metadata, what-metadata-must - A task type is a kind of in-game task or activity, for example radar...
- [When the owner names a task](task-intake-sections/when-the-owner.md) - when-the-owner - Check first.
- [When execution does happen and 1 more](task-intake-sections/when-execution-does.md) - when-execution-does, one-off-work - The recording rules govern it - approvals first for purchases, diamond spending, PvP, alliance...
- [Standalone task-list retirement - 2026-11-01](task-intake-sections/day-20261101.md) - day-20261101 - Owner instruction - plan and implement removal of the old task-list folder.

## Changelog

- 1.3.0, 2026-11-23 - Split verbatim by split_doc.py into 5 articles; --check EQUAL, sha256 71041ebb36ed; the unsplit 1.2.1 file is commit 6d019ade
