---
title: Harvest queue run 1634
created: 2026-11-04T16:34:00-08:00
modified: 2026-11-04T16:34:00-08:00
version: 1.0.0
description: Ticker unit harvest-2026-11-04-1403 failed, Mac screen capture failure on all attempts, ninth consecutive ticker pass on this blocker
status: failed
grounded_in:
  - source: live device checks on the owner Mac mini, 2026-11-04 16:34 to 16:48 PST
---

# Harvest queue run 1634

Unit: harvest-2026-11-04-1403, executor ticker-1634.
Session window: 2026-11-04 16:34 to about 16:40 PST, device
sessions cc-469 and cc-470. No different-device dialog was
observed (no screen was ever captured) and no device
takeover was needed. No diamonds, money, speedup items or
paid button touched. No building or research started, no
assembly, no teleport.

## Not performed

- No game screen was ever read and no game input was
  dispatched. The Mac screen capture stream failed on every
  attempt, so the base, its resource bubbles and the HUD
  totals could not be read, and no bubble was tapped or
  verified. No harvest was collected.

## Blocker, measured

- Device: Zhen's Mac mini (1c817413-83e2-0545-cb90-36d5e096a6bd),
  listed online, connection health healthy on both native
  and web transports. LastWar (com.lastwar.ios, pid 59735)
  running fullscreen 1920x1080, Google Chrome frontmost.
- computer.control list_windows (cc-469) succeeded and
  listed the LastWar window, so the control channel itself
  was reachable; the capture stream was not.
- Attempt 1: computer.control activate LastWar (cc-469)
  selected the window for background input but captured no
  observation: "Failed to start stream due to audio/video
  capture failure".
- Attempt 2: computer.observe (cc-469, compact view)
  failed with the same error.
- Attempt 3, after ending cc-469 and a 30 second wait:
  computer.observe (cc-470, image view) failed with the
  same error.
- Attempt 4: computer.control describe LastWar (cc-470)
  failed with the same error, so even the accessibility-tree
  route was unavailable.
- No blind taps were dispatched: without an observation, any
  tap could land on the wrong control, so the unit stops
  here under the check-first rule. This satisfies and
  exceeds the standing at-least-3-attempts retry rule.

## Repeated failure mode

- This is the ninth consecutive ticker pass to fail on this
  exact blocker, following ticker-1224 (help), ticker-1327
  (mail), ticker-1340 (star-ceremony), ticker-1404 (train),
  ticker-1434 (passes), ticker-1504 (donations),
  ticker-1534 (radar) and ticker-1604 (arms-race), per the
  day INDEX and GitHub Issue #284. This pass commented on
  #284 instead of filing a duplicate. Until the Mac
  screen-recording stream recovers, further ticker passes
  will fail their first unit the same way; the inbox held
  72 units at this pass.

## Other pass steps

- Own PRs checked first: open records PRs 286
  (2026-11-04, post-1500 batch), 265 (2026-11-02), 256
  (2026-11-03) and 187 (2026-11-01) all name Owner
  lastwar-pr-integrator, none names this job, and none
  carries a question addressed to this job, so nothing was
  owed before game work.
- Sync: reaped 0, expired 0, produced nothing new, 21
  regulars already queued.
- No zombie seeding: zombie chain zombie-2026-10-28 closed
  with unit 066 on 2026-10-30 (event ended about the 19:00
  reset 2026-10-30, no Zombie tab in the Events hub).
- Tracker untouched: a failed unit does not mark the
  regular, so the next tick re-produces the harvest unit.

## Outcome

Failed. No resource collected, no diamonds, money,
speedups or other spending. No alliance diplomacy, no
assembly, no teleport.

## Result stats

- target full base sweep, achieved 0, resources_gained
  none, costs 0, verified no, blocker_category f,
  device_takeovers 0, issue 284
