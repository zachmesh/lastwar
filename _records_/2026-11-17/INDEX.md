---
title: Play Record 2026-11-17
created: 2026-11-17T08:12:00Z
modified: 2026-11-17T08:12:00Z
level: L0
version: 1.0.0
description: The 0000 PR integration pass - FAILED, VPS SSH unreachable (Permission denied publickey, same outage as 2026-11-12 12.47 PT); one hundredth consecutive failed pass, no merges, no comments, no records PR opened. Checker _tools_/records_batch.py (local fallback from main a858a0fca) reports NOT DUE at the trigger time 00.00.54 PT, at clock time and merge-aware - non-batch pass, no batch merge owed, missed batches stay 27. Open PRs 711/708/425 unchanged since Nov 12, merge-tree exit 0 for all three against main a858a0fca. This record committed locally on records/2026-11-17, UNPUSHED - it needs the VPS route back before it can land
status: unverified

# 2026-11-17
All times America/Los_Angeles. Actor Muse, under the owner standing
instruction of 2026-10-25 to run the regulars and the queue design
of 2026-10-28.
## 00:00 to about 00:12 - PR integration pass

- Integrator pass pr-integration-2026-11-17-0000.
  FAILED, one hundredth consecutive failure for the
  same break: VPS SSH publickey rejected once (about
  00:04 PT; the rejection is server-side, local key
  fingerprint re-verified this pass and unchanged), no
  merges, no comments, no records PR opened. NON-BATCH
  pass for records purposes: the checker
  (_tools_/records_batch.py) reports NOT DUE at the
  scheduled pass start 00:00:54 PT (exit 1, outside
  every batch window), at clock time and merge-aware -
  so no batch merge was owed and missed batches stay 27;
  next batch point 03:00 PT. Open PRs 711/708/425
  unchanged since Nov 12 (heads e3c3dfd0, 2f59c270,
  4f41cdd6); merge-tree exit 0 for all three against
  main a858a0fca (trees f46bfda1, e05ec8b5, 08e8515a,
  identical to all prior probes). PR comment detail not
  re-read this pass (call-read-tool rejects
  pull_request_read, verified again this pass);
  newest-comment facts carried forward from the 2300
  pass, verified only by unchanged updated_at and head
  SHAs - nothing new addressed to this pass. PR 711
  feedback stands (no repeat comment due); PR 425 still
  owner-gated (OD-20261108-01 open, re-read stands from
  the 0015 pass). Records branches: 13 via ls-remote,
  latest records/2026-11-12, none for 11-13 to 11-17 on
  the remote, so no new records PR. Mac mini back online
  per ticker 2102/2348 on 11-16 - context only, VPS
  route still down. This record committed locally on
  records/2026-11-17, UNPUSHED - push via the standard
  VPS route once SSH returns. Status: failed.
  Full detail in pr-integration/0000-run.md.

## 01:01 to about 01:16 - Ticker pass ticker-0101

- 01:01 PT 2026-11-17, ticker-0101 - 1 unit done, Mac mini online.
  Sync: 22 due, 0 produced (all already queued), 0 expired, 0
  reaped; completion marker reaped harvest-2026-11-16-2203.
  Zombie chain stays closed (event ended 2026-10-30, unit 066).
  Own PRs first: open PRs #711, #708, #425 via the authenticated
  GitHub connector - none owned by this job, heads and updated_at
  unchanged since Nov 12.
- radar-2026-11-16-2203 done (stack day, duel day 2 Base
  Expansion): radar entered and verified (Lv.13, 468 points,
  stored 7/40, stamina 103); Quick Execute ran 2 ordinary tasks
  (stamina 103 to 83), nothing claimed; re-entry shows 10 task
  rewards pending for the day-3 release (Claim All NOT tapped);
  9 map pins inventoried untapped; stored still 7/40 after the
  2 executions - open question for the release-day unit (does
  stored count completed-but-unclaimed tasks?). Tracker radar
  done. Record: radar-tasks/0115-queue-run.md.
- Push and PR blocked - VPS SSH still Permission denied
  (publickey), about 108 hours into the outage; record committed
  locally only on ticker-0101-1117-delivery, UNPUSHED, push
  pending VPS recovery. No PR opened for records/2026-11-17.
## 01:00 to about 01:18 - PR integration pass

- Integrator pass pr-integration-2026-11-17-0100.
  FAILED, one hundred and first consecutive failure for
  the same break: VPS SSH publickey rejected once (about
  01:13 PT; the rejection is server-side, local key
  fingerprint re-verified this pass and unchanged), no
  merges, no comments, no records PR opened. NON-BATCH
  pass for records purposes: the checker
  (_tools_/records_batch.py) reports NOT DUE at the
  scheduled pass start 01:00:54 PT (exit 1, outside
  every batch window), at clock time and merge-aware -
  so no batch merge was owed and missed batches stay 27;
  next batch point 03:00 PT. Open PRs 711/708/425
  unchanged since Nov 12 (heads e3c3dfd0, 2f59c270,
  4f41cdd6); merge-tree exit 0 for all three against
  main a858a0fca (trees f46bfda1, e05ec8b5, 08e8515a,
  identical to all prior probes). PR comment detail not
  re-read this pass (call-read-tool rejects
  pull_request_read, verified at the 0000 pass);
  newest-comment facts carried forward from the 0000
  pass, verified only by unchanged updated_at and head
  SHAs - nothing new addressed to this pass. PR 711
  feedback stands (no repeat comment due); PR 425 still
  owner-gated (OD-20261108-01 open, re-read stands from
  the 0015 pass). Records branches: 13 via ls-remote,
  latest records/2026-11-12, none for 11-13 to 11-17 on
  the remote, so no new records PR. Local
  records/2026-11-17 exists (0000 pass, tip ffa29ae856)
  and ticker-0101-1117-delivery adds the radar record
  on top - both UNPUSHED, push pending VPS recovery.
  Mac mini back online per ticker-0101 at 01:01 PT -
  context only, VPS route still down. This record
  committed locally on records/2026-11-17, UNPUSHED -
  push via the standard VPS route once SSH returns.
  Status: failed.
  Full detail in pr-integration/0100-run.md.
