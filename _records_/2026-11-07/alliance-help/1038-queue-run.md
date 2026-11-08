---
title: Alliance help 1038 queue run
created: 2026-11-07T18:38:00Z
modified: 2026-11-07T18:38:00Z
version: 1.0.0
description: Ticker-1020 help unit failed, game window off-screen on an inactive Space, screen-capture channel deadlocked
status: unverified
grounded_in:
  - source: in-game state observed on the owner Mac mini, 2026-11-07
  - source: device channel evidence in this pass
---

# Alliance help 1038 queue run

- Unit: help-2026-11-07-0630, executor ticker-1020.
- Session: about 10:23 to 10:39 local. Status: failed
  (access-failed, screen-capture channel failure).
- No Help All press happened. No help count or points
  figure was read. No game input was dispatched to Last
  War at all. Nothing was claimed, spent or changed in
  the game. No diamonds, no money, no speedup items, no
  red line touched.

## What changed since the 1003 failure

- The Mac mini is back online. device.list at about
  10:23 local showed Zhen's Mac mini
  (1c817413-83e2-0545-cb90-36d5e096a6bd) online with
  last_seen 2026-11-07T18:19:37Z, fresh. The 1003 pass
  failed with the Mac offline (last_seen frozen at
  2026-11-05T15:36:52Z, Issue 284, 106th consecutive
  access-failed pass). This pass is NOT that failure:
  the device answers, the computer-use channel works,
  and the blocker moved to the game window itself.
- Connection health on both native and web transports:
  connected and healthy.

## The blocker

- The Last War window (1920x1080, window_id 160366) sits
  at global (0, -360) and reports window_on_screen false.
  Every capture attempt failed with "Failed to start
  stream due to audio/video capture failure" - the
  off-screen window pixel stream, the same class as the
  2026-11-04 1235 unit and the 2026-11-05 correction
  (windowed 1920x1080 window on an inactive Space).
- This is NOT a missing owner authorization and NOT a
  different-device dialog. No such dialog appeared at
  any point.

## Recovery attempts (all in this pass)

- Activate LastWar, observe, open_app LastWar, describe:
  capture failure each time, window not on screen.
- set_window_frame to (0, 0, 1920, 1080): refused, needs
  a fresh observation, which the capture failure blocks.
- Activating Finder (window 168864, helper) worked once
  and produced a full observation - proving the channel
  itself is alive.
- open_app Mission Control (first launch) opened the
  overview: every later activate and observe failed with
  geometry_mismatch origin_delta 256+, agent_display
  false, and all key input gated on observation_required.
  A second open_app Mission Control closed the overview
  and the observation channel recovered - launching
  Mission Control twice toggles it. Lesson: do NOT open
  Mission Control unless the overview itself is the
  work; the toggle back is a second launch.
- Background Ctrl+Right does NOT switch Spaces: the key
  went to the Finder column view (CUHelper textfield
  selected, no Space change). Background keyboard input
  reaches the selected window, not the system Space
  switcher. No Space-switch route through this channel
  worked.
- Mission Control overview itself cannot be observed or
  clicked through this channel: observe fails with no
  target window while it is open, and input stays gated
  on a fresh observation. Its thumbnails are not
  reachable from here.
- The known reliable unblock stands (2026-11-05
  correction): the owner clicking the LastWar Dock icon
  once brings the window to the active Space. That step
  needs the owner at the Mac; it was not available in
  this detached pass. No Dock icon was clicked blind:
  the icon position is unverified and a blind Dock click
  could activate the wrong app.

## Side effects of this pass

- None in the game. Outside the game: Mission Control
  was opened and closed twice (left closed, verified by
  a working Finder observation afterwards). One Finder
  column-view selection changed (CUHelper textfield
  selected by the Ctrl+Right test); no file was opened,
  renamed or moved. The Mac was left with the Finder
  helper window observable and Mission Control closed.

## Follow-up

- Tracker untouched per the failed-unit rule; the
  regular remains due and the next tick re-produces it
  as a fresh unit.
- If the window is still off-Space at the next pass, the
  owner clicking the LastWar Dock icon once is the
  unblock. This is a different failure mode from Issue
  284 (Mac offline): the device is online and the
  window is off-Space.
- Channel note for the next executor: never open Mission
  Control as a recovery step; if it is open, a second
  launch closes it and restores observation.
