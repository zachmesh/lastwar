---
title: Model policy
created: 2026-11-23T07:02:07Z
modified: 2026-11-23T07:02:07Z
version: 0.1.0
sequence: 10
description: Owner decision, 2026-11-22 2022 PT - every DSH session under /Users/zhenchen/zachmesh/lastwar runs Claude Sonnet 5.5 at
---
### Model policy

Owner decision, 2026-11-22 20:22 PT: every DSH session under
`/Users/zhenchen/zachmesh/lastwar` runs **Claude Sonnet 5.5 at xHigh effort**
(`claude-sonnet-5-5`, `reasoningEffort: xhigh`, provider `meta-claude`).

- Applied through `session/selectModel` to the nine top-level sessions (the
  Steward, Coordinator and seven seats) and verified by `session-relay
  inspect`, which reports `model=claude-sonnet-5-5/xhigh` for each.
- The seven retired child-session predecessors are owned by subagent routing;
  the host refuses `selectModel` on them (`session/agent-busy`). They are idle
  and unused; they stay as they are until archived, and no new work goes to
  them.
- A running session picks the new model up at its next turn.
- The computer-use run model is a separate setting (`--model` on
  `cu_bridge.py start`, currently `claude-gateway/claude-sonnet-5-5`).

The gate supplies the cookie; no seat reads the DSH launch token.

