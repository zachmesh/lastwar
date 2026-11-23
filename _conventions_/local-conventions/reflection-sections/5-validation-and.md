---
title: 5. Validation and honest limits
created: 2026-11-23T09:01:51Z
modified: 2026-11-23T09:01:51Z
version: 0.1.0
sequence: 8
description: tools_/regulars.json parses, the tracker lists daily-missions as due on the daily-reset rule, and a planner run
---
## 5. Validation and honest limits

- _tools_/regulars.json parses, the tracker lists daily-missions as
  due on the daily-reset rule, and a planner run against a scratch
  pool root produced the daily-missions unit for the current reset
  period alongside the other regulars, with no duplication on a
  second run. The live pool was not touched by the validation.
- The planner cannot yet express fixed clock slots such as 17:30
  and 18:30 - its cadences are the 4 hour segment anchors, the
  daily reset and Thursdays. Section 12 of the queue design
  documents the planner-side interface still to build and the
  manual enqueue practice in force until then. The sweep pair
  above was enqueued by that practice.
- These fixes change rules, scheduling and checklists. They do
  not play the game. Whether they work is measurable from the
  same place the audit read - the queue stats and the round
  summaries of the next days. The miss count, the unverified
  count and the named open items are the scoreboard.
