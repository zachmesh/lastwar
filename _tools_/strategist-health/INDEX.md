---
title: Strategist Health
created: 2026-11-23T09:09:13Z
modified: 2026-11-23T09:09:13Z
version: 1.0.0
description: strategist_health.py, the read-only counts-only check that the Strategist and its strategy are observed and learning, with tests
---

# Strategist health

`strategist_health.py` turns Steer A's prototype into a tool: is the Strategist observed and learning? It reads
`_records_/<date>/strategy/`, git's view of it and `session-relay.py inspect`; it writes nothing and prints counts only (no claim
text, no ids, no file names).

`python3 _tools_/strategist-health/strategist_health.py [--format json] [--no-session]`; exit 0 healthy, 1 an alarm, 2 unreadable.
Each threshold is a flag.

| Check | Alarm |
|---|---|
| durability | a strategy file untracked or uncommitted for over 2 h |
| freshness | newest key file over 12 h old; no plan of record |
| register | a claim lacks a test, an owner seat or a read-by date; an open claim is overdue |
| forecasts | Brier over 0.25; interval hit rate more than 20 points from 80; bias beyond 20 percent; no ledger beside a plan |
| session | the strategist's context at or over 75 percent |

Calibration scores binary and continuous rows only: deterministic and retired rows are excluded, as is a continuous row whose
point is not inside its interval. Under 5 scored rows it is a note, not an alarm. Errors are split by source tag (M, D, S, G).
Reliability is by probability band. A check with no data is n/a. The session id comes from the strategist seat in `TEAM.yaml`;
tests set `STRATEGIST_HEALTH_RELAY`.

Tests: `python3 -m unittest discover -s _tools_/strategist-health`.
