---
title: Harvest queue run 0034
created: 2026-11-05T00:34:00-08:00
modified: 2026-11-05T00:41:00-08:00
level: L0
version: 1.0.0
description: Ticker-0034 harvest unit, failed on Mac screen capture failure, twenty-fourth consecutive pass with this blocker (Issue 284)
status: unverified
---

# 0034 queue run - Harvest

Executor: ticker-0034. Unit: harvest-2026-11-04-2203.
Session window about 00:34 to 00:41 America/Los_Angeles.
Device token taken 08:34:46Z, released 08:41:23Z.

## Not performed

- No game screen was ever read and no game input was dispatched.
  The Mac screen capture stream failed on every attempt, so no
  resource bubble was collected, no resource total was read, and
  the Armed Truck state is unknown. Nothing was claimed.

## Blocker - Mac screen capture failure (Issue 284)

- Twenty-fourth consecutive ticker pass failed on this blocker
  (ticker-0004 at 00:04 was the twenty-third, per the recount
  in its correction file).
- LastWar (bundle com.lastwar.ios, pid 59735) is running,
  fullscreen 1920x1080 at (0,0) on an inactive Space; Google
  Chrome is frontmost. `activate` reports `window_on_screen:
  false`.
- Capture attempts, all with the same error "Failed to start
  stream due to audio/video capture failure": the executor
  subagent tried `computer.observe` (compact, image, full),
  `computer.control` screenshot and describe, and `screen.snap`,
  six or more attempts; the parent then tried once more in a
  fresh computer session (cc-502) with `computer.observe`
  view=image, same error. The capture pipeline itself works:
  a Chrome window observed and screenshotted normally in the
  same session.
- Space-switch attempts failed: Ctrl+Right / Ctrl+Left
  dispatched but the Space did not switch; Cmd+Tab is blocked
  by the tool; the Dock icon could not be located from a
  window-relative observation, so no blind click was attempted.
  The menu path View -> Exit Full Screen needs a fresh
  observation of the game window, which is exactly what fails.
- No "active on a different device" dialog appeared, no fresh
  login or verification code was demanded, no red-line action
  was taken. This is not an authorization problem: the device
  is online, the session works, the app is running. The
  fullscreen game window on its inactive Space is simply not
  capturable.
- The unit's 15 minute budget was spent on control-channel
  recovery attempts; game time was zero. No other unit was
  attempted in this pass: every unit needs the same game
  screen, so all would fail identically.
- Unblocking needs the game window back on an active Space or
  out of fullscreen - the owner clicking the LastWar Dock icon
  once is the known reliable step - or a future windowed run.
  Until then every ticker pass will fail the same way.

## Result

- Unit harvest-2026-11-04-2203 completed as failed. Tracker
  untouched, so the next tick re-produces the harvest regular.
- Stats: target full main-base bubble sweep, achieved 0,
  resources_gained none, costs about 7 minutes executor time
  with no stamina or items spent, verified no, blocker_category
  f (missing precondition - game screen not observable).
- Issue 284 updated with this pass as the twenty-fourth
  consecutive failure.
