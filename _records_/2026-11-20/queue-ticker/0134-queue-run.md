---
title: Queue ticker run failure - Mac mini offline, eighty-second consecutive occurrence
created: 2026-11-20T09:44:00Z
modified: 2026-11-20T09:44:00Z
version: 1.0.0
description: Queue ticker 2026-11-20 01:34 PT run failure, Mac mini offline, no game input possible
status: run-failure
grounded_in:
  - source: _records_/2026-11-20/queue-ticker/0004-queue-run.md read during the run (records/2026-11-20 branch, commit e4bc0a344d) - the newest ticker record
  - source: _records_/2026-11-20/INDEX.md tail read during the run
  - source: device.list and device.describe on 1c817413-83e2-0545-cb90-36d5e096a6bd, 2026-11-20T09:41Z
  - source: connection.health x3 on the same device, 2026-11-20T09:41Z to 09:43Z, all node_offline
  - source: tools/mac_capture_probe.py --evidence /tmp/lw-probe-0134.json, 2026-11-20T09:43Z
  - source: tools/queue.py sync, 2026-11-20T09:40Z
  - source: GitHub connector open-PR read on zachmesh/lastwar, 2026-11-20T09:43Z
  - source: VPS SSH probe, 2026-11-20T09:40Z
---

# Queue ticker 2026-11-20 01:34 to about 01:50 PT (ticker-0134) - FAILED

No unit claimed, no unit completed. No screen entered, nothing
read or claimed. The blocker is the eighty-second consecutive failed
ticker pass by chain arithmetic (ticker-0004 at 00:04 PT Nov 20
was the eighty-first and the third device-offline occurrence;
no ticker record exists for the 00:34 or 01:04 slots, so the count
advances by this pass alone; the counting basis is retro-owned -
chain arithmetic here, process-failure-record basis elsewhere).
This is the FOURTH device-offline occurrence: the Mac mini itself
is offline, not merely windowless.

## Route - PARTIALLY honored, deviation owned

This pass repeated the token-before-probe ordering slip: queue sync
ran before the newest queue-ticker record was read (0004, branch-only,
read after the sync). The material part was honored - the probe ran
before any token or claim, the token was acquired only after the
probe classified the device offline, `next` was never called, and
NO unit was claimed, so no unit attempt was burned
(vip-2026-11-19-1800 stays in inbox at attempts 0 of 3). The
deviation-watch of fully-honoring passes therefore stays at THREE
(0434, 1347, 1404); this pass joins 1645, 1740, 1926, 2043, 2157,
2304 and 0004 as partially honoring. The next pass must read the
newest queue-ticker record first - checking BOTH the main worktree
AND the records/2026-11-20 branch, since the 0004 record lives only
on the branch - then sync, then probe, then token and claim only if
the probe passes.

## Sync and seeding

