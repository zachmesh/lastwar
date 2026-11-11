---
title: Shop claims queue run 1458
created: 2026-11-07T22:58:00Z
modified: 2026-11-07T22:58:00Z
level: L0
version: 1.0.0
description: Ticker-1452 passes unit, failed on screen-capture channel failure, Last War window off-Space, same blocker as Issue 282
status: unverified
---

# 1458 queue run - Shop Claims

Executor: ticker-1452. Unit: passes-2026-11-07-1057.
Session window about 14:52 to 14:58 America/Los_Angeles.

## Not performed

- No game screen was ever read and no game input was dispatched.
  Every screen-capture step failed, so the shop was never opened,
  no Hot Deals free pack was checked, no Weekly Pass Free Supply
  auto-claim was seen, no Coin or Monthly pass daily pickup was
  read, and nothing was claimed. The loss is the unexecuted
  passes unit for this slot (planned 10:57 local 2026-11-07,
  expires 14:57 local 2026-11-07 - the unit was already past
  its expiry when claimed, so it also counts as late in the
  stats). Whether any shop claim stood unclaimed against
  today's cycle is unknown from this pass - nothing was read
  live and nothing was executed or claimed. The last live
  passes read stands at the 0633 checked-only unit of
  2026-11-07 (shop-claims/0633-queue-run.md).

## Blocker, measured

- Device: Zhen's Mac mini (1c817413-83e2-0545-cb90-36d5e096a6bd),
  ONLINE. device.list last_seen 2026-11-07T22:39:40Z (14:39
  local 2026-11-07) - fresh, about 13 minutes before this pass
  started. connection.health on the Mac mini: native and web
  transports both connected and healthy (native
  lastResponseAgeSeconds 0, web 3). The offline aspect (Issue
  284) is over; this pass is the capture failure in its new
  form, Issue 282.
- Window: Last War (window_id 160366, pid 59735) 1920x1080 at
  global (0, -360), window_on_screen false - an inactive Space,
  exactly as the ticker-1020, ticker-1104, ticker-1204 and
  ticker-1334 passes found it. Same window, same pid, same
  position.
- Nine device invokes, zero game screens:
  - computer.session start (cc-7) on the Mac mini: started.
  - computer.control activate LastWar: selected for background
    input, brought_to_front false, window_on_screen false,
    evidence_error "Failed to start stream due to
    audio/video capture failure".
  - computer.observe (attempt 1): screen_failed, same capture
    failure.
  - computer.observe (attempt 2, image view): screen_failed,
    same capture failure.
  - computer.session end (cc-7): ended.
  - computer.session start (cc-8): started.
  - computer.control list_windows LastWar: 1 window,
    (0, -360), 1920x1080, pid 59735 - the control channel
    itself is reachable while the capture stream is not.
  - computer.control activate LastWar: selected for background
    input, brought_to_front false, window_on_screen false,
    same capture failure.
  - computer.observe (attempt 3): screen_failed, same capture
    failure.
  - connection.health on the Mac mini: both transports
    connected and healthy (see above).
  - computer.session end (cc-8): ended.
  Five capture attempts failed (two activate evidences plus
  three observes), all with the identical "Failed to start
  stream due to audio/video capture failure". This meets the
  standing retry rule of at least 3 attempts before recording
  a unit as access-failed, and the extra attempts added no
  new route.
- Recovery routes NOT retried, deliberately, per the
  ticker-1020 lessons folded into alliance-help 1.27.0 and
  alliance-donations 1.47.0 and confirmed by ticker-1104,
  ticker-1204 and ticker-1334: Mission Control was not
  opened (it wedged the channel in 1020), background
  Ctrl+Right was not tried (it does not switch Spaces
  through this channel), and open_app was not retried (1104:
  outcome_unknown, no relaunch and no move).
  set_window_frame was not retried (1204: refused with
  observation_required - an earlier input result needs fresh
  observation; no capture exists to satisfy it, so the move
  could not be attempted).
- The known reliable unblock stands (2026-11-05 correction):
  the owner clicking the LastWar Dock icon once brings the
  window to the active Space. That step needs the owner at
  the Mac. No "active on a different device" dialog appeared,
  so no takeover was needed or made.

## Repeated failure mode

- This is the same blocker already filed as GitHub Issue #282
  (label knowledge, still open at this pass): the
  one-hundred-eleventh recorded consecutive access-failed pass,
  fifth in the new form (device online, capture failing) after
  the 106-pass offline streak ended with ticker-1003. The last
  recorded one was ticker-1334, the one-hundred-tenth, about
  1 hour 20 minutes before this pass. No executed pass is
  recorded between 1334 and this one. This pass commented on
  #282 instead of filing a duplicate. Until the capture stream
  is restored or the owner clicks the Dock icon, further ticker
  passes will fail their first unit the same way; the inbox
  held 66 units at this pass's stats.

## Other pass steps

- Own PRs checked first: PR 398 (records/2026-11-07, post-1100
  batch) is open, Owner lastwar-pr-integrator. Its newest
  comments are the integrator's own 13:30 conflict note and
  13:41 correction (the conflict call was wrong; the PR is
  MERGEABLE/CLEAN and awaits the 15:00 batch) - nothing is
  addressed to this job. Older records PRs 351, 301 and 256
  remain open under the integrator, unchanged. No new PR was
  opened: PR 398 already covers the records/2026-11-07 branch.
- Sync: reaped 0, expired 9, due 22, produced
  duel-score-2026-11-07-1430, all 20 other regulars already
  queued. Queue stats at 22:54Z: inbox 66, claimed 0,
  done 1077.
- No zombie seeding: zombie chain zombie-2026-10-28 closed
  with unit 066 on 2026-10-30 (event ended about the 19:00
  reset 2026-10-30, no Zombie tab in the Events hub), and the
  seeding rule forbids a fresh chain until a Zombie Invasion
  tab is seen live again.
- Pre-reset zero-sweep pair for the 2026-11-07 19:00 reset
  (chain pre-reset-sweep-2026-11-07) sits in the inbox
  (pending 2); not yet due, untouched by this pass. If the
  capture channel recovers before 19:00, the 17:30 and 18:30
  sweeps are the backstop for the day's unmeasured shop
  claim state.
- Tracker untouched: a failed unit does not mark the regular,
  so the next tick re-produces the passes unit.
- Delivery note: the local working tree sits on branch
  work/ops-execution-records and holds another job's
  in-flight state (unrelated modifications and deletions),
  and the records/2026-11-07 branch itself is checked out in
  another worktree (pi-0330-1107), so this pass's outputs were
  delivered through a temporary worktree at the fetched branch
  tip (7b17e39373), leaving both states undisturbed. PR 398
  already covers the branch, so no new PR was opened.
- The pass stopped after this one unit: with the capture
  channel down, further units would fail identically.

## Outcome

Failed. No shop screen read, no free pack checked, no pass
pickup claimed. No diamonds, money, speedups or other
spending. No alliance diplomacy, no assembly, no teleport.

## Result stats

- target 1, achieved 0, resources_gained none,
  costs no_game_input, verified no, blocker_category e,
  device_takeovers 0, capture_attempts 5, issue 282
