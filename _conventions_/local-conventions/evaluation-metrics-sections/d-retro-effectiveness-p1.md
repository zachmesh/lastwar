---
title: D. Retro effectiveness part 1
created: 2026-11-23T09:02:25Z
modified: 2026-11-23T09:02:25Z
version: 0.1.0
sequence: 8
description: Per retro and rolling.
---
## D. Retro effectiveness

Per retro and rolling. Sources - the retro's own execution
records at `_records_/<date>/retro-review/` are the
authoritative source for the run itself (that it ran, when,
what it filed), under the
[ops execution records](ops-execution-records.md) standard;
the improvements backlog `_records_/retro/improvements.md`,
one entry per improvement task carrying its id, its class
(execution-knowledge, meta-knowledge, tooling,
knowledge-organization), the leak it addresses, its target
metric with the value at filing, its verification method, its
opened date, its status and its closing date, is the source
for entry state. Commit and PR traces are cross-check only,
never the source. The backlog file is created by the first
retro that files into it; entry-state metrics are data-gaps
until it exists, while run metrics read from the execution
records from 2026-10-31 onward (period 0 reconstructed).

