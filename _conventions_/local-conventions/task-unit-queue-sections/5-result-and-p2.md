---
title: 5. Result and result statistics part 2
created: 2026-11-23T09:03:48Z
modified: 2026-11-24T16:09:43Z
version: 0.2.0
sequence: 11
description: The matching _records_ execution file is still written as today (C1 append-only audit); the unit references
---
The matching `_records_` execution file is still written as today
(C1 append-only audit); the unit references it under `evidence`.

**The closing rule** - Steer A's rule of 2026-11-24 16:03Z (sheet `_records_/2026-11-22/queue-planning/3170-closing-rule-done-and-partial.md`). A unit closes `done` by one of two paths. (a) The claim it was staged for was TAKEN (the tap paid): the summary carries the counter or the card state read after the tap. (b) A verified nothing-to-claim, nothing-to-do state was READ in a frame (the card reads "Already claimed today", the station shows no train in preparation, the gate shows no survivor, the counter reads full): the result then carries ONE line with the key `state_read`, `state_read: <what was read, quoted> | <frame: step number or file> | <HH:MM:SSZ>`, for example `state_read: Already claimed today (S1) | step 6 frame | 15:07:44Z`; the key `evidence` stays the record path. A nothing-to-do without the line is `partial`, as is a unit that could not read the state (a blocked route, an alert, a foreground loss) or could not complete the route (a badge absent, a clipped claim): never close `done` to lower the partial rate. The Coach audits five `done` units a day and reports the share that carry the line in the strict pattern. `_tools_/queue.py complete` is to validate the pattern, a warning for the first week and then an error for a nothing-to-do `done` without it (pending, the Toolsmith).
