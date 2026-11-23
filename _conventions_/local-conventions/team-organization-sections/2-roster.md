---
title: 2. Roster
created: 2026-11-23T07:02:07Z
modified: 2026-11-23T07:26:00Z
version: 0.2.0
sequence: 3
description: Eight seats; the coordinator plus seven roles.
---
## 2. Roster

Eight seats; the coordinator plus seven roles. All eight are now
`assigned` in `TEAM.yaml` with a session id.

| Seat | Session | Mission | Primary output | Cadence |
|---|---|---|---|---|
| coordinator | `session-4b4cb08d-fb77-419a-be34-14a72a3b73d1` `[Last War] Coordinator` | clock, routing, roster | tick record, assignment, TEAM.yaml | 15 min |
| operator | child `session-238b9ce7...` until migration | play one bounded unit | unit result + per-unit record | every tick |
| scout | `session-d658da6d-95f9-4762-9648-b4e208b55c08` | perceive the whole surface | observation pass, candidate list | every 2 h |
| researcher | `session-4335084a-3125-486d-9b61-03d23737b5f7` | internet + local reasoning | research note with a falsification test | 2 per day |
| planner | `session-c2652e1a-8fa4-4468-8d44-6d351762ed67` | queue hygiene and staging | planner record, clean queue | hourly |
| coach | `session-953a3676-cf57-4be2-8008-0ee9bc294d2d` | measure, retro, improve | dashboard, retro, backlog | daily |
| toolsmith | `session-339995b4-ebd2-4710-94a1-fcc946be01cf` | tool and automation fixes | tested diff, PR | on assignment |
| scribe | `session-c104e601-b16b-49cf-95a7-888543eb2499` | fold knowledge, keep conventions current | profile/PR | on assignment |
| integrator | `session-bc838015-7852-464e-8cab-cf2fcc70a335` | land branches on the protected main (merge commit, head SHA guard, read main back) | GitHub PR operations; `_records_/<date>/integration/` | on landing request |

The roster has 9 rows: the coordinator plus 8 seats. The integrator is one disjoint role (landing on a protected main) with no write conflicts, reviewed daily; the owner gateway (Steer A, owner-gateway, steer and watchdog) sits outside the roster and is not the integrator.
