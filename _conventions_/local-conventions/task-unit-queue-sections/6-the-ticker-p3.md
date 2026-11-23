---
title: 6. The ticker and the executor loop part 3
created: 2026-11-23T08:37:05Z
modified: 2026-11-23T08:37:05Z
version: 0.1.0
sequence: 11
description: All steps are idempotent at the unit level - before acting, the executor checks the game
---
All steps are idempotent at the unit level - before acting, the
executor checks the game state the unit acts on (the standing
check-first rule), so a re-executed unit does not double-claim.

One honest limit - the loop runs inside the ticker's passes, not
as a literal daemon; between ticks the pool simply waits in
`inbox`. The unit cap is what makes that safe - no pass can be
captured by one task for longer than 15 minutes, and no unit can
starve the pool behind a long task the way the segment runs did.

