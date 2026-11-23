---
title: 9. Tool - _tools_/scout_diff.py (Phase 2, implemented) part 1
created: 2026-11-23T08:37:03Z
modified: 2026-11-23T08:37:03Z
version: 0.1.0
sequence: 20
description: Implemented 2026-11-01 as _tools_/scout_diff.py (standard library only), to the design this section fixed in Phase 1.
---
## 9. Tool - _tools_/scout_diff.py (Phase 2, implemented)

Implemented 2026-11-01 as `_tools_/scout_diff.py` (standard library
only), to the design this section fixed in Phase 1. The tool is
the diff of section 5 as a program, so the step from observation
to queue stops depending on an executor remembering to do it.

**CLI usage**

```text
_tools_/scout_diff.py --observation FILE [--date YYYY-MM-DD]
                    [--out DIR] [--root POOL] [--repo DIR]
                    [--regulars FILE] [--ledger FILE]
                    [--now ISO] [--apply] [--format text|json]
```

- The observation is the day observation file, or any file in the
  same shape - a Markdown or YAML text carrying `observed_items`
  blocks (frontmatter, fenced or body blocks all count, because
  every pass of the day appends to one file) plus any
  `unmatched_labels` lists, or a JSON document with the same keys
  at any depth.
- Without `--apply` the tool is a dry run - it writes its three
  outputs and changes no pool. With `--apply` it writes the
  enqueue plan into the pool through `_tools_/queue.py enqueue`,
  one call per unit, so every unit it creates passes the same
  validation as a manual enqueue - the cap check, the chain
  homogeneity check, the file layout. `--apply` refuses to run
  unless the pool root is named explicitly with `--root`; pool
  reads for the dedupe checks and the learned estimates likewise
  happen only against a named root.
- Outputs land in `--out` (default - a `scout-diff-output` folder
  beside the observation file), named with the date - the enqueue
  plan as JSONL (one `queue.py enqueue` argument set per line,
  each entry carrying its action - enqueue, already-queued or
  raise - and its source items), the candidate filings, and the
  coverage report.
- `--now` pins the clock for the priority formula and the
  production windows; it exists for tests and replays. Production
  runs leave it unset.

**Inputs**

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

