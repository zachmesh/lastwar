---
title: 11. Phased roadmap part 2
created: 2026-11-23T09:03:33Z
modified: 2026-11-23T09:03:33Z
version: 0.1.0
sequence: 38
description: Phase 2 - the diff tool and the planner hookup (implemented 2026-11-01).
---
- **Phase 2 - the diff tool and the planner hookup
  (implemented 2026-11-01).** `_tools_/scout_diff.py` is
  implemented to the design of section 9 - dry run by default,
  `--apply` only against an explicitly named pool root - and
  the queue tool priority entries for the scout regulars are
  landed (SYNC_PRIORITY and SYNC_EST_MINUTES in
  `_tools_/queue.py`). The tool was validated on a scratch pool
  against a synthetic observation covering a known actionable
  item, known items blocked by state and by red line, an unknown
  candidate and unmatched labels - classification, the priority
  formula, apply and rerun idempotency (second run zero new)
  all asserted. What remains of this phase is operational, not
  design: the planner pass runs the tool after each scout chain
  completes, so dynamic units land in the pool without waiting
  for an executor to transcribe them; wiring that invocation
  into the scheduled planner's instructions is an operations
  step outside this document. This is also where the planner
  changes species - from staging units by time slot to
  consuming observations plus profile trigger conditions and
  producing units when triggers fire, with the slot staging
  kept only as the floor check of section 5. Version 1.2.0 of
  this design, landed the same day, adds the learning and
  knowledge hardening protocol of section 10.
