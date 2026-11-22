---
title: Radar queue run 1228
created: 2026-11-19T20:28:00Z
modified: 2026-11-19T20:33:00Z
version: 1.0.0
description: Radar unit radar-2026-11-19-1003 failed - Last War game window unavailable on the Mac mini
---

# Radar queue run 1228

- Executor: ticker-1228
- Unit: radar-2026-11-19-1003 (regular radar, activity radar-tasks)
- Session window: 12:28-12:33 PST, 2026-11-19
- Status: failed - device access, game window unavailable

## What happened

- Sync ran at 12:28: 23 due, 0 produced (all already queued), 0 reaped.
  Branch reconcile warning: fetch of records/2026-11-19 failed
  (could not find remote ref), reconcile skipped (issue #446) - the
  branch has never been pushed; expected, not a new failure.
- Zombie seeding skipped: the Zombie Invasion event is not live. The
  chain zombie-2026-11-10 closed on 2026-11-14/15 when its last unit
  (037) found no Zombie Invasion tab in the Events hub, and the
  activity metadata says not to seed a fresh chain until the tab is
  seen live again. No zombie unit sits in inbox or claimed.
- Token acquired by ticker-1228 until 12:44:06 PST. Next unit picked:
  radar-2026-11-19-1003, claimed until 12:49:21 PST. Duel day 4,
  radar posture STACK (complete, do not claim); the unit's
  expires_at is 14:03 PST, so the unit was still live when picked.
- Mac mini (1c817413-83e2-0545-cb90-36d5e096a6bd) is ONLINE -
  device.list shows connection_state online, last seen 12:06:05 PST.
- environment.describe lists LastWar among running apps, but the app
  has no window: the same window-lost state as since 2026-11-17 03:33.
- Recovery attempts, all inside computer session cc-134 (started,
  ended clean):
  - activate LastWar - ax_windows_empty, no bound window
    (attempt 1)
  - open_app LastWar - outcome_unknown (action AABE797F)
    (attempt 2)
  - list_windows app LastWar - 0 windows
  - computer.observe mode current - observation_unavailable, no
    target window
  - open_app LastWar again - outcome_unknown (action B3E4A3F9)
    (attempt 3)
  - list_windows app LastWar - 0 windows again
  - screen.snap with no target - observation_unavailable
- No game input was possible, so the radar screen was never entered,
  no stored count or stamina was read, no Quick Execute ran, and
  nothing was claimed. Nothing was tapped, spent, or claimed.
- The failure is device-level, not unit-level: every further unit in
  this pass would fail the same way, so the execute loop stops here
  instead of burning the pass on identical failures.
- Unit completed as failed (tracker untouched, per the queue rules
  for failed units). Result stats: target execute stored radar tasks
  on stack day 4 (complete, do not claim) and record closing reads;
  achieved no game input, LastWar window unavailable;
  resources_gained none; costs about 5 minutes device time, no
  stamina or items; verified yes; blocker_category f.

## Own PRs first

- VPS SSH is down, so the gh CLI route could not run. Checked the
  open PRs on zachmesh/lastwar through the unauthenticated GitHub
  REST API instead: #711 knowledge (head work/ko-1132-lock-1047,
  updated 2026-11-12T20:04:57Z), #708 records 2026-11-12, #425
  tools. All three match the 0934 pass verification - unchanged,
  no new comment or review, nothing addressed to this job. No open
  PR exists for records/2026-11-19 (branch 404 on the API); main
  HEAD is a858a0fca, unchanged. Nothing to reply to or fix; no PR
  work was owed by this pass beyond its own delivery, which is
  blocked below.

## VPS and delivery blockers

- VPS SSH still down: ssh centos@66.179.249.233 returns
  Permission denied (publickey), probed at the start of this pass,
  same as since about 2026-11-12 12:46 PT - about 167.8 hours into
  the outage. The owner-chosen IONOS console recovery (2026-11-14)
  is still not landed or verified.
- Because the VPS is unreachable, the push-and-PR delivery for this
  pass cannot run: no bundle to the VPS, no push of
  records/2026-11-19, no PR check or creation. This pass is partial
  on delivery; its commit stays on the local records/2026-11-19
  branch.
- The local working tree sits on branch work/ops-execution-records
  with another job's in-flight state (including staged deletions of
  tools/state/*.json while the files exist on disk). Per the task
  body, that state was not disturbed; this pass's records were
  committed from a temporary worktree instead.

## Consequences

- Duel day 4 runs to 18:00 PT Nov 19 with radar on STACK posture -
  the stack cannot be worked until the window returns. Inbox holds
  77 units at this pass's end; nothing due was played.
- No game unit has played since ticker-0214 gifts on Nov 17 02:14 PT
  (about 58 hours). This is the 67th consecutive window-loss
  occurrence by chain arithmetic (ticker-1104 was the 66th); the
  retro owns the count.
- The wedged windowless LastWar process needs a quit-and-relaunch
  on the Mac (or the owner's intervention) before any ticker pass
  can execute again. No device command available to this pass can
  quit a windowless app: menu needs a selected window, and there is
  no shell or process command.
- Previous passes were also access failures (most recently
  ticker-0934 at 09:34 PT today); this pass reports in Chinese per
  the reporting rule.

## Delivery repair (same pass, before any push)

- The first commit of this pass (8f6dfdda89) copied the main worktree's
  day INDEX and action log over the branch versions wholesale. That
  clobbered branch-only content: the 0834 ticker section in the day
  INDEX (which the main-tree INDEX lacks) and about 1,579 action-log
  lines present only on the branch. Caught by the commit's own
  stat review before any push; the commit was amended in place
  (still local, never pushed) to restore both branch files from
  the parent commit and re-apply only this pass's own additions
  (one INDEX section, one log line), matching the 0934/1104
  pattern. Lesson for the next pass: never copy the live-tree
  INDEX or action log onto the records branch - append only the
  pass's own section/line onto the branch versions.
