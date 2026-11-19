---
title: Queue ticker pass 1404
created: 2026-11-19T22:04:00Z
modified: 2026-11-19T22:10:00Z
version: 1.0.0
description: Ticker pass 1404 failed - Last War game window unavailable on the Mac mini, no unit claimed
---

# Queue ticker pass 1404

- Executor: ticker-1404
- Unit: none claimed (probe failed before claim, per the honored route)
- Session window: 14:04-14:10 PST, 2026-11-19
- Status: failed - device access, game window unavailable

## What happened

- Sync ran at 14:04: 23 due, 0 produced (all already queued), 4
  expired reaped. Branch reconcile warning: fetch of
  records/2026-11-19 failed (could not find remote ref),
  reconcile skipped (issue #446) - the branch has never been
  pushed; expected, not a new failure.
- Zombie seeding skipped: the Zombie Invasion event is not live. The
  event ended at about the 19:00 reset on 2026-10-30, the chain
  zombie-2026-11-10 closed on 2026-11-14/15 when its last unit
  found no Zombie Invasion tab in the Events hub, and the activity
  metadata says not to seed a fresh chain until the tab is seen
  live again. No zombie unit sits in inbox or claimed.
- Route honored (deviation watch): the newest record
  (ticker-1347, queue-ticker/1347-queue-run.md) was re-read first,
  and the device was probed BEFORE any claim. The probe failed,
  so no unit was claimed and no token was acquired - this pass
  burns no unit attempt on a known-dead channel. The would-be
  unit (next pick, read-only) was help-2026-11-19-1030; it stays
  in inbox for a future pass once the window returns. No token
  was taken, so no token release is owed.
- Mac mini (1c817413-83e2-0545-cb90-36d5e096a6bd) is ONLINE -
  device.list shows connection_state online, last seen 13:55:23
  PST; environment.describe lists LastWar among running apps,
  but the app has no window: the same window-lost state as since
  2026-11-17 03:33.
- Recovery attempts, all inside computer session cc-136 (started,
  ended clean):
  - list_windows app LastWar - 0 windows
  - activate LastWar - ax_windows_empty, no bound window
    (attempt 1)
  - open_app LastWar - outcome_unknown (action 218EF462)
    (attempt 2)
  - list_windows app LastWar - 0 windows again
  - computer.observe mode current - observation_unavailable, no
    target window
  - open_app LastWar again - outcome_unknown (action EC428886)
    (attempt 3)
  - list_windows app LastWar - 0 windows again
- No game input was possible, so no screen was ever entered,
  nothing was read, claimed, tapped, or spent. The tracker is
  untouched. The failure is device-level, not unit-level: every
  further unit in this pass would fail the same way, so the
  execute loop stops here instead of burning the pass on
  identical failures.

## Own PRs first

- VPS SSH is down, so the gh CLI route could not run. Checked the
  open PRs on zachmesh/lastwar through the unauthenticated GitHub
  REST API instead: #711 knowledge (head work/ko-1132-lock-1047,
  2026-11-12), #708 records 2026-11-12, #425 tools. All three
  match the 1347 pass verification - unchanged, no new comment
  or review, nothing addressed to this job. #708 (Owner
  lastwar-pr-integrator) has 0 comments. No open PR exists for
  records/2026-11-19 (branch never pushed). Nothing to reply to
  or fix; no PR work was owed by this pass beyond its own
  delivery, which is blocked below.

## VPS and delivery blockers

- VPS SSH still down: ssh centos@66.179.249.233 returns
  Permission denied (publickey), probed at the start of this pass,
  same as since about 2026-11-12 12:46 PT - about 169.3 hours into
  the outage. The owner-chosen IONOS console recovery (2026-11-14)
  is still not landed or verified.
- Because the VPS is unreachable, the push-and-PR delivery for this
  pass cannot run: no bundle to the VPS, no push of
  records/2026-11-19, no PR check or creation. This pass is partial
  on delivery; its commit stays on the local records/2026-11-19
  branch.
- The local working tree sits on branch work/ops-execution-records
  with another job's in-flight state. Per the task body, that state
  was not disturbed; this pass's records were committed from the
  records worktree instead, appending only this pass's own section
  and log line onto the branch versions of the day INDEX and the
  action log (never copying the live-tree versions over them).

## Consequences

- Duel day 4 runs to 18:00 PT Nov 19 with radar on STACK posture -
  the stack cannot be worked until the window returns. Inbox holds
  72 units at this pass's end; nothing due was played.
- No game unit has played since ticker-0214 gifts on Nov 17 02:14 PT
  (about 60 hours). This is the 69th consecutive window-loss
  occurrence by chain arithmetic (ticker-1347 was the 68th); the
  retro owns the count. Missed batches stand at 42 per the
  planner-1240 pass at 12:40 PT today.
- The wedged windowless LastWar process needs a quit-and-relaunch
  on the Mac (or the owner's intervention) before any ticker pass
  can execute again. No device command available to this pass can
  quit a windowless app: menu needs a selected window, and there is
  no shell or process command.
- Previous passes were also access failures (most recently
  ticker-1347 at 13:47 PT today); this pass reports in Chinese per
  the reporting rule.
