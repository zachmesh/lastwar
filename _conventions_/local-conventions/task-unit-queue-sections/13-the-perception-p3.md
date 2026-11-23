---
title: 13. The perception layer (scout) part 3
created: 2026-11-23T09:03:48Z
modified: 2026-11-23T09:03:48Z
version: 0.1.0
sequence: 45
description: Dynamic production.
---
- **Dynamic production.** Units created from an observation are
  ordinary units - they pass the same enqueue validation, obey
  the (regular, planned_for) invariant where the planner
  produces them, and carry their source observation in their
  window text when the diff creates them. Unknown items enter as
  priority 2 exploration units and are governed by rule R5 from
  their first day. The diff itself is a program since Phase 2 -
  `_tools_/scout_diff.py` reads the day observation file, diffs it
  against the regulars, the `_activities_` roster with its
  candidate register, the ledger and the pool, and produces the
  enqueue plan, the candidate filings and the coverage report
  (dry run by default; `--apply` enqueues through this tool,
  only against an explicitly named pool root).
