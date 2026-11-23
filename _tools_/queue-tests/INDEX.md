---
title: Queue Tests
created: 2026-11-23T07:50:00Z
modified: 2026-11-23T17:06:03Z
version: 1.7.0
description: Tests for the queue unit serves key, run against throwaway pools in temporary git repositories
---

# Queue tests

Tests for the `serves` tag of a queue unit, the forecast checks built on it, the device token and the unit brief. Each pool is a throwaway
repository under /tmp with the tool's temp-dir and currency guards bypassed through `LASTWAR_QUEUE_ALLOW_*`, so the live pool is never touched.

`test_serves.py`: `enqueue --serves` writes the key and a `Serves:` line, empty refused; the key survives claim, release and complete; `enqueue`
refuses a unit with no serves unless its roster regular supplies one; `plan`, `sync` and `sweep` copy the roster's; `validate` reports a live
inbox unit without one as an error, a claimed upgrade-type one as a warning; `sync` only warns. `test_roster_serves.py` holds the roster to it:
every `serves` is an exempt word or a plan item with a ledger row.

`test_next_expired.py`: `next` never names a unit whose window has closed, and `claim` refuses one by name.

`test_forecast.py`: `validate` warns (never errors) for a live inbox unit whose serves names a plan item with no ledger row, or is neither a
ledger plan item nor an exempt word, and for a missing ledger when a unit needs it; counts and unit names only.

`test_require_forecast.py`: the switch `coordination.queue.require_forecast` in TEAM.yaml (off when absent) makes `enqueue`, the minting of
`plan`, `sweep` and `sync`, and `scout_diff.py`'s enqueue calls refuse a unit with no ledger row; `--no-require-forecast` overrides.

`test_token_lease.py`: `token-acquire --lease-minutes N` (1 to 60, default 15) and `--exclusive`, which makes `claim` refuse every other
executor while the token is live (`claim --ignore-token` passes); an ordinary token never blocks a claim.

`test_unit_brief.py`: every unit minted for a roster regular - `plan`, `sweep` and its fix-ups, `sync`, `enqueue` - carries the `## Brief`
definition block; a pointer to a missing file is left out; every roster regular has its digest and INDEX tracked.

Run: `python3 -m unittest discover -s _tools_/queue-tests`.
