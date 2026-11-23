---
title: 11. Phased roadmap
created: 2026-11-23T08:37:03Z
modified: 2026-11-23T08:37:03Z
version: 0.1.0
sequence: 28
description: Phase 1 - this document and the modelling (landed with this change).
---
## 11. Phased roadmap

- **Phase 1 - this document and the modelling (landed with this
  change).** This design, the perception layer section of the
  task unit queue design, the observed items schema, the
  traversal checklist, and the scout regulars in
  `_tools_/regulars.json` with their activity metadata. Scout
  passes run as executor-produced chains under the existing
  planner; the diff of section 5 is applied by the executor
  from the observation file, by hand, under the rules above.
  Version 1.1.0 of this design, landed the same day under the
  owner refinement, re-based the layer on trigger-based
  scheduling - profiles instead of timetable entries, the
  trigger list and priority formula of section 5, the discovery
  protocol of section 6, and the anchored passes demoted to a
  guaranteed floor under rolling and change-triggered
  perception. The executor applies those rules by hand in this
  phase exactly as it applies the diff.
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
- **Phase 3 - reporting and promotion automated.** The coverage
  report, unmatched labels included, joins the round summary as
  a standing section, the unknown items naming becomes
  automatic, candidate filings and exploration units are
  produced by the tool from the unmatched labels, and the
  promotion of a proven candidate into an active profile is
  proposed by the tool from its exploration record - free and
  safe promotions land under the envelope of section 6, the
  rest still come to the owner with the evidence.

