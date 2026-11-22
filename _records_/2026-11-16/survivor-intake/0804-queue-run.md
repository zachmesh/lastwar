---
title: Survivors 2026-11-16 ticker-0804 failed, Mac mini offline
created: 2026-11-16T16:24:00Z
modified: 2026-11-16T16:24:00Z
version: 1.0.0
description: Survivors unit survivors-2026-11-16-0603 failed, Mac mini unreachable
status: failed
grounded_in:
  - source: device.list and device.describe on 1c817413-83e2-0545-cb90-36d5e096a6bd, 2026-11-16T16:16Z to 16:17Z
  - source: device.invoke connection.health on 1c817413-83e2-0545-cb90-36d5e096a6bd, connection.repair and connection.health on its recovery device, 2026-11-16T16:19Z to 16:21Z
  - source: tools/duel.py --json, 2026-11-16T16:18Z
  - source: GitHub connector list_pull_requests for zachmesh/lastwar, 2026-11-16T16:17Z
  - source: VPS SSH probe, 2026-11-16T16:15Z
---

# Survivors 2026-11-16 ticker-0804 failed, Mac mini offline

- Executor: ticker-0804
- Unit: survivors-2026-11-16-0603, regular survivors, activity survivor-intake, priority 3, est 3 minutes
- Session window: 08:04-08:24 local, token held 08:17-08:24 local

## What happened

- The Mac mini (Zhen's Mac mini, 1c817413-83e2-0545-cb90-36d5e096a6bd)
  is still OFFLINE. Five device probes, all offline or timed out, no
  wake-up path: device.list, device.describe, connection.health on
  the Mac (node_offline), connection.repair on the recovery device
  (first attempt refused with invalid_command_params for target
  "web", second attempt with target "native" timed out after 25s),
  connection.health on the recovery device (25s timeout).
  last_seen frozen at 2026-11-15T13:19:56Z (05:19 PT Nov 15), about
  27h04m stale at 16:24Z. This is the nineteenth consecutive ticker
  pass to fail on the offline Mac (2143, 2204, 2234, 2304, 2334, 0004,
  0112, 0134, 0204, 0234, 0304, 0334, 0404, 0528, 0604, 0634, 0704,
  0734 before it).
- No survivor work was executed, nothing claimed, nothing spent. The
  tracker is untouched. The pass stopped after this unit rather than
  cascading failed units.

## Own PRs first

- VPS route down (SSH Permission denied, see below), so the check ran
  through the GitHub connector's list_pull_requests for zachmesh/lastwar.
- Open PRs: #711 (knowledge, Owner lastwar-knowledge-organizer), #708
  (records 2026-11-12, Owner lastwar-pr-integrator), #425 (tooling,
  Owner lastwar-tool-developer). Heads and updated_at unchanged since
  Nov 12 (#708 2026-11-12T20:44:37Z, #711 2026-11-12T20:04:57Z, #425
  2026-11-12T19:29:37Z). None is owned by this job; no open PR for
  records/2026-11-16. No question addressed to this job, nothing to fix.
- Limitation: the live GitHub MCP server does not advertise a
  read-only PR detail tool, so the newest PR comments could not be
  read this pass. The list output (state, head SHA, updated_at) is
  the only live read available; no comment activity is visible from
  it, and updated_at has not moved since Nov 12.

## Sync and seeding

- Sync: reaped 0, expired 0, due 22, produced 0, already queued 20
  (mail, help, gifts, harvest, vip, passes, daily-missions, secrets,
  treasures, survivors, trucks, train, training, donations, events,
  arms-race, star-ceremony, duel-score, scout, scout-midday);
  skipped_closed: radar-2026-11-16-0603. Roster stale warning for
  building-queues and research (issue #198). Branch reconcile skipped
  with a warning: fetch of records/2026-11-16 failed (remote ref
  missing), issue #446.
- Zombie seeding no-op: the Glacieradon event ended Nov 14 (live
  check by unit 037, no Zombie Invasion tab in the Events hub), the
  chain zombie-2026-11-10 stays closed, and no zombie-invasion unit
  sits in inbox or claimed. No fresh chain is seeded until a Zombie
  Invasion tab is seen live in the Events hub again.

## Duel posture (read from tools/duel.py, not from the screen)

- Duel day 1, Radar Training, RELEASE posture. Claims score +30,000 per
  task. Day ends 18:00 PT Nov 16, 9.7 hours left at the 08:18 read.
  The release stays missed while the Mac is offline; the window is
  still open.

## Delivery

- VPS SSH still Permission denied (publickey), probed 16:15Z, about
  91.6 hours into the break (outage since about 12:46 PT 2026-11-12;
  owner chose the IONOS console route 2026-11-14 17:37 PT; no fix
  yet). Push and PR are blocked. Missed integrator batches stay 23
  (next batch point 11:00 PT Nov 16).
- Delivery PARTIAL: record committed locally on
  ticker-0804-1116-delivery, UNPUSHED, push pending VPS recovery;
  mirror copy in the live tree plus identical backup in the goal
  hidden_files. No Slack sync. Chat report owed per the ticker rule
  (previous pass also access-failed); this pass's final message
  carries it.

## Standing git status anomaly in the live mirror (persists)

- `git status` in the live mirror still reports a large changed set
  (modified activity files, deleted inbox unit files) while the
  queue tools run against the files on disk. No commit was attempted
  from this tree; the delivery commit goes through the worktree on
  ticker-0804-1116-delivery, as in the previous passes.
