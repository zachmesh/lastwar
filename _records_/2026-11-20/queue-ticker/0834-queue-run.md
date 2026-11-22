---
title: Queue ticker run failure - Mac mini offline, eighty-eighth consecutive occurrence
created: 2026-11-20T16:50:00Z
modified: 2026-11-20T16:50:00Z
version: 1.0.0
description: Queue ticker 2026-11-20 08:34 PT run failure, Mac mini offline, no game input possible
status: run-failure
grounded_in:
  - source: _records_/2026-11-20/queue-ticker/0704-queue-run.md read during the run (records/2026-11-20 branch, commit 5b2368e485) - the newest ticker record
  - source: _records_/2026-11-20/INDEX.md tail read during the run (records worktree, through queue-ticker-0704 and knowledge-organization-0832)
  - source: device.list and device.describe on 1c817413-83e2-0545-cb90-36d5e096a6bd, 2026-11-20T16:40-16:41Z
  - source: computer.session start x3 on the same device, 2026-11-20T16:43-16:44Z, all node_offline
  - source: connection.repair and connection.health on the recovery device endo-recovery-8a2744fe-3281-4d50-a6d1-0ad28e99c05c, 2026-11-20T16:44Z, both timed out after 25s
  - source: tools/mac_capture_probe.py --evidence /tmp/lw-probe-0841.json, 2026-11-20T16:45Z
  - source: tools/queue.py sync, 2026-11-20T16:41Z
  - source: tools/queue.py stats --format json, 2026-11-20T16:41Z
  - source: GitHub connector open-PR read on zachmesh/lastwar, 2026-11-20T16:41Z
  - source: VPS SSH probe, 2026-11-20T16:39Z
---

# Queue ticker 2026-11-20 08:34 to about 08:50 PT (ticker-0834) - FAILED

No unit claimed, no unit completed. No screen entered, nothing
read or claimed. The blocker is the eighty-eighth consecutive failed
ticker pass by recorded-slot chain arithmetic (ticker-0704 at 07:04 PT
Nov 20 was the eighty-seventh and left a record; this pass is the
next recorded slot, so the count advances by this pass alone; the
counting basis is retro-owned - chain arithmetic here,
process-failure-record basis elsewhere). This is the TENTH
device-offline occurrence: the Mac mini itself is offline, not
merely windowless.

Executor name is ticker-0841, not ticker-0834: the schedule fired
at 08:34 PT but this run started late, about 08:39 PT
(dependency_probe trigger), so the token lease carries the
start-time name. The record file keeps the scheduled-slot name
0834, matching the 0004/0134/0234/0334/0434/0604/0704 convention.

Caveat on the count: slots 0734 and 0804 left no record anywhere
checked (branch queue-ticker folder, branch log, goal hidden_files
mirror), so they are NEW chain-gap candidates for retro ruling. If
either slot ran and failed, the true consecutive-failed count is
higher than 88 and the true device-offline occurrence count higher
than 10. The 88/10 figures are the recorded-slot figures only.

## Route - PARTIALLY honored, deviations owned

This pass repeated the ordering slip in the 0604 and 0704 forms
and added nothing new. The sync ran before the newest
queue-ticker record was read (0704, branch-only, read after the
probe), and the device probe (computer.session start x3) and the
open-PR check ran before that read as well. Second, the token was
acquired BEFORE the probe (16:42:13Z, lease until 16:57:13Z),
where the 0604 pass acquired it only after the probe classified
the device offline. The material part was honored - the probe ran
before any claim, `next` was never called, and NO unit was
claimed, so no unit attempt was burned (vip-2026-11-19-1800 stays
in inbox at attempts 0 of 3, expires_at 2026-11-21T02:00:00Z,
verified first-hand from the unit file). The token was released
promptly after the probe (about 16:44Z). The deviation-watch of
fully-honoring passes therefore stays at THREE; this pass joins
0604 and 0704 and the earlier partials. The next pass must read
the newest queue-ticker record first - checking BOTH the main
worktree AND the records/2026-11-20 branch, since the 0704
record lives only on the branch - then sync, then probe, then
token and claim only if the probe passes.

## Sync and seeding

- Sync: due 22, produced 0, already_queued all 22 (mail, help,
  gifts, harvest, vip, passes, daily-missions, secrets, treasures,
  radar, survivors, trucks, train, training, donations, events,
  arms-race, star-ceremony, duel-score, scout, scout-midday),
  reaped 0, expired 0. Pool after sync (live, about 16:41Z):
  inbox 77, claimed 0, done 2633.
  Branch reconcile warning: fetch of records/2026-11-20 failed
  (remote ref missing, issue #446), reconcile skipped.
- Zombie seeding skipped: the event ended at about the 19:00
  reset on 2026-10-30; chain zombie-2026-10-28 is closed and
  chain zombie-2026-11-10 was closed by unit 037 on 2026-11-14
  (verified first-hand in the 0704 pass from the unit file:
  status failed, "Glacieradon event ended: no Zombie Invasion
  tab in Events hub"); no zombie unit sits in inbox or claimed;
  do not seed until the tab is seen live again. A live re-check
  is impossible this pass (device offline).

## Own PRs first

- VPS route blocked: ssh to centos@66.179.249.233 returned
  Permission denied (publickey) at about 16:39Z, about 187.9 hours
  into the outage. The VPS gh CLI check could not run.
- Fallback via the GitHub connector (read-only open-PR list on
  zachmesh/lastwar, about 16:41Z): exactly three open PRs, all
  unchanged since 2026-11-12 - #711 knowledge fold (Owner
  lastwar-knowledge-organizer, head e3c3dfd0, updated
  2026-11-12T20:04:57Z), #708 records 2026-11-12 (Owner
  lastwar-pr-integrator, head 2f59c270, updated
  2026-11-12T20:44:37Z), #425 tools log gate (Owner
  lastwar-tool-developer, head 4f41cdd6, updated
  2026-11-12T19:29:37Z). None is owned by this job, and no open PR
  exists for records/2026-11-19 or records/2026-11-20. No new
  question or numbered fix point is addressed to this job.