- Sync: due 22, produced 0, already_queued all 22 (mail, help,
  gifts, harvest, vip, passes, daily-missions, secrets, treasures,
  radar, survivors, trucks, train, training, donations, events,
  arms-race, star-ceremony, duel-score, scout, scout-midday),
  reaped 0, expired 0. Pool after sync: inbox 73, claimed 0, done
  2598 - identical to the 0004 read. Branch reconcile warning:
  fetch of records/2026-11-20 failed (remote ref missing, issue
  #446), reconcile skipped.
- Zombie seeding skipped: the event ended at about the 19:00
  reset on 2026-10-30; chain zombie-2026-10-28 is closed and
  chain zombie-2026-11-10 was closed by unit 037 on 2026-11-14
  (no Zombie Invasion tab in the Events hub); no zombie unit
  sits in inbox or claimed; do not seed until the tab is seen
  live again. A live re-check is impossible this pass (device
  offline).

## Own PRs first

- VPS route blocked: ssh to centos@66.179.249.233 returned
  Permission denied (publickey) at about 09:40Z, about 181 hours
  into the outage. The VPS gh CLI check could not run.
- Fallback via the GitHub connector (read-only open-PR list on
  zachmesh/lastwar): exactly three open PRs, all unchanged since
  2026-11-12 - #711 knowledge fold (Owner
  lastwar-knowledge-organizer, head e3c3dfd0, updated
  2026-11-12T20:04:57Z), #708 records 2026-11-12 (Owner
  lastwar-pr-integrator, head 2f59c270, updated
  2026-11-12T20:44:37Z), #425 tools log gate (Owner
  lastwar-tool-developer, head 4f41cdd6, updated
  2026-11-12T19:29:37Z). Updated timestamps identical to the
  ticker-0004 read, so no new comment or review can have landed.
  None is owned by this job, and no open PR exists for
  records/2026-11-19 or records/2026-11-20. No new question or
  numbered fix point is addressed to this job. The connector
  cannot read PR comments through the reviewed read set (carried
  from 2157: 0 comments on #708 at the pr-catchall-2039 read).
- No new issue filed: the gh route is down and the connector
  identity is dtadpole, forbidden for this repo per the 2032
  tool-development record. The window-loss failure-mode filing
  and the device-offline mode filing stay owed, for a pass with
  a working gh route.

## Probe - device offline, fourth occurrence

- Mac mini OFFLINE per device.list, last_seen
  2026-11-20T04:16:40Z (20:16:40 PST Nov 19, about 5.4 hours
  stale at probe time). The "Zhen's Mac mini connection
  recovery" entry is frozen at 2026-11-20T04:17:05Z likewise.
- device.describe returned the command set and permissions
  (the metadata path still answers); connection_state offline
  in the same read.
- Attempt 1, 2, 3, connection.health 09:41Z to 09:43Z -
  node_offline every time: device is offline and does not
  advertise a wake-up path. Three attempts satisfy the
  retry-at-least-3 rule; no computer session can start against
  an offline device, so no session was started and no window
  probe was possible. The game window state is unverifiable
  while the device channel is down.
- Probe classification: tools/mac_capture_probe.py v1.2.0 on
  the assembled evidence (/tmp/lw-probe-0134.json) returns
  DEVICE_OFFLINE, high confidence, stop_pass yes (exit 13).
  Same label as 2157, 2304 and 0004. (First classification
  attempt returned UNKNOWN, low confidence: the evidence file
  lacked the device_list_online flag, so neither DEVICE_OFFLINE
  branch fired despite the 3-item node_offline list; adding
  device_list_online false and device_last_seen_stale true
  re-classified correctly. Next pass: include both flags from
  the start.) Recovery still stands as bringing the Mac mini
  back online first (power, wake, network); the Dock-icon step
  and the gateway restart both need the Mac reachable, and
  neither applies while the device is offline.

## Unit

- None claimed, none completed. `next` was never called, so no
  unit attempt was burned. The token was acquired after the
  probe (ticker-0134, until 2026-11-20T09:58:44Z) and is
  released before pass end. Tracker untouched.
  vip-2026-11-19-1800 stays in inbox at attempts 0 of 3,
  expires_at 2026-11-21T02:00:00Z.

## Standing counts

- No game unit since ticker-0214 gifts Nov 17 02:14 PT
  (about 71.5 hours missed). The newest finished unit in the
  pool is ghost-ops-2026-11-19-0000, expired by the 0004 sync;
  the prior newest was harvest-2026-11-19-1803, finished
  2026-11-20T04:52:24Z (the 2043 pass's failed completion,
  carried).
- Seventh consecutive missed VIP day (same reset day 0004
  counted, ending at the 02:00Z boundary Nov 21, 18:00 PST
  Nov 20; the new reset day's VIP unit is in inbox, attempts 0,
  unexecuted).
- Nov 19 pre-reset sweep pair expired unexecuted at 18:19:25 PT
  (carried from 1818/2140); the sweep night is fully missed -
  sixth missed sweep night per retro-2100.
- Missed batches stay 42 per the adopted worker definition
  plus 2 due-but-unexecuted per retro-2100 (15:00 and 19:00);
  no batch point passed during this run window (next 03:00).
  The 23:00 batch point arrived during the 2304 pass and no
  23:00 integrator record was visible then (latest pr-integration
  record 2215) - this pass does NOT count it as missed; whether
  it executes is the integrator's record to make.
- The ticker-2143 chain-gap candidate (pr-catchall-2239: no
  record landed by 22:41 PT) stays uncounted, carried.
- Contradiction with MEMORY.md (43 as of the 15:00 batch, 44
  after the 19:00 batch) carried as retro flag (i); the
  sweep-night count discrepancy carried as retro flag (k);
  neither adopted.
- Duel day 4 Train Heroes ended 18:00 PT Nov 19, unreachable;
  day 5 posture unread while the device is offline.
- VPS SSH still Permission denied (publickey), about 181 hours
  into the outage; delivery blocked, commit left on local
  records/2026-11-20, no PR. This pass is partial.

## Repo-state note

- The main worktree sits on branch work/ops-execution-records
  with another job's in-flight state, so this delivery reuses
  the existing clean worktree
  lastwar-worktrees/ticker-0004-1120-records on records/2026-11-20
  (verified clean at tip e4bc0a344d before writing) and stages by
  explicit pathspec only: the record file, the day INDEX section,
  and the action-log entry. The tools/ to _tools_ compatibility
  symlink makes git status report tools/* as deleted in this
  worktree; that artifact was not touched and is not part of this
  delivery.

## Time note

- The reset-day boundary is 02:00Z: the sweep windows end
  02:00Z and the VIP unit expires 02:00Z. In winter (PST,
  UTC-8) that is 18:00 PT; the repo's standing "19:00 PT
  reset" label is the PDT-era reading of the same 02:00Z
  instant. Times in this record use PST (UTC-8) unless marked
  Z. The integrator batch points (19:00, 23:00, 03:00, 07:00,
  11:00, 15:00 local) are a separate local-time schedule and
  are unaffected.
