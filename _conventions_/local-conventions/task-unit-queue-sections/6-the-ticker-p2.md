---
title: 6. The ticker and the executor loop part 2
created: 2026-11-23T09:03:48Z
modified: 2026-11-23T09:03:48Z
version: 0.1.0
sequence: 13
description: The token file lives in the main checkout's _queue_/claimed/, shared by every worktree of the repository,
---
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

1. Take the device token. No token, no game input - whoever holds
   it finishes their unit first (at most 15 minutes). Contention
   becomes a short wait, never a collision or a stand-down.
