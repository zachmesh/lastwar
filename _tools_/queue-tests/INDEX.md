---
title: Queue Tests
created: 2026-11-23T07:50:00Z
modified: 2026-11-24T16:21:10Z
version: 1.9.0
description: Tests for the queue unit serves key, run against throwaway pools in temporary git repositories
---

# Queue tests

Tests for the `serves` tag of a queue unit, the forecast checks built on it, the device token, the unit brief and `complete`'s `state_read`.
Each pool is a throwaway repository under /tmp with the tool's guards bypassed (`LASTWAR_QUEUE_ALLOW_*`) and a TEAM.yaml that does
not exist (forecast switch off) unless a test writes its own; the live pool is never touched.

`test_serves.py`: `enqueue --serves` writes the key and a `Serves:` line, empty refused; the key survives claim, release and complete; `enqueue`
refuses a unit with no serves unless its roster regular supplies one. `test_roster_serves.py`: every roster `serves` is an exempt word or a ledger plan item.

`test_next_expired.py`: `next` skips a unit whose window has closed; `claim` refuses one by name.

`test_forecast.py`: `validate` warns (never errors) for a live inbox unit whose serves has no ledger row or fails the strict rule (each comma or
semicolon part must be a ledger plan item or an exempt word), and for a missing ledger; counts only.

`test_require_forecast.py`: the switch `coordination.queue.require_forecast` in TEAM.yaml makes `enqueue`, the minting of `plan`, `sweep` and
`sync`, and `scout_diff.py` refuse such a unit, saying which rule failed; `--no-require-forecast` overrides, and a unit it saved from refusal
is marked `forecast_override`, counted by `queue.py forecast-overrides`.

`test_token_lease.py`: `token-acquire --lease-minutes N` (1 to 60) and `--exclusive` (`claim` refuses others).

`test_unit_brief.py`: every unit minted for a roster regular carries the `## Brief` block.

`test_state_read.py`: `complete --state-read` (or a `state_read:` line in the summary) stores `result.state_read` beside `evidence`, its
pattern `what was read | step N or file | HH:MM:SSZ` checked (a mismatch is a warning); `--state-change yes|no` stores the unit's declaration;
with `require_state_read` on, a `no` DONE without a valid line is downgraded to partial with a note, never refused.

Run: `python3 -m unittest discover -s _tools_/queue-tests`.
