---
title: Entry fields and 2 more
created: 2026-11-23T06:02:05Z
modified: 2026-11-23T06:02:05Z
version: 0.1.0
sequence: 2
description: id - OD- YYYYMMDD- n, assigned at filing, never reused.
---
## Entry fields

- id - OD-<YYYYMMDD>-<n>, assigned at filing, never reused.
- opened - the local date the item first needed a decision.
- item - the decision, in one line.
- context - the evidence, with record pointers.
- decision needed - the exact question put to the owner.
- age tracking - days since opened, recomputed by the retro
  at every run and reported with the item until it closes.
- status - open or decided (with the decision and its date
  recorded under the entry).

## Maintenance rules

- The daily retro maintains this register in the same run
  that maintains the improvements backlog - new
  skipped-needs-owner outcomes and new owner-gated items are
  filed here the day they occur.
- Every retro reports the open items with their ages in its
  delivery, however quiet the rest of the run is. An open
  item is never dropped from the report because it is old.
- When the owner decides, the retro records the decision
  and its date under the entry and marks it decided. The
  entry stays in this file as the decision's record.
- An item whose in-game window expires undecided is marked
  decided by expiry, with the expiry noted - it is never
  silently deleted.

## Open

