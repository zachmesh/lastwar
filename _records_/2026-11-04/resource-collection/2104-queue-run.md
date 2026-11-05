---
title: Harvest queue run 2104
created: 2026-11-04T21:04:00-08:00
modified: 2026-11-04T21:04:00-08:00
version: 1.0.0
description: Ticker unit harvest-2026-11-04-1803 failed, Mac screen capture failure on all attempts, same blocker as Issue 284, continuing the consecutive failure run
status: failed
grounded_in:
  - source: live device checks on the owner Mac mini, 2026-11-04 21:04 to 21:12 PST
---

# Harvest queue run 2104

Unit: harvest-2026-11-04-1803, executor ticker-2104.
Session window: 2026-11-04 21:04 to about 21:12 PST, device
sessions cc-486 and cc-487. No different-device dialog was
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
  and web transports (last response 0 seconds old at check
  time).
- LastWar window present: com.lastwar.ios, pid 59735,
  fullscreen 1920x1080, with Google Chrome frontmost.
- Session cc-486: computer.control list_windows succeeded
  and listed the LastWar window, so the control channel
  itself was reachable; the capture stream was not.
- Attempt 1 (cc-486): computer.observe compact failed with
  "Failed to start stream due to audio/video capture
  failure".
- Attempt 2 (cc-486): computer.control activate selected
  the LastWar window for background input but captured no
  observation, same capture failure; computer.observe
  image view failed with the same error.
- Attempt 3 (cc-487, fresh session after ending cc-486
  and a connection.health check): computer.observe compact
  failed with the same error.
- Attempt 4 (cc-487): computer.control describe for
  LastWar failed with the same error, so even the
  accessibility-tree route was unavailable.
- Total capture attempts: 4, all failing with the identical
  audio/video capture error, across 2 sessions. This meets
  and exceeds the standing at-least-3-attempts retry rule.
- No blind taps were dispatched: without an observation, any
  tap could land on the wrong control, so the unit stops
  here under the check-first rule. This is a device capture
  failure, not an authorization failure: the standing owner
  authorization is intact, the device is online, and the app
  is running.

## Repeated failure mode

- This is the same blocker already filed as GitHub Issue
  #284 (label tooling, still open at this pass). The
  2034 pass recorded it as the next ticker pass after
  ticker-1934 (fifteenth consecutive capture-failure pass)
  to fail identically, with no ticker-2004 record in the
  local tree; this pass is the next ticker pass after
  2034 known to have failed identically and does not
  assert an exact consecutive count beyond that. This pass
  commented on #284 instead of filing a duplicate. Until
  the Mac screen-recording stream recovers, further ticker
  passes will fail their first unit the same way; the
  inbox held 72 units at this pass.

## Other pass steps

- Own PRs checked first: open records PRs 293
  (2026-11-04, post-1931 merge, awaiting the 2300 batch),
  265 (2026-11-02), 256 (2026-11-03) and 187 (2026-11-01)
  all name Owner lastwar-pr-integrator, none names this
  job, and none carries a question addressed to this job,
  so nothing was owed before game work. PR 293 carries no
  comments. The older three remain CONFLICTING on the
  action-log file per the integrator's re-check comments;
  that reconciliation belongs to the integrator, not to
  this ticker pass, and was not attempted inside this
  pass's 25-minute budget.
- Sync: reaped 0, expired 0, produced nothing new, 21
  regulars already queued.
- No zombie seeding: zombie chain zombie-2026-10-28 closed
  with unit 066 on 2026-10-30 (event ended about the 19:00
  reset 2026-10-30, no Zombie tab in the Events hub), and
  the seeding rule forbids a fresh chain until a Zombie
  Invasion tab is seen live again.
- Tracker untouched: a failed unit does not mark the
  regular, so the next tick re-produces the harvest unit.
- Delivery note: the local working tree sits on branch
  work/ops-execution-records and holds another job's
  in-flight state (unrelated modifications and deletions),
  so this pass's outputs were delivered through a temporary
  worktree onto the records/2026-11-04 branch, leaving that
  state undisturbed.

## Outcome

Failed. No resource collected, no diamonds, money,
speedups or other spending. No alliance diplomacy, no
assembly, no teleport.

## Result stats

- target full base sweep, achieved 0, resources_gained
  none, costs 0, verified no, blocker_category f,
  device_takeovers 0, capture_attempts 4, issue 284
