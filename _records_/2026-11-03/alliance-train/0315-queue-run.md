---
title: Alliance Train Queue Run 0315
created: 2026-11-03T03:15:00-08:00
modified: 2026-11-03T03:15:00-08:00
level: L0
version: 1.0.0
description: Ticker pass ticker-0304 train unit train-2026-11-03-0230
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-11-03
---

# Alliance train, 03:15 queue run

Executor ticker-0304, unit train-2026-11-03-0230, status
partial. Tracker untouched: a partial unit does not mark the
tracker, so the next tick re-produces this regular.

## What was done

- Base screen inspected first: no "Boarding closes in"
  banner under the resource bar.
- Wrong tap, recovered without action: a fresh visual
  grounding put the train icon at (53, 637), but tapping it
  opened the Secret Command Post (Secret Mobile Squad).
  Nothing inside it was tapped - no task, no Mega Deploy,
  no Mega Refresh - and it was closed with its back arrow
  at (157, 946), back to the base. This repeats the
  (53, 630) mislabelling already recorded in the
  2026-11-02 0348 unit; grounding must not be trusted for
  this icon.
- Measured tap: (52, 548), the point taken from the
  2026-11-02 0044 and 0348 records, was tapped on a fresh
  base screenshot. The camera did not pan - the view stayed
  on the base centre, with no station, no train, no plus
  bubble and no station countdown in view. This matches the
  2026-11-03 0035 unit, which also got no pan from the
  neighbouring points and closed partial.
- No station view was achieved in this unit, so no
  preparing train was confirmed and none was ruled out
  beyond the absent banner.

## Result

- Status partial. No boarding action was taken, no Trade
  Contracts spent, no train summoned, no conductor role
  taken. The Secret Command Post screen was only passed
  through; nothing read on it is this unit's data, and the
  secrets unit must re-read its own counters live.
- Gap: already tracked as GitHub Issue #205 (class
  knowledge) - left-column mapping and the train icon
  appearing only while a train is preparing. This unit's
  repeat is commented on #205, not filed as a new issue.
