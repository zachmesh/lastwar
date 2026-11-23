---
title: 13. The perception layer (scout) part 2
created: 2026-11-23T09:03:48Z
modified: 2026-11-23T09:03:48Z
version: 0.1.0
sequence: 44
description: Chain splitting.
---
- **Chain splitting.** One pass is one homogeneous chain of
  scout units, split by surface group - scout-base, scout-events,
  scout-store, scout-alliance - because a full traversal does not
  fit the 15 minute unit cap. The chain id is `scout-<reset
  date>` for the post-reset pass and `scout-mid-<reset date>`
  for the midday pass; the units run in order inside the pass
  window, and a unit that cannot finish its group closes partial
  with the unwalked surfaces named and a successor enqueued for
  the remainder. The regulars schema cannot express the split -
  cadence stages one unit per regular per window - so the staged
  unit is the chain head, and the executor extends the chain
  from it under the chain rules of section 2.
- **The observation output.** Every scout unit appends its
  surface sections to the day observation file,
  `_records_/<local date>/perception-scout/observation.md` - one
  file per reset day, append-only inside the day, carrying the
  day counters in its frontmatter and the observed items in the
  schema the perception document defines. The zero sweep of
  section 12 reads this file alongside the ledger, so observed
  items are swept by the same standard as modelled lines.
- **Result contract.** A scout unit result must reference the
  observed items it produced - `evidence` names the day
  observation file, `stats` carries surfaces_walked,
  items_observed, red_dots_seen, red_dots_explained,
  unexplained_red_dots and unknown_items, and `follow_up` names
  the units the diff enqueued or raised, or the unknowns
  awaiting exploration. A pass that closes with unexplained red
  dots closes partial - the zero unexplained red dots standard
  of the perception document is a closing condition, not a
  report nicety.
