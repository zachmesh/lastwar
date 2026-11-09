---
title: Arms Race queue run 1204
created: 2026-11-07T20:32:00Z
modified: 2026-11-07T20:40:00Z
level: L0
version: 1.0.0
description: Ticker-1204 arms-race unit, failed on screen-capture channel failure, Last War window off-Space, same blocker as Issue 282
status: unverified
---

# 1204 queue run - Arms Race

Executor: ticker-1204. Unit: arms-race-2026-11-07-1003.
Session window about 12:30 to 12:40 America/Los_Angeles.

## Not performed

- No game screen was ever read and no game input was dispatched.
  Every screen-capture step failed, so the Arms Race phase was never
  read, no live score was taken, no scoring action was done, no
  chest was claimed. The loss is the unexecuted arms-race unit for
  this slot (planned 10:03 local 2026-11-07, expires 14:03 local
  2026-11-07, window duel day 6). Whether the live phase's top
  chest threshold stood met or short is unknown from this pass -
  nothing was read live and nothing was executed or claimed.

## Blocker, measured

- Device: Zhen's Mac mini (1c817413-83e2-0545-cb90-36d5e096a6bd),
  ONLINE. device.list last_seen 2026-11-07T18:41:20Z (10:41
  local 2026-11-07) - stale about 1 hour 50 minutes at the
  12:31 re-check, unchanged since the ticker-1104 pass about
  1 hour 10 minutes earlier. connection.health on the Mac mini:
  native and web transports both connected and healthy (native
  lastResponseAgeSeconds 0, web 0). The offline aspect (Issue
  284) is over; this pass is the capture failure in its new
  form, Issue 282.
- Window: Last War (window_id 160366, pid 59735) 1920x1080 at
  global (0, -360), window_on_screen false - an inactive Space,
  exactly as the ticker-1020 and ticker-1104 passes found it.
  Same window, same pid, same position.
- Nine device invokes, zero game screens:
  - computer.session start (cc-5) on the Mac mini: started.
  - list_windows LastWar: 1 window, (0, -360), 1920x1080.
  - activate LastWar: selected for background input, brought_to_front
    false, window_on_screen false, evidence_error "Failed to
    start stream due to audio/video capture failure".
  - computer.observe (attempt 1): screen_failed, same capture
    failure.
  - set_window_frame LastWar to (0, 0): refused with
    observation_required - an earlier input result needs fresh
    observation; no capture exists to satisfy it, so the move
    could not be attempted. Tried before any open_app this
    pass, so the ordering differs from 1104 but the gate is
    the same.
  - computer.observe (attempt 2): screen_failed, same capture
    failure.
  - connection.health on the Mac mini: both transports
    connected and healthy (see above).
  - computer.observe (attempt 3): screen_failed, same capture
    failure.
  - computer.session end (cc-5): ended.
  Four capture attempts failed (activate evidence plus three
  observes), all with the identical "Failed to start stream due
  to audio/video capture failure". This meets the standing retry
  rule of at least 3 attempts before recording a unit as
  access-failed, and the extra attempts added no new route.
- Recovery routes NOT retried, deliberately, per the
  ticker-1020 lessons folded into alliance-help 1.27.0 and
  confirmed by ticker-1104: Mission Control was not opened (it
  wedged the channel in 1020), background Ctrl+Right was not
  tried (it does not switch Spaces through this channel), and
  open_app was not retried (1104: outcome_unknown, no relaunch
  and no move). set_window_frame was tried once and is gated on
  an observation that cannot be produced, so it is not a live
  route while capture is down.
- The known reliable unblock stands (2026-11-05 correction):
  the owner clicking the LastWar Dock icon once brings the
  window to the active Space. That step needs the owner at
  the Mac. No "active on a different device" dialog appeared,
  so no takeover was needed or made.

## Repeated failure mode

- This is the same blocker already filed as GitHub Issue #282
  (label knowledge, still open at this pass): the
  one-hundred-ninth recorded consecutive access-failed pass,
  third in the new form (device online, capture failing) after
  the 106-pass offline streak ended with ticker-1003. The last
  recorded one was ticker-1104, the one-hundred-eighth, about
  1 hour 10 minutes before this pass. No executed pass is
  recorded between 1104 and this one. This pass commented on
  #282 instead of filing a duplicate. Until the capture stream
  is restored or the owner clicks the Dock icon, further ticker
  passes will fail their first unit the same way; the inbox
  held 78 units at this pass's stats.

## Other pass steps

- Own PRs checked first: PR 398 (records/2026-11-07, post-1100
  batch) is open with 0 comments - nothing addressed to this
  job. Older records PRs 351, 301 and 256 remain open under the
  integrator, unchanged; the 12:00 and 12:15 integrator passes
  verified PR 398 MERGEABLE/CLEAN, awaiting the 15:00 batch.
- Sync: reaped 0, expired 0, due 20, produced nothing new,
  all 20 regulars already queued. Queue stats at 20:29Z:
  inbox 78, claimed 0, done 1128.
- No zombie seeding: zombie chain zombie-2026-10-28 closed
  with unit 066 on 2026-10-30 (event ended about the 19:00
  reset 2026-10-30, no Zombie tab in the Events hub), and the
  seeding rule forbids a fresh chain until a Zombie Invasion
  tab is seen live again.
- Pre-reset zero-sweep pair for the 2026-11-07 19:00 reset
  (chain pre-reset-sweep-2026-11-07) sits in the inbox
  (pending 2); not yet due, untouched by this pass.
- Tracker untouched: a failed unit does not mark the regular,
  so the next tick re-produces the arms-race unit.
- Delivery note: the local working tree sits on branch
  work/ops-execution-records and holds another job's
  in-flight state (unrelated modifications and deletions),
  so this pass's outputs were delivered through a temporary
  worktree onto the records/2026-11-07 branch, leaving that
  state undisturbed. PR 398 already covers the branch, so no
  new PR was opened.
- The pass stopped after this one unit: with the capture
  channel down, further units would fail identically.

## Outcome

Failed. No Arms Race screen read, no task executed, no claim made.
No diamonds, money, speedups or other spending. No alliance
diplomacy, no assembly, no teleport.

## Result stats

- target 1, achieved 0, resources_gained none,
  costs no_game_input, verified no, blocker_category e,
  device_takeovers 0, capture_attempts 4, issue 282
