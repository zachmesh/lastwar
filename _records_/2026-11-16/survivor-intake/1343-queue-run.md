---
title: Survivors 2026-11-16 ticker-1343 failed, Mac mini offline
created: 2026-11-16T21:51:00Z
modified: 2026-11-16T21:51:00Z
version: 1.0.0
description: Survivors unit survivors-2026-11-16-1003 failed, Mac mini unreachable
status: failed
grounded_in:
  - source: device.list and device.describe on 1c817413-83e2-0545-cb90-36d5e096a6bd, 2026-11-16T21:43Z to 21:44Z
  - source: device.invoke connection.health and connection.repair on 1c817413-83e2-0545-cb90-36d5e096a6bd, 2026-11-16T21:45Z to 21:46Z, device.list again after 60s
  - source: tools/duel.py --json, 2026-11-16T21:50Z
  - source: unauthenticated GitHub REST API reads of zachmesh/lastwar PRs 711, 708, 425 and their comments, 2026-11-16T21:43Z
  - source: VPS SSH probe, 2026-11-16T21:43Z
---

# Survivors 2026-11-16 ticker-1343 failed, Mac mini offline

- Executor: ticker-1343
- Unit: survivors-2026-11-16-1003, regular survivors, activity survivor-intake, priority 3, est 3 minutes
- Session window: 13:43-13:51 local, token held 13:43-13:51 local

## What happened

- The Mac mini (Zhen's Mac mini, 1c817413-83e2-0545-cb90-36d5e096a6bd)
  is still OFFLINE. Five device probes, all offline, no wake-up
  path: device.list, device.describe, connection.health on the Mac
  (node_offline), connection.repair with target "web" (node_offline),
  device.list again after 60 seconds. last_seen frozen at
  2026-11-15T13:19:56Z (05:19 PT Nov 15), about 32h30m stale at
  21:51Z. This is the twenty-fourth consecutive ticker pass to fail
  on the offline Mac (ticker-1236 counted twenty-three at 12:34 PT;
  no ticker unit finished between 1236 and this pass).
- No survivor work was executed, nothing claimed, nothing spent. The
  tracker is untouched. The pass stopped after this unit rather than
  cascading failed units.
- Note: the evidence path passed to `queue.py complete` first named
  `_records_/2026-11-16/survivors/1343-queue-run.md`; the activity
  folder is `survivor-intake`, so the evidence field in the done unit
  file was corrected to that path before this record was written. No
  other unit field was touched.

## Own PRs first

- VPS route down (SSH Permission denied, see below), so the check ran
  through the unauthenticated public GitHub REST API for
  zachmesh/lastwar (PR list plus per-PR comments).
- Open PRs: #711 (knowledge, Owner lastwar-knowledge-organizer),
  #708 (records 2026-11-12, Owner lastwar-pr-integrator), #425
  (tooling, Owner lastwar-tool-developer). Heads and updated_at
  unchanged since Nov 12 (#708 2026-11-12T20:44:37Z, #711
  2026-11-12T20:04:57Z, #425 2026-11-12T19:29:37Z). None is owned
  by this job; no open PR for records/2026-11-16. Newest comments:
  #711 latest 2026-11-12T19:55:59Z (zachmesh note that PR #710
  merged after it; the held fixable item, amending the 705 claims
  superseded by PR #710, stays blocked and its reply draft unposted
  until VPS returns - not this job's PR); #708 no comments; #425
  latest 2026-11-08. No question addressed to this job, nothing to
  fix.

## Sync and seeding

- Sync: reaped 0, expired 0, due 22, produced 0, already queued 22
  (mail, help, gifts, harvest, vip, passes, daily-missions, secrets,
  treasures, radar, survivors, trucks, train, training, donations,
  events, arms-race, star-ceremony, duel-score, scout, scout-midday);
  completion marker reaped: radar-2026-11-16-1003. Branch reconcile
  skipped with a warning: fetch of records/2026-11-16 failed
  (remote ref missing), issue #446.
- Zombie seeding no-op: the Zombie Invasion event ended (live check
  by unit zombie-invasion-zombie-2026-11-10-037, finished
  2026-11-15T02:35:26Z, no Zombie Invasion tab in the Events hub),
  the chain zombie-2026-11-10 stays closed, and no zombie-invasion
  unit sits in inbox or claimed. No fresh chain is seeded until a
  Zombie Invasion tab is seen live in the Events hub again.

## Duel posture (read from tools/duel.py, not from the screen)

- Duel day 1, Radar Training, RELEASE posture. Claims score +30,000 per
  task. Day ends 18:00 PT Nov 16, 4.2 hours left at the 13:50 read.
  The release stays missed while the Mac is offline; the window is
  still open.

## Delivery

- VPS SSH still Permission denied (publickey), probed 21:43Z, about
  97.1 hours into the break (outage since about 12:46 PT 2026-11-12;
  owner chose the IONOS console route 2026-11-14 17:37 PT; no fix
  yet). Push and PR are blocked. Missed integrator batches stay 24
  (next batch point 15:00 PT Nov 16).
- Delivery PARTIAL: record committed locally on
  ticker-1343-1116-delivery, UNPUSHED, push pending VPS recovery;
  mirror copy in the live tree plus identical backup in the goal
  hidden_files. No Slack sync. Chat report owed per the ticker rule
  (previous pass also access-failed); this pass's final message
  carries it.

## Delivery anomaly found while committing

- While staging the delivery commit, the wholesale copy of the live
  `_records_/2026-11-16/INDEX.md` and `_logs_/repo-actions/action-log.jsonl`
  into the worktree would have deleted content from the delivery-branch
  lineage: the live INDEX (1,735 lines) no longer contains the
  ticker-0734 section that the parent branch holds, and the live
  action-log (502 lines) is far shorter than the parent branch's
  (1,975 lines). Some other job rewrote the live INDEX between 12:34
  and 13:52 PT. The commit was therefore restaged from the parent
  versions with only this pass's section and log line appended, so
  the delivery branch loses nothing. The live-tree divergence itself
  is unresolved and is flagged here for the integrator; no GitHub
  Issue could be filed (VPS SSH down).

## Standing git status anomaly in the live mirror (persists)

- `git status` in the live mirror still reports a large changed set
  (modified activity files, deleted inbox unit files) while the
  queue tools run against the files on disk. The live tree sits on
  branch work/ops-execution-records, another job's in-flight state;
  no commit was attempted from this tree. The delivery commit goes
  through a temporary worktree on ticker-1343-1116-delivery, based
  on ticker-1236-1116-delivery, as in the previous passes.
