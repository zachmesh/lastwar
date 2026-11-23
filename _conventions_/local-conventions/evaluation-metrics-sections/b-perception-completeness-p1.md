---
title: B. Perception completeness part 1
created: 2026-11-23T09:02:25Z
modified: 2026-11-23T09:02:25Z
version: 0.1.0
sequence: 4
description: Per perception day.
---
## B. Perception completeness

Per perception day. Sources - the day observation file
`_records_/<date>/perception-scout/observation.md`, the scout
diff coverage output `scout-coverage-<date>.md` (and its JSON
form) written beside it, the zero sweep records under
`_records_/<date>/daily-activities/`, and the 23 lines of the
[daily collection ledger](daily-collection-ledger.md).

- **Ledger coverage** - ledger lines closed on a live read that
  day, over 23. A line closed as explicitly unverified under
  the ledger standard counts as read; a line never walked
  counts as not covered. The two pre-reset sweeps are the
  primary walk; scout and producing-unit reads close lines the
  same way when they carry the closing read.
- **Unexplained red dots** - `unexplained_red_dots` from the
  coverage report. The completeness standard of the perception
  design (its section 3) already fixes the target - zero, every
  day, no exceptions averaged away.
- **Conversion** - observed to actionable to enqueued:
  `actionable_items` over `items_observed`, and (`to_enqueue`
  plus `already_queued` plus `raises`) over `actionable_items`.
  `already_satisfied` and `not_actionable` are reported with
  their reasons so a falling conversion is diagnosable - a drop
  caused by more items being read as already satisfied is
  health, a drop caused by red-line blocks is information, a
  drop with neither is a diff defect.
- **Perception latency** - for each enqueued unit, its
  `created_at` in the pool minus the time of the observation
  pass that saw its item. Reported as median and maximum per
  day where both timestamps exist.

