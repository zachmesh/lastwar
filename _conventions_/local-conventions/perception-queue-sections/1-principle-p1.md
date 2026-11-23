---
title: 1. Principle part 1
created: 2026-11-23T09:03:33Z
modified: 2026-11-23T09:03:33Z
version: 0.1.0
sequence: 2
description: Until now the day was defined by a static list - the 19 regulars in _tools_/regulars.json.
---
## 1. Principle

Until now the day was defined by a static list - the 19 regulars
in `_tools_/regulars.json`. The planner staged one unit per regular
per window, and the executor worked the list. The miss audit of
2026-10-31 showed the structural cost of that definition - work
the list did not name did not exist. Daily missions were modelled
but never scheduled. The Crystal Shop and the Glittering Market
sat outside the list entirely. State-dependent availability - a
train in preparation, a phase that just rotated, a market whose
contents changed - was discovered late or never, because nothing
looked at the game before deciding what the day contained.

The owner direction of 2026-10-31 inverts the flow -

- **Perceive first.** Scout units walk the game interface
  systematically and record what is actually available to do, as
  a structured observation.
- **Diff, then enqueue.** The observation is compared against
  the modelled work - the regulars, the daily collection ledger
  and the pool. Execution units are generated, updated or closed
  from what was seen, not from what the static list assumed.
- **The static list is the baseline, not the day.** The regulars
  still guarantee the floor - every modelled line is checked on
  its cadence whether or not a scout saw it. The scout layer adds
  the two things the list cannot do - discovering work outside
  the models, and confirming the real availability of work inside
  them.

The owner refinement of 2026-10-31 sharpens the principle one
step further -

