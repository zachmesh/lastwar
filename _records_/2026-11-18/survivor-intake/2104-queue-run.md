---
title: Survivors queue run 2104
created: 2026-11-19T05:25:00Z
modified: 2026-11-19T05:25:00Z
version: 1.0.0
description: Survivors unit survivors-2026-11-18-1803 failed - Last War game window unavailable on the Mac mini
---

# Survivors queue run 2104

- Executor: ticker-2104
- Unit: survivors-2026-11-18-1803 (regular survivors, activity survivor-intake)
- Session window: 21:04-21:25 PST, 2026-11-18
- Status: failed - device access, game window unavailable

## What happened

- Sync ran at 21:05: 22 due, 0 produced (all already queued), 0 expired,
  1 completion marker reaped (radar-2026-11-18-1803). Inbox holds 73 units.
- Zombie seeding skipped: the Zombie Invasion event is not live. The
  chain zombie-2026-11-10 closed on 2026-11-14/15 when its last unit
  (037) found no Zombie Invasion tab in the Events hub, and the
  activity metadata says not to seed a fresh chain until the tab is
  seen live again. No zombie unit sits in inbox or claimed.
- OWN PRS FIRST could not run via the VPS gh CLI (VPS SSH down, see
  below). Fallback check via the unauthenticated GitHub API on the
  public repo: 3 open PRs - #711 (knowledge, work/ko-1132-lock-1047),
  #708 (records 2026-11-12), #425 (tools log gate). #711 has 0
  comments. None is the live records/2026-11-18 PR, none is owned by
  this job, and nothing is addressed to the ticker. No open PR exists
  for records/2026-11-18. Nothing for this pass to answer.
- Token acquired by ticker-2104 until 21:38:54 PST. Next unit picked:
  survivors-2026-11-18-1803, claimed until 21:44:01 PST.
- Mac mini (1c817413-83e2-0545-cb90-36d5e096a6bd) is ONLINE -
  device.list shows connection_state online, last seen 20:26:03 PST.
- environment.describe lists LastWar among running apps, but the app
  has no window: computer.control activate failed with
  ax_windows_empty, and list_windows (11 windows) lists no LastWar
  window. This is the same window-lost state as since 2026-11-17 03:33.
- Recovery attempts, all inside computer session cc-111 (at least 3,
  per the owner rule):
  - activate LastWar - ax_windows_empty, no bound window
    (action FAC24E20)
  - open_app LastWar - outcome_unknown (action 7B20EE14), no window
    appeared on re-check; the result said to inspect before
    repeating the launch, so it was not repeated
  - list_windows - 11 windows, none LastWar
  - environment.describe refresh - LastWar still running, still
    windowless
  - computer.observe - observation_unavailable, no target window
- No game input was possible, so no survivor intake was performed, no
  tasks were claimed or executed, and no game state was read. Nothing
  was tapped, spent, or claimed. This is the 55th consecutive
  windowless-LastWar occurrence.
- The failure is device-level, not unit-level: every further unit in
  this pass would fail the same way, so the execute loop stops here
  instead of burning the pass on identical failures. The survivors unit
  closed failed; the tracker was left untouched.
- Token released by ticker-2104; computer session cc-111 ended.

## VPS and delivery blockers

- VPS SSH still down: ssh centos@66.179.249.233 returns
  Permission denied (publickey), same as since about 2026-11-12
  12:46 PT (about 152 hours). The owner-chosen IONOS console recovery
  (2026-11-14) is still not landed or verified.
- Because the VPS is unreachable, the push-and-PR delivery for this
  pass cannot run: no bundle to the VPS, no push of
  records/2026-11-18, no PR check or creation via the VPS gh CLI.
  This pass is partial on delivery; its commits stay on the local
  records branch, unpushed, with no PR for records/2026-11-18.
  Missed integrator batches stand at 39 after the 19:00 point; with
  no PR from this pass, the 23:00 batch will also be missed.
- The local working tree sits on branch work/ops-execution-records
  with another job's in-flight state. Per the task body, that state
  was not disturbed; this pass's records were committed from the
  records worktree instead.

## Consequences

- The survivors unit failed unplayed, so no survivor intake happened
  in this pass. The reset-day units (73 in inbox) remain unplayed.
- No game unit has executed since ticker-0214 gifts on Nov 17 02:14 PT.
- The Mac being back online is not enough without a game window. The
  wedged windowless LastWar process needs a quit-and-relaunch on the
  Mac (or the owner's intervention) before any ticker pass can
  execute again.
- Previous pass was also an access failure; this pass reports in
  Chinese per the reporting rule.
