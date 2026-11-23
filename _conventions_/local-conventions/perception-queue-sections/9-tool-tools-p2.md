---
title: 9. Tool - _tools_/scout_diff.py (Phase 2, implemented) part 2
created: 2026-11-23T09:03:33Z
modified: 2026-11-23T09:03:33Z
version: 0.1.0
sequence: 27
description: The observation is the day observation file, or any file in the same shape - a
---
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

