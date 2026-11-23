---
title: Queue Tests
created: 2026-11-23T07:50:00Z
modified: 2026-11-23T13:40:23Z
version: 1.5.0
description: Tests for the queue unit serves key, run against throwaway pools in temporary git repositories
---

# Queue tests

Tests for the `serves` tag of a queue unit and the forecast checks built on it. Each pool is a throwaway repository under /tmp with the
tool's temp-dir and currency guards bypassed through `LASTWAR_QUEUE_ALLOW_*`, so nothing touches the live pool.

`test_serves.py`: `enqueue --serves` writes the key and a `Serves:` body line, folded to one line, empty refused; the key survives claim,
release and complete; `enqueue` refuses a unit with no serves unless its roster regular supplies one (default `upkeep`); `plan`, `sync` and
`sweep` copy the roster's serves; `validate` reports a live inbox unit without one as an error, a claimed upgrade-type one as a warning;
`sync` only warns.

`test_next_expired.py`: `next` never names a unit whose window has closed, and `claim` refuses one by name.

`test_forecast.py`: `validate` warns (never errors) for a live inbox unit whose serves names a plan item with no row in the newest
`_records_/<date>/strategy/forecast-ledger.csv`, or is neither a ledger plan item nor an exempt word, and for a missing ledger when a unit
needs it; counts and unit names only. `enqueue --require-forecast` refuses the same.

`test_require_forecast.py`: the switch `coordination.queue.require_forecast` in TEAM.yaml (off when absent) makes `enqueue`, the minting
of `plan`, `sweep` and `sync`, and `scout_diff.py`'s enqueue calls refuse a unit with no ledger row; `--no-require-forecast` overrides and
the refusal names it.

Run: `python3 -m unittest discover -s _tools_/queue-tests`.
