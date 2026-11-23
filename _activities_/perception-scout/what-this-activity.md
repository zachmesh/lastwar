---
title: What this activity is
created: 2026-11-23T06:53:15Z
modified: 2026-11-23T06:53:15Z
version: 0.1.0
sequence: 2
description: The perception layer of the routine.
---
## What this activity is

The perception layer of the routine. A scout pass walks the
game interface systematically - base screen, HUD, Events hub,
Store by section, markets, alliance panel and station, mail,
duel and radar, world map, VIP, passes, daily missions - and
records what is actually available to do as structured observed
items. It exists because the miss audit of 2026-10-31 proved
that work no static model named was never done - the scout is
how the day finds out what it contains before the day is worked.

Executions are recorded in `_records_/<date>/perception-scout/`,
one observation file per reset day, appended to by every scout
unit of that day. The full design - traversal checklist,
completeness standard, observed items schema, diff rules - is
the [perception-driven queue](../../_conventions_/local-conventions/perception-driven-queue.md)
document in the local conventions. Section 13 of the task unit
queue design fixes the unit contract.

