---
title: 9. Tool - _tools_/scout_diff.py (Phase 2, implemented) part 5
created: 2026-11-23T09:03:33Z
modified: 2026-11-23T09:03:33Z
version: 0.1.0
sequence: 30
description: Idempotency - the tool obeys the pool invariant it feeds.
---
**Idempotency** - the tool obeys the pool invariant it feeds.
Produced units dedupe on (regular, planned_for) exactly as sync
and plan do. Dynamic units carry their source in their window
text and chain id, and the tool checks the pool for an existing
unit from the same observation item - same date, surface and
label - before enqueueing. A second run over the same
observation produces an empty enqueue plan and an unchanged
pool. The tool never completes, claims or deletes a unit - it
only proposes and, with `--enqueue`, enqueues.

**Priority support from the queue tool** - produced scout units
stage at priority 2, windowed work. The queue tool takes
production priority from its SYNC_PRIORITY table; the Phase 2
change landed `scout` and `scout-midday` there at priority 2,
with SYNC_EST_MINUTES seeds of 10 minutes each until the pool
learns better, instead of silently defaulting scout production
to priority 3. The tool reads its expected durations through
the queue tool learned estimates, so its priority formula and
the planner seeds never drift apart.

