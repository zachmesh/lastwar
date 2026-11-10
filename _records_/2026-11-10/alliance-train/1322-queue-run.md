---
title: Alliance train queue run 1322
created: 2026-11-10T21:22:00Z
modified: 2026-11-10T21:22:00Z
level: L0
version: 1.0.0
description: Train unit train-2026-11-10-1030, no train preparing, closed partial per activity metadata
status: unverified
---

# Alliance train 13:22 to 13:25 - ticker-1314

Unit train-2026-11-10-1030 (planned for the 10:30 cycle,
expires 14:30). Executor ticker-1314. Session cc-461 on the owner
Mac mini (session cc-460 from the previous unit had closed in
between; a fresh session was started, no game state lost).

## Live reads

- Clean base view at 13:23: neither preparation signal is
  present. No train icon in the left icon column (hammer 1/4,
  flask 1/2, chat with badge 2, truck, radar with badge 11,
  hammer), and no "Boarding closes in" banner under the
  resource bar. A red-badge icon with a 00:00:54 countdown
  sits at the right edge mid-screen; that is a different
  event, not the train banner.
- Per the alliance-train activity metadata, the unit closes
  partial without panning the base edge, and re-checks only
  when a train is preparing. No station panel was opened and
  no boarding action was taken. No login or verification was
  demanded, and no different-device dialog appeared.

## Outcome

- No train preparing at this check. Nothing boarded.
- The 04:13 unit of this reset day already boarded carriage 2
  of the Missile Apex train, so today's regular train is
  accounted for; a later Mega Express preparation, if any,
  will be picked up by the next train unit.

## Figures read live on screen

- Food 615.9M, iron 938.8M, coin 84.1M, power 148,765,978,
  diamonds 6,207 at entry.

## Result statistics

- target 1, achieved 0, resources_gained none, costs about
  3 minutes play, verified yes, blocker_category h
  (by-design partial, no train preparing), device_takeovers 0

No diamonds or money spent. No other task type was executed
in this unit.
