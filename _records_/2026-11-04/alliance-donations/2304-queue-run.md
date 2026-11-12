---
title: Alliance donations queue run 2304
created: 2026-11-05T07:05:00Z
modified: 2026-11-05T07:18:00Z
level: L0
version: 1.0.0
description: Ticker-2304 donations unit, failed on Mac screen capture failure, same blocker as Issue 284
status: unverified
---

# 2304 queue run - alliance donations

Executor: ticker-2304. Unit: donations-2026-11-04-2203.
Session window about 23:04 to 23:18 America/Los_Angeles.

## Not performed

- No game screen was ever read and no game input was dispatched.
  The Mac screen capture stream failed on every attempt, so the
  Alliance menu, the Alliance Techs tree and the Rallied Attack
  panel could not be opened, no Donation Count was read live,
  and no coin donation was made or verified.

## Blocker, measured

- Device: Zhen's Mac mini (1c817413-83e2-0545-cb90-36d5e096a6bd),
  listed online. Connection health observed healthy on both
  native and web transports (native last response 0 seconds
  old, web 2 seconds old at check time).
- LastWar window present: com.lastwar.ios, window 160366,
  with Google Chrome frontmost.
- Session cc-494: computer.control activate selected the
  LastWar window for background input but captured no
  observation, "Failed to start stream due to audio/video
  capture failure"; computer.observe failed with the same
  error.
- Session cc-495 (after ending cc-494): open_app LastWar
  returned outcome_unknown (launch result unverifiable,
  not repeated); computer.observe failed again with the
  same error.
- Session cc-496 (after ending cc-495): computer.control
  activate again selected the window with the same capture
  failure; computer.observe failed a final time with the
  same error.
- Total capture attempts: 5, all failing with the identical
  audio/video capture error, across 3 sessions. This meets
  the standing retry rule of at least 3 attempts before
  recording a unit as access-failed.
- No blind taps were dispatched: without an observation, any
  tap could land on the wrong control, so the unit stops here
  under the check-first rule. No different-device dialog was
  observed (no screen was ever captured) and no device
  takeover was needed.

## Repeated failure mode

- This is the same blocker already filed as GitHub Issue #284
  (label tooling, still open at this pass): ticker-1934 on
  2026-11-04 commented there as the fifteenth consecutive
  capture-failure pass, and the ticker-2034 and ticker-2134
  passes failed identically later the same day. This pass
  commented on #284 instead of filing a duplicate. Until the
  Mac screen-recording stream recovers, further ticker passes
  will fail their first unit the same way; the inbox held 70
  units at this pass.

## Other pass steps

- Own PRs checked first: open records PRs 265 (2026-11-02),
  256 (2026-11-03) and 187 (2026-11-01) name Owner
  lastwar-pr-integrator, all conflicting on the single file
  _logs_/repo-actions/action-log.jsonl (append-append), with
  integrator re-check comments only and no question
  addressed to this job, so nothing was owed before game
  work. (PR 293 for records/2026-11-04, noted by the
  ticker-2034 pass, was re-checked at delivery time.)
- Sync: reaped 0, expired 4, produced nothing new, 21
  regulars already queued.
- No zombie seeding: zombie chain zombie-2026-10-28 closed
  with unit 066 on 2026-10-30 (event ended about the 19:00
  reset 2026-10-30, no Zombie tab in the Events hub), and
  the seeding rule forbids a fresh chain until a Zombie
  Invasion tab is seen live again.
- Tracker untouched: a failed unit does not mark the
  regular, so the next tick re-produces the donations unit.
- Delivery note: the local working tree sits on branch
  work/ops-execution-records and holds another job's
  in-flight state (unrelated modifications and deletions),
  so this pass's outputs were delivered through a temporary
  worktree onto the records/2026-11-04 branch, leaving that
  state undisturbed.
- Day INDEX note: _records_/2026-11-04/INDEX.md did not exist in
  the main working tree when this pass ran (that tree sits on
  another branch); the records/2026-11-04 branch holds its own
  INDEX.md, and this pass appended its entry there.

## Outcome

Failed. No donation checked or made, no diamonds, money,
speedups or other spending. No alliance diplomacy, no
assembly, no teleport.

## Result stats

- target 30, achieved 0, resources_gained none, costs
  duration_10min_no_game_input, verified no,
  blocker_category e, device_takeovers 0,
  capture_attempts 5, issue 284
