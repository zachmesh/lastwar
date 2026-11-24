---
title: Forecast refusal on main by Steer A
created: 2026-11-24T10:50:43Z
modified: 2026-11-24T10:50:43Z
version: 1.0.0
description: Steer A run of the require_forecast switch on main at 10:49Z, no flags, TEAM.yaml 0.7.5, PR 959 - the five cases, an addendum to the branch-run record, which stays as written
status: done
activity: tool-development
run_id: steer-a-forecast-refusal-main-run-2026-11-24
---

# Forecast refusal on main, 2026-11-24

Steer A's run at 10:49Z on main (b341250ac, PR #959 land/forecast-flip-rb) in a scratch root, with main's `TEAM.yaml` 0.7.5 (`coordination.queue.require_forecast: true`, lines 70 and 71), main's `queue.py`, the real ledger and no flag. It adds to the [branch-run record](1030-forecast-refusal-probe.md), which describes the run before the flip and stays as written.

| Case | serves | Result |
|---|---|---|
| a | PL-99 | REFUSED: names a plan item id that has no row in the forecast ledger, nothing queued |
| b | no serves line | REFUSED |
| c | upkeep | ACCEPTED |
| d | PL-17 | ACCEPTED |
| f | PL-17 the Oil Well chain | REFUSED with the strict-rule text of PR #957: each comma or semicolon part must be a plan item id with a ledger row or an exempt word |

All 51 live inbox units classified ok. The scribe's read-only check of main's own code found both texts in `queue.py` and the same verdicts from `forecast_class` (PL-99 no row, PL-17 ok, upkeep ok, the chain unknown), and the 46 units then in the inbox all ok. Case a differs from the branch run only because that run wrote PL-99 with trailing words.

The emergency path `--no-require-forecast` stays; each use goes into the action log with its reason and the unit name.
