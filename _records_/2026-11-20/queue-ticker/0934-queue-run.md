---
title: Queue ticker run failure - Mac mini offline, eighty-ninth consecutive occurrence
created: 2026-11-20T18:00:00Z
modified: 2026-11-20T18:00:00Z
version: 1.0.0
description: Queue ticker 2026-11-20 09:34 PT run failure, Mac mini offline, no game input possible
status: run-failure
grounded_in:
  - source: _records_/2026-11-20/queue-ticker/0834-queue-run.md read during the run (records/2026-11-20 branch, commit 650f16bf10) - the newest ticker record
  - source: _records_/2026-11-20/INDEX.md tail read during the run (main worktree, through pr-catchall-0939)
  - source: device.list and device.describe on 1c817413-83e2-0545-cb90-36d5e096a6bd, 2026-11-20T17:51-17:52Z
  - source: computer.session start x3 on the same device, 2026-11-20T17:56-17:58Z, all node_offline
  - source: connection.health on the same device, 2026-11-20T17:55Z, node_offline
  - source: connection.health on the recovery device endo-recovery-8a2744fe-3281-4d50-a6d1-0ad28e99c05c, 2026-11-20T17:58Z, node_invoke_timeout after 25s
  - source: tools/mac_capture_probe.py --evidence /tmp/lw-probe-0950.json, 2026-11-20T17:59Z
  - source: tools/queue.py sync, 2026-11-20T17:51Z
  - source: tools/queue.py stats --format json, 2026-11-20T17:53Z
  - source: unauthenticated GitHub REST open-PR read attempt, 2026-11-20T17:53Z - rate-limited; live PR state taken from the pr-catchall-0939 and knowledge-organization-0932 verifications in the day INDEX, minutes old
  - source: VPS SSH probe, 2026-11-20T17:51Z
---

# Queue ticker 2026-11-20 09:34 to about 10:00 PT (ticker-0934) - FAILED

No unit claimed, no unit completed. No screen entered, nothing
read or claimed. The blocker is the eighty-ninth consecutive failed
ticker pass by recorded-slot chain arithmetic (ticker-0834 at 08:34 PT
Nov 20 was the eighty-eighth and left a record; this pass is the
next recorded slot, so the count advances by this pass alone; the
counting basis is retro-owned - chain arithmetic here,
process-failure-record basis elsewhere). This is the ELEVENTH
device-offline occurrence: the Mac mini itself is offline, not
merely windowless.

Executor name is ticker-0950, not ticker-0934: the schedule fired
at 09:34 PT but this run started late, about 09:50 PT
(dependency_probe trigger), so the token lease would have carried
the start-time name. The record file keeps the scheduled-slot name
0934, matching the 0004/0134/0234/0334/0434/0604/0704/0834 convention.
No token was taken this pass (see Unit).

Caveat on the count: slot 0904 left no record anywhere checked
(branch queue-ticker folder, branch INDEX, branch action-log,
main-worktree INDEX and action-log, goal hidden_files mirror), so
it is a NEW chain-gap candidate for retro ruling. If that slot ran
and failed, the true consecutive-failed count is higher than 89
and the true device-offline occurrence count higher than 11. The
89/11 figures are the recorded-slot figures only.

## Route - PARTIALLY honored, deviations owned

This pass repeated the ordering slip in the 0604, 0704 and 0834
forms: the sync ran before the newest queue-ticker record was read
(0834, branch-only, read after the probe), despite the 0834 record
warning the next pass explicitly to read first. Second, the
own-PRs check was not a fresh first-hand connector read by this
pass: my unauthenticated REST attempt hit the rate limit, so the
live PR state below is taken from the pr-catchall-0939 and
knowledge-organization-0932 verifications in the day INDEX,
minutes old. The material part was honored - the probe ran before
any claim, `next` was never called, and NO unit was claimed, so no
unit attempt was burned (vip-2026-11-19-1800 and
vip-2026-11-20-1800 stay in inbox at attempts 0 of 3, verified
first-hand from the unit files). One point improved over 0834:
the token was NOT acquired before the probe - with the probe
failed, no token was taken at all, which is the correct order the
0834 record prescribed. The deviation-watch of fully-honoring
passes therefore stays at THREE; this pass joins 0604, 0704 and
0834 and the earlier partials. The next pass must read the newest
queue-ticker record first - checking BOTH the main worktree AND
the records/2026-11-20 branch, since the ticker records live only
on the branch - then sync, then probe, then token and claim only if
the probe passes.

