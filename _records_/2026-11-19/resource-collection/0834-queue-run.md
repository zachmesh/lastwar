---
title: Harvest queue run 0834
created: 2026-11-19T16:45:00Z
modified: 2026-11-19T16:45:00Z
version: 1.0.0
description: Harvest unit harvest-2026-11-19-0603 failed - Last War game window unavailable on the Mac mini
---

# Harvest queue run 0834

- Executor: ticker-0834
- Unit: harvest-2026-11-19-0603 (regular harvest, activity resource-collection)
- Session window: 08:34-08:47 PST, 2026-11-19
- Status: failed - device access, game window unavailable

## What happened

- Sync ran at 08:34: 23 due, 0 produced (all already queued), 0 reaped.
  Branch reconcile warning: fetch of records/2026-11-19 failed
  (could not find remote ref), reconcile skipped (issue #446) - the
  branch has never been pushed; expected, not a new failure.
- Zombie seeding skipped: the Zombie Invasion event is not live. The
  chain zombie-2026-11-10 closed on 2026-11-14/15 when its last unit
  (037) found no Zombie Invasion tab in the Events hub, and the
  activity metadata says not to seed a fresh chain until the tab is
  seen live again. No zombie unit sits in inbox or claimed.
- Token acquired by ticker-0834 until 08:51:36 PST. Next unit picked:
  harvest-2026-11-19-0603, claimed until 08:56:47 PST.
- Mac mini (1c817413-83e2-0545-cb90-36d5e096a6bd) is ONLINE -
  device.list shows connection_state online, last seen 04:25:42 PST.
- environment.describe lists LastWar among running apps, but the app
  has no window: the same window-lost state as since 2026-11-17 03:33.
- Recovery attempts, all inside computer session cc-131 (started,
  ended clean):
  - open_app Last War - open_failed, no installed app matches
    (wrong name; the app is LastWar)
  - open_app LastWar - outcome_unknown (action 4A23F046)
  - computer.observe - observation_unavailable, no target window
  - activate LastWar - ax_windows_empty, no bound window
  - list_windows - 11 windows, no LastWar window
  - screen.snap - observation_unavailable
  - open_app LastWar again - outcome_unknown (action 0CDB9A12),
    list_windows app=LastWar still 0 windows
  - menu LastWar Quit - observation_required, no window to act on
- No game input was possible, so no bubbles were collected and no
  resource totals were read. Nothing was tapped, spent, or claimed.
- The failure is device-level, not unit-level: every further unit in
  this pass would fail the same way, so the execute loop stops here
  instead of burning the pass on identical failures.
- Unit completed as failed (tracker untouched, per the queue rules
  for failed units). Result stats: target collect ready resource
  bubbles and Armed Truck loot; achieved no game input, LastWar
  window unavailable; resources_gained none; costs about 10
  minutes device time, no stamina or items; verified yes;
  blocker_category f.

## Own PRs first

- VPS SSH is down, so the gh CLI route could not run. Checked the
  open PRs on zachmesh/lastwar through the unauthenticated GitHub
  REST API instead: #711 knowledge (head work/ko-1132-lock-1047,
  updated 2026-11-12T20:04:57Z), #708 records 2026-11-12, #425
  tools. All three match the 08:32 knowledge-organization pass's
  verification - unchanged, no new comment or review, nothing
  addressed to this job. No open PR exists for records/2026-11-19.
  Nothing to reply to or fix; no PR work was owed by this pass
  beyond its own delivery, which is blocked below.

## VPS and delivery blockers

- VPS SSH still down: ssh centos@66.179.249.233 returns
  Permission denied (publickey), probed at the start of this pass,
  same as since about 2026-11-12 12:46 PT - about 164 hours into
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

- The 19:00 reset on 2026-11-18 passed during this outage window
  with the VIP, passes, mail, gifts, help, events and other
  reset-day units still sitting in the inbox (78 units at this
  pass's sync). Nothing due was played in this pass.
- The Mac being online is not new, but without a game window the
  ticker still cannot play. The wedged windowless LastWar process
  needs a quit-and-relaunch on the Mac (or the owner's intervention)
  before any ticker pass can execute again. No device command
  available to this pass can quit a windowless app: menu needs a
  selected window, and there is no shell or process command.
- Previous passes were also access failures (most recently
  ticker-0704 at 07:04 PT today, the 63rd consecutive
  window-loss occurrence in today's records); this pass reports
  in Chinese per the reporting rule.
