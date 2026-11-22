---
title: Queue ticker run failure - Mac mini offline, ninetieth consecutive occurrence
created: 2026-11-20T19:16:00Z
modified: 2026-11-20T19:16:00Z
version: 1.0.0
description: Queue ticker 2026-11-20 11:04 PT run failure, Mac mini offline, no game input possible
status: run-failure
grounded_in:
  - source: _records_/2026-11-20/queue-ticker/0934-queue-run.md read during the run (records/2026-11-20 branch, commit e01b24d8cf) - the newest ticker record
  - source: _records_/2026-11-20/INDEX.md tail read during the run (records/2026-11-20 branch through ticker-0934; main worktree through queue-planning-1040)
  - source: device.list and device.describe on 1c817413-83e2-0545-cb90-36d5e096a6bd, 2026-11-20T19:08-19:09Z
  - source: connection.health, connection.repair and computer.session start on the same device, 2026-11-20T19:09-19:10Z, all node_offline
  - source: tools/mac_capture_probe.py --evidence /tmp/lw-probe-1104.json, 2026-11-20T19:11Z and 19:13Z
  - source: tools/queue.py sync, 2026-11-20T19:07Z
  - source: tools/queue.py stats --format json, 2026-11-20T19:08Z
  - source: GitHub connector open-PR read on zachmesh/lastwar, 2026-11-20T19:12Z
  - source: VPS SSH probe, 2026-11-20T19:08Z
---

# Queue ticker 2026-11-20 11:04 to about 11:25 PT (ticker-1104) - FAILED

No unit claimed, no unit completed. No screen entered, nothing
read or claimed. The blocker is the ninetieth consecutive failed
ticker pass by recorded-slot chain arithmetic (ticker-0934 at 09:34 PT
Nov 20 was the eighty-ninth and left a record; this pass is the
next recorded slot, so the count advances by this pass alone; the
counting basis is retro-owned - chain arithmetic here,
process-failure-record basis elsewhere). This is the TWELFTH
device-offline occurrence: the Mac mini itself is offline, not
merely windowless.

Executor name is ticker-1104, matching the scheduled slot: the
schedule fired at 11:04 PT and this run started about 11:07 PT
(dependency_probe trigger).

Caveat on the count: slot 1034 left no record anywhere checked
(branch queue-ticker folder, branch INDEX, branch action-log,
main-worktree INDEX and action-log, git log --all), so it is a
NEW chain-gap candidate for retro ruling. If that slot ran and
failed, the true consecutive-failed count is higher than 90 and
the true device-offline occurrence count higher than 12. The
90/12 figures are the recorded-slot figures only. (The two
ticker-1034 executor entries in the main-worktree action-log are
from 2026-10-29 and 2026-10-31, not today.)

## Route - PARTIALLY honored, deviation owned

This pass repeated the ordering slip in the 0604, 0704, 0834 and
0934 forms: the sync ran before the newest queue-ticker record
was read (0934, branch-only, read after the probe), despite the
0934 record warning the next pass explicitly to read first. The
material part was honored - the probe ran before any token or
claim, `next` was never called, and NO unit was claimed, so no
unit attempt was burned. The deviation-watch of fully-honoring
passes therefore stays at THREE (0434, 1347, 1404). A second
small slip: the first probe run returned UNKNOWN with low
confidence because the evidence file used the wrong key
(device_list_offline instead of device_list_online); the key
was corrected and the probe re-run in the same pass, returning
DEVICE_OFFLINE with high confidence.

## Sync and seeding

- Sync: due 22, produced 0, already_queued all 22 (mail, help,
  gifts, harvest, vip, passes, daily-missions, secrets, treasures,
  radar, survivors, trucks, train, training, donations, events,
  arms-race, star-ceremony, duel-score, scout, scout-midday),
  reaped 0, expired 0. Pool after sync: inbox 77, claimed 0,
  done 2650. Branch reconcile warning: fetch of records/2026-11-20
  failed (remote ref missing, issue #446), reconcile skipped.
- Zombie seeding skipped: the event ended at about the 19:00
  reset on 2026-10-30; chain zombie-2026-10-28 is closed and
  chain zombie-2026-11-10 was closed by unit 037 on 2026-11-14
  (no Zombie Invasion tab in the Events hub); no zombie unit
  sits in inbox or claimed; do not seed until the tab is seen
  live again. A live re-check is impossible this pass (device
  offline).

## Own PRs first

- VPS route blocked: ssh to centos@66.179.249.233 returned
  Permission denied (publickey) at about 19:08Z, about 190
  hours into the outage. The VPS gh CLI check could not run.
- Fallback via the GitHub connector (fresh read-only open-PR
  list on zachmesh/lastwar, this pass): exactly three open PRs,
  all unchanged since 2026-11-12 - #711 knowledge fold (Owner
  lastwar-knowledge-organizer, head e3c3dfd0, updated
  2026-11-12T20:04:57Z), #708 records 2026-11-12 (Owner
  lastwar-pr-integrator, head 2f59c270, updated
  2026-11-12T20:44:37Z), #425 tools log gate (Owner
  lastwar-tool-developer, head 4f41cdd6, updated
  2026-11-12T19:29:37Z). Updated timestamps identical to the
  ticker-0934 and earlier reads, so no new comment or review
  can have landed. None is owned by this job, and no open PR
  exists for records/2026-11-20. No new question or numbered
  fix point is addressed to this job. The connector identity
  is dtadpole (read-only use here); no write goes through it
  for this repo.
