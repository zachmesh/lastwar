---
title: Model Guard
created: 2026-11-23T09:20:47Z
modified: 2026-11-23T09:20:47Z
version: 1.0.0
description: model_guard.py, the quiet check that every roster seat runs the approved model, with tests
---

# Model guard

Owner order 2026-11-23: every seat runs Claude Sonnet 5.5 at xhigh. `model_guard.py` is Steer A's 45-line v1 rebuilt for the
coordinator's 15-minute tick: the roster is read with `yaml.safe_load` (the `seats` list and the `steward` block, skipping seats
with no session or a concluded assignment), the policy from `TEAM.yaml` `coordination.execution.approved_model`,
`approved_effort` and `approved_provider`.

`python3 _tools_/model-guard/model_guard.py [--apply] [--verbose] [--team TEAM.yaml]`

| Case | Result |
|---|---|
| no seat drifted | prints NOTHING, exit 0 (`--verbose` prints the table) |
| drift, no `--apply` | reports, exit 1 |
| idle seat, `--apply` | corrected through `session/selectModel`, read back, exit 0 |
| running seat | left, retried next tick, exit 1 |
| refusal, failed correction, unreadable session | reported, exit 1; the other seats are still checked |
| child or subagent session | informational, never touched |
| policy or roster unreadable | exit 2 |

Output holds seat keys, the first 16 characters of a session id, model names and states: no token, cookie, URL or relay output.
Spawn a seat with `_tools_/spawn-seat/`, never a bare `session-relay spawn`. Tests use `fake_relay.py` (`SESSION_RELAY_MODULE`):
`python3 -m unittest discover -s _tools_/model-guard`.
