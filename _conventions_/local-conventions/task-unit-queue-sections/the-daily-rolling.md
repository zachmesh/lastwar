---
title: The daily rolling retro
created: 2026-11-23T09:03:48Z
modified: 2026-11-23T09:03:48Z
version: 0.1.0
sequence: 53
description: Once a day, timed with the post-reset perception round, a retro pass looks back over the
---
### The daily rolling retro

Once a day, timed with the post-reset perception round, a
retro pass looks back over the past 7 days. Per task type it
reads the trends and names the largest loss points - where
target attainment leaks, where a blocker repeats, where time
goes without output. It produces improvement actions of two
kinds -

- **Execution knowledge** - what the game taught, written back
  into the corresponding `_activities_` profile with its
  version raised, under the hardening protocol of the
  perception document (section 10).
- **Meta knowledge** - what the system taught about itself -
  revisions to the scheduling triggers, the priority formula,
  the queue rules of section 11 or this design, proposed as
  document changes with their changelog entries.

Every improvement action carries its verification method and
the next-day recheck item that will prove or close it, written
into that day's retro file. An action not closed by its recheck
rolls into the next day's retro list - open actions are a
standing list, never a one-day note. The retro's headline
findings join the round summary as pointers to the retro file;
the file is the record, the summary is the pointer.

The retro itself, and every other standing activity of the
loop, is an execution and leaves its own record under the
[ops execution records](ops-execution-records.md) standard -
the retro measures the loop from those records, not from
session traces.

