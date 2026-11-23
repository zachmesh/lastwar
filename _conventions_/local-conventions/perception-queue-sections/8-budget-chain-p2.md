---
title: 8. Budget, chain splitting and the observation file part 2
created: 2026-11-23T09:03:33Z
modified: 2026-11-23T09:03:33Z
version: 0.1.0
sequence: 25
description: Scout unit results.
---
**Scout unit results.** A scout unit completes through
`_tools_/queue.py complete` like any unit. Its result must carry -

- `evidence` - the day observation file.
- `stats` - surfaces_walked, items_observed, red_dots_seen,
  red_dots_explained, unexplained_red_dots, unknown_items.
- `follow_up` - the units the diff enqueued or raised, or the
  unknowns awaiting their exploration unit, named - never a bare
  `none` while the pass holds an open signal.

