---
title: 1. Principle part 2
created: 2026-11-23T08:37:03Z
modified: 2026-11-23T08:37:03Z
version: 0.1.0
sequence: 3
description: Scheduling is observation-triggered, not fixed-slot.
---
- **Scheduling is observation-triggered, not fixed-slot.** No
  execution unit exists because a clock slot said so. A unit is
  produced when perception fires a trigger from the list in
  section 5 - a badge turned claimable, a deadline approaching,
  a storage about to fill, a phase rotated, a train entering
  preparation, a quota behind pace, a new element on screen.
  Fixed time slots survive only as the safety net underneath -
  the cadence checks and the two anchored scout passes of
  section 7 are the floor that guarantees nothing modelled is
  ever left unchecked, never the primary mechanism and never
  the ceiling.
- **The regulars are a capability profile library.** Each known
  task is kept as a profile, not a timetable entry - its entry
  point, its rules, its red lines, the live read that verifies
  it, its trigger conditions, its deadline shape, its cooldown
  and its expected duration. Section 5 fixes the profile fields.
  The clock keeps only two jobs - the perception heartbeat (the
  ticker cadence that keeps perception rolling) and the game
  hard deadlines (the trade-day reset, absolute 02:00 UTC, Arms Race phase windows, the
  quota checkpoints of rule R3).
- **New tasks are discovered, not waited for.** Anything the
  screen shows that no profile owns enters the discovery
  protocol of section 6 - filed as a provisional candidate,
  learned by exploration units, promoted to an active profile
  and scheduled by the same triggers, or rejected with the
  reason kept. Discovery is part of comprehensiveness, not an
  exception path.

A scout unit never does the work it finds. It observes, records
and hands over. Execution stays one unit, one task type, under
the queue design - the scout layer changes where units come
from, not how they run.