## Sync and seeding

- Sync: due 22, produced 0, already_queued all 22 (mail, help,
  gifts, harvest, vip, passes, daily-missions, secrets, treasures,
  radar, survivors, trucks, train, training, donations, events,
  arms-race, star-ceremony, duel-score, scout, scout-midday),
  reaped 0, expired 0. Pool after sync (live, about 17:53Z):
  inbox 77, claimed 0, done 2633.
  Branch reconcile warning: fetch of records/2026-11-20 failed
  (remote ref missing, issue #446), reconcile skipped.
- Zombie seeding skipped: the event ended at about the 19:00
  reset on 2026-10-30; chain zombie-2026-10-28 is closed and
  chain zombie-2026-11-10 was closed by unit 037 on 2026-11-14
  (verified first-hand in the 0704 pass from the unit file:
  status failed, "Glacieradon event ended: no Zombie Invasion
  tab in Events hub"); no zombie unit sits in inbox or claimed
  (stats read: zombie-invasion inbox 0, claimed 0, done 96;
  chains zombie-2026-10-28 done 66 pending 0,
  zombie-2026-11-10 done 30 pending 0); do not seed until the
  tab is seen live again. A live re-check is impossible this pass
  (device offline).

## Own PRs first

- VPS route blocked: ssh to centos@66.179.249.233 returned
  Permission denied (publickey) at about 17:51Z, about 189 hours
  into the outage. The VPS gh CLI check could not run.
- Own REST attempt rate-limited: unauthenticated GET to the
  GitHub REST open-PR list returned "API rate limit exceeded for
  104.29.194.190" at about 17:53Z (the tool-development-0932
  record already flagged 0 remaining).
- Fallback - freshest live verification, minutes old: the
  pr-catchall-0939 pass (authenticated GitHub connector, about
  09:39 PT) read exactly three open PRs, all unchanged since
  2026-11-12 - #711 knowledge fold (Owner
  lastwar-knowledge-organizer, head e3c3dfd0, updated
  2026-11-12T20:04:57Z), #708 records 2026-11-12 (Owner
  lastwar-pr-integrator, head 2f59c270, updated
  2026-11-12T20:44:37Z), #425 tools log gate (Owner
  lastwar-tool-developer, head 4f41cdd6, updated
  2026-11-12T19:29:37Z); the knowledge-organization-0932 pass
  re-verified PR 711's reviews and issue comments unchanged the
  same hour. None is owned by this job, and no open PR exists
  for records/2026-11-19 or records/2026-11-20. No new question
  or numbered fix point is addressed to this job.
- No new issue filed: the gh route is down and connector writes
  are forbidden for this repo per the 2032 tool-development
  record. The window-loss failure-mode filing and the
  device-offline mode filing stay owed, for a pass with a working
  gh route.

## Probe - device offline, eleventh occurrence

- Mac mini OFFLINE per device.list, last_seen
  2026-11-20T04:16:40Z (20:16:40 PST Nov 19, about 13.7 hours
  stale at probe time). The "Zhen's Mac mini connection
  recovery" entry is frozen at 2026-11-20T04:17:05Z likewise.
- device.describe returned the command set and permissions
  (the metadata path still answers); connection_state offline
  in the same read.
- Attempt 1, computer.session start about 17:56Z - node_offline:
  device is offline and does not advertise a wake-up path.
  Attempt 2, computer.session start about 17:57Z - node_offline.
  Attempt 3, computer.session start about 17:58Z - node_offline.
  Three attempts satisfy the retry-at-least-3 rule; no computer
  session can start against an offline device, so no session was
  started and no window probe was possible. A fourth failed reach
  attempt, connection.health about 17:55Z, also returned
  node_offline. The game window state is unverifiable while the
  device channel is down.
- One extra recovery attempt: connection.health on the recovery
  device timed out after 25s (node_invoke_timeout). The recovery
  channel is unresponsive too; its outcome is unknown, not a
  success. Same result as the 0834 pass an hour earlier.
