---
title: D. Retro effectiveness
created: 2026-11-23T08:36:55Z
modified: 2026-11-23T08:36:55Z
version: 0.1.0
sequence: 5
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

- **Critical improvements proposed** - entries filed per retro,
  split by class. Critical means the entry addresses a named
  top leak of its retro; the retro marks them, the count is not
  inferred later.
- **Filing rate** - of the top leaks a retro names, the share
  that became backlog entries. A leak named twice with no entry
  is a filing failure and is itself named.
- **Closure rate and dwell** - entries closed over entries
  opened, per week, and the median days from opened to closed.
  Closure keeps the standing rule - the target metric moved, or
  the stated verification passed; an edit alone never closes.
- **Recurrence rate** - the core quality metric of this family.
  Of the improvements closed in a period, the share whose root
  cause class (the miss audit classes a to i, carried in the
  entry and in unit `blocker_category`) reappears in the done
  pool within 7 days of closure. A closed improvement whose
  problem comes back was a paper fix, and this metric is how
  the system knows.
- **Open roll-forward** - entries still open at each retro,
  counted and aged; the oldest open age feeds family G.

Thresholds - any recurrence is named (target zero). Closure
dwell has no threshold yet; two weeks of baseline come first.

Known defects - recurrence reads `blocker_category`, which
depends on executors filling it - family A's enforcement gap is
this family's data risk, and the queue tool validation filed in
the tool-developer backlog is the fix both families wait on.

