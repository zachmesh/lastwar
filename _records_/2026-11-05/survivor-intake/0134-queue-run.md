---
title: Survivors queue run 0134
created: 2026-11-05T01:34:00-08:00
modified: 2026-11-05T01:57:00-08:00
level: L0
version: 1.0.0
description: Ticker-0134 survivors unit, failed on Mac screen capture failure, twenty-sixth consecutive pass with this blocker (Issue 284)
status: unverified
---

# 0134 queue run - Survivors

Executor: ticker-0134. Unit: survivors-2026-11-04-2203.
Session window about 01:34 to 01:57 America/Los_Angeles.
Device token taken 09:35:09Z.

## Not performed

- No game screen was ever read and no game input was dispatched.
  The Mac screen capture stream failed on every attempt, so the
  gate line was never seen, no survivor was verified, and no
  Quick Dispatch ran. Nothing was claimed.

## Blocker - Mac screen capture failure (Issue 284)

- Twenty-sixth consecutive ticker pass failed on this blocker
  (ticker-0104 at 01:04 was the twenty-fifth).
- LastWar (bundle com.lastwar.ios, pid 59735) is running with one
  window, 1920x1080 at (0,0); Google Chrome is frontmost.
  `activate` reports `window_on_screen: false` and
  `brought_to_front: false` on every attempt.
- New diagnosis this pass, session cc-505 (fresh pivots after the
  25 identical failures):
  - `list_windows` with the correct app name "LastWar" (earlier
    passes used "Last War" and read 0 windows) confirms the
    window exists: 1920x1080 at (0,0), window_id 160366.
  - A `menu` action on View failed with "Exit Full Screen" not
    there, and the error listed the View menu contents:
    Landscape Orientation, Portrait Orientation, Zoom to Fit,
    Enter Full Screen. "Enter Full Screen" being present means
    the app is NOT in native fullscreen - it is a windowed
    1920x1080 window sitting on an inactive Space. The capture
    failure is the pixel stream of an off-screen window, not a
    broken screen-recording permission: Chrome windows observe
    normally in the same sessions.
  - `open_app` for LastWar returned outcome_unknown; a following
    `list_windows` showed the window unchanged.
  - Background-sent Space keys do not switch Spaces: Ctrl+Right,
    Ctrl+Left and Ctrl+Up (Mission Control) all dispatched with
    input_dispatched true while Chrome was selected and observed,
    but the frontmost app stayed Chrome and the game window
    stayed off-screen after each. Computer control sends input
    in the background and never brings apps to the front, so
    system Space shortcuts do not fire from it.
  - `set_window_frame` on the game window is gated by the
    stale-observation rule: it needs an observation_id from an
    observation of that window, which is exactly what the capture
    failure prevents. No input was sent.
  - `inspect_menu` for the Window menu failed with
    stale_observation: the app menu is not bound to the selected
    main window.
- Capture attempts in cc-505: `computer.observe` compact x2,
  `computer.control` activate x3, `open_app` x1, menu x1 - all
  with the same error "Failed to start stream due to audio/video
  capture failure" wherever evidence was requested.
- Device connection health at the same time: both native and web
  transports connected and healthy (native lastResponseAgeSeconds
  0, web 4). This is not a connectivity problem.
- No "active on a different device" dialog appeared, no fresh
  login or verification code was demanded, no red-line action
  was taken, no blind tap was made. This is not an authorization
  problem.
- The unit's 15 minute budget was spent on capture attempts and
  the new pivots; game time was zero. No other unit was
  attempted in this pass: every unit needs the same game screen,
  so all would fail identically.
- Unblocking still needs the game window back on the active
  Space - the owner clicking the LastWar Dock icon once is the
  known reliable step - or a control route that can switch
  Spaces. The background input channel cannot do it: no key,
  menu or frame action available to it moves the window across
  Spaces without a fresh observation of the window itself.

## Result

- Unit survivors-2026-11-04-2203 completed as failed.
  Tracker untouched, so the next tick re-produces the
  survivors regular.
- Stats: target survivors collected from gate line, achieved 0,
  resources_gained none, costs about 20 minutes executor time,
  0 stamina, 0 items, verified no, blocker_category e (repeated
  blocker).
- Issue 284 commented with this pass's new diagnosis (menu read,
  Space-switch attempts, set_window_frame gate).
