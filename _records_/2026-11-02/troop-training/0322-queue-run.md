---
title: Training queue run 0322
created: 2026-11-02T11:22:00Z
modified: 2026-11-02T11:30:00Z
version: 1.0.0
description: Ticker training unit, TRAIN UNITS panel not reached
status: partial
grounded_in:
  - source: game screen on the owner Mac mini 2026-11-02 03:22 to 03:30 PST
---

# Training queue run 0322

Unit: training-2026-11-02-0203, executor ticker-0308, status
partial. Session window 03:22 to 03:30 PST on the owner Mac mini.
No batch was queued and no training state was verified.

## What was done

- Grounded the four barracks tents on the live base screenshot:
  norm (308,552), (409,606), (546,544), (608,518). This locates
  the tent rows that issue #150 records as not located.
- Tapped the first tent and confirmed the selection label
  Barracks Lv.27 with the three-button action row: paw (details),
  pistol (train per the activity doc), green up arrow (upgrade).
- Tapped the pistol button at norm (405,568). The panel that
  opened was the Lv.27 to 28 UPGRADE panel, not TRAIN UNITS:
  Unit Training Cap 540 to 550, Unit Training Level 9 to 9,
  cost coins 43.7M of 127.5M and iron 565.3M of 314.5M, Upgrade
  timer 19d 14:30:46, Finish Now 187,490. It was closed with
  the panel X. No Upgrade, no Finish Now, no Obtain, no building
  started.
- Tapped the paw button at norm (311,552) on the re-selected
  tent. No panel opened.
- Deselected with a tap on empty ground, leaving the game on
  the base screen.

## Why partial, not done

- The TRAIN UNITS panel was not reached, so no barracks queue
  state was read, no idle barracks was requeued, and the Drill
  Ground state was not read. The other three barracks were not
  inspected. The activity doc's pistol-to-TRAIN-UNITS mapping
  did not hold on this tap; whether the mapping is stale or the
  tap landed on a neighbouring control is unresolved.
- Tracker untouched, per the rule for partial units.

## Follow-up

- Commented on issue #150 with the located tent rows and the
  unresolved TRAIN UNITS entry, so the next unit re-grounds the
  action row before tapping.
