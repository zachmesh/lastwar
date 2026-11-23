---
title: 1. Scope and method
created: 2026-11-23T09:03:19Z
modified: 2026-11-23T09:03:19Z
version: 0.1.0
sequence: 2
description: Primary scope - every queue unit in _queue_/done whose result evidence points into _records_/2026-10-30/ or _records_/2026-10-31/.
---
## 1. Scope and method

- Primary scope - every queue unit in `_queue_/done` whose result
  evidence points into `_records_/2026-10-30/` or
  `_records_/2026-10-31/`. That is 196 units.
- Two owner-requested truck units (trucks-2026-10-31-0350 and
  trucks-2026-10-31-0423) carry an empty evidence field, but their
  follow-up text names records in `_records_/2026-10-30/truck-plunder/`
  (2052 and 2124 queue runs). They are included, which brings the
  audited total to 198 units - exactly the 198 execution record files
  in the two date folders (116 plus 82, day INDEX files excluded).
- The day trackers in `_tools_/state/2026-10-30.json` and
  `_tools_/state/2026-10-31.json` are last-write snapshots per regular
  (13 and 11 entries), not unit counts. Each shows one skipped entry,
  the Base Building Arms Race miss of that day. Both are already
  counted once in the queue scope and are not double counted here.
- Literal status check - no unit in scope carries the result status
  `miss`, `failed` or `expired`. A miss in this system is a narrative
  outcome (a tier-3 target not met, a daily quota short at the reset),
  recorded as `partial` or `skipped-needs-owner`. Across all 426 units
  in `_queue_/done`, the 7 `failed` units all carry evidence dated
  2026-10-28 or 2026-10-29 and are outside this audit window.
- Root cause assignment - each non-done unit gets exactly one primary
  cause, taken from the blocker named in its own result summary.
  Where the same blocker repeats across units, the repetition itself
  is the primary cause (category E). Secondary causes are named in
  the text. Counts therefore sum to the non-done total.

