---
title: Harvest 2026-11-16 ticker-0704 failed, Mac mini offline
created: 2026-11-16T15:12:00Z
modified: 2026-11-16T15:12:00Z
version: 1.0.0
description: Harvest unit harvest-2026-11-16-0603 failed, Mac mini unreachable
status: failed
grounded_in:
  - source: device.list and device.describe on 1c817413-83e2-0545-cb90-36d5e096a6bd, 2026-11-16T15:05Z to 15:09Z
  - source: device.invoke connection.health on 1c817413-83e2-0545-cb90-36d5e096a6bd and connection.repair plus connection.health on its recovery device, 2026-11-16T15:09Z to 15:11Z
  - source: tools/duel.py --json, 2026-11-16T15:08Z
  - source: GitHub connector list_pull_requests for zachmesh/lastwar, 2026-11-16T15:09Z
  - source: VPS SSH probe, 2026-11-16T15:04Z
---

# Harvest 2026-11-16 ticker-0704 failed, Mac mini offline

- Executor: ticker-0704
- Unit: harvest-2026-11-16-0603, regular harvest, activity resource-collection, priority 3, est 9 minutes
- Session window: 07:04-07:12 local, token held 07:08-07:11 local

## What happened

- The Mac mini (Zhen's Mac mini, 1c817413-83e2-0545-cb90-36d5e096a6bd)
  is still OFFLINE. Six device probes, all offline or timed out, no
  wake-up path: device.list, device.describe on the Mac and on its
  connection-recovery device, connection.health on the Mac
  (node_offline), connection.repair on the recovery device (25s
  timeout), connection.health on the recovery device (25s timeout).
  last_seen frozen at 2026-11-15T13:19:56Z (05:19 PT Nov 15), about
  25h52m stale at 15:11Z. This is the seventeenth consecutive ticker
  pass to fail on the offline Mac (2143, 2204, 2234, 2304, 2334, 0004,
  0112, 0134, 0204, 0234, 0304, 0334, 0404, 0528, 0604, 0634 before it).
- No harvest work was executed, nothing claimed, nothing spent. The
  tracker is untouched. The pass stopped after this unit rather than
  cascading failed units.

## Own PRs first

- Open PRs re-checked live via the GitHub connector
  (list_pull_requests, zachmesh/lastwar): only #711, #708, #425.
  Heads and updated_at identical to the 0634 pass readings and
  unchanged since Nov 12 (711 updated 2026-11-12T20:04:57Z, 708
  updated 2026-11-12T20:44:37Z, 425 updated 2026-11-12T19:29:37Z).
  None is owned by this job (Owners: lastwar-knowledge-organizer,
  lastwar-pr-integrator, lastwar-tool-developer). No PR exists for
  records/2026-11-16. No new comment or question addressed to this
  job; nothing to reply to or fix.

## Sync and seeding

- Sync: reaped 0, expired 5, due 22, produced 0, already queued 22.
  Expired units: trucks-2026-11-16-0257, treasures-2026-11-16-0257,
  secrets-2026-11-16-0257, events-2026-11-16-0257,
  scout-midday-2026-11-15-0700. Completion marker reaped:
  passes-2026-11-16-0257. Branch reconcile skipped with a warning:
  fetch of records/2026-11-16 failed (remote ref missing), issue #446.
- Zombie seeding no-op: the Glacieradon event ended Nov 14 (live
  check by unit 037, no Zombie Invasion tab in the Events hub), the
  chain zombie-2026-11-10 stays closed, no successor enqueued.

## Duel posture

- Duel day 1, Radar Training release posture, read live from
  tools/duel.py at 15:08Z: claims score +30,000 per task, the day
  runs until 18:00 PT Nov 16 (10.9 hours left). The release stays
  missed while the Mac is offline; the window is still open.

## Delivery

- VPS SSH still Permission denied (publickey), probed 15:04Z, about
  90.3 hours into the break (outage since about 12:46 PT 2026-11-12;
  owner chose the IONOS console route 2026-11-14 17:37 PT; no fix
  yet). Push and PR are blocked. The 07:00 PT integrator batch point
  passed just before this pass started with no merge possible, so
  missed batches rise to 23 (next batch point 11:00 PT Nov 16).
- Delivery PARTIAL: record committed locally on
  ticker-0704-1116-delivery, UNPUSHED, push pending VPS recovery;
  mirror copy in the live tree plus identical backup in the goal
  hidden_files. No Slack sync. Chat report owed per the ticker rule
  (previous pass also access-failed); this pass's final message
  carries it.

## Standing git status anomaly in the live mirror (persists)

- `git status` in the live mirror still reports tools/*.py as deleted
  (2215 changed paths total) while the files exist on disk and run
  (queue.py sync and duel.py ran this pass). No commit was attempted
  from this tree; the delivery commit goes through the /tmp worktree
  on ticker-0704-1116-delivery, as in the previous passes.