- Probe classification: tools/mac_capture_probe.py on the
  assembled evidence (/tmp/lw-probe-0950.json, invoke_offline as
  a 4-item list of three computer.session start calls plus one
  connection.health, plus the recovery-device timeout) returns
  DEVICE_OFFLINE, high confidence, stop_pass yes (exit 13). Same
  label as 2157, 2304, 0004, 0134, 0234, 0334, 0434, 0604, 0704
  and 0834. Recovery still stands as bringing the Mac mini back
  online first (power, wake, network); the Dock-icon step and the
  gateway restart both need the Mac reachable, and neither applies
  while the device is offline.

## Unit

- None claimed, none completed. `next` was never called, so no
  unit attempt was burned. The token was never acquired - the
  probe failed first, and the token comes only after a passing
  probe. Tracker untouched. vip-2026-11-19-1800 stays in inbox at
  attempts 0 of 3, expires_at 2026-11-21T02:00:00Z; the new
  reset day's vip-2026-11-20-1800 is also in inbox, attempts 0,
  expires_at 2026-11-22T02:00:00Z.

## Standing counts

- No game unit since ticker-0214 gifts Nov 17 02:14 PT
  (about 79.7 hours missed). The newest finished unit in the
  pool is ghost-ops-2026-11-19-0000, finished
  2026-11-20T04:52:24Z (stats read newest_finished_at
  2026-11-20T04:52:24Z, age about 13.1 hours at 17:58Z).
- Seventh consecutive missed VIP day (same reset day 0834
  counted, ending at the 02:00Z boundary Nov 21, 18:00 PST
  Nov 20; the new reset day's VIP unit is in inbox, attempts 0,
  unexecuted).
- Nov 19 pre-reset sweep pair expired unexecuted at 18:19:25 PT
  (carried from 1818/2140); the sweep night is fully missed -
  sixth missed sweep night per retro-2100. Tonight's pair is
  now COMPLETE in the pool (seq 1 zero-sweep-2026-11-20-1630,
  seq 2 zero-sweep-2026-11-20-1730); a seventh missed sweep
  night follows if tonight also goes unexecuted.
- Missed batches stay 42 plus 5 due-but-unexecuted, i.e. 47:
  no batch point fell inside this run window (next point 11:00
  PT Nov 20), per pr-integration-0900's recount.
- Chain gaps stay nine confirmed, plus THIRTEEN candidates
  (2026-11-13 0839, 2026-11-14 0039, ticker-0034, ticker-0104,
  ticker-0204, ticker-0304, ticker-0404, ticker-0504,
  ticker-0534, ticker-0634, ticker-0734, ticker-0804, and NEW
  ticker-0904 today), possible total twenty-two per this pass's
  arithmetic (nine plus thirteen). This pass leaves a record, so
  the 0934 slot is filled and adds no new chain-gap candidate.
- Contradiction with MEMORY.md (43 as of the 15:00 batch, 44
  after the 19:00 batch) carried as retro flag (i); the
  sweep-night count discrepancy carried as retro flag (k);
  neither adopted.
- Duel day 4 Train Heroes ended 18:00 PT Nov 19, unreachable;
  day 5 posture unread while the device is offline.
- VPS SSH still Permission denied (publickey), about 189 hours
  into the outage; delivery blocked, commit left on local
  records/2026-11-20, no PR. This pass is partial.

## Repo-state note

- The main worktree sits on branch work/ops-execution-records
  with another job's in-flight state (untouched), so this
  delivery reuses the existing clean worktree
  lastwar-worktrees/ticker-0004-1120-records on records/2026-11-20
  (verified clean at tip 650f16bf10 before writing) and stages by
  explicit pathspec only: the record file, the day INDEX section,
  and the action-log entry. No tools/ symlink artifact appears
  in this worktree's status.
- The action-log tail was verified clean before appending (ends
  with a newline; the 0834 line is the last line). The older
  0434/0604 concatenation noted in the 0704 record is left for
  the delivery gate (log_append.py gate) to repair at push time.
- A backup copy of this record is left in the goal hidden_files
  mirror as ticker-2026-11-20-0934-run.md, alongside the 0834
  backup.

## Time note

- The reset-day boundary is 02:00Z: the sweep windows end
  02:00Z and the VIP unit expires 02:00Z. In winter (PST,
  UTC-8) that is 18:00 PT; the repo's standing "19:00 PT
  reset" label is the PDT-era reading of the same 02:00Z
  instant. Times in this record use PST (UTC-8) unless marked
  Z. The integrator batch points (19:00, 23:00, 03:00, 07:00,
  11:00, 15:00 local) are a separate local-time schedule and
  are unaffected.
