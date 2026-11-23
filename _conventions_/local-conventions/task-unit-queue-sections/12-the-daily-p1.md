---
title: 12. The daily collection ledger and the pre-reset zero sweep part 1
created: 2026-11-23T09:03:48Z
modified: 2026-11-23T09:03:48Z
version: 0.1.0
sequence: 40
description: The daily collection ledger is the master list of everything collectible or due in one reset
---
## 12. The daily collection ledger and the pre-reset zero sweep

The [daily collection ledger](daily-collection-ledger.md) is the
master list of everything collectible or due in one reset day,
each line with the live read that closes it. It is part of this
design - a unit that works a ledger line closes it by the ledger
standard, and the round summary reports ledger lines with no
producing unit as unscheduled, never as absent.

**The zero sweep.** Twice before each daily reset - the absolute instant 02:00 UTC (about 18:00 PST in winter, 19:00 PDT in summer) - at 120 and 60 minutes before the reset instant (16:00 and 17:00 PST in winter, 17:00 and 18:00 PDT in summer), a sweep unit walks the ledger item
by item. Each line is read live - at zero, not at zero, or
unreadable. A line not at zero gets a priority 1 unit of its own
type enqueued before the sweep closes, named in the sweep record;
the final sweep repeats the walk so the fix-up units it spawned
are themselves verified. Both sweeps expire at the reset instant itself.

