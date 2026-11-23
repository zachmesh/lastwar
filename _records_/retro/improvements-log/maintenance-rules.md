---
title: Maintenance rules
created: 2026-11-23T06:02:05Z
modified: 2026-11-23T06:02:05Z
version: 0.1.0
sequence: 3
description: The daily retro updates statuses every run and is the only role that closes an entry.
---
## Maintenance rules

- The daily retro updates statuses every run and is the only
  role that closes an entry. An entry closes only when its
  target metric actually moved, or its stated verification
  passes. Merged code or an edited document alone never
  closes an entry.
- The fixer roles (tool developer, knowledge organizer, and
  this retro's own write-backs) may move an entry to
  implemented with the commit or PR that carries the fix -
  never to closed.
- A closed entry whose root cause recurs within 7 days is
  reopened by the retro and counted in the recurrence metric
  of evaluation metrics family D.
- New entries are inserted in leak-size order within their
  status group - the largest leak first - so the top of the
  open list is always the next thing to work on.
- Owner-decision items are not improvement entries. They live
  in the companion register `owner-decisions.md` in this
  folder and are maintained by the retro alongside this file.