- No new issue filed: the gh route is down and the connector
  identity is dtadpole, forbidden for this repo per the 2032
  tool-development record. The window-loss failure-mode filing
  and the device-offline mode filing stay owed, for a pass with
  a working gh route.

## Probe - device offline, twelfth occurrence

- Mac mini OFFLINE per device.list, last_seen
  2026-11-20T04:16:40Z (20:16:40 PST, about 15 hours stale at
  probe time). The "Zhen's Mac mini connection recovery" entry
  is frozen at 2026-11-20T04:17:05Z likewise.
- device.describe returned the command set and permissions
  (the metadata path still answers); connection_state offline
  in the same read.
- Attempt 1, connection.health, attempt 2, connection.repair
  (target web), attempt 3, computer.session start, 19:09Z to
  19:10Z - node_offline every time: device is offline and does
  not advertise a wake-up path. Three attempts satisfy the
  retry-at-least-3 rule; no computer session can start against
  an offline device, so no window probe was possible. The game
  window state is unverifiable while the device channel is down.
- Probe classification: tools/mac_capture_probe.py v1.2.0 on
  the assembled evidence (/tmp/lw-probe-1104.json) returns
  DEVICE_OFFLINE, high confidence, stop_pass yes (exit 13).
  Same label as 0934 and the ten device-offline passes before
  it. Recovery still stands as bringing the Mac mini back
  online first (power, wake, network); the Dock-icon step and
  the gateway restart both need the Mac reachable, and neither
  applies while the device is offline.

## Unit

- None claimed, none completed. `next` was never called, so no
  unit attempt was burned. The token was acquired after the
  probe (ticker-1104, until 2026-11-20T19:28:29Z) and is
  released before pass end. Tracker untouched.
  vip-2026-11-19-1800 and vip-2026-11-20-1800 stay in inbox at
  attempts 0 of 3, expiring 2026-11-21T02:00:00Z and
  2026-11-22T02:00:00Z.

## Standing counts

- No game unit since ticker-0214 gifts Nov 17 02:14 PT
  (about 80.8 hours missed). The newest finished unit in the
  pool is harvest-2026-11-19-1803, finished 2026-11-20T04:52:24Z
  (the 2043 pass's failed completion, carried).
- Seventh consecutive missed VIP day (the reset day ending at
  the 02:00Z boundary Nov 21, 18:00 PST Nov 20; the new reset
  day's VIP unit is in inbox, attempts 0, unexecuted).
- Tonight's pre-reset sweep pair (zero-sweep-2026-11-20-1630
  and -1730) is staged in the pool, not yet due; last night's
  pair expired unexecuted at 18:19:25 PT Nov 19, sixth missed
  sweep night, seventh if tonight also goes unexecuted.
- Missed batches stay 47 per the adopted worker definition
  (pr-integration-1000). The 11:00 batch point arrived during
  this pass and no 11:00 integrator record was visible in the
  worktree or on the branch at record-writing time (latest
  pr-integration record 1000) - this pass does NOT count it as
  missed; whether it executes is the integrator's record to
  make.
- NEW chain-gap candidate ticker-1034 (no record anywhere
  checked); candidates now FOURTEEN, possible total
  twenty-three (planner-1040 counted THIRTEEN / twenty-two
  with 1034 still in window).
- Contradiction with MEMORY.md (43 as of the 15:00 batch, 44
  after the 19:00 batch) carried as retro flag (i); the
  sweep-night count discrepancy carried as retro flag (k);
  neither adopted.
- Duel day 4 Train Heroes ended 18:00 PT Nov 19, unreachable.
- VPS SSH still Permission denied (publickey), about 190
  hours into the outage; delivery blocked, commit left on
  local records/2026-11-20, no PR. This pass is partial.

## Repo-state note

- The main worktree sits on branch work/ops-execution-records
  with another job's in-flight state, so this delivery used the
  existing clean branch worktree
  lastwar-worktrees/ticker-0004-1120-records (verified clean at
  the branch tip e01b24d8cf before reuse) and staged by explicit
  pathspec only: the record file, the day INDEX section and the
  action-log entry. The tools/ to _tools_ compatibility symlink
  makes git status report tools/* as deleted in this worktree;
  that artifact was not touched and is not part of this delivery.

## Time note

- The reset-day boundary is 02:00Z: the sweep windows end
  02:00Z and the VIP unit expires 02:00Z. In winter (PST,
  UTC-8) that is 18:00 PT; the repo's standing "19:00 PT
  reset" label is the PDT-era reading of the same 02:00Z
  instant. Times in this record use PST (UTC-8) unless marked
  Z. The integrator batch points (19:00, 23:00, 03:00, 07:00,
  11:00, 15:00 local) are a separate local-time schedule and
  are unaffected.
