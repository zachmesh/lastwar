---
title: Scout midday queue run 0104
created: 2026-11-05T01:04:00-08:00
modified: 2026-11-05T01:07:00-08:00
level: L0
version: 1.0.0
description: Ticker-0104 scout-midday unit, failed on Mac screen capture failure, twenty-fifth consecutive pass with this blocker (Issue 284)
status: unverified
---

# 0104 queue run - Scout midday

Executor: ticker-0104. Unit: scout-midday-scout-mid-2026-11-02-001.
Session window about 01:04 to 01:07 America/Los_Angeles.
Device token taken 09:05:08Z.

## Not performed

- No game screen was ever read and no game input was dispatched.
  The Mac screen capture stream failed on every attempt, so no
  surface was walked, no item was observed, and no red dot was
  explained. Nothing was claimed.

## Blocker - Mac screen capture failure (Issue 284)

- Twenty-fifth consecutive ticker pass failed on this blocker
  (ticker-0034 at 00:34 was the twenty-fourth).
- LastWar (bundle com.lastwar.ios, pid 59735) is running,
  fullscreen 1920x1080 at (0,0) on an inactive Space; Google
  Chrome is frontmost. `activate` reports `window_on_screen:
  false` and `brought_to_front: false`.
- Capture attempts, all with the same error "Failed to start
  stream due to audio/video capture failure": session cc-503
  `computer.observe` compact, `computer.control` activate,
  `computer.observe` image; fresh session cc-504 `computer.control`
  activate, `computer.observe` compact. Five attempts across two
  computer sessions.
- Device connection health at the same time: both native and web
  transports connected and healthy (native lastResponseAgeSeconds
  0, web 7). This is not a connectivity problem: the device is
  online, the sessions work, the app is running. The fullscreen
  game window on its inactive Space is simply not capturable.
- No "active on a different device" dialog appeared, no fresh
  login or verification code was demanded, no red-line action
  was taken. This is not an authorization problem.
- The unit's 15 minute budget was spent on capture attempts; game
  time was zero. No other unit was attempted in this pass: every
  unit needs the same game screen, so all would fail identically.
- Unblocking needs the game window back on an active Space or
  out of fullscreen - the owner clicking the LastWar Dock icon
  once is the known reliable step - or a future windowed run.
  Until then every ticker pass will fail the same way.

## Result

- Unit scout-midday-scout-mid-2026-11-02-001 completed as failed.
  Tracker untouched, so the next tick re-produces the
  scout-midday regular.
- Stats: target one midday scout pass surface group, achieved 0,
  resources_gained none, costs about 3 minutes executor time
  with no stamina or items spent, verified no, blocker_category
  f (missing precondition - game screen not observable).
- Issue 284 updated with this pass as the twenty-fifth
  consecutive failure.
