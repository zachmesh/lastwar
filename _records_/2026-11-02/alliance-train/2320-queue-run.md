---
title: Alliance train queue run 2320
created: 2026-11-02T23:20:00Z
modified: 2026-11-02T23:24:00Z
version: 1.0.0
description: Queue unit train-2026-11-02-2230 executed by ticker-2304
status: partial
grounded_in:
  - source: game screen reads live in this unit on the owner Mac mini
  - source: _records_/2026-11-02/alliance-train/2045-queue-run.md for the prior entry method
---

# Alliance train - queue run 2320

Executor: ticker-2304. Unit: train-2026-11-02-2230. Status:
partial. Session window: about 23:20 to 23:24 local, inside the
15 minute unit cap. Tracker untouched: a partial unit does not
mark the tracker, so the next tick re-produces this regular.

## What was done

- Base screen inspected first: no "Boarding closes in" banner
  under the resource bar.
- First entry attempt, wrong icon: a tap at (35,675) in the left
  column opened Secret Command Post (Secret Mobile Squad), not
  the station. Nothing inside it was tapped: no task, no Mega
  Deploy, no refresh. Exited by the visually grounded back point
  (158,945) back to the base.
- Second entry attempt, stale point: the 2045 record's
  left-column train icon point (52,548) produced no camera pan
  this time; the base view was unchanged on screenshot.
- Third entry attempt, mislabelled grounding: visual grounding
  on the base screenshot labelled the point (53,576) as the
  train icon, but tapping it opened the truck screen ("Today's
  Trade Count: 4/5", "Your Truck" tab, a yellow truck labelled
  [AP3x]KpyKat). Nothing on that screen was tapped: no
  dispatch, no plunder, no tab change beyond the view itself.
  Returned to the base with the back tile point (82,930).
- No station view was achieved in this unit, so no preparing
  train was confirmed and none was ruled out beyond the absent
  banner. No boarding action was taken, no Trade Contracts
  spent, no train summoned, no conductor role taken.

## Gap found (filed as GitHub Issue #205, class knowledge)

- The train entry point has drifted: the 2045 point (52,548)
  no longer pans, and visual grounding mislabels the truck
  icon as the train icon. The activity metadata's entry
  section needs a re-grounded train icon point and a
  station-drag route that does not depend on the stale point.
  The next train unit should re-ground the icon from the
  base screenshot before tapping, and must not treat the
  truck screen as the station.

## Incidental observation, not this unit's data

- The truck screen read "Today's Trade Count: 4/5" while
  passing through. This is NOT a trucks-unit closing count:
  it was read outside the trucks unit, so the trucks unit
  must re-read its own counter live in its own unit.

## Red lines

- No diamonds or money spent, no paid button tapped, no
  Mega Deploy, no assembly, no summoning.
