---
title: Spawn Seat
created: 2026-11-23T09:18:27Z
modified: 2026-11-23T09:18:27Z
version: 1.0.0
description: spawn_seat.py, the only way to spawn a roster seat, with the model fixed from TEAM.yaml and read back
---

# Spawn seat

Owner order 2026-11-23: every seat runs Claude Sonnet 5.5 at xhigh. `session-relay spawn` defaults to claude-opus-5-5, so a bare
spawn brought the operator up on the wrong model. A seat is spawned ONLY with this command; a bare `session-relay spawn` for a
seat is forbidden.

`python3 _tools_/spawn-seat/spawn_seat.py --title TITLE [--prompt-file F] [--goal-file F] [--workspace DIR] [--dry-run]`

It reads `coordination.execution.approved_model`, `approved_effort` and `approved_provider` from `TEAM.yaml` (yaml.safe_load) and
passes them to the relay's spawn; there is no `--model`, `--effort` or `--provider`. Then it READS THE MODEL BACK with
`inspect`; if it differs and the seat is idle it runs `session/selectModel` once and reads again; if it still differs, a spawn
step failed or the model cannot be read, it FAILS LOUDLY (exit 1, message on stderr, the session id still printed). A running
seat cannot be changed, so `model_guard.py --apply` corrects it later. Success prints the session id and the read-back model,
nothing else: no token, cookie, URL or relay output. Exit 0 verified, 1 not verified, 2 policy or argument unusable.

Tests use `fake_relay.py` (`SESSION_RELAY_MODULE`): `python3 -m unittest discover -s _tools_/spawn-seat`.
