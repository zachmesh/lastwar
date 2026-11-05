---
title: Harvest queue run 0434
created: 2026-11-05T04:34:00-08:00
modified: 2026-11-05T04:44:00-08:00
version: 1.0.0
description: Ticker unit harvest-2026-11-05-0203 failed, Mac screen capture failure on all attempts, same blocker as Issue 284, thirty-second consecutive pass; probe classifies OFF_SCREEN_WINDOW
status: failed
grounded_in:
  - source: live device checks on the owner Mac mini, 2026-11-05 04:35 to 04:44 PST
---

# Harvest queue run 0434

Unit: harvest-2026-11-05-0203, executor ticker-0434.
Session window: 2026-11-05 04:35 to about 04:44 PST, device
sessions cc-518, cc-519 and cc-520. No different-device dialog was
observed (no screen was ever captured) and no device
takeover was needed. No diamonds, money, speedup items or
paid button touched. No building or research started, no
assembly, no teleport.

## Not performed

- No game screen was ever read and no game input was
  dispatched. The Mac screen capture stream failed on every
  attempt, so the base, its resource bubbles and the HUD
  totals could not be read, and no bubble was tapped or
  verified. No harvest was collected. The Armed Truck state
  is unknown.

## Blocker, measured

- Device: Zhen's Mac mini (1c817413-83e2-0545-cb90-36d5e096a6bd),
  listed online, connection health healthy on both native
  and web transports (last response 0 to 1 seconds old at
  check time).
- LastWar window present: com.lastwar.ios, pid 59735,
  fullscreen 1920x1080 at 0,0, window_id 160366, with Google
  Chrome frontmost (Gmail inbox).
- Attempt 1 (cc-518): computer.control activate selected the
  LastWar window for background input but captured no
  observation - "Failed to start stream due to audio/video
  capture failure"; window_on_screen false,
  brought_to_front false.
- Attempt 2 (cc-518): computer.observe compact failed with
  the same error.
- Attempt 3 (cc-518): computer.observe image failed with the
  same error.
- Attempt 4 (cc-519, fresh session): computer.observe compact
  failed with the same error.
- Attempt 5 (cc-519): computer.control describe for LastWar
  failed with the same error, so even the
  accessibility-tree route was unavailable.
- Control check (cc-520): a Chrome window observation in a
  fresh session succeeded with a full accessibility tree
  (Gmail inbox, 60 elements), so the control channel works
  for other apps and the failure is specific to the game
  window.
- Total capture attempts: 5, all failing with the identical
  audio/video capture error, across 2 sessions, plus 1
  successful Chrome observation. This meets and exceeds the
  standing at-least-3-attempts retry rule.
- No blind taps were dispatched: without an observation, any
  tap could land on the wrong control, so the unit stops
  here under the check-first rule. This is a device capture
  failure, not an authorization failure: the standing owner
  authorization is intact, the device is online, and the app
  is running.

## Probe classification

- `_tools_/mac_capture_probe.py` (tool version 1.0.0) run
  against this pass's evidence classifies OFF_SCREEN_WINDOW
  (high confidence), stop_pass yes, exit code 10. Evidence:
  LastWar window_on_screen false; the identical capture
  error; Chrome observes normally; activate reports
  on_screen false and brought_to_front false. One probe step
  is missing: the View-menu inspect (Enter/Exit Full
  Screen), because the describe route is itself
  capture-blocked.
- Recovery still needs the one owner step: click the LastWar
  Dock icon once on the Mac mini (or run
  `_tools_/mac_lastwar_front.sh` in Terminal), then
  re-probe. No background control route moves the window -
  Space keys sent in the background do not switch Spaces,
  open_app returns outcome_unknown, and set_window_frame
  needs a fresh observation, which is exactly what the
  failure prevents. Never use Control-Command-F or Escape
  on this app (both crash it).

## Repeated failure mode

- This is the same blocker already filed as GitHub Issue
  #284 (label tooling, still open at this pass). The
  consecutive chain is: ticker-0304 the 29th (PR 310 body),
  ticker-0334 the 30th, ticker-0404 the 31st, this pass the
  32nd consecutive ticker pass with this blocker. This pass
  commented on #284 instead of filing a duplicate. Until
  the Mac screen-recording stream recovers - which needs the
  owner step above - further ticker passes will fail their
  first unit the same way; the inbox held 72 units at this
  pass.

## Other pass steps

- Own PRs checked first: the live records PR for today, PR
  310 (records/2026-11-05), carries no comments and no
  reviews, so nothing was owed before game work. The older
  open records PRs name Owner lastwar-pr-integrator, not
  this job.
- Sync: reaped 0, expired 0, due 21, produced nothing new,
  all 21 regulars already queued. Pool: inbox 72, claimed 0,
  done 893.
- No zombie seeding: zombie chain zombie-2026-10-28 closed
  with unit 066 on 2026-10-30 (event ended about the 19:00
  reset 2026-10-30, no Zombie tab in the Events hub), and
  the seeding rule forbids a fresh chain until a Zombie
  Invasion tab is seen live again. Zombie-invasion inbox 0
  per stats.
- Tracker untouched: a failed unit does not mark the
  regular, so the next tick re-produces the harvest unit.
- The pass stopped after this one unit - every unit needs
  the same game screen, and the probe says to stop.
- Delivery note: the local working tree sits on branch
  work/ops-execution-records and holds another job's
  in-flight state (unrelated modifications and deletions),
  so this pass's outputs were delivered through a temporary
  worktree onto the records/2026-11-05 branch, leaving that
  state undisturbed.

## Outcome

Failed. No resource collected, no diamonds, money,
speedups or other spending. No alliance diplomacy, no
assembly, no teleport.

## Result stats

- target full base sweep, achieved 0, resources_gained
  none, costs 0, verified no, blocker_category f,
  device_takeovers 0, capture_attempts 5, issue 284