- No new issue filed: the gh route is down and connector writes
  are forbidden for this repo per the 2032 tool-development
  record. The window-loss failure-mode filing and the
  device-offline mode filing stay owed, for a pass with a working
  gh route.

## Probe - device offline, tenth occurrence

- Mac mini OFFLINE per device.list, last_seen
  2026-11-20T04:16:40Z (20:16:40 PST Nov 19, about 12.4 hours
  stale at probe time). The "Zhen's Mac mini connection
  recovery" entry is frozen at 2026-11-20T04:17:05Z likewise.
- device.describe returned the command set and permissions
  (the metadata path still answers); connection_state offline
  in the same read.
- Attempt 1, computer.session start about 16:43Z - node_offline:
  device is offline and does not advertise a wake-up path.
  Attempt 2, computer.session start about 16:43Z - node_offline.
  Attempt 3, computer.session start about 16:44Z - node_offline.
  Three attempts satisfy the retry-at-least-3 rule; no computer
  session can start against an offline device, so no session was
  started and no window probe was possible. The game window state
  is unverifiable while the device channel is down.
- One extra recovery attempt: connection.repair on the recovery
  device timed out after 25s (node_invoke_timeout), and a
  follow-up connection.health on the same device also timed out
  after 25s. The recovery channel is unresponsive too; its
  outcome is unknown, not a success.
- Probe classification: tools/mac_capture_probe.py on the
  assembled evidence (/tmp/lw-probe-0841.json, invoke_offline as
  a 3-item list of computer.session start calls, plus the two
  recovery-device timeouts) returns DEVICE_OFFLINE, medium
  confidence, stop_pass yes (exit 13). Same label as 2157, 2304,
  0004, 0134, 0234, 0334, 0434, 0604 and 0704. Recovery still
  stands as bringing the Mac mini back online first (power,
  wake, network); the Dock-icon step and the gateway restart
  both need the Mac reachable, and neither applies while the
  device is offline.

## Unit

- None claimed, none completed. `next` was never called, so no
  unit attempt was burned. The token was acquired (ticker-0841,
  until 2026-11-20T16:57:13Z) and released before pass end.
  Tracker untouched. vip-2026-11-19-1800 stays in inbox at
  attempts 0 of 3, expires_at 2026-11-21T02:00:00Z; the new
  reset day's vip-2026-11-20-1800 is also in inbox, attempts 0,
  expires_at 2026-11-22T02:00:00Z.

## Standing counts

- No game unit since ticker-0214 gifts Nov 17 02:14 PT
  (about 78.5 hours missed). The newest finished unit in the
  pool is ghost-ops-2026-11-19-0000, finished
  2026-11-20T04:52:24Z (stats read newest_finished_at
  2026-11-20T04:52:24Z, age about 11.9 hours at 16:45Z).
- Seventh consecutive missed VIP day (same reset day 0704
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
  PT Nov 20), per pr-integration-0745's recount.
- Chain gaps stay nine confirmed, plus TWELVE candidates
  (2026-11-13 0839, 2026-11-14 0039, ticker-0034, ticker-0104,
  ticker-0204, ticker-0304, ticker-0404, ticker-0504,
  ticker-0534, ticker-0634, ticker-0734, ticker-0804),
  possible total twenty-one per this pass's arithmetic (nine
  plus twelve). This pass leaves a record, so the 0834 slot is
  filled and adds no new chain-gap candidate.
- Contradiction with MEMORY.md (43 as of the 15:00 batch, 44
  after the 19:00 batch) carried as retro flag (i); the
  sweep-night count discrepancy carried as retro flag (k);
  neither adopted.
- Duel day 4 Train Heroes ended 18:00 PT Nov 19, unreachable;
  day 5 posture unread while the device is offline.
- VPS SSH still Permission denied (publickey), about 187.9 hours
  into the outage; delivery blocked, commit left on local
  records/2026-11-20, no PR. This pass is partial.

## Repo-state note

- The main worktree sits on branch work/ops-execution-records
  with another job's in-flight state (untouched), so this
  delivery reuses the existing clean worktree
  lastwar-worktrees/ticker-0004-1120-records on records/2026-11-20
  (verified clean at tip 5b2368e485 before writing) and stages by
  explicit pathspec only: the record file, the day INDEX section,
  and the action-log entry. No tools/ symlink artifact appears
  in this worktree's status.
- The action-log tail was verified clean before appending (ends
  with a newline; the 0704 line is the last line). The older
  0434/0604 concatenation noted in the 0704 record is left for
  the delivery gate (log_append.py gate) to repair at push time.

## Time note

- The reset-day boundary is 02:00Z: the sweep windows end
  02:00Z and the VIP unit expires 02:00Z. In winter (PST,
  UTC-8) that is 18:00 PT; the repo's standing "19:00 PT
  reset" label is the PDT-era reading of the same 02:00Z
  instant. Times in this record use PST (UTC-8) unless marked
  Z. The integrator batch points (19:00, 23:00, 03:00, 07:00,
  11:00, 15:00 local) are a separate local-time schedule and
  are unaffected.
