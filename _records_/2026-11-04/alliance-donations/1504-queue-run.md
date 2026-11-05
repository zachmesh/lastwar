---
title: Alliance donations queue run 1504
created: 2026-11-04T23:04:00Z
modified: 2026-11-04T23:15:00Z
level: L0
version: 1.0.0
description: Ticker-1504 donations unit, failed on Mac screen capture failure, sixth consecutive pass with this blocker
status: unverified
---

# 1504 queue run - alliance donations

Executor: ticker-1504. Unit: donations-2026-11-04-1403.
Session window about 15:04 to 15:15 America/Los_Angeles.

## Not performed

- No game screen was ever read and no game input was dispatched.
  The Mac screen capture stream failed on every attempt, so the
  Alliance menu, the Alliance Techs tree and the Rallied Attack
  panel could not be opened, no Donation Count was read live,
  and no coin donation was made or verified.

## Blocker, measured

- Device: Zhen's Mac mini (1c817413-83e2-0545-cb90-36d5e096a6bd),
  listed online, connection health healthy on both native and
  web transports. LastWar (com.lastwar.ios, pid 59735) running
  fullscreen 1920x1080, Google Chrome frontmost.
- computer.control activate (session cc-464) selected the
  LastWar window for background input but captured no
  observation: "Failed to start stream due to audio/video
  capture failure".
- computer.control screenshot (cc-464) failed with the same
  error, no input dispatched.
- computer.observe (cc-464, compact view) failed with the same
  error.
- A fresh computer session (cc-465, after ending cc-464):
  open_app LastWar returned outcome_unknown (launch result
  unverifiable, not repeated), and computer.observe (image
  view) failed with the same error.
- computer.control describe (cc-465) failed with the same
  error, so even the accessibility-tree route was unavailable.
- After a 30 second wait, computer.observe (image view) failed
  a final time with the same error.
- No blind taps were dispatched: without an observation, any
  tap could land on the wrong control, so the unit stops here
  under the check-first rule. No different-device dialog was
  observed (no screen was ever captured) and no device
  takeover was needed.

## Repeated failure mode

- This is the sixth consecutive ticker pass to fail on this
  exact blocker: ticker-1224 (about 12:24, help unit),
  ticker-1327 (about 13:27, mail unit), ticker-1340
  (about 13:40, star-ceremony unit), ticker-1404
  (about 14:04, train unit) and ticker-1434
  (about 14:34, passes unit) failed identically, per
  the day INDEX. The blocker was already filed as GitHub
  Issue #284 (label tooling) by ticker-1340; this pass
  commented on #284 instead of filing a duplicate, noting
  this sixth occurrence. Until the Mac screen-recording
  stream recovers, further ticker passes will fail their
  first unit the same way; the inbox held 70 units at this
  pass.

## Other pass steps

- Own PRs checked first: open records PRs 279 (2026-11-04),
  265 (2026-11-02), 256 (2026-11-03) and 187 (2026-11-01) all
  name Owner lastwar-pr-integrator, none names this job, and
  none carries a question addressed to this job (PR 279 has
  no comments), so nothing was owed before game work.
- Sync: reaped 0, expired 4, produced nothing new, 20
  regulars already queued.
- No zombie seeding: zombie chain zombie-2026-10-28 closed
  with unit 066 on 2026-10-30 (event ended about the 19:00
  reset 2026-10-30, no Zombie tab in the Events hub).
- Tracker untouched: a failed unit does not mark the
  regular, so the next tick re-produces the donations unit.

## Outcome

Failed. No donation checked or made, no diamonds, money,
speedups or other spending. No alliance diplomacy, no
assembly, no teleport.

## Result stats

- claimed_count 0, resources_gained none, costs 0,
  verified no, blocker_category f, device_takeovers 0,
  issue 284
