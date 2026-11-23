---
title: Queue Planning Researcher Verifier Units 2480 2026-11-23
created: 2026-11-23T01:54:00-08:00
modified: 2026-11-23T01:54:00-08:00
level: L0
version: 1.0.0
description: Planner staging of the Researcher's three falsification units for assignment A-20261123-0945 - T1 donation tap twice, T2 donation cost, T3 check-in Go - with window choices, the guard gap that preceded them, and the retirement of a redundant store unit
status: done
activity: queue-planning
run_id: queue-planning-2026-11-23-0154-verifier-units
trigger: Researcher assignment A-20261123-0945, confirmed by the coordinator after the live tool sync
started_at: 2026-11-23T01:49:00-08:00
finished_at: 2026-11-23T01:54:00-08:00
verified: the four units read back with serves and windows; pool simulated with and without them; validate exit 0 under the serves-enforcing tool
grounded_in:
  - source: _records_/2026-11-22/research/playbook-card-tests.csv and the three brief files beside it
  - source: _tools_/queue.py refuse_if_tool_stale
---

# Researcher verifier units, 2480

## 1. Staged

Each carries `--serves "playbook card test Tn for OD-20261123-15"` and points at its brief under `_records_/2026-11-22/research/` (under 310 words).

| Unit | Window (Z) | Rule |
|---|---|---|
| `donations-playbook-t1-2026-11-23-001` | 13:10 to 15:10 | run only if the entry count is 1 or 2 right after a donations unit |
| `donations-playbook-t1-2026-11-23-002` | 14:20 to 16:20 | second trial, only if the first finished at least 60 minutes earlier |
| `donations-playbook-t2-2026-11-23-001` | 10:00 to 14:45 | read-only |
| `passes-playbook-t3-2026-11-23-001` | 13:30 to 15:45 | one click on Go, stop and record needs-owner if a browser takes the front |

## 2. Why these windows

A first simulation put T1 at 12:48Z, against the 12:51Z Secrets claim, and the second T1 only 18 minutes later, so I moved them behind the claim and the 13:00Z power read and 70 minutes apart. The four tests add no expiry to the pool. T1 needs a count of 1 or 2, which is only likely right after a donations unit; the queue orders by expiry and cannot say right after, so the coordinator may dispatch T1 by name just after one. T3 is the riskiest surface (a browser or the web store may take focus).

## 3. Guard gap

The sync after PR 885 arrived late: `enqueue` was refused at 09:50:32Z and `next` at 09:50:43Z, I polled, and the guard cleared at 09:52:28Z, when the four units were minted. No bypass flag was used. The sync commit named by the coordinator is eaa68756.

## 4. ST1b

The store follow-up was done by a direct assignment, so unit `-021` was redundant. It is tracked by git now, so I did not delete it; I set its expiry to 09:54Z and `sync` retires it as an expired unit. The two card statuses the Researcher flagged as over-claimed (alliance-donations R1 and shop-claims digest 9) go to the scribe, not to me.
