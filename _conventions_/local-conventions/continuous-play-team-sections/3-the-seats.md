---
title: 3. The seats
created: 2026-11-23T07:20:36Z
modified: 2026-11-23T08:18:43Z
version: 0.3.0
sequence: 8
description: Ten roster rows, the coordinator and nine seats.
---
## 3. The seats

Ten roster rows, the coordinator and nine seats. DSH Team capacity is
eight members, so the integrator and strategist seats, added on
2026-11-23, run under the recorded size exception in `TEAM.yaml`. Roles may combine
temporarily, but write scopes stay disjoint.

| Seat | Responsibility | Write scope | Cadence |
|---|---|---|---|
| coordinator | dispatch, queue health, owner gateway, team review | `TEAM.yaml`, `_seats_/`, `_records_/retro/improvements.md` proposals | 15 min tick |
| operator | play units, hold the device token, close records | `_queue_/claimed`, `_queue_/done`, `_records_/<date>/<activity>` | every tick |
| scout | perceive surfaces, ledger walk, file candidates | `_records_/<date>/perception-scout`, `_activities_` candidates by proposal | every 2 h |
| researcher | internet and local-interaction research | `_records_/<date>/research`, `_knowledge_` by proposal | 2 questions per day |
| planner | queue hygiene, staging, slot coverage | `_queue_/inbox`, `_tools_/state` | hourly |
| coach | metrics, retro, improvement backlog | `_records_/retro`, `_records_/<date>/retro-review` | daily and weekly |
| toolsmith | tool and automation improvements | `_tools_/` code and tests | on assignment |
| scribe | knowledge and activity folding, conventions upkeep | `_knowledge_`, `_activities_`, `_conventions_` on a branch the integrator lands | on assignment |
| integrator | lands coordinator-handed branches on the protected main (whole-tree privacy scan, push, pull request, merge commit, read-back) and merges code pull requests after their checks | `_records_/<date>/integration` | per branch handed over |
| strategist | owns the growth strategy of record (ranked levers with evidence tags, hypothesis register, resource policy), writes decision records above one builder-day or 5 percent of a stock and drafts the weekly owner digest, red-teams the plan | `_records_/<date>/strategy` | 7-day plan daily, season plan weekly |

Every seat reads its own `bootstrap.md`, `duties.md` and
`handover.md` before acting. A seat that is not loaded receives its
messages when it wakes; the coordinator is the clock and the router.

## Changelog

- 0.2.0, 2026-11-23 - Integrator row added (session-bc838015), scribe row no longer lists pull request integration, seat count corrected to nine rows.
- 0.3.0, 2026-11-23 - Strategist row added (session-5b02c501), seat count corrected to ten rows.
