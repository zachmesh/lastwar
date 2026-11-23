---
title: 9. Tool - _tools_/scout_diff.py (Phase 2, implemented) part 3
created: 2026-11-23T09:03:33Z
modified: 2026-11-23T09:03:33Z
version: 0.1.0
sequence: 28
description: The day observation file, _records_/ date/perception-scout/observation.md, parsed for its observed items.
---
- The day observation file,
  `_records_/<date>/perception-scout/observation.md`, parsed for
  its observed items.
- The observation `unmatched_labels` list - every label the
  passes met that no roster entry owns (section 3), the raw
  material of discovery.
- The candidate register - the provisional profiles under
  `_activities_` and their states (section 6), so a candidate
  already filed is recognised, not rediscovered.
- `_tools_/regulars.json` - the profile library index, read for
  its trigger conditions and deadline shapes, not only its
  cadences - the planner evolution of section 5 consumes
  observations plus profile triggers, and this tool is that
  consumer in program form.
- The daily collection ledger - its lines and the regular that
  produces each.
- The pool itself, read through the queue tool list and stats
  functions - what is already queued, claimed or done.

**Outputs**

