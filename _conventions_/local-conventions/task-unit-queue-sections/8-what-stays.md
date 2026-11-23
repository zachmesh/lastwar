---
title: 8. What stays the same
created: 2026-11-23T08:37:05Z
modified: 2026-11-23T08:37:05Z
version: 0.1.0
sequence: 13
description: The red lines, the kick rule for the different-device dialog, the Arms Race just-enough rule and
---
## 8. What stays the same

- The red lines, the kick rule for the different-device dialog, the
  Arms Race just-enough rule and every other standing order bind units
  exactly as they bind segment runs. A unit inherits its regular's
  activity metadata in `_activities_`.
- The regulars tracker stays the cadence source of truth; the pool is
  a work distribution layer over it, not a replacement.
- The `segment` field survives only as a reporting tag recording
  which slice a regular belonged to under the old routine; nothing
  schedules by it anymore.
- The round summary for Slack assembles from the `done` units'
  structured result sections, gathered by `_tools_/queue.py stats`,
  instead of three segment records. The same command doubles as the
  pool health report for the owner.

