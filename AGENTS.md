---
title: Last War Agent Entry Point
created: 2026-10-25T17:56:00Z
modified: 2026-11-23T08:39:25Z
version: 1.5.0
description: Project instructions and adoption of reflection typed-folder conventions
grounded_in:
  - source: owner request to adopt dtadpole/reflection shared conventions
---

# Last War

This project records knowledge, activity definitions, queued work and play records for the
owner's Last War Survival account. It adopts **dtadpole/reflection's
typed-folder format**. Read the [canonical conventions](https://github.com/dtadpole/reflection/blob/78195f50d43cc96b8cdd09b00b8118204b22715d/shared/_conventions_/core-conventions/INDEX.md),
the [local conventions](_conventions_/INDEX.md) and the
[knowledge index](_knowledge_/INDEX.md) first.

## Format

- Types use underscore-wrapped plural nouns. Reuse reflection's vocabulary
  where a row exists; local types are registered in
  [typed-folder adoption](_conventions_/local-conventions/typed-folder-adoption.md).
- Instances sit directly inside their type, use 2 to 4 lowercase kebab-case
  words, and match `^[a-z0-9]+(-[a-z0-9]+){1,3}$`.
- A type folder holds only its `INDEX.md` and its instances. Every content
  folder carries an `INDEX.md`. This file serves the root.
- Leaf files are kebab-case with a real extension. A type is kept in
  single-file form or folder form, never both.
- Every authored Markdown file carries frontmatter. Entry points carry the
  identifying fields only, with no `level` and no `status`. No value contains
  a colon. `created` never changes; `modified` and `version` move with edits.

## Everything lives in this repository

Owner rule, 2026-10-25: everything that helps play this account lives in this repository, never only in chat or in the agent's memory; a fact, rule, list or tool that would matter next week is written here in the same session. Use `_tools_/` in tool commands and Git stage pathspecs, and stage `_tools_/state/` explicitly with records. The full rule is in [repository first rule](_conventions_/local-conventions/agent-entry-notes/repository-first-rule.md).


## Governance

Constitutions C1 to C5 of dtadpole/reflection govern this repository by
reference, pinned in
[typed-folder adoption](_conventions_/local-conventions/typed-folder-adoption.md).
They are human-only to amend (C3), so this repository never copies or edits
them. Play records are immutable trajectories (C1). Knowledge is versioned
and never destroyed (C2). Every claim carries a resolvable evidence chain or
an explicit unverified label (C4, C5).

## Task intake

For an in-game activity request, check `_activities_` first. Activity
definitions live there, concrete executions live in `_queue_`, and
execution evidence lives under `_records_` by date. Preserve the
existing new-type versus existing-type execution rule in the
[task intake workflow](_conventions_/local-conventions/task-intake-workflow.md).

One-off investigation and improvement work is tracked only in the
[improvements backlog](_records_/retro/improvements.md), with a
checkable completion condition. Pending proposals and owner-only
choices go to the [owner decisions register](_records_/retro/owner-decisions.md).
The former standalone task list is retired; do not recreate it or
maintain a second backlog.

## Delivery

Reply to the owner in Chinese. Tracked content and the append-only logs are
in English, following reflection's working agreements. Commit and push
scoped Conventional Commits together with the
[action log](_logs_/repo-actions/INDEX.md) and the
[input log](_logs_/user-inputs/INDEX.md). Keep private account data out of repository content.
In-game purchases, alliance diplomacy and other consequential actions need
the owner's approval first.

## Account privacy

Refer to the account as `owner account`. Follow the
[account privacy convention](_conventions_/local-conventions/account-privacy.md)
for public repository content and executor output.

## Changelog

- 1.5.0, 2026-11-23 - The long text of the repository-first rule moved verbatim to an article; the rule, the tools path and the staging line stay here.
