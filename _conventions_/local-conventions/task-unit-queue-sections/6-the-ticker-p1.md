---
title: 6. The ticker and the executor loop part 1
created: 2026-11-23T09:03:48Z
modified: 2026-11-23T09:03:48Z
version: 0.1.0
sequence: 12
description: One scheduled job drives everything - the ticker, firing every 30 minutes (owner direction 2026-10-28).
---
## 6. The ticker and the executor loop

One scheduled job drives everything - the **ticker**, firing every
30 minutes (owner direction 2026-10-28). The three segment
schedules are gone; there is nothing else to coordinate. Each tick
runs four steps.

1. **Reap** - return units whose leases expired to `inbox` (or
   dead-letter them when their attempts are spent).
2. **Produce** - ask the tracker what is due and enqueue one unit
   per due regular, idempotently, so a regular already queued or
   running is never duplicated. Chain continuations are enqueued at
   completion time by the executor (step 4 below); the producer
   only seeds a chain's first unit and tops up chains whose next
   unit is missing.
3. **Execute** - run the executor loop below until no due unit
   remains or the pass budget runs out (proposed 25 minutes,
   inside the 30 minute interval). Partial units requeue safely,
   so stopping mid-drain loses nothing.
4. **Skip** - when nothing was enqueued and nothing executed, the
   tick exits silently. An empty tick costs one tracker call.

Overlap is expected and harmless - a pass still executing when the
next tick fires holds the device token, and the new tick sees the
token held and skips its execute step. Only one pass ever plays.

