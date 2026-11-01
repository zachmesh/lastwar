---
title: Owner decisions register
created: 2026-11-01T05:42:09Z
modified: 2026-11-01T05:42:09Z
version: 1.0.0
description: The standing register of items that only the owner can decide - each with its context, the exact decision needed, and its age - maintained by the daily retro and reported until decided
status: active
grounded_in:
  - source: owner instruction of 2026-10-31 - add or modify steps so every open item has a closed loop
  - source: improvements backlog in this folder - the companion register IMP-20261031-08
---

# Owner decisions register

Items the loop cannot close by itself, because the decision
belongs to the owner alone - a red-line exception, a one-off
in-game choice, anything consequential that the standing
rules deliberately leave unapproved. The register exists so
a pending decision ages in the open instead of sinking after
one mention in a summary.

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

### OD-20261031-01 - arms race phases with no scoring path inside the red lines

- opened: 2026-10-31
- item: whether Arms Race Base Building and Tech Research
  phases may ever use an exception means when no scoring
  path exists inside the standing red lines.
- context: these phases repeatedly close as
  skipped-needs-owner with a tier-3 gap of 30,000 and every
  scoring path inside a red line. On 2026-10-31 alone, three
  units closed this way - Tech Research at 02:11 (research
  queues idle, no completion landing in the window) and Base
  Building at 06:15 and 18:44 (building queue holding only
  long upgrades). Records -
  _records_/2026-10-31/arms-race/0211-queue-run.md,
  0615-queue-run.md and 1844-queue-run.md. Earlier instances
  of the same pattern are in the miss audit of 2026-10-31,
  root cause class g.
- decision needed: give a standing exception rule for these
  phases (and its limits), or keep deciding case by case -
  in which case each occurrence keeps filing here until
  answered.
- age tracking: opened 2026-10-31, age 0 days at filing;
  the retro recomputes and reports the age every run.
- status: open

### OD-20261031-02 - Halloween Day 07 decoration choice

- opened: 2026-10-31
- item: the Halloween Check-In Day 07 reward is a Decoration
  Choice Chest VI (UR) x2; only the preview has been seen
  and no decoration has been chosen.
- context: Days 01-06 are claimed. Across the 2026-10-31
  events sweeps the Day 07 tile opened only a preview with
  no Claim button, and no decoration was chosen - records
  in _records_/2026-10-31/INDEX.md and
  _records_/2026-10-31/event-claims/0812-queue-run.md,
  1244-queue-run.md and 1745-queue-run.md.
- decision needed: whether a decoration should be chosen at
  all, and if so which one - or whether the item should be
  left unclaimed.
- age tracking: opened 2026-10-31, age 0 days at filing;
  the retro recomputes and reports the age every run. Note
  the item is event-bound and can expire undecided.
- status: open

## Decided

None yet.
