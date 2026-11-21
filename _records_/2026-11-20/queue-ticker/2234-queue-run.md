---
title: Queue ticker run failure - Mac mini offline, twenty-first device-offline occurrence
created: 2026-11-21T06:56:00Z
modified: 2026-11-21T06:56:00Z
version: 1.0.0
description: Queue ticker 2026-11-20 22:34 PT run failure, Mac mini offline, no game input possible
status: run-failure
grounded_in:
  - source: _records_/2026-11-20/queue-ticker/2037-queue-run.md read during the run (records/2026-11-20 branch copy in the delivery worktree) - the newest ticker record
  - source: _records_/2026-11-20/INDEX.md tail read during the run
  - source: device.list and device.describe on 1c817413-83e2-0545-cb90-36d5e096a6bd, 2026-11-21T06:47Z
  - source: connection.health x2, connection.repair, computer.session start on the same device, 2026-11-21T06:48Z, all node_offline
  - source: tools/mac_capture_probe.py --evidence /tmp/lw-probe-2234.json, 2026-11-21T06:52Z
  - source: tools/queue.py sync, 2026-11-21T06:35Z
  - source: GitHub connector open-PR read on zachmesh/lastwar, 2026-11-21T06:50Z
  - source: VPS SSH probe, 2026-11-21T06:35Z
---

# Queue ticker 2026-11-20 22:34 to about 22:59 PT (ticker-2234) - FAILED

No unit claimed, no unit completed. No screen entered, nothing
read or claimed. The blocker is the ninety-ninth consecutive failed
ticker pass by chain arithmetic (ticker-2037 at 20:37 PT was the
ninety-eighth and the newest ticker record anywhere checked; no
ticker record exists for the 21:04 or 22:04 slots, so the count
advances by this pass alone; the counting basis is retro-owned -
chain arithmetic here, process-failure-record basis elsewhere).
This is the TWENTY-FIRST device-offline occurrence: the Mac mini
itself is offline, not merely windowless.

## Route - PARTIALLY honored, deviations owned

This pass repeated the token-before-probe ordering slip twice over:
queue sync ran before the newest queue-ticker record was re-read
(2037, branch-only, read after the sync), and the device token was
acquired before the probe classified the device offline. The
material part was honored - the probe ran before any claim, `next`
was never called, and NO unit was claimed, so no unit attempt was
burned (vip-2026-11-20-1800 stays in inbox at attempts 0 of 3).
The fully-honoring watch therefore stays at ZERO; the next pass
must read the newest queue-ticker record first - checking BOTH the
main worktree AND the records/2026-11-20 branch, since the newest
records live only on the branch - then probe, then token and claim
only if the probe passes.

## Sync and seeding

- Sync: due 22, produced 0, already_queued all 22 (mail, help,
  gifts, harvest, vip, passes, daily-missions, secrets, treasures,
  radar, survivors, trucks, train, training, donations, events,
  arms-race, star-ceremony, duel-score, scout, scout-midday),
  reaped 0, expired 12 (the 18:03/18:30 slot units: arms-race,
  donations, duel-score, gifts, harvest, help, mail, radar,
  survivors, train, training and star-ceremony, all
  2026-11-20-1803/1830). Pool after sync: inbox 61, claimed 0,
  done 2701. Branch reconcile warning: fetch of
  records/2026-11-20 failed (remote ref missing, issue #446),
  reconcile skipped.
- Zombie seeding skipped: the event ended; chain
  zombie-2026-10-28 is closed and chain zombie-2026-11-10 was
  closed by unit 037 on 2026-11-14 (no Zombie Invasion tab in
  the Events hub); no zombie unit sits in inbox or claimed; do
  not seed until the tab is seen live again. A live re-check is
  impossible this pass (device offline).

## Own PRs first

- VPS route blocked: ssh to centos@66.179.249.233 returned
  Permission denied (publickey) at about 06:35Z, about 202
  hours into the outage. The VPS gh CLI check could not run.
- Fallback via the GitHub connector (read-only open-PR list on
  zachmesh/lastwar): exactly three open PRs, all unchanged since
  2026-11-12 - #711 knowledge fold (Owner
  lastwar-knowledge-organizer, head e3c3dfd0, updated
  2026-11-12T20:04:57Z), #708 records 2026-11-12 (Owner
  lastwar-pr-integrator, head 2f59c270, updated
  2026-11-12T20:44:37Z), #425 tools log gate (Owner
  lastwar-tool-developer, head 4f41cdd6, updated
  2026-11-12T19:29:37Z). Updated timestamps identical to the
  ticker-2037 and pr-catchall-2139 reads, so no new comment or
  review can have landed. None is owned by this job, and no open
  PR exists for records/2026-11-20. No new question or numbered
  fix point is addressed to this job.
