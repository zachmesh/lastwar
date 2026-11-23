---
title: 1. The diagnosis at establishment
created: 2026-11-23T07:20:36Z
modified: 2026-11-23T07:20:36Z
version: 0.1.0
sequence: 2
description: Measured from this checkout on 2026-11-22 at about 1900 PT, before any repair -
---
## 1. The diagnosis at establishment

Measured from this checkout on 2026-11-22 at about 19:00 PT, before
any repair:

| Observation | Reading | Source |
|---|---|---|
| Inbox units | 766, oldest unit window 2026-11-10 (12 units), then 2026-11-11 (3) | `_queue_/inbox` |
| Done units | 2,310 | `_queue_/done` |
| `queue.py next` | returned `scout-midday-2026-11-12-0700`, a unit about ten days past its window | tool output |
| Latest retro | 2026-11-21 | `_records_/retro/2026-11-21.md` |
| Duel days lost | five consecutive, duel day 6 lost whole | same retro, top leak 1 |
| Donations | 0 of 30 on a day the game ran | same retro, top leak 2 |
| Unverified rate | 91.3 percent | same retro, top leak 6 |
| Ledger coverage | 5 of 23 lines | same retro, top leak 5 |
| Unexplained red dots | one (red target badge) | same retro, top leak 7 |
| Recordless passes | ticker, planner, knowledge organiser, catch-all | same retro, top leak 9 |
| Prior executor | the Muse app, stopped on the owner's request this day | owner instruction |

The system did not fail because the game was unavailable. It failed
because the loop lost its clock, its queue hygiene, its verification
discipline and its recovery path at the same time. A new team that
simply resumes the old schedule would replay the same failure. The
first duty is therefore a measured reset, not a backlog burn-down.

