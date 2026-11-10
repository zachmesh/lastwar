---
title: Alliance Help queue run 1019
created: 2026-11-09T18:19:00Z
modified: 2026-11-09T18:19:00Z
version: 1.0.0
description: Ticker-1004 help unit, Alliance button unresponsive to background clicks, Help All not reached
status: partial
grounded_in:
  - source: live game screen on the owner Mac mini, 2026-11-09 10:06-10:19 PT
---

# Alliance Help queue run 1019 (ticker-1004)

Unit: help-2026-11-09-0630. Status: partial.
Activity: alliance-help.

## Live reads

- Base screen at entry (fullscreen 1920x1080, window 642x951 zoomed
  via the green zoom button): power 149,217,331, coin 46.2M,
  food 544.5M, iron 871.8M. The bottom bar was clipped in the
  windowed view, so the pass went fullscreen for a full view.
- Green up-arrow menu button tapped once at (484, 975): the side
  menu expanded (HEROES / WORLD labels, Alliance, Mail,
  Inventory buttons visible on the right). Background input
  reaches the game for this control.
- Alliance shield button carries a RED DOT (seen live in a
  cropped screenshot, top-right of the tile) - help requests
  are waiting. The Help page was never reached, so the points
  header was never read and no points figure is claimed.

## What was tried

- Alliance button tapped six times in four input variants,
  all at the freshly grounded centre (visual grounding bbox
  x 626-673, y 678-747; centre about (650, 712); cursor seen
  on the shield in the cropped screenshot):
  1. click at (715, 701) on window 489932 - no change
  2. click at (650, 712) on window 489932 - no change
  3. left_mouse_down / 1s hold / left_mouse_up at (641, 694)
     on window 489932 - no change; the tool advised that
     background clicks do not reach some controls and to use
     click_element with the control's visible label
  4. click at (650, 712) on window 508052 - small press
     animation only (5% changed area), panel never opened
  5. left_press at (650, 700) on window 508052, 3s wait -
     no change
  6. move + click at (654, 700) on window 508052, 3s wait -
     no change
- Two LastWar windows exist, both 1920x1080 at (0, 0):
  window 489932 titled "Last War" and window 508052 with an
  empty title. The first activate reported window 489932
  covered by LastWar; switching the target to 508052 did not
  fix the Alliance tap. The duplicate window is a new finding
  and may be part of the blocker.

## Blocker (rule R2)

- Same-method taps ended after the second no-change tap; the
  variants above were the pivot attempts inside this unit.
  The Alliance button does not respond to background
  coordinate clicks in this fullscreen session, while the
  green menu arrow does. Changed method for the next unit:
  exit fullscreen to the native 642x951 window (menu View
  to Exit Full Screen) and retry the Alliance tap there, or
  find a click_element route if an Alliance label element
  appears in the observation. Do NOT repeat the fullscreen
  background-click sequence.
- The red dot means the objective is still pending, not
  absent: the next help unit must still press Help All.

## Red lines

- No diamonds or money spent. No other unit's work touched.
  Assemble was not opened. No mail deleted.

## Stats

- target: 1
- achieved: 0
- resources_gained: none
- costs: about 13 minutes of unit time, no items spent
- verified: no
- blocker_category: c
- points: 0
