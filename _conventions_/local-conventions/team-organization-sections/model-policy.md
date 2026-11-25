---
title: Model policy
created: 2026-11-23T09:04:37Z
modified: 2026-11-25T05:03:17Z
version: 0.3.0
sequence: 12
description: Owner decision, 2026-11-22 2022 PT - every DSH session under /Users/zhenchen/zachmesh/lastwar runs Claude Sonnet 5.5 at
---
### Model policy

Owner decision, 2026-11-22 20:22 PT: every DSH session under
`/Users/zhenchen/zachmesh/lastwar` runs **Claude Sonnet 5.5** (`claude-sonnet-5-5`, provider `meta-claude`). The effort was
xHigh until the owner's request at the GUI, 2026-11-25 05:05Z, which set **High** (`reasoningEffort: high`).
- Applied through `session/selectModel`; `session-relay inspect` reports `model=claude-sonnet-5-5/high`. On 2026-11-25 the
  guard fixed nine idle seats and the coordinator re-pointed the running three; the guard reads `approved_effort: high` from `TEAM.yaml`.
- Child (subagent) sessions are refused by the host (`session/agent-busy`; 58 on 2026-11-25): they are finished and
  stay as they are.
- A running session picks the new model up at its next turn.
- The computer-use run model is a separate setting (`--model` on
  `cu_bridge.py start`, currently `claude-gateway/claude-sonnet-5-5`).

The gate supplies the cookie; no seat reads the DSH launch token.

### Persistence (OD-20261123-16, 2026-11-23)

The operator's respawn at 09:07Z came up on the host default, `claude-opus-5-5`, because a bare `session-relay spawn` keeps it. The owner ordered the policy to persist. Three layers hold it:

1. `_tools_/spawn-seat/spawn_seat.py` is the only way to spawn a seat. It passes the `TEAM.yaml` keys `coordination.execution.approved_model`, `approved_effort` and `approved_provider`, reads the model back with `inspect`, corrects an idle seat once, and fails loudly (exit 1) on a difference.
2. `_tools_/model-guard/model_guard.py` compares every roster seat with the policy, fixes idle seats with `--apply`, retries running ones at the next tick, and prints nothing at zero drift. The coordinator runs it in its tick and Steer A hourly.
3. This section, the record OD-20261123-16 and the three keys.

Respawn checklist:

1. `python3 _tools_/spawn-seat/spawn_seat.py --title "<seat title>" --prompt-file <bootstrap>`; never a bare spawn.
2. The printed read-back must be `claude-sonnet-5-5/high`; exit 1 means stop and tell the coordinator.
3. Confirm with `session-relay inspect`: `model=claude-sonnet-5-5/high`.
4. A running seat that drifts is left to `model_guard.py --apply`.

TEAM.yaml lists ten seats and the steward, eleven sessions in all, and the guard checks every one.
