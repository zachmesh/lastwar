---
title: Open link 1 - scout_diff auto-invocation (highest priority) and 2 more
created: 2026-11-23T09:06:14Z
modified: 2026-11-23T09:06:14Z
version: 0.1.0
sequence: 2
description: scout_diff.py exists and is validated, but nothing runs it automatically after scout units produce an observation.
---
## Open link 1 - scout_diff auto-invocation (highest priority)

scout_diff.py exists and is validated, but nothing runs it
automatically after scout units produce an observation. The wiring
step is a planner cron body change (after plan: read the newest
observation, run scout_diff dry-run, then --apply against the live
pool root). Pending owner approval in chat on 2026-10-31. Until it
lands, the perception-to-queue link works only when an operator
runs the tool by hand.

## Open link 2 - pre-reset sweep production is manual

The 17:30 / 18:30 zero-sweep pair is not produced by the planner
(it cannot express fixed time slots; queue design section 12 notes
the interface as pending). The 2026-11-02 pair was hand-enqueued
again on 2026-10-31 (chain pre-reset-sweep-2026-11-02). Structural
fixes, either acceptable: planner fixed-slot production, or a
pre-reset scout anchor in regulars whose observation feeds
scout_diff fix-up enqueueing (depends on open link 1).

## Open link 3 - measurement is detected, not enforced

Unit result stats (queue design section 14) are filled by executor
discipline. The retro counts closings with missing or unverified
stats, so the loop detects bad data, but queue.py complete does
not yet validate required fields. Validation is tooling backlog
item (b) in the tool-developer job. retro_report.py (backlog item
(a), in build on 2026-10-31) covers the aggregation half.

