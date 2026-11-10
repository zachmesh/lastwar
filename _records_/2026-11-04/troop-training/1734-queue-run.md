---
title: Troop Training Queue Run 1734
created: 2026-11-05T01:34:00Z
modified: 2026-11-05T01:46:00Z
level: L0
version: 1.0.0
description: Ticker-1734 training unit, failed on Mac screen capture failure, eleventh consecutive pass with this blocker
status: unverified
---

# 1734 queue run - troop training

Executor: ticker-1734. Unit: training-2026-11-04-1403.
Session window about 17:34 to 17:46 America/Los_Angeles.

## Not performed

- No game screen was ever read and no game input was dispatched.
  The Mac screen capture stream failed on every attempt, so no
  barracks was opened, the Drill Ground full blocker recorded by
  the 2026-10-31 retro could not be re-read live, no batch was
  collected or requeued, and no training count was verified.

## Blocker, measured

- Device: Zhen's Mac mini (1c817413-83e2-0545-cb90-36d5e096a6bd),
  listed online, connection health healthy on both native and
  web transports (connection.repair web confirmed). LastWar
  (com.lastwar.ios, pid 59735) running fullscreen 1920x1080,
  Google Chrome frontmost. Screen-recording permission is
  granted on the device.
- Session cc-473: open_app LastWar returned outcome_unknown
  (launch result unverifiable, not repeated per its guidance);
  computer.observe (compact view) failed: "Failed to start
  stream due to audio/video capture failure".
- Session cc-474 (after ending cc-473): computer.observe
  (compact view) failed with the same error.
- computer.control list_apps succeeded without a stream and
  confirmed LastWar running and selected as target.
- computer.control activate (cc-474) selected the LastWar
  window for background input but captured no observation,
  same capture error; computer.observe (compact) failed again.
- computer.observe (image view) failed with the same error.
- connection.repair web reported healthy on both transports.
- Final computer.observe (compact view) failed with the same
  error.
- No blind taps were dispatched: without an observation, any
  tap could land on the wrong control, so the unit stops here
  under the check-first rule. No different-device dialog was
  observed (no screen was ever captured) and no device
  takeover was needed.

## Repeated failure mode

- This is the eleventh consecutive ticker pass to fail on this
  exact blocker, counting from the records branch day INDEX:
  ticker-1224, ticker-1327, ticker-1340, ticker-1404,
  ticker-1434, ticker-1504, ticker-1534, ticker-1634 and
  ticker-1704 failed identically before this pass, per the day
  records. The blocker is tracked as GitHub Issue #284
  (label tooling); this pass commented on #284 instead of
  filing a duplicate (comment 6647208826).
- The pass stopped after this unit rather than failing further
  units identically: every further unit needs the same capture
  channel, so repeating the attempt across more units would
  only add failed units, not progress. The next pass should
  retry capture first; if it recovers, the training unit is
  re-produced by the tracker as a fresh unit (tracker untouched).

## Other pass steps

- Own PRs checked first: open records PRs 286 (2026-11-04),
  265 (2026-11-02), 256 (2026-11-03) and 187 (2026-11-01) all
  name Owner lastwar-pr-integrator, none names this job, and
  PR 286 carries no comments, so nothing was owed before
  game work.
- Sync: reaped 0, expired 0, produced nothing new, 21
  regulars already queued. Inbox held 70 units at this pass.
- No zombie seeding: zombie chain zombie-2026-10-28 closed
  with unit 066 on 2026-10-30 (event ended about the 19:00
  reset 2026-10-30, no Zombie tab in the Events hub since),
  and the activity metadata forbids seeding a fresh chain
  until such a tab is seen live again.
- Tracker untouched: a failed unit does not mark the
  regular, so the next tick re-produces the training unit.
- Working-tree note: this pass ran with the main tree on
  branch work/ops-execution-records holding other state
  (including a modified _activities_/alliance-donations/
  INDEX.md, a tier-2 change). That change was left exactly
  as found and is not part of this pass's delivery; delivery
  used a fresh temporary worktree on records/2026-11-04.

## Outcome

Failed. No training checked or queued, no diamonds, money,
speedups, research, buildings, assembly or teleport touched.
Nothing claimed.

## Result stats

- target 1, achieved 0, resources_gained none, costs 0,
  verified no, blocker_category f, device_takeovers 0,
  issue 284
