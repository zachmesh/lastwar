---
title: Alliance train queue run 1404
created: 2026-11-04T22:10:00Z
modified: 2026-11-04T22:10:00Z
level: L0
version: 1.0.0
description: Ticker-1404 train unit, failed on Mac screen capture failure, fourth consecutive pass with this blocker
status: unverified
---

# 1404 queue run - alliance train

Executor: ticker-1404. Unit: train-2026-11-04-1030.
Session window about 14:04 to 14:10 America/Los_Angeles.

## Not performed

- No game screen was ever read and no game input was dispatched.
  The Mac screen capture stream failed on every attempt, so the
  train boarding check could not be performed, and no seat was
  taken, no Trade Contract spent, and no train summoned.

## Blocker, measured

- Device: the owner's Mac mini (1c817413-83e2-0545-cb90-36d5e096a6bd),
  listed online. LastWar (com.lastwar.ios, pid 59735) running
  fullscreen 1920x1080, Google Chrome frontmost.
- computer.control activate selected the LastWar window for
  background input but reported it not on screen and captured
  no observation: "Failed to start stream due to audio/video
  capture failure".
- computer.observe (compact) failed with the same error, twice
  across two computer sessions (cc-460, then cc-461 after
  ending cc-460 and starting fresh).
- computer.control describe on the LastWar window failed with
  the same error.
- computer.control open_app returned outcome_unknown; a
  re-list showed LastWar still running under the same pid, so
  no restart or duplicate launch happened, and the launch was
  not repeated.
- Control observation of the Google Chrome window succeeded in
  the same session (Gmail inbox tree read), so the control
  channel itself works and the failure is specific to the
  Last War fullscreen window, not a whole-device outage.
- No blind taps were dispatched: without an observation, any
  tap could land on the wrong control, so the unit stops here
  under the check-first rule.

## Repeated failure mode

- This is the fourth consecutive ticker pass to fail on this
  exact blocker: ticker-1224 (about 12:24, help unit),
  ticker-1327 (about 13:27, mail unit) and ticker-1340
  (about 13:40, star-ceremony unit) failed identically, per
  the day INDEX. The blocker is already filed as GitHub
  Issue #284 (label tooling); this pass commented on that
  issue instead of filing a duplicate. Until the Mac
  screen-recording stream recovers for the game window,
  further ticker passes will fail their first unit the same
  way; the inbox held 65 units at this pass.

## Other pass steps

- Own PRs checked first: open records PRs 279 (2026-11-04),
  265 (2026-11-02), 256 (2026-11-03) and 187 (2026-11-01) all
  name Owner lastwar-pr-integrator, none names this job, and
  none carries a question addressed to this job, so nothing
  was owed before game work.
- No zombie seeding: zombie chain zombie-2026-10-28 closed
  with unit 066 on 2026-10-30 (event ended about the 19:00
  reset 2026-10-30, no Zombie tab in the Events hub).
- Tracker untouched: a failed unit does not mark the
  regular, so the next tick re-produces the train unit.

## Outcome

Failed. No train checked, no seat taken, no contracts spent,
no diamonds, money, speedups or other spending. No
different-device dialog appeared. No device takeover needed.

## Result stats

- target 1, achieved 0, resources_gained none, costs 0,
  verified no, blocker_category f, device_takeovers 0,
  issue 284
