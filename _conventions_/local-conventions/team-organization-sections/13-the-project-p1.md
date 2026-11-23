---
title: 13. The project board part 1
created: 2026-11-23T09:04:37Z
modified: 2026-11-23T09:04:37Z
version: 0.1.0
sequence: 16
description: Work is tracked as GitHub issues in zachmesh/lastwar and shown on one GitHub Project - https
---
## 13. The project board

Work is tracked as GitHub issues in `zachmesh/lastwar` and shown on one
GitHub Project: <https://github.com/users/zachmesh/projects/1> (private, linked to this repository, moved 2026-11-23; the earlier board under another user is a closed, superseded backup).
It follows [project boards](https://github.com/dtadpole/reflection/blob/main/_conventions_/issue-driven-work/project-boards.md)
and [work hierarchy](https://github.com/dtadpole/reflection/blob/main/_conventions_/issue-driven-work/work-hierarchy.md),
and was copied from the `nexus` board so its fields and five views match the
other boards exactly. The Coordinator owns it.

| View (tab order) | Columns | Filter |
|---|---|---|
| `Kanban` | Status | `no:feedback-state -label:epic` |
| `By Agent` | Agent | `-status:Done,Sunset` |
| `Recently Done` | Agent | `status:Done,Sunset updated:>@today-14d` |
| `Feedback loop` | Status | `has:feedback-state updated:>@today-14d` |
| `Epics` | Status | `label:epic` |

- **Agent** options are `owner (zhenc)` plus
  `lastwar <seat>` for each of the eight seats. When a seat changes, the
  Coordinator updates the field the same day.
- **Hierarchy.** A user-owned repository has no `Epic` issue type, so Epics
  carry the label `epic` and Stories the label `story`. The five Epics are
  #861 L1 Execution, #862 L2 Discovery, #863 L3 Learning, #864 Team and
  platform, #865 Maintenance 2026-11; each has an `## Acceptance criteria`
  section taken from the metric hierarchy above.
- **Status flow for a seat's card:** `Ready` -> `In progress` (one per seat) ->
  `In review` -> `Done`; `Waiting` needs a reason in the issue; `Needs owner`
  routes the card to `owner (zhenc)`.
- **Feeding the board.** The board is linked to the repository, but nothing adds issues automatically yet. The Steward adds new issues in batches of 8 or fewer and each Coordinator pass verifies the board and sets Status.
- **Seeded 2026-11-22:** 215 issues (190 open Ready, 5 `Needs owner`, 19 Done,
  1 Sunset, the 5 Epics In progress); Kind set from the labels `tooling`,
  `knowledge`, `play`, `records`, `compliance`, `idea`.

Known limits, as on the `nexus` and `dsh-web-ops` boards:

