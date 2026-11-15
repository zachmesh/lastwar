---
title: Play Record 2026-11-15
created: 2026-11-15T15:05:00Z
modified: 2026-11-15T15:05:00Z
level: L0
version: 1.0.0
description: The 0655 PR integration pass - FAILED, VPS SSH unreachable (Permission denied publickey, same outage as 2026-11-12 12:47 PT); no gh merge/comment possible, no checker run, no records push. Read-only API verification only: open PRs 708 (records 2026-11-12, CLEAN, awaits a 15:00 batch that never ran), 711 (knowledge, held by the 1145 review on one fixable item), 425 (tools, still owner-gated OD-20261108-01); main frozen at a858a0fca (PR 710, 2026-11-12 11:52 PT); no records branch after 2026-11-12. This run record committed locally only on records/2026-11-15, UNPUSHED - it needs the VPS route back before it can land
status: unverified
---

# 2026-11-15

All times America/Los_Angeles. Actor Muse, under the owner standing
instruction of 2026-10-25 to run the regulars and the queue design
of 2026-10-28.

## 06:45 to about 07:05 - PR integration 0655 run, FAILED (VPS SSH unreachable)

- Integrator pass pr-integration-2026-11-15-0655. FAILED:
  VPS SSH returns "Permission denied (publickey)" - the
  2026-11-12 ~/.ssh loss is still unrepaired (owner chose
  the IONOS-console recovery on 2026-11-14, not yet
  landed). No merge, comment, checker run or records push
  was possible. Read-only verification via the public
  GitHub API only. Open PRs 708 (records 2026-11-12, head
  2f59c270, 26 commits, CLEAN, awaits the 15:00 batch of
  11-12 that never ran - three days overdue), 711
  (knowledge, head e3c3dfd0 unchanged, held by the 1145
  review on amending the superseded #705 lines per PR
  710), 425 (tools, head 4f41cdd6a unchanged, still
  owner-gated OD-20261108-01, no owner decision). Main
  frozen at a858a0fca (PR 710, 2026-11-12 11:52 PT). No
  records branch after 2026-11-12; no new records PR to
  open. This pass started before the 07:00 batch point,
  so it would have been NON-batch in any case. This
  record committed locally only on records/2026-11-15,
  UNPUSHED - push via the standard VPS route once SSH
  returns. Status: failed. Full detail in
  pr-integration/0655-run.md.

## 08:00 to about 08:14 - PR integration 0800 run, FAILED (VPS SSH unreachable)

- Integrator pass pr-integration-2026-11-15-0800. FAILED:
  VPS SSH returns "Permission denied (publickey)" - the
  2026-11-12 ~/.ssh loss is still unrepaired (owner chose
  the IONOS-console recovery on 2026-11-14, not yet
  landed). Sixtieth consecutive failed pass for the same
  break. No merge, comment or records push was possible.
  Checker _tools_/records_batch.py run locally from a
  main copy: NOT DUE (outside every batch window, next
  batch point 11:00 PT), so this pass is NON-batch and
  adds no missed batch (still 17 - the 07:00 batch was
  already counted at the 0655 pass). Read-only
  verification via the public GitHub API only. Open PRs
  708 (records 2026-11-12, head 2f59c270, 26 commits,
  CLEAN, awaits the 15:00 batch of 11-12 that never ran
  - three days overdue), 711 (knowledge, head e3c3dfd0
  unchanged, held by the 1145 review on amending the
  superseded #705 lines per PR 710), 425 (tools, head
  4f41cdd6a unchanged, still owner-gated OD-20261108-01,
  no owner decision). Main frozen at a858a0fca (PR 710,
  2026-11-12 11:52 PT). No records branch after
  2026-11-12; no new records PR to open. This record
  committed locally only on records/2026-11-15,
  UNPUSHED - push via the standard VPS route once SSH
  returns. Status: failed. Full detail in
  pr-integration/0800-run.md.

- 08:04 PT, perception-scout 0804 run - failed, 1 unit
  (scout-scout-2026-11-10-017, chain scout-2026-11-10 seq 17):
  Mac mini offline again (last seen 05:19 PT; 4 device probes all
  node_offline, no wake-up path), no observation made, no claims;
  successor 018 enqueued. Own PRs re-checked live via the public
  API: #711, #708, #425 still open, none owned by this job, nothing
  addressed to it; no PR for records/2026-11-14 or
  records/2026-11-15. Zombie seeding no-op (Glacieradon ended).
  VPS SSH still Permission denied, commit stays local, no PR.
  Record: perception-scout/0804-queue-run.md.