- No new issue filed: the gh route is down and the connector
  identity is dtadpole, forbidden for this repo per the 2032
  tool-development record. The window-loss failure-mode filing
  and the device-offline mode filing stay owed, for a pass with
  a working gh route.

## Probe - device offline, twenty-first occurrence

- Mac mini OFFLINE per device.list, last_seen
  2026-11-20T04:16:40Z (20:16:40 PST Nov 19, about 26.5 hours
  stale at probe time). The "Zhen's Mac mini connection
  recovery" entry is frozen at 2026-11-20T04:17:05Z likewise.
- device.describe returned the command set and permissions
  (the metadata path still answers); connection_state offline
  in the same read.
- Attempts 1 to 4, 06:48Z - connection.health x2,
  connection.repair, computer.session start, node_offline every
  time: device is offline and does not advertise a wake-up
  path. Four attempts satisfy the retry-at-least-3 rule; no
  computer session can start against an offline device, so no
  session was started and no window probe was possible. The game
  window state is unverifiable while the device channel is down.
- Probe classification: tools/mac_capture_probe.py v1.2.0 on
  the assembled evidence (/tmp/lw-probe-2234.json) returns
  DEVICE_OFFLINE, high confidence, stop_pass yes (exit 13).
  Same label as 2037. Recovery still stands as bringing the Mac
  mini back online first (power, wake, network); the Dock-icon
  step and the gateway restart both need the Mac reachable, and
  neither applies while the device is offline.

## Unit

- None claimed, none completed. `next` was never called, so no
  unit attempt was burned. The token was acquired before the
  probe (ticker-2234, until 2026-11-21T07:04:47Z) and is
  released before pass end. Tracker untouched.
  vip-2026-11-20-1800 stays in inbox at attempts 0 of 3,
  expires_at 2026-11-22T02:00:00Z.

## Standing counts

- No game unit since ticker-0214 gifts Nov 17 02:14 PT
  (about 92.3 hours missed). The newest finished unit in the
  pool is harvest-2026-11-19-1803, finished 2026-11-20T04:52:24Z
  (the 2043 pass's failed completion, carried).
- Seventh consecutive missed VIP day (ticker count; KO chain
  counts 8 by a different口径, pending retro裁定) and seventh
  consecutive missed sweep night - tonight's pre-reset sweep
  pair (1630/1730) expired unexecuted (per
  queue-planning-1740); vip-2026-11-20-1800 still in inbox,
  attempts 0, expires 2026-11-22T02:00:00Z.
- Duel day 5 lost, day 6 blocked (per retro-2039); no score
  read today.
- Missed batches stay 50 per the adopted worker definition
  plus the retro-2039 count (42 + 8); the 23:00 batch point
  arrives after this pass ends and is NOT counted missed here -
  whether it executes is the integrator's record to make.
- The ticker-2104 and ticker-2204 slots left no record anywhere
  checked: two NEW chain-gap candidates, carried to retro
  (numbering for the KO pass; the ticker-side possible total
  stands at twenty-eight from 1434 plus these two).
- Contradiction with MEMORY.md (43 as of the 15:00 batch, 44
  after the 19:00 batch) carried as retro flag (i); the
  sweep-night count discrepancy carried as retro flag (k);
  neither adopted.
- VPS SSH still Permission denied (publickey), about 202 hours
  into the outage; delivery blocked, commit left on local
  records/2026-11-20, no PR. This pass is partial.

## Repo-state note

- The main worktree sits on branch work/ops-execution-records
  with another job's in-flight state, so this delivery used the
  existing clean branch worktree
  lastwar-worktrees/ticker-0004-1120-records (verified clean at
  the branch tip 3e16ece96e before reuse) and staged by explicit
  pathspec only: the record file, the day INDEX section, the
  action-log entry, and the 12 unit files this sync expired.
  The tools/ to _tools_ compatibility symlink makes git status
  report tools/* as deleted in this worktree; that artifact was
  not touched and is not part of this delivery.

## Time note

- The reset-day boundary is 02:00Z: the sweep windows end
  02:00Z and the VIP unit expires 02:00Z. In winter (PST,
  UTC-8) that is 18:00 PT; the repo's standing "19:00 PT
  reset" label is the PDT-era reading of the same 02:00Z
  instant. Times in this record use PST (UTC-8) unless marked
  Z. The integrator batch points (19:00, 23:00, 03:00, 07:00,
  11:00, 15:00 local) are a separate local-time schedule and
  are unaffected.
