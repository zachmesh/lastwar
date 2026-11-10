---
title: Alliance train queue run 0035
created: 2026-11-03T08:35:00Z
modified: 2026-11-03T08:44:00Z
version: 1.0.0
description: Queue unit train-2026-11-02-0847 executed by ticker-0034
status: partial
grounded_in:
  - source: game screen reads live in this unit on the owner Mac mini
  - source: _records_/2026-11-02/alliance-train/2320-queue-run.md for the prior entry-point gap
---

# Alliance train - queue run 0035

Executor: ticker-0034. Unit: train-2026-11-02-0847. Status:
partial. Session window: about 00:35 to 00:44 local, inside the
15 minute unit cap. Tracker untouched: a partial unit does not
mark the tracker, so the next tick re-produces this regular.

## What was done

- Base screen inspected first: no "Boarding closes in" banner
  under the resource bar.
- Icon probe 1, fresh grounding, wrong screen: visual grounding
  on this unit's base screenshot labelled the point (52,567)
  as the train icon, but tapping it opened the truck screen
  ("Your Truck" tab). Nothing on that screen was tapped: no
  dispatch, no plunder, no tab change. Returned to the base
  with the back point (82,930). This repeats the 2320
  mislabelling, in which (53,576) also opened the truck
  screen: the 540 to 580 band of the left column is the truck
  entry, not the train entry, and visual grounding must not
  be trusted for this icon again.
- Icon probe 2: tapping (52,626) opened Secret Command Post
  (Secret Mobile Squad). Nothing inside it was tapped: no
  task, no Mega Deploy, no Mega Refresh. Exited with the
  blue back arrow, measured fresh at (160,945), back to the
  base. An earlier tap at (55,930) missed that arrow and
  left the screen unchanged.
- Icon probe 3: tapping (52,508) opened the temperature
  panel (base temperature 6.5 degrees C, Permafrost Area,
  Alliance Furnace, High-Heat Furnace lines). Closed with
  its X at (850,137), back to the base. No furnace was
  turned on or off, and no temperature setting was changed.
- Drag route, changed method: dragging the camera from
  (600,600) to (300,300) reached empty snow southwest of
  the base, with no train, no station building and no plus
  bubble. Reversing the drag and a further diagonal drag
  returned the view to the base centre. A final drag from
  (300,300) to (600,600) produced no view change, and the
  base centre again showed no train, no station plus
  bubble and no station countdown.
- No station view was achieved in this unit, so no
  preparing train was confirmed and none was ruled out
  beyond the absent banner. The 2026-11-02 0044 record's
  correction stands as a warning here: a single pan view
  once missed a preparing train that a later camera
  restore revealed.

## Result

- Status partial. No boarding action was taken, no Trade
  Contracts spent, no train summoned, no conductor role
  taken.
- The truck screen and the Secret Command Post screen were
  only passed through. Nothing read on them is this unit's
  data, and nothing read on them is counted for any other
  regular: the trucks and secrets units must re-read their
  own counters live in their own units.

## Gap found (commented on GitHub Issue #205, class knowledge)

- Empirical left-column mapping measured in this unit:
  (52,508) is temperature, (52,567) is trucks, (52,626) is
  Secret Command Post. None of them is the train entry.
  The 2045 point (52,548) panned the camera when a train
  was preparing; it is possible the train icon only appears
  while a train is preparing, which would explain both the
  2320 no-pan and this unit's neighbouring-icon hits.
- Next train unit, changed method: probe the remaining
  left-column icons one at a time from a fresh screenshot,
  or wait for a "Boarding closes in" banner, and do not
  reuse (52,508), (52,567) or (52,626) as the train entry.
  A station view that shows only the base centre is not a
  completed station check.

## Red lines

- No diamonds or money spent, no paid button tapped, no
  Mega Deploy, no assembly, no summoning, no furnace change.
