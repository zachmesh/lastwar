---
title: L1 - execution effectiveness
created: 2026-11-23T07:20:36Z
modified: 2026-11-23T07:20:36Z
version: 0.1.0
sequence: 5
description: Sources are the per-unit result fields in _queue_/done and the canonical appendix _records_/retro/ date-data.json.
---
### L1 - execution effectiveness

Sources are the per-unit `result` fields in `_queue_/done` and the
canonical appendix `_records_/retro/<date>-data.json`. The measures
are the ones [evaluation metrics](evaluation-metrics.md) family A
already specifies - done rate, duration median and p90, attempts,
target attainment, resource yield, points per minute, unverified
rate and blocker category - read per regular and per day.

Additions for continuous play:

- **Tick yield** - the share of 15-minute ticks that closed at least
  one done unit. A tick that only re-read state is not a yield.
- **Token wait** - seconds an operator waits for the one device
  token, per hour. This is the serialisation cost of one account.
- **Freshness** - the age of the oldest inbox unit the operator could
  have picked. Anything over one window is queue debt, not work.

