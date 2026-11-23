---
title: Recording Rules
created: 2026-10-25T17:56:00Z
modified: 2026-11-23T08:37:03Z
level: L2
version: 1.10.0
description: Evidence, language and append-only rules for knowledge, tasks, activities and play records
status: unverified
grounded_in:
  - source: human-authored, owner requests 2026-10-25 on recording scope
builds_on:
  - _conventions_/local-conventions/typed-folder-adoption.md@1.0.0
---

# Recording Rules

Evidence, language and append-only rules for knowledge, tasks, activities and play records. This register stays at this path as an entry page; its text was split verbatim into 8 articles in [recording-rules-sections](recording-rules-sections/INDEX.md), unchanged and in reading order.

## Adding an entry

Add one small article file `recording-rules-sections/<entry-id>.md`, named by an entry id that starts with letters (for example `entry-20261123-01.md`), with the frontmatter fields title, created, modified, version and description, then add one line for it at the end of this page: `- [Title](recording-rules-sections/entry-20261123-01.md) one sentence`. Never edit an existing article.

## Articles

- [Recording rules](recording-rules-sections/recording-rules.md)
- [Evidence](recording-rules-sections/evidence-section.md) - evidence-section - Every figure comes from the game screen, checked at the time of writing, or...
- [Where work and evidence live](recording-rules-sections/where-work-and.md) - where-work-and - Knowledge (_knowledge_) — versioned claims about the game.
- [Task intake](recording-rules-sections/task-intake.md) - task-intake - How a task the owner names is handled — check whether its task type...
- [Commit discipline - execution commits stay on records](recording-rules-sections/commit-discipline-execution.md) - commit-discipline-execution - Pushes run under the PR-only policy of push and PR policy (owner decision, 2026-10-31...
- [Owner-only actions](recording-rules-sections/owner-only-actions.md) - owner-only-actions - Assembling is the owner's alone (owner rule, 2026-10-25).
- [Device access](recording-rules-sections/device-access.md) - device-access - Retry the device-access error at least 3 times (owner rule, 2026-10-26).
- [Language and scope](recording-rules-sections/language-and-scope.md) - language-and-scope - Tracked content and logs are English.

## Changelog

- 1.10.0, 2026-11-23 - Split verbatim by split_doc.py into 8 articles; --check EQUAL, sha256 0d89b4effc5c; the unsplit 1.9.2 file is commit 6d019ade
