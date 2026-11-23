---
title: E. Tool developer impact
created: 2026-11-23T09:02:25Z
modified: 2026-11-23T09:02:25Z
version: 0.1.0
sequence: 10
description: Per tool landing, rolled up weekly.
---
## E. Tool developer impact

Per tool landing, rolled up weekly. Sources - the tool
developer's execution records at
`_records_/<date>/tool-development/` are authoritative for
deliveries, validation and timing, under the
[ops execution records](ops-execution-records.md) standard;
the tooling entries of the improvements backlog carry the
filed dates and target metrics; the target metric series
lives in the dated retro data files. The git history of
`_tools_/` is cross-check only - a landing with no execution
record is treated as not proven to have happened.

- **Tools delivered** - tooling entries reaching implemented
  per period, and the median days from filed to implemented.
- **Target metric movement** - every tooling entry must name,
  at filing time, the one metric it exists to move (from any
  family in this specification) and its value at filing. Impact
  is the metric's 7 day window before the landing commit
  against the 7 day window after it, reported as the pair of
  values with the landing date between them - never as a single
  improvement percentage with the windows hidden. Standing
  examples - the unverified rate (family A) around the queue
  tool stats validation; the perception conversion rate
  (family B) around the scout diff auto-invocation; the p90 and
  attempts availability itself around the extension filed
  below.
- **No-target landings** - a tool that lands with no target
  metric named at filing is counted here, by name. It may still
  be worth building; it is not allowed to claim impact.

Known defects - windows are small and the game is not a
laboratory; duel posture, event calendars and the owner's own
play all move the same metrics. The before and after pair is
evidence for the retro's judgement, not a proof, and is written
that way in the retro file.

