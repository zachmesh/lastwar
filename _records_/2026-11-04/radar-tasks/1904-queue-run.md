---
title: Radar queue run 1904
created: 2026-11-05T03:04:00Z
modified: 2026-11-05T03:15:00Z
level: L0
version: 1.0.0
description: Ticker-1904 radar unit, failed on Mac screen capture failure, continuing the 2026-11-04 blocker run
status: unverified
---

# 1904 queue run - radar tasks

Executor: ticker-1904. Unit: radar-2026-11-04-1803.
Session window about 19:04 to 19:15 America/Los_Angeles.

## Not performed

- No game screen was ever read and no game input was dispatched.
  The Mac screen capture stream failed on every attempt, so the
  radar screen was never entered or verified, no stored task
  count, stamina figure, restore line or pin scan was read, and
  no Quick Execute, Claim All or pin march was run.

## Posture note

- The unit window reads duel day 3, radar release, but that slot
  (18:03 local) predates the 19:00 reset. Live posture at this
  pass, recomputed with tools/duel.py under
  America/Los_Angeles time, is duel day 4, Train Heroes, radar
  STACK: complete ordinary tasks but do not claim, do not tap
  pins. The unit's work, when the screen returns, is the stack
  execution, not the stale release wording. The 1005 unit's
  Doom Elite pin expired about 11:46 local and is gone; the
  restore line at the 1005 close pointed to 12 tasks restoring
  about 15:42 local, so the next live unit should expect a
  fresh stored batch.

## Blocker, measured

- Device: Zhen's Mac mini (1c817413-83e2-0545-cb90-36d5e096a6bd),
  listed online, connection health healthy on both native and
  web transports (checked this pass).
- LastWar (com.lastwar.ios, pid 59735) running fullscreen
  1920x1080, Google Chrome frontmost.
- computer.session cc-479 started, list_apps confirmed LastWar
  as target; computer.observe (compact) failed: "Failed to start
  stream due to audio/video capture failure".
- computer.control activate selected the LastWar window for
  background input but captured no observation, same error.
- computer.observe (compact) failed again with the same error;
  connection.health at the same time reported both transports
  connected and healthy.
- Session cc-479 ended, fresh session cc-480 started;
  computer.control activate again selected the window with no
  observation, same error.
- computer.observe (image view) in cc-480 failed with the same
  error. Session cc-480 ended.
- Three observation attempts across two sessions, two views,
  plus two activates: all failed with the identical signature.
  No blind taps were dispatched: without an observation, any
  tap could land on the wrong control, so the unit stops here
  under the check-first rule. No different-device dialog was
  observed (no screen was ever captured) and no device
  takeover was needed.

## Blocker history

- The same signature failed the 12:35, 13:33, 13:44, 14:34,
  14:39, 15:04, 15:34, 16:34, 17:07, 17:34, 18:04 and 18:34
  passes of 2026-11-04, and this pass continues it past the
  19:00 reset. The blocker is filed as GitHub Issue #284
  (tooling, open, 11 comments); this pass commented on it
  rather than filing a duplicate.
- The pass stops after this one unit rather than claiming
  further units: every further unit would fail on the same
  capture error and burn attempts, so the inbox is left for
  the first pass after capture recovers.

## Remaining work, carried forward

- This unit's stack work (enter and verify the radar screen,
  run Quick Execute batches until no offer remains, record
  stored count, pending reward count, stamina, restore line
  and the pin inventory untapped) is still owed and the
  tracker stays untouched; the next tick re-produces the
  regular.
- No diamonds spent, no paid button tapped.
