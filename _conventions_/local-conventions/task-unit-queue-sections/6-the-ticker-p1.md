---
title: 6. The ticker and the executor loop part 1
created: 2026-11-23T08:37:05Z
modified: 2026-11-23T08:37:05Z
version: 0.1.0
sequence: 9
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

The token file lives in the main checkout's `_queue_/claimed/`,
shared by every worktree of the repository, so a pass running in a
fresh detached worktree still sees a token held by a pass still
running (issue #383) - a worktree-local token would be invisible to
the next tick and the guard above would not hold. A re-acquire by the
same executor within 60 seconds of expiry renews the lease instead of
reporting held (issue #461) - the 2026-11-08 ticker-1049 secrets unit
re-acquired 3 seconds before expiry, was refused, and its game input
ran with no token held until the next acquire.

Latency is bounded and measurable - a fresh unit waits at most one
tick interval plus the remainder of the unit currently running
(itself capped at 15 minutes). Expiry-critical work is protected by
construction - the producer enqueues it ahead of its deadline
(reset and phase times are known in advance) and the loop picks
earliest expiry first. The stats report's `late` list is the
feedback signal - if units start finishing late, the interval
shortens to 15 minutes; the mechanism does not change.

The executor loop itself, run by the main agent inside the tick's
execute step, and equally by any owner-directed session that takes
the token.

