---
title: 8. Rollout and acceptance
created: 2026-11-23T07:20:36Z
modified: 2026-11-23T07:20:36Z
version: 0.1.0
sequence: 13
description: Phase Duration Output Acceptance
---
## 8. Rollout and acceptance

| Phase | Duration | Output | Acceptance |
|---|---|---|---|
| P0 reset | first 3 planner passes | clean queue, baseline dashboard | no inbox unit older than one window; `validate` exits 0 |
| P1 play | first 24 h | at least one done unit per hour of game availability | tick yield at or above 0.75; every done unit has stats |
| P2 discover | first 3 days | full ledger walk, two research notes per day | coverage at or above 20 of 23; unexplained red dots zero on two days |
| P3 learn | first 7 days | three improvements closed with verified movement | recurrence zero; weekly review names one meta-change |

The pilot is reviewed at 24 hours and 7 days. A phase that misses
its acceptance is not declared done; it is re-planned with the
measured gap and one named change.

