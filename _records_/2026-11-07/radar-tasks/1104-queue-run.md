---
title: Radar tasks queue run 1104
created: 2026-11-07T19:27:00Z
modified: 2026-11-07T19:27:00Z
level: L0
version: 1.0.0
description: Ticker-1104 radar unit, failed on screen-capture channel failure, Last War window off-Space, same blocker as Issue 282
status: unverified
---

# 1104 queue run - Radar Tasks

Executor: ticker-1104. Unit: radar-2026-11-07-1003.
Session window about 11:19 to 11:27 America/Los_Angeles.

## Not performed

- No game screen was ever read and no game input was dispatched.
  Every screen-capture step failed, so the radar screen was never
  entered, no ordinary task was executed, no stored count,
  stamina, restore line or pin inventory was read. The loss is
  the unexecuted radar unit for this slot (planned 10:03 local
  2026-11-07, expires 14:03 local 2026-11-07, window duel day 6
  - radar stack). Whether any stored tasks sat unexecuted, or
  any pin stood waiting, is unknown from this pass - nothing was
  read live and nothing was executed or claimed.

## Blocker, measured

- Device: Zhen's Mac mini (1c817413-83e2-0545-cb90-36d5e096a6bd),
  ONLINE. device.list last_seen 2026-11-07T18:41:20Z (10:41
  local 2026-11-07) - fresh at the 11:19 check. connection.health
  on the Mac mini: native and web transports both connected and
  healthy (native lastResponseAgeSeconds 0, web 9). The offline
  aspect (Issue 284) is over; this pass is the capture failure
  in its new form, Issue 282.
- Window: Last War (window_id 160366, pid 59735) 1920x1080 at
  global (0, -360), window_on_screen false - an inactive Space,
  exactly as the ticker-1020 pass found it about 40 minutes
  earlier. Same window, same pid, same position.
- Eleven device invokes, zero game screens:
  - computer.session start (cc-4) on the Mac mini: started.
  - list_windows LastWar: 1 window, (0, -360), 1920x1080.
  - activate LastWar: selected for background input, brought_to_front
    false, window_on_screen false, evidence_error "Failed to
    start stream due to audio/video capture failure".
  - computer.observe (attempt 1): screen_failed, same capture
    failure.
  - open_app LastWar: outcome_unknown - "The launch request was
    sent before its result could be verified", no retained
    evidence, retryable false, required_next observe.
  - computer.observe (attempt 2): screen_failed, same capture
    failure.
  - list_windows LastWar again: unchanged - same pid 59735,
    still (0, -360). The open_app launch produced no relaunch
    and no move.
  - set_window_frame LastWar to (0, 0): refused with
    observation_required - an earlier input result needs fresh
    observation; no capture exists to satisfy it, so the move
    could not be attempted.
  - connection.health on the Mac mini: both transports
    connected and healthy (see above).
  - computer.observe (attempt 3): screen_failed, same capture
    failure.
  - computer.session end (cc-4): ended.
  Four capture attempts failed (activate evidence plus three
  observes), all with the identical "Failed to start stream due
  to audio/video capture failure". This meets the standing retry
  rule of at least 3 attempts before recording a unit as
  access-failed, and the extra attempts added no new route.
- Recovery routes NOT retried, deliberately, per the
  ticker-1020 lessons folded into alliance-help 1.27.0:
  Mission Control was not opened (it wedged the channel in
  1020), and background Ctrl+Right was not tried (it does not
  switch Spaces through this channel). set_window_frame was
  tried once and is gated on an observation that cannot be
  produced, so it is not a live route while capture is down.
- The known reliable unblock stands (2026-11-05 correction):
  the owner clicking the LastWar Dock icon once brings the
  window to the active Space. That step needs the owner at
  the Mac. No "active on a different device" dialog appeared,
  so no takeover was needed or made.

## Repeated failure mode

- This is the same blocker already filed as GitHub Issue #282
  (label knowledge, still open at this pass): the
  one-hundred-eighth recorded consecutive access-failed pass,
  second in the new form (device online, capture failing) after
  the 106-pass offline streak ended with ticker-1003. The last
  recorded one was ticker-1020, the one-hundred-seventh, about
  40 minutes before this pass. No executed pass is recorded
  between 1020 and this one. This pass commented on #282
  instead of filing a duplicate. Until the capture stream is
  restored or the owner clicks the Dock icon, further ticker
  passes will fail their first unit the same way; the inbox
  held 74 units at this pass's stats (73 after this unit was
  claimed and the 5 expired units were reaped).

## Other pass steps

- Own PRs checked first: PR 398 (records/2026-11-07, post-1100
  batch) is open with 0 comments - nothing addressed to this
  job. Older records PRs 351, 301 and 256 remain open under the
  integrator, unchanged.
- Sync: reaped 0, expired 5, due 20, produced nothing new,
  all 20 regulars already queued. Queue stats at 19:19Z:
  inbox 74, claimed 0, done 1127. The 5 expired units are the
  unexecuted 0657 slot units (events, passes, secrets,
  treasures, trucks 2026-11-07-0657), moved to done as expired
  in the live pool.
- No zombie seeding: zombie chain zombie-2026-10-28 closed
  with unit 066 on 2026-10-30 (event ended about the 19:00
  reset 2026-10-30, no Zombie tab in the Events hub), and the
  seeding rule forbids a fresh chain until a Zombie Invasion
  tab is seen live again.
- Pre-reset zero-sweep pair for the 2026-11-07 19:00 reset
  (chain pre-reset-sweep-2026-11-07) sits in the inbox
  (pending 2); not yet due, untouched by this pass.
- Tracker untouched: a failed unit does not mark the regular,
  so the next tick re-produces the radar unit.
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

Failed. No radar screen read, no task executed, no claim made.
No diamonds, money, speedups or other spending. No alliance
diplomacy, no assembly, no teleport.

## Result stats

- target 1, achieved 0, resources_gained none,
  costs no_game_input, verified no, blocker_category e,
  device_takeovers 0, capture_attempts 4, issue 282
