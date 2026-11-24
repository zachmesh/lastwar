---
title: Forecast refusal probe by Steer A
created: 2026-11-24T10:33:11Z
modified: 2026-11-24T10:33:11Z
version: 1.0.0
description: Steer A probe of the require_forecast switch in a scratch queue root - five cases, the strict rule as implemented with two examples, the scratch path rule and the 51 live inbox units
status: done
activity: tool-development
run_id: steer-a-forecast-refusal-probe-2026-11-24
---

# Forecast refusal probe, 2026-11-24

Steer A's probe at 10:30Z, recorded by the scribe on Steer A's order. Setup: a scratch queue root (`/Users/zhenchen/workspace/lastwar-worktrees/steer-a-probe`, removed after; the tool refuses a pool under /tmp, issue #429, because a /tmp worktree can vanish mid-pass), origin/main's `_tools_/queue.py`, the `TEAM.yaml` of the flip commit 93ad21dae (`coordination.queue.require_forecast: true`, lines 70 and 71) and the real forecast ledger (181 rows).

## The five cases

| Case | serves | Result |
|---|---|---|
| a | PL-99, an imaginary plan item | REFUSED: neither a ledger plan item nor an exempt word |
| b | no serves line | REFUSED: a unit needs a serves line |
| c | upkeep | ACCEPTED |
| d | PL-17 | ACCEPTED |
| e | the PL-99 unit with `--no-require-forecast` | ACCEPTED, the emergency path |

## The rule as implemented

`forecast_class` in `queue.py` splits the serves line on commas and semicolons, and every part must be a ledger plan item id, an exempt word (upkeep, snapshot, baseline) or fill idle slot. `PL-17` and `PL-17, PL-08` pass; `PL-17 the Oil Well chain` and `PL-17; free text` are refused. It is strict by design: a unit cannot pass on wording. Steer A first wrote case d with trailing words and read the refusal as a defect; it is the rule. The Toolsmith is asked to word the refusal: each comma or semicolon part must be a plan item id with a ledger row or an exempt word.

## The live queue

All 51 inbox units classified ok under the flip, none would be refused. The scribe's read-only re-run at 1033 Z, with the tool's own `forecast_class` and ledger loader (18 plan items), found 50 units, all ok; one has left the inbox.

## Left for criterion 1

The merge of `land/forecast-flip` by the Integrator and the live `TEAM.yaml` carrying the key; Steer A then re-runs a, b and c against it with no override file.