- 09:34 PT, queue-ticker 0934 run - failed, 1 unit failed
  (harvest-2026-11-15-0603, Mac mini offline again, last_seen
  05:19 PT, 4 device probes all node_offline, no collection,
  no claims, tracker untouched); sync reaped 0, expired 0,
  due 22, produced 0; zombie seeding no-op (Glacieradon
  ended); own PRs re-checked via public API (#711, #708,
  #425, none owned by this job); pass stopped after this
  unit rather than cascading failures; VPS SSH still
  Permission denied (publickey), commit stays on local
  records/2026-11-15, no PR.
  Record: resource-collection/0934-queue-run.md.

## 10:20 to about 10:24 - PR integration 1020 run, FAILED (VPS SSH unreachable)

- Integrator pass pr-integration-2026-11-15-1020. FAILED:
  VPS SSH returns "Permission denied (publickey)" - the
  2026-11-12 ~/.ssh loss is still unrepaired (owner chose
  the IONOS-console recovery on 2026-11-14, not yet
  landed). Sixty-first consecutive failed pass for the
  same break. No merge, comment or records push was
  possible. Checker _tools_/records_batch.py run locally
  from a main copy: NOT DUE (outside every batch window,
  next batch point 11:00 PT), so this pass is NON-batch
  and adds no missed batch (still 17 - the 07:00 batch
  was already counted at the 0655 pass). Read-only
  verification via the public GitHub API only. Open PRs
  708 (records 2026-11-12, head 2f59c270, 26 commits,
  CLEAN, awaits the 15:00 batch of 11-12 that never ran
  - three days overdue), 711 (knowledge, head e3c3dfd0
  unchanged, held by the 1145 review on amending the
  superseded #705 lines per PR 710), 425 (tools, head
  4f41cdd6a unchanged, still owner-gated OD-20261108-01,
  no owner decision). Main frozen at a858a0fca (PR 710,
  2026-11-12 11:52 PT). No records branch after
  2026-11-12; no new records PR to open. This record
  committed locally only on records/2026-11-15,
  UNPUSHED - push via the standard VPS route once SSH
  returns. Status: failed. Full detail in
  pr-integration/1020-run.md.

- 10:51 PT, queue-ticker 1051 run - failed, 1 unit failed
  (scout-scout-2026-11-10-018, chain scout-2026-11-10 seq 18,
  Mac mini offline again, last_seen 05:19 PT, 5 device probes
  all node_offline or invoke timeout, no wake-up path, no
  observation, no claims, tracker untouched); sync reaped 0,
  expired 0, due 22, produced 0; zombie seeding no-op
  (Glacieradon ended); own PRs re-checked via public API
  (#711, #708, #425, none owned by this job, no PR for
  records/2026-11-15); pass stopped after this unit rather
  than cascading failures; VPS SSH still Permission denied
  (publickey), commit stays on local records/2026-11-15,
  no PR.
  Record: perception-scout/1051-queue-run.md.

## 11:27 to about 11:33 - PR integration 1127 run, FAILED (VPS SSH unreachable, BATCH PASS missed)

- Integrator pass pr-integration-2026-11-15-1127. FAILED:
  VPS SSH returns "Permission denied (publickey)" - the
  2026-11-12 ~/.ssh loss is still unrepaired (owner chose
  the IONOS-console recovery on 2026-11-14, not yet
  landed). Sixty-second consecutive failed pass for the
  same break. No merge, comment or records push was
  possible. Checker _tools_/records_batch.py run locally
  from a main copy: DUE (exit 0, batch window 11:00-12:00
  PT, 30 minutes left at check), so this pass IS a batch
  pass - the first pass at or after 11:00 PT - and it
  could not merge: the 11:00 batch is the eighteenth
  missed batch. Read-only verification via the public
  GitHub API only. Open PRs 708 (records 2026-11-12,
  head 2f59c270, 26 commits, CLEAN, batch pass missed),
  711 (knowledge, head e3c3dfd0 unchanged, held by the
  1145 review on amending the superseded #705 lines per
  PR 710), 425 (tools, head 4f41cdd6a unchanged, still
  owner-gated OD-20261108-01, no owner decision). Main
  frozen at a858a0fca (PR 710, 2026-11-12 11:52 PT). No
  records branch after 2026-11-12; no new records PR to
  open. This record committed locally only on
  records/2026-11-15, UNPUSHED - push via the standard
  VPS route once SSH returns. Status: failed. Full
  detail in pr-integration/1127-run.md.
- 12:02 PT, queue-ticker 1202 run - failed, 1 unit failed
  (harvest-2026-11-15-1003, Mac mini offline again,
  last_seen 05:19 PT, 5 device probes - connection.health,
  environment.describe, computer.session all node_offline,
  recovery-device health and repair both invoke timeout,
  no wake-up path, no collection, no claims, tracker
  untouched); sync reaped 0, expired 0, due 22, produced 0;
  zombie seeding no-op (Glacieradon ended); own PRs
  re-checked via public API (#711, #708, #425, none owned
  by this job, no PR for records/2026-11-15); pass stopped
  after this unit rather than cascading failures; VPS SSH
  still Permission denied (publickey), commit stays on local
  records/2026-11-15, no PR.
  Record: resource-collection/1206-queue-run.md.

- 13:31 PT, queue-ticker 1331 run - failed, 1 unit failed
  (radar-2026-11-15-1003, Mac mini offline again,
  last_seen 05:19 PT, 5 device probes - connection.health,
  environment.describe, computer.session all node_offline,
  recovery-device health and repair both invoke timeout,
  no wake-up path, no radar claims, tracker
  untouched); sync reaped 0, expired 0, due 22, produced 0,
  1 completion marker reaped (harvest-2026-11-15-1003);
  zombie seeding no-op (Glacieradon ended); own PRs
  re-checked via public API (#711, #708, #425, none owned
  by this job, no PR for records/2026-11-15); pass stopped
  after this unit rather than cascading failures; VPS SSH
  still Permission denied (publickey), commit stays on local
  records/2026-11-15, no PR.
  Record: radar-tasks/1331-queue-run.md.

- 14:04 PT, queue-ticker 1404 run - failed, 1 unit failed
  (help-2026-11-15-1030, Mac mini offline again,
  last_seen 05:19 PT, 4 device probes all node_offline,
  no wake-up path, no help pressed, tracker untouched);
  sync reaped 0, expired 6 (the 2026-11-15-1003 set,
  unexecuted), due 22, produced 0; zombie seeding no-op
  (Glacieradon ended); own PRs re-checked via public API
  (#711, #708, #425, none owned by this job, no PR for
  records/2026-11-15); pass stopped after this unit rather
  than cascading failures; VPS SSH still Permission denied
  (publickey), commit stays on local records/2026-11-15,
  no PR.
  Record: alliance-help/1404-queue-run.md.
