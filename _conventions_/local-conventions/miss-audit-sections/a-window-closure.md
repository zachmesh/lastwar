---
title: A. Window closure and deferral past the window - 6 units
created: 2026-11-23T09:03:19Z
modified: 2026-11-23T09:03:19Z
version: 0.1.0
sequence: 5
description: Instances -
---
### A. Window closure and deferral past the window - 6 units

Instances:

- arms-race-2026-10-30-0203 - Drone Boost 12,000 of 30,000, the
  18,000 gap left for the next re-check; the next Arms Race unit read
  a different phase, so the gap never closed
  (`_records_/2026-10-30/arms-race/0210-queue-run.md`).
- arms-race-2026-10-31-1003 - Drone Boost score 0, tier-3 gap 30,000
  left for the next re-check; the phase rolled before any re-check
  landed (`_records_/2026-10-31/arms-race/1010-queue-run.md`).
- trucks-2026-10-30-1457 - dispatch reached 5 of 5 at 17:28 with
  plunder 0 of 4 still pending; the next truck unit executed after
  the 19:00 reset under a new trade day, so that trade day closed
  with plunder unattempted in its final window
  (`_records_/2026-10-30/truck-plunder/1728-queue-run.md`).
- events-2026-10-30-1857 and events-2026-10-31-1857 - Events tabs
  left unscanned when the pass budget or unit cap ended
  (`_records_/2026-10-30/event-claims/1953-queue-run.md`,
  `_records_/2026-10-31/event-claims/2012-queue-run.md`).
- passes-2026-10-31-1857 - Hot Deals pack claimed, Weekly and Super
  tabs unchecked at the unit cap
  (`_records_/2026-10-31/shop-claims/2017-queue-run.md`).

Prevention rule A - a gap may never be left for the next re-check
across a window boundary. When a unit reads a phase or trade-day gap
with under 60 minutes to the window close, it either finishes inside
the unit or enqueues a priority 1 successor on disk with its expiry
set to the window close, and the closing summary names that successor.

