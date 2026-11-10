---
title: Alliance Gifts Queue Run
created: 2026-11-05T02:04:00-08:00
modified: 2026-11-05T02:24:00-08:00
version: 1.0.0
description: Gifts unit gifts-2026-11-04-2230 executed by ticker-0204, failed on Mac screen capture failure, twenty-seventh consecutive pass with this blocker
status: failed
grounded_in:
  - source: Mac mini device channel responses on 2026-11-05 about 02:04 to 02:24 local
---

# Alliance gifts 2026-11-05, ticker-0204

Unit gifts-2026-11-04-2230, failed. No gift screen was ever read
and no gift was claimed: the Mac screen-capture channel failed on
every attempt, so no game input was dispatched.

## Attempts

- Mac mini 1c817413-83e2-0545-cb90-36d5e096a6bd online;
  LastWar (com.lastwar.ios, pid 59735) running, window
  1920x1080 at (0,0), Google Chrome frontmost.
- Computer session cc-506: computer.control list_windows
  succeeded and listed the LastWar window, so the control
  channel itself was reachable; the capture stream was not.
  computer.control activate LastWar selected the window for
  background input but captured no observation, error
  "Failed to start stream due to audio/video capture
  failure"; computer.observe (compact) failed with the same
  error three times; screen.snap failed with the same error;
  computer.control describe LastWar failed with the same
  error. connection.health reported both transports healthy
  (native and web connected), so the failure is in the
  screen-capture stream, not the connection.
- Computer session cc-507 (fresh, after ending cc-506):
  computer.observe (compact) failed with the same error.
- Computer session cc-508 (fresh): the View-menu probe
  first run by ticker-0134 was repeated to check whether
  anything changed: computer.control menu View > Exit Full
  Screen on the LastWar window. The menu path still does
  not exist: the View menu still contains Landscape
  Orientation, Portrait Orientation, Zoom to Fit and Enter
  Full Screen. No menu input was sent. This confirms
  ticker-0134's finding unchanged - the app is still a
  windowed 1920x1080 window on an inactive Space
  (activate reports window_on_screen false, Chrome
  frontmost), not in native fullscreen, and the capture
  failure persists in that state. No further recovery was
  attempted inside the unit budget: Space switching and
  the set_window_frame gate were already tried and ruled
  out by ticker-0134, and Cmd+Tab is blocked by the tool.
- Total capture attempts: 8 across 3 sessions, all failing
  with the identical audio/video capture error. This meets
  and exceeds the standing at-least-3-attempts retry rule.
- No blind taps were dispatched: without an observation, any
  tap could land on the wrong control, so the unit stops here
  under the check-first rule. No different-device dialog was
  observed (no screen was ever captured) and no device
  takeover was needed.

## Repeated failure mode

- This is the same blocker already filed as GitHub Issue
  #284 (label tooling, still open at this pass). The
  ticker-0134 pass was the twenty-sixth consecutive ticker
  pass to fail identically (survivors unit, finished
  09:39:35Z); this pass is the twenty-seventh. This pass
  commented on #284 instead of filing a duplicate. The
  View-menu probe only re-confirms ticker-0134's diagnosis
  (game windowed on an inactive Space); no new diagnosis
  was found this pass.
- This is a device capture failure, not an authorization
  failure: the standing owner authorization is intact, the
  device is online, and the app is running.

## Other pass steps

- Own PRs checked first: open records PR 304 (2026-11-05,
  ticker-0004) names Owner lastwar-pr-integrator, not this
  job; it is MERGEABLE with CLEAN state and no comments, so
  nothing was owed before game work. Older open records PRs
  301 (2026-11-04), 265 (2026-11-02), 256 (2026-11-03) and
  187 (2026-11-01) likewise name the integrator; their
  action-log conflicts were resolved on the branch side by
  the ticker-0004 pass and await the integrator's batch
  merge, so nothing was attempted on them inside this pass.
- Sync: reaped 0, expired 1, produced nothing new, 21
  regulars already queued.
- No zombie seeding: no zombie-invasion unit in inbox or
  claimed; the chain zombie-2026-10-28 closed with unit 066
  on 2026-10-30 (event ended about the 19:00 reset
  2026-10-30, no Zombie tab in the Events hub), and the
  activity metadata forbids seeding a fresh chain until a
  Zombie Invasion tab is seen live again.
- Tracker untouched: a failed unit does not mark the
  regular, so the next tick re-produces the gifts unit.
- Pass stopped after this unit: with no observation channel,
  a second unit would fail identically and burn the pass
  budget, so the remaining inbox units were left queued
  (inbox 69 at this pass).
- Delivery note: the local working tree sits on branch
  work/ops-execution-records and holds another job's
  in-flight state (unrelated modifications and deletions),
  so this pass's outputs were delivered through a temporary
  worktree onto the records/2026-11-05 branch, leaving that
  state undisturbed.

## Outcome

Failed. No gift checked or claimed, no diamonds, money,
speedups or other spending. No alliance diplomacy, no
assembly, no teleport.

## Result stats

- target 0, achieved 0, resources_gained none, costs 0,
  verified no, blocker_category f, device_takeovers 0,
  capture_attempts 8, regular_claimed 0, premium_claimed 0,
  issue 284
