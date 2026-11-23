---
title: 11. Phased roadmap part 1
created: 2026-11-23T09:03:33Z
modified: 2026-11-23T09:03:33Z
version: 0.1.0
sequence: 37
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
