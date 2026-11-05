---
title: Alliance donations queue run 1427
created: 2026-11-02T22:27:00Z
modified: 2026-11-02T22:27:00Z
version: 1.0.0
description: Ticker unit donations-2026-11-02-1403, Alliance menu not reached, entry-route blocker third consecutive unit, no donations made, no count read
status: partial
---

# Alliance donations queue run 1427

- Unit: donations-2026-11-02-1403, executor ticker-1412.
- Outcome: no donations made, no Donation Count read live, no
  coin or diamond spent. Status partial, tracker untouched.
  This unit does NOT close on arithmetic - no count figure is
  claimed anywhere in this record, per the hard closing rule
  and rule R1.
- Entry attempt, changed method per rule R2 (this is the
  third unit with this entry-route blocker, after 0621 and
  1020): the Alliance icon was re-grounded on the current
  full-base screenshot with the visual grounding tool, which
  returned (934,747), and the tap went there. Result
  identical to 0621 and 1020: the tap panned the base camera
  to the Drill Ground cluster (Drill Ground Lv.25, three
  floating round buttons at the bottom right) and no
  Alliance menu opened. The fresh measured centre of the
  Alliance shield icon on that same screenshot is
  (903,787), about 38 normalized units below the grounding
  point, so the grounding point likely landed on map
  terrain above the button; the measured centre was not
  tried in this unit because the camera had already panned
  and the Alliance button was no longer in frame.
- Recovery attempts inside the unit, both no-change and
  retired per rule R2: a tap on empty ground at (500,550)
  only scrolled the announcement banner, and drag-pans in
  both directions, (300,400) to (550,650) and back, moved
  the camera not at all. Drag-pan is therefore retired
  for restoring the base framing from the Drill Ground
  view, matching the survivors unit experience.
- Rule R2 third-unit consequence: the blocker is written
  into the alliance-donations activity metadata by this
  pass as a working-tree change (tier 2, NOT swept into
  this pass records commit, left for the PR flow), and the
  entry route for the next donations unit changes: it
  must restore the base framing first (candidates are
  tapping the Alliance HQ building on the map itself, or
  re-entering the base view) and then tap the fresh
  measured Alliance centre (903,787), never a
  grounding-tool point above the button. No new re-read
  unit is enqueued from this unit: the re-read unit
  donations-2026-11-02-1344 already sits in the inbox.
- Prior state carried, not re-verified: the 0545 unit read
  the remaining count down to 1 of 30 before the coin
  button greyed on a timer, so the day is one coin
  donation short of 30 of 30 on the last live read,
  pending a successful menu entry.
- Game left safe: no panel opened beyond the camera pan,
  no purchase, no upgrade, no dispatch, no train
  boarding touched.
- Result stats: target 30, achieved unverified, verified no,
  blocker_category c (entry-route tap method: Alliance
  icon tap pans the camera to Drill Ground instead of
  opening the Alliance menu, in this camera framing;
  third consecutive unit with this blocker).
  Donations landed in this unit: 0.
