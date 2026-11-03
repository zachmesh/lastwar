---
title: Star ceremony queue run 2326
created: 2026-11-02T23:26:00Z
modified: 2026-11-02T23:30:00Z
version: 1.0.0
description: Queue unit star-ceremony-2026-11-02-2230 executed by ticker-2304
status: partial
grounded_in:
  - source: game screen reads live in this unit on the owner Mac mini
---

# Star ceremony - queue run 2326

Executor: ticker-2304. Unit: star-ceremony-2026-11-02-2230.
Status: partial. Session window: about 23:26 to 23:30 local.
Tracker untouched: a partial unit does not mark the tracker, so
the next tick re-produces this regular.

## Ceremony check: done, nothing waiting

- Base screen inspected: no trophy icon beside the Alliance
  icon on the right side. Per the activity metadata the icon
  is present only while a ceremony is waiting and disappears
  once it has been played and claimed. No ceremony was
  played in this unit because none was waiting.

## Duel total read: unverified, pass budget ended the hunt

- Opened the Alliance Duel panel from the VS icon. Duel
  Progress, Today's Duel, theme Base Expansion, countdown
  18:33:56 at entry.
- Alliance totals read live: The Apex 260,334,917 (46%)
  against [Kmf] 311,756,756 (54%).
- Personal row hunt: the visible MVP list showed Abyss Apex
  18,306,600, [Kmf] 11,296,350 and [Kmf] Maison JP 10,407,300.
  One upward drag scrolled the list to further rows, but the
  account's own row (Bears Lair) was not reached before the
  pass budget ended. The personal daily total is therefore
  UNREAD in this unit, and no total or gap against 3,600,000
  is reported: a fragment or alliance figure never substitutes
  for the personal total.
- Follow-up: the next tick re-produces this regular (tracker
  untouched), and that unit should resume the ranking scroll
  to the account's own row. Note also that the owner decision
  of 2026-11-01 moved the total read to the duel-score
  regular; this checkout (work/ops-execution-records branch)
  carries alliance-duel INDEX 1.3.0 and no duel-score
  regular, so this unit followed the metadata in front of it.
  The duel-score unit, where present, is the other reader of
  this same line.

## Red lines

- No diamonds or money spent, no spin tokens bought or used,
  no paid button tapped. The duel panel was left via its back
  arrow to the base screen.
