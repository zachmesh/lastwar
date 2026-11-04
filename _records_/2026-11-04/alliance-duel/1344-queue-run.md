---
title: Alliance Duel queue run 1344
created: 2026-11-04T21:44:00Z
modified: 2026-11-04T21:44:00Z
level: L0
version: 1.0.0
description: Ticker-1340 star-ceremony unit, failed on Mac screen capture failure, third consecutive pass with this blocker
status: unverified
---

# 1344 queue run - alliance duel / star ceremony

Executor: ticker-1340. Unit: star-ceremony-2026-11-04-1030.
Session window about 13:40 to 13:44 America/Los_Angeles.

## Not performed

- No game screen was ever read and no game input was dispatched.
  The Mac screen capture stream failed on every attempt, so the
  Star Ceremony trophy check and the personal duel total read
  could not be performed, and no claim was made or verified.

## Blocker, measured

- Device: Zhen's Mac mini (1c817413-83e2-0545-cb90-36d5e096a6bd),
  listed online. Connection health: native and web transports
  both connected. LastWar (com.lastwar.ios, pid 59735) running
  fullscreen 1920x1080, Google Chrome frontmost.
- computer.observe (image, then compact) failed: "Failed to
  start stream due to audio/video capture failure".
- computer.control screenshot failed with the same error;
  activate selected the LastWar window for background input
  but captured no observation, same error.
- A fresh computer session (cc-459, after ending cc-458) failed
  identically on activate and observe.
- computer.control open_app returned outcome_unknown; a
  re-list showed LastWar still running under the same pid, so
  no restart or duplicate launch happened, and the launch was
  not repeated.
- No blind taps were dispatched: without an observation, any
  tap could land on the wrong control, so the unit stops here
  under the check-first rule.

## Repeated failure mode

- This is the third consecutive ticker pass to fail on this
  exact blocker: ticker-1224 (about 12:24, help unit) and
  ticker-1327 (about 13:27, mail unit) failed identically, per
  the day INDEX. The blocker is therefore filed as GitHub
  Issue #284 (label tooling), not left only in this prose
  record. Until the Mac screen-recording stream recovers,
  further ticker passes will fail their first unit the same
  way; the inbox held 66 units at this pass.

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
  regular, so the next tick re-produces the star-ceremony
  unit.

## Outcome

Failed. No ceremony checked, no duel total read, no diamonds,
money, speedups or other spending. No different-device dialog
appeared. No device takeover needed.

## Result stats

- target 3600000, achieved unmeasured, resources_gained none,
  costs 0, verified no, blocker_category f, ceremonies_claimed 0,
  device_takeovers 0, issue 284
