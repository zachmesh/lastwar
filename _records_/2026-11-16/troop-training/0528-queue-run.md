---
title: Troop Training 2026-11-16 ticker-0528 failed, Mac mini offline
created: 2026-11-16T13:47:00Z
modified: 2026-11-16T13:47:00Z
version: 1.0.0
description: Training unit training-2026-11-16-0203 failed, Mac mini unreachable
status: failed
grounded_in:
  - source: device.list and device.describe on 1c817413-83e2-0545-cb90-36d5e096a6bd, 2026-11-16T13:30Z to 13:35Z
  - source: device.invoke connection.health twice and computer.session start on 1c817413-83e2-0545-cb90-36d5e096a6bd, 2026-11-16T13:31Z to 13:37Z
  - source: tools/duel.py --json, 2026-11-16T13:35Z
  - source: GitHub REST API list_pull_requests and pull comments for zachmesh/lastwar, 2026-11-16T13:32Z
  - source: VPS SSH probe, 2026-11-16T13:30Z
---

# Troop Training 2026-11-16 ticker-0528 failed, Mac mini offline

- Executor: ticker-0528
- Unit: training-2026-11-16-0203, regular training, activity troop-training, priority 3, est 4 minutes
- Session window: 05:28-05:47 local, token held 05:28-05:51 local

## What happened

- The Mac mini (Zhen's Mac mini, 1c817413-83e2-0545-cb90-36d5e096a6bd)
  is still OFFLINE. Five device probes, all node_offline, no wake-up
  path: device.list, device.describe, connection.health twice, and
  computer.session start. last_seen frozen at 2026-11-15T13:19:56Z
  (05:19 PT Nov 15), about 24h15m stale at 13:35Z. This is the
  fourteenth consecutive ticker pass to fail on the offline Mac
  (2143, 2204, 2234, 2304, 2334, 0004, 0112, 0134, 0204, 0234, 0304,
  0334, 0404 before it).
- No training work was executed. No barracks queue refilled, nothing
  claimed, nothing spent. The tracker is untouched (failed units
  leave it alone).
- The pass stopped after this unit rather than cascading failed units
  across the inbox, per the standing pattern of the previous
  thirteen offline passes.

## Own PRs first

- VPS route down (SSH Permission denied, see below), so the check ran
  through the public GitHub REST API (unauthenticated read of a
  public repo) for zachmesh/lastwar.
- Open PRs: #711 (knowledge, Owner lastwar-knowledge-organizer), #708
  (records 2026-11-12, Owner lastwar-pr-integrator), #425 (tooling,
  Owner lastwar-tool-developer). All three mergeable and clean, heads
  and updated_at unchanged since Nov 12 (#708 2026-11-12T20:44:37Z,
  #711 2026-11-12T20:04:57Z, #425 2026-11-12T19:29:37Z). None is
  owned by this job; no open PR for records/2026-11-15 or
  records/2026-11-16. Newest comments read: #711 carries a zachmesh
  note for the integrator and the next knowledge-organizer run (PR
  #710 merged after #711 opened); #425's newest comments are the Nov
  8 integrator conflict notes, superseded by the live clean state;
  #708 has no comments. No question addressed to this job, nothing
  to fix.

## Sync and seeding

- Sync: reaped 0, expired 0, due 22, produced 0 (all 22 already
  queued); completion marker reaped: survivors-2026-11-16-0203.
  Branch reconcile skipped with a warning: fetch of
  records/2026-11-16 failed (remote ref missing), issue #446.
- Zombie seeding no-op: Glacieradon ended Nov 14 (unit 037,
  ticker-1804, no Zombie Invasion tab in the Events hub); chain
  zombie-2026-11-10 is closed, and no fresh chain is seeded until a
  Zombie Invasion tab is seen live in the Events hub again.
- Queue hygiene note: ten empty 0-byte unit files sit in
  _queue_/inbox (zombie-invasion-zombie-2026-11-10-028 through
  -037); sync does not reap them and stats counts zombie-invasion
  inbox 0, so they are inert. Left in place. Gap owed: file a
  tooling issue for unparseable unit files never reaped by sync at
  VPS recovery (gh filing route is down with the VPS); closest
  existing issue is #705, sync reap acting on the worktree
  snapshot rather than the live pool.

## Duel posture (read from tools/duel.py, not from the screen)

- Duel day 1, Radar Training, RELEASE posture. Claims score +30,000 per
  task. Day ends 18:00 PT Nov 16, 12.4 hours left at 05:35. The release
  stays missed while the Mac is offline, but the window is still open.

## Delivery blocked

- VPS SSH still Permission denied (publickey), probed 13:30Z, about
  89 hours into the break (since ~12:46 PT Nov 12). No bundle, no
  push, no PR. Missed integrator batches stay 22 (next batch point
  07:00 PT Nov 16).
- Delivery PARTIAL: this record is committed locally on
  ticker-0528-1116-delivery (branched from
  planner-0440-1116-delivery), UNPUSHED, push pending VPS recovery.
  Mirror copy in the live tree plus an identical backup in the goal
  hidden_files. No PR for records/2026-11-16 can be opened while
  the VPS is down.
- No Slack sync. Chat report owed per the ticker rule (previous pass
  also access-failed); this pass's final message carries it.
