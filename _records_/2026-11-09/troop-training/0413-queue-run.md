---
title: Troop training queue run 0413
created: 2026-11-09T12:21:00Z
modified: 2026-11-09T12:21:00Z
level: L0
version: 1.0.0
description: Ticker-0404 training unit, fullscreen zoom-out variant tried, no barracks tent verified
status: unverified
---

# 0413 queue run - Troop training

Executor: ticker-0404. Unit: training-2026-11-09-0203.
Session window about 04:10 to 04:13 America/Los_Angeles.
Computer session cc-217 on the owner Mac mini.

## Performed

- Entry snapshot, read live on the opening base screen:
  food 540.1M, iron 864.9M, coin 42.9M, diamonds 13.22K,
  total power 149,217,331, window 642 by 951. LastWar
  already frontmost; no different-device dialog, no login
  or verification demanded.
- Fresh grounding for a barracks tent on the opening
  windowed frame returned no tent. The tents are not in
  this framing.
- Changed method one, per queue rule R2: a west road drag
  (norm 500,700 to 150,700) along the bottom road produced
  no view change. A blocked drag, not a "no tents here"
  result; the method ends here.
- Changed method two, per queue rule R2 and the
  zoom-out-first variant named by the 1216 and 1651
  units and still untried until now: native fullscreen
  via the green zoom button. The fullscreen frame
  (1280 by 720 capture) shows a wider base view. Fresh
  grounding found one tent candidate at norm 445,665;
  the tap on the fresh frame produced no change - no
  building label, no action row, no panel. The point
  did not resolve to a tappable tent, so per rule R2
  the method ends after the one no-change tap and the
  point was not tapped again.
- Fullscreen exit, measured: the menu bar did not drop
  from a pointer move to the top edge (the control
  channel delivers the pointer to the window only, not
  the system cursor), but computer.control inspect_menu
  with path ["View"] lists "Exit Full Screen" enabled,
  and the menu action with path ["View", "Exit Full
  Screen"] returned the game to the 642 by 951 window
  with no crash and no login demanded. This is the
  working exit route for this control channel; never
  use Ctrl-Cmd-F or Escape.
- No barracks panel opened, no batch state verified, no
  batch queued. The retired routes were not re-tapped:
  the yellow-green fenced structure (Aircraft Center
  Lv.29) and the red troop formation (Drill Ground
  Lv.30). The Drill Ground screen was therefore not
  re-read in this unit, and the 39,460 of 39,460 figure
  stays a 2026-10-31 read, neither confirmed nor
  cleared here.
- "Violet's Gift received!" toast seen in the fullscreen
  frame; it belongs to the gifts regular and was not
  acted on from this training unit. No diamonds or
  money spent, no Finish Now, no upgrade shortcut, no
  speedup burned.

## Closing reads

- Barracks verified 0, batches queued 0. Training state
  unverified; the game was left on the base screen in
  its normal windowed framing.

## Outcome

Partial. No barracks tent verified in the windowed or the
fullscreen framing; no idle barracks requeued.

## Result stats

- target 4, achieved 0, resources_gained none,
  costs 10m_wall_no_stamina, verified no,
  blocker_category c, barracks_verified 0,
  batches_queued 0, device_takeovers 0
