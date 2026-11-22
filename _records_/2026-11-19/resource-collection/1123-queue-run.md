---
title: Harvest queue run 1104
created: 2026-11-19T19:23:00Z
modified: 2026-11-19T19:23:00Z
version: 1.0.0
description: Harvest unit harvest-2026-11-19-1003 failed - Last War game window unavailable on the Mac mini
---

# Harvest queue run 1104

- Executor: ticker-1104
- Unit: harvest-2026-11-19-1003 (regular harvest, activity resource-collection)
- Session window: 11:04-11:23 PST, 2026-11-19
- Status: failed - device access, game window unavailable

## What happened

- Sync ran at 11:04: 23 due, 0 produced (all already queued),
  5 expired, 0 reaped, 1 completion marker reaped
  (radar-2026-11-19-0603). Branch reconcile warning: fetch of
  records/2026-11-19 failed (could not find remote ref), reconcile
  skipped (issue #446) - the branch has never been pushed; expected,
  not a new failure. Inbox 73 units.
- Zombie seeding skipped: the Zombie Invasion event is not live. The
  chain zombie-2026-11-10 closed on 2026-11-14/15 when its last unit
  (037) found no Zombie Invasion tab in the Events hub, and the
  activity metadata says not to seed a fresh chain until the tab is
  seen live again. No zombie unit sits in inbox or claimed.
- Token acquired by ticker-1104 until 11:29:38 PST. Next unit picked:
  harvest-2026-11-19-1003, claimed until 11:34:59 PST.
- Mac mini (1c817413-83e2-0545-cb90-36d5e096a6bd) is ONLINE -
  device.list shows connection_state online, but last_seen
  09:57:39 PST, about 83 minutes stale at probe time - the same
  frozen-last_seen shade earlier passes recorded on a live channel.
- environment.describe lists LastWar among running apps, but the app
  has no window: the same window-lost state as since 2026-11-17 03:33.
- Recovery attempts, all inside computer session cc-133 (started,
  ended clean):
  - activate LastWar - ax_windows_empty, no bound window
  - list_windows app=LastWar - 0 windows
  - screen.snap - computer_busy, then observation_unavailable
  - open_app LastWar - outcome_unknown (action CF56C4E8), not repeated
  - computer.observe mode=current - observation_unavailable
  - list_windows (all) - 11 windows, no LastWar window
  - list_windows app=LastWar again - still 0 windows
  - environment.describe refresh - LastWar still listed running
  - frontmost_app - the assistant itself, no game window to select
  - activate LastWar again - ax_windows_empty a second time
  - key ctrl+right (switch Space) - observation_required, no input
    dispatched, no target window exists to observe
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
  updated 2026-11-12T20:04:57Z), #708 records 2026-11-12 (head
  records/2026-11-12, updated 2026-11-12T20:44:37Z), #425 tools
  (head work/log-append-delivery-gate, updated
  2026-11-12T19:29:37Z). All three match the 00:32
  knowledge-organization pass's verification - unchanged, no new
  comment or review, nothing addressed to this job. No open PR
  exists for records/2026-11-19. Nothing to reply to or fix; no PR
  work was owed by this pass beyond its own delivery, which is
  blocked below.

## VPS and delivery blockers

- VPS SSH still down: ssh centos@66.179.249.233 returns
  Permission denied (publickey), probed at the start of this pass,
  same as since about 2026-11-12 12:46 PT - about 167 hours into
  the outage. The owner-chosen IONOS console recovery (2026-11-14)
  is still not landed or verified.
- Because the VPS is unreachable, the push-and-PR delivery for this
  pass cannot run: no bundle to the VPS, no push of
  records/2026-11-19, no PR check or creation. This pass is partial
  on delivery; its commit stays on the local records/2026-11-19
  branch.
- The local working tree sits on branch work/ops-execution-records
  with another job's in-flight state (2,582 changed paths,
  including staged deletions of _queue_/inbox files). Per the task
  body, that state was not disturbed; this pass's records were
  committed from a temporary worktree instead.

## Consequences

- No game unit has executed since ticker-0214 gifts on Nov 17
  02:14 PT - about 57 hours missed. Duel day 4 Train Heroes runs
  to 18:00 PT Nov 19 and its duel-score units sit unplayed in the
  inbox (73 units at this pass's sync). Nothing due was played in
  this pass.
- The Mac being online is not new, but without a game window the
  ticker still cannot play. The wedged windowless LastWar process
  needs a quit-and-relaunch on the Mac (or the owner's intervention)
  before any ticker pass can execute again. No device command
  available to this pass can quit a windowless app: menu needs a
  selected window, and there is no shell or process command.
- Previous passes were also access failures (most recently
  ticker-0934 at 09:34 PT today, the 65th consecutive window-loss
  occurrence); this pass is the 66th by chain arithmetic, and it
  reports in Chinese per the reporting rule. Retro owns the count.
