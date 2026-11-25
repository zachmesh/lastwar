---
title: 8. Migration from child sessions
created: 2026-11-23T09:04:37Z
modified: 2026-11-25T05:03:17Z
version: 0.2.0
sequence: 11
description: The first team used delegated child sessions.
---
## 8. Migration from child sessions

The first team used delegated child sessions. The organization now
moves to top-level DSH sessions, created through the DSH client RPC
with the local gate:

| Phase | Act | State |
|---|---|---|
| M0 | spawn six top-level seats (scout, researcher, planner, coach, toolsmith, scribe) | done 2026-11-23T04:01Z |
| M0b | spawn the top-level Coordinator; move the seat from the Steward; delete the Steward schedule | done 2026-11-23T04:04Z |
| M1 | verify each seat reads its brief and replies | in progress |
| M2 | after the operator's current unit closes, spawn `[Last War] Operator`; update its session id | pending |
| M3 | record the child sessions as predecessors in each handover; stop using them | pending |
| M4 | first full-team tick through `session-relay`; 24 h pilot | pending |
| M5 | weekly review: keep top-level or roll back | pending |

Rollback: if a top-level seat fails, revert its `TEAM.yaml` id to the
child session and record why. The child sessions remain until the
pilot passes.

The top-level sessions are created with:

```bash
DSH_WEB_URL=http://localhost:8080 SESSION_RELAY_JAR=/tmp/dsh-gate.cj \
  python3 ~/dtadpole/reflection/_tools_/session-relay/session-relay.py spawn \
  --workspace /Users/zhenchen/zachmesh/lastwar --title '[Last War] <Role>' \
  --model claude-sonnet-5-5 --effort high \
  --prompt-file /tmp/lw-<role>-bootstrap.md
```

The explicit `--model` and `--effort` are required: the relay's own default
is `claude-opus-5-5`, so a replacement seat spawned without them comes up on
the wrong model.

