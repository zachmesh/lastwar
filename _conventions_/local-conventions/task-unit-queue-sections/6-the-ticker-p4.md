---
title: 6. The ticker and the executor loop part 4
created: 2026-11-23T09:03:48Z
modified: 2026-11-23T09:03:48Z
version: 0.1.0
sequence: 15
description: Release the token and go back to step 1.
---
5. Release the token and go back to step 1. Every unit boundary is
   a scheduling point - a VIP unit that lands while a background
   chain is mid-run waits at most for the current unit to end.
6. A reaper pass (part of the producer job) returns any `claimed`
   unit whose `lease_until` has passed to `inbox`, clearing the
   claim stamps. A crashed executor therefore strands at most one
   unit for at most one lease period - the direct fix for the
   2026-10-26 lock failure mode at the work level.
7. Dead letters - a unit whose `attempts` reach `max_attempts` is
   not requeued again. It moves to `done` with result status
   `failed`, and the stats report surfaces it, so a poison unit
   cannot spin the loop forever.

All steps are idempotent at the unit level - before acting, the
executor checks the game state the unit acts on (the standing
check-first rule), so a re-executed unit does not double-claim.

One honest limit - the loop runs inside the ticker's passes, not
as a literal daemon; between ticks the pool simply waits in
`inbox`. The unit cap is what makes that safe - no pass can be
captured by one task for longer than 15 minutes, and no unit can
starve the pool behind a long task the way the segment runs did.

