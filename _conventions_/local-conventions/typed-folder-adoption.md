---
title: Typed-folder Adoption
created: 2026-10-25T17:56:00Z
modified: 2026-11-01T07:09:43Z
level: L2
version: 1.3.0
description: Adoption of reflection typed-folder format and constitutions, with the local type registry
status: unverified
grounded_in:
  - source: human-authored, owner request 2026-10-25 to follow reflection shared conventions
  - source: owner request 2026-10-31 to remove the credentials folder
---

# Typed-folder adoption

This repository adopts the typed-folder format of `dtadpole/reflection`,
pinned at commit `78195f50d43cc96b8cdd09b00b8118204b22715d`. The canonical
texts are the [core conventions](https://github.com/dtadpole/reflection/blob/78195f50d43cc96b8cdd09b00b8118204b22715d/shared/_conventions_/core-conventions/INDEX.md)
and the [constitutions](https://github.com/dtadpole/reflection/blob/78195f50d43cc96b8cdd09b00b8118204b22715d/shared/_constitutions_/INDEX.md)
at version 1.1.0. They are linked, never copied, so no second version can
drift (DRY).

## Constitutions in force

- C1 — trajectories and experiences are immutable. Play records are never
  edited or deleted; a correction is a new appended entry.
- C2 — knowledge is versioned, never destroyed. Every artifact references
  its origin in `grounded_in`, pinned where the source is versioned.
- C3 — governance is human-only. Agents never amend C1 to C5 and never
  promote this project's knowledge into a global repository.
- C4 — observability. Actions, inputs and results are recorded with
  resolvable evidence, in `_logs_` and `_records_`.
- C5 — evidence-based rationale. A claim rests on fresh observation, not
  memory. Measured, inferred and assumed stay distinct, and an ungrounded
  claim carries the unverified label.

## Local type registry

Introducing a type registers it here in the same commit.

| Type | Holds | Source |
|---|---|---|
| `_knowledge_` | game knowledge, one instance per topic | local, registered 2026-10-25 |
| `_activities_` | activity checklists and activity records | local, registered 2026-10-25 |
| `_records_` | append-only audit records of play on the game account | reflection vocabulary |
| `_logs_` | append-only repository entries | reflection vocabulary |
| `_conventions_` | convention articles, agent-maintainable | reflection vocabulary |
| `_queue_` | task units of the play routine, in inbox, claimed and done state subfolders | local, registered 2026-10-28 |
| `_context_` | gathered source material that grounds a topic | reflection vocabulary |

## Read next

[Recording rules](recording-rules.md) for how each local type is written.
