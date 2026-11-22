---
title: Resource Collection 2026-11-16 ticker-1949 failed, Mac mini offline
created: 2026-11-17T03:57:00Z
modified: 2026-11-17T03:57:00Z
version: 1.0.0
description: Harvest unit harvest-2026-11-16-1803 failed, Mac mini unreachable
status: failed
grounded_in:
  - source: device.list and device.describe on 1c817413-83e2-0545-cb90-36d5e096a6bd, 2026-11-17T03:49Z to 03:53Z
  - source: device.invoke computer.session start (3 attempts) on 1c817413-83e2-0545-cb90-36d5e096a6bd, 2026-11-17T03:50Z to 03:52Z
  - source: tools/duel.py --json, 2026-11-17T03:53Z
  - source: unauthenticated GitHub REST API reads of zachmesh/lastwar PRs 711, 708, 425 and their comments, 2026-11-17T03:54Z to 03:56Z
  - source: VPS SSH probe, 2026-11-17T03:49Z
---

# Resource Collection 2026-11-16 ticker-1949 failed, Mac mini offline

- Executor: ticker-1949
- Unit: harvest-2026-11-16-1803, regular harvest, activity resource-collection, priority 3, est 9 minutes, expires 2026-11-17T06:03:00Z (22:03 PT Nov 16)
- Session window: 19:49-19:58 local, token held 19:49-19:58 local

## What happened

- The Mac mini (Zhen's Mac mini, 1c817413-83e2-0545-cb90-36d5e096a6bd)
  is still OFFLINE. Five device probes, all offline, no wake-up
  path: device.list, device.describe, computer.session start
  (three attempts, all node_offline). last_seen frozen at
  2026-11-15T13:19:56Z (05:19 PT Nov 15), about 38.6 hours stale at
  03:55Z. This is the twenty-ninth consecutive ticker pass to fail
  on the offline Mac (ticker-1842 counted twenty-eight at 18:42 PT;
  no ticker unit finished between 1842 and this pass). This is NOT
  the outcome_unknown control-lock (Issue 689), so no
  blocker_overlay was recorded and the next tick probes again.
- No harvest work was executed, nothing claimed, nothing spent. The
  tracker is untouched. The pass stopped after this unit rather than
  cascading failed units, as in the ticker-1842 pass. The harvest
  unit expires 22:03 PT Nov 16 and the harvest regular stays due, so
  the next tick re-produces it. The stalled priority-1 vip unit
  vip-2026-11-16-1803 (planned 18:00 PT, expires 18:00 PT Nov 17)
  also remains unexecuted while the Mac is offline.

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
  latest 2026-11-08T20:24:14Z (integrator notes, conflicting - not
  this job's PR). No question addressed to this job, nothing to fix.

## Sync and seeding

- Sync: reaped 0, expired 0, due 22, produced 0, already queued 22
  (mail, help, gifts, harvest, vip, passes, daily-missions,
  secrets, treasures, radar, survivors, trucks, train, training,
  donations, events, arms-race, star-ceremony, duel-score, scout,
  scout-midday, zombie-invasion); completion markers reaped:
  passes-2026-11-16-1457. Branch reconcile skipped with a warning:
  fetch of records/2026-11-16 failed (remote ref missing),
  issue #446. The 22nd due regular is zombie-invasion, whose
  seeding is a no-op (event ended, see below).
- Zombie seeding no-op: the Zombie Invasion event ended (live check
  by unit zombie-invasion-zombie-2026-11-10-037, finished
  2026-11-15T02:35:26Z, no Zombie Invasion tab in the Events hub),
  the chain zombie-2026-11-10 stays closed, and no zombie-invasion
  unit sits in inbox or claimed. No fresh chain is seeded until a
  Zombie Invasion tab is seen live in the Events hub again.

## Duel posture (read from tools/duel.py, not from the screen)

- Duel day 2, Base Expansion, day ends 18:00 PT Nov 17, 22.1 hours
  left at the 19:53 read. Radar posture STACK - complete tasks but
  do NOT claim (odd-day claim rule). UR truck dispatches score
  100,000 each; Legendary secret tasks 75,000 each. Building power
  gained on collecting finished upgrades scores.
- Duel day 1 (Radar Training, RELEASE, +30,000 per claimed task)
  closed at 18:00 PT Nov 16 with the whole day missed while the Mac
  was offline; no claim was possible in the window.

## Delivery

- VPS SSH still Permission denied (publickey), probed 03:49Z, about
  103.1 hours into the break (outage since about 12:46 PT 2026-11-12;
  owner chose the IONOS console route 2026-11-14 17:37 PT; no fix
  yet). Push and PR are blocked. Missed integrator batches stand at
  26 (the 19:00 batch missed; next 23:00 PT).
- Delivery PARTIAL: record committed locally on
  ticker-1949-1116-delivery, UNPUSHED, push pending VPS recovery;
  mirror copy in the live tree plus identical backup in the goal
  hidden_files. No Slack sync. Chat report owed per the ticker rule
  (previous pass also access-failed); this pass's final message
  carries it.

## Delivery anomaly found while committing

- As in the ticker-1501, ticker-1604, ticker-1704 and ticker-1842
  passes: a wholesale copy of the live `_records_/2026-11-16/INDEX.md`
  and `_logs_/repo-actions/action-log.jsonl` into the worktree would
  have deleted content from the delivery-branch lineage: the live
  INDEX still lacks the ticker-0734 section that the parent branch
  holds, and the live action-log (506 lines) and the parent branch's
  (1980 lines) are different lineages. The commit was therefore
  restaged from the parent versions with only this pass's section
  and log line appended, so the delivery branch loses nothing. The
  live-tree divergence itself is unresolved and is flagged here for
  the integrator; no GitHub Issue could be filed (VPS SSH down).

## Standing git status anomaly in the live mirror (persists)

- `git status` in the live mirror still reports a large changed set
  (modified activity files, deleted inbox unit files) while the
  queue tools run against the files on disk. The live tree sits on
  branch work/ops-execution-records, another job's in-flight state;
  no commit was attempted from this tree. The delivery commit goes
  through a temporary worktree on ticker-1949-1116-delivery, based
  on ticker-1842-1116-delivery, as in the previous passes.
