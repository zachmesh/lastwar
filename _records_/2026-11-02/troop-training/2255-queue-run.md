---
title: Training queue run 2255
created: 2026-11-02T22:55:00-08:00
executor: ticker-2234
unit: training-2026-11-02-2203
status: partial
---

# Training - 2026-11-02 22:55 queue run (ticker-2234)

## Outcome

Partial: 0 barracks verified, 0 batches queued, tracker
untouched, so the next tick re-produces this regular.

## What was done

- Base screen confirmed live at entry; HUD food 230.0M,
  second top-bar 564.7M, coins 5.9M, second-row first
  resource 18.7M. An "Alliance Gifts received!" toast
  was visible at entry; it belongs to the gifts regular
  and was not acted on from this training unit.
- Dragged the base view upward (500,700 to 500,400) to
  expose the lower-middle barracks tents, per the
  1949 unit's attempt. Unlike 1949, the drag did move
  the view this time: the central cluster shifted to
  the top of the screen and the lower area showed
  empty snow, with no barracks tent brought into view.
  No tent point was therefore tapped, and no TRAIN
  UNITS panel was opened.
- Dragged back (500,400 to 500,700) to restore the
  starting view. Game left safe on the base screen.
- No Drill Ground figure was read live in this unit,
  and no Drill Ground Full state is claimed. The
  2026-10-31 Drill Ground blocker in the activity
  metadata is therefore neither confirmed nor cleared
  here. The Lv.24 batch queued at 11:34 today (T8 x666,
  1 day 4 hours, per the 1146 and 1723 records) is
  not a live read in this unit and is not claimed as
  a verified busy state.

## Why partial, not done

- No barracks queue was verified and no idle barracks
  was requeued, so the "keep every barracks busy"
  standard is unmet. The matching open issue is #150
  (tooling/knowledge): this unit's drag-moved-but-no-
  tent result is a further data point for that issue,
  not a new issue.

## Red lines

Nothing spent, no Finish Now, no green upgrade shortcut,
no other activity's rewards claimed, no building started.

## Result stats

- target 4, achieved 0, resources_gained none,
  costs 0 stamina, verified no, blocker_category c
- barracks_checked 0, batches_queued 0,
  device_takeovers 0
