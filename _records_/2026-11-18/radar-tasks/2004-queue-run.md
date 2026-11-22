---
title: Radar queue run 2004
created: 2026-11-19T04:17:00Z
modified: 2026-11-19T04:17:00Z
version: 1.0.0
description: Radar unit radar-2026-11-18-1803 failed - Last War game window unavailable on the Mac mini
---

# Radar queue run 2004

- Executor: ticker-2004
- Unit: radar-2026-11-18-1803 (regular radar, activity radar-tasks, duel day 3 release)
- Session window: 20:04-20:16 PST, 2026-11-18
- Status: failed - device access, game window unavailable

## What happened

- Sync ran at 20:05: 22 due, 0 produced (all already queued), 0 expired,
  1 completion marker reaped (harvest-2026-11-18-1803). Inbox holds 68 units.
- Zombie seeding skipped: the Zombie Invasion event is not live. The
  chain zombie-2026-11-10 closed on 2026-11-14/15 when its last unit
  (037) found no Zombie Invasion tab in the Events hub, and the
  activity metadata says not to seed a fresh chain until the tab is
  seen live again. No zombie unit sits in inbox or claimed.
- OWN PRS FIRST could not run via the VPS gh CLI (VPS SSH down, see
  below). Fallback check via the unauthenticated GitHub API on the
  public repo: 3 open PRs - #711 (knowledge, work/ko-1132-lock-1047),
  #708 (records 2026-11-12), #425 (tools log gate). None is the live
  records/2026-11-18 PR, none is owned by this job, and the newest
  comment on #711 is a note for the integrator and the next
  knowledge-organizer run, not for the ticker. The #708 comments read
  hit the unauthenticated API rate limit. No open PR exists for
  records/2026-11-18. Nothing for this pass to answer.
- Token acquired by ticker-2004 until 20:23:50 PST. Next unit picked:
  radar-2026-11-18-1803, claimed.
- Mac mini (1c817413-83e2-0545-cb90-36d5e096a6bd) is ONLINE -
  device.list shows connection_state online, last seen 19:04:50 PST.
- environment.describe lists LastWar among running apps, but the app
  has no window: computer.control activate failed with
  ax_windows_empty, and list_windows (11 windows) lists no LastWar
  window. This is the same window-lost state as since 2026-11-17 03:33.
- Recovery attempts, all inside computer session cc-110:
  - open_app LastWar - outcome_unknown (action FE7BE7D5), no window
    appeared on re-check
  - computer.observe - observation_unavailable, no target window
  - activate LastWar - ax_windows_empty, no bound window
  - list_windows - no LastWar window
  - environment.describe refresh - LastWar still running, still
    windowless
- No game input was possible, so no radar screen was entered, no tasks
  were claimed or executed, and no duel score was read. Nothing was
  tapped, spent, or claimed. This is the 54th consecutive
  windowless-LastWar occurrence.
- The failure is device-level, not unit-level: every further unit in
  this pass would fail the same way, so the execute loop stops here
  instead of burning the pass on identical failures. The radar unit
  closed failed; the tracker was left untouched.
- Token released by ticker-2004; computer session cc-110 ended.

## VPS and delivery blockers

- VPS SSH still down: ssh centos@66.179.249.233 returns
  Permission denied (publickey), same as since about 2026-11-12
  12:46 PT (about 151 hours). The owner-chosen IONOS console recovery
  (2026-11-14) is still not landed or verified.
- Because the VPS is unreachable, the push-and-PR delivery for this
  pass cannot run: no bundle to the VPS, no push of
  records/2026-11-18, no PR check or creation via the VPS gh CLI.
  This pass is partial on delivery; its commits stay on the local
  records branch, unpushed, with no PR for records/2026-11-18.
  Missed integrator batches rise 38 to 39 (the 19:00 batch point
  passed during the previous pass with no records PR to merge).
- The local working tree sits on branch work/ops-execution-records
  with another job's in-flight state. Per the task body, that state
  was not disturbed; this pass's records were committed from the
  records worktree instead.

## Consequences

- The duel day 3 radar release unit failed unplayed, so the stacked
  radar claims for duel day 3 were not released in this pass. The
  reset-day units (68 in inbox) remain unplayed.
- No game unit has executed since ticker-0214 gifts on Nov 17 02:14 PT.
- The Mac being back online is not enough without a game window. The
  wedged windowless LastWar process needs a quit-and-relaunch on the
  Mac (or the owner's intervention) before any ticker pass can
  execute again.
- Previous pass was also an access failure; this pass reports in
  Chinese per the reporting rule.
