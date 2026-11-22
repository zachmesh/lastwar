---
title: Donations queue run 1340
created: 2026-11-21T21:36:00Z
modified: 2026-11-21T21:36:00Z
version: 1.0.0
description: Queue unit donations-2026-11-21-1003, executor ticker-1318 - partial, Alliance menu would not open
status: unverified
---

# Donations 13:27-13:36 PT - partial, Alliance menu would not open

Executor ticker-1318. Unit donations-2026-11-21-1003 (planned 10:03 PT,
expires 14:03 PT). Session 13:27-13:36 PT, about 9 minutes in game.

## What was verified live

- Game windowed 788x1083 on the base screen, input routes working for
  canvas taps (hero select, empty-ground tap both took effect this
  pass). HUD: food 730.5M, iron 1.1G, coin 88.2M, diamonds 5,236,
  total power 149,653,371.
- Alliance button freshly measured this unit by visual grounding:
  bbox (888, 689)-(992, 751) in image coordinates, centre window
  (940, 720); the label centre is (940, 735). The 2026-11-02 metadata
  centre (903, 787) is stale for this window geometry - fresh
  measurement wins per queue rule R2.

## What was tried, all no-effect on the menu

1. Coordinate tap at the fresh measured icon centre (940, 720) - no
   change, menu did not open, camera did not pan.
2. Coordinate tap at the label centre (940, 735) - only the
   announcement banner/chat advanced; menu still closed.
3. Accessibility click_element on the 'Alliance' OCR text (element 13,
   fresh observation) - 1 percent visual change, menu still closed.

No donation was made and no Donation Count was read. This is NOT the
2026-11-02 failure signature: those taps panned the camera to the
Drill Ground cluster. Here the taps neither open the menu nor move
the camera - the button itself does not respond through any input
route tried. The "wrong tap point" hypothesis from 2026-11-02 is
therefore disproven for this window state: the fresh measured centre
fails exactly like the grounding point did.

## Outcome

- Donations made: 0. Donation Count read: none (live read required by
  the hard closing rule; no arithmetic close attempted).
- Status partial, verified no, blocker_category c (entry-route tap
  method). Tracker untouched. Re-read owed at the next donations slot
  with a different entry route - candidates: tap the Alliance HQ
  building on the map itself, or re-enter the base view first.
- Process-failure flag per queue rule R2: this is the fourth
  consecutive donations partial on the Alliance-entry blocker (0621,
  1020, 1427 on 2026-11-02, now this unit). It is a process failure,
  not a result, and is reported to the owner as one.
- Metadata update owed (tier 2, NOT in this records commit): record in
  _activities_/alliance-donations that the fresh measured centre
  (940, 720) and the Accessibility element click both fail with no
  camera pan in the windowed 788x1083 state, and that the entry route
  must change before the next donations unit runs.

## Red lines

No diamonds or money spent, no paid button tapped, no speedup burned,
no research, building, assembly or teleport touched. The diamond
donation button was never reached.
