---
title: Item 4. Daily activity chests
created: 2026-11-23T08:37:03Z
modified: 2026-11-23T08:37:03Z
version: 0.1.0
sequence: 19
description: Verdict - cannot be confirmed from the records, and the agent-side gap is structural.
---
### Item 4. Daily activity chests

Verdict - cannot be confirmed from the records, and the agent-side
gap is structural. There is no daily missions execution at all on
either day.

- Neither date folder contains a daily missions record folder, and
  no unit of either day opened the Mission panel, read an activity
  points total, or claimed an activity chest.
- The reason is visible in the tooling - daily missions has
  activity metadata (`_activities_/daily-missions/INDEX.md`, which
  still carries only 2026-10-25 knowledge, activity 100 points with
  the 40 and 80 point chests claimed that day) but it is not one of
  the 18 regulars in `_tools_/regulars.json`, so the planner never
  produced a unit for it. This was not a failed execution. It was
  never scheduled.
- Whether the chests were claimed some other way, for example by
  the owner on his phone, cannot be confirmed or refuted from
  these records.

Prevention rule 4 - daily missions join the master collection
checklist and the pre-reset sweep even before any queue change is
decided - the sweep opens Mission, reads the activity points and
each chest state live, claims what is claimable, and records the
read. A checklist item with no producing unit is flagged as
unscheduled in the summary, not silently absent.

