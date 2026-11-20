---
title: Queue ticker run failure - Mac mini offline, eighty-fourth consecutive occurrence
created: 2026-11-20T12:00:00Z
modified: 2026-11-20T12:00:00Z
version: 1.0.0
description: Queue ticker 2026-11-20 03:34 PT run failure, Mac mini offline, no game input possible
status: run-failure
grounded_in:
  - source: _records_/2026-11-20/queue-ticker/0234-queue-run.md read during the run (records/2026-11-20 branch, commit d4661ca3ba) - the newest ticker record
  - source: _records_/2026-11-20/INDEX.md tail read during the run
  - source: device.list and device.describe on 1c817413-83e2-0545-cb90-36d5e096a6bd, 2026-11-20T11:51Z
  - source: connection.health x3 on the same device, 2026-11-20T11:52Z, all node_offline
  - source: tools/mac_capture_probe.py --evidence /tmp/lw-probe-0334.json, 2026-11-20T11:53Z
  - source: tools/queue.py sync, 2026-11-20T11:51Z
  - source: GitHub connector open-PR read on zachmesh/lastwar, 2026-11-20T11:53Z
  - source: VPS SSH probe, 2026-11-20T11:51Z
---

# Queue ticker 2026-11-20 03:34 to about 04:00 PT (ticker-0334) - FAILED

No unit claimed, no unit completed. No screen entered, nothing
read or claimed. The blocker is the eighty-fourth consecutive failed
ticker pass by chain arithmetic (ticker-0234 at 02:34 PT Nov 20
was the eighty-third and the fifth device-offline occurrence;
no ticker record exists for the 03:04 slot, so the count
advances by this pass alone; the counting basis is retro-owned -
chain arithmetic here, process-failure-record basis elsewhere).
This is the SIXTH device-offline occurrence: the Mac mini itself
is offline, not merely windowless.

## Route - PARTIALLY honored, deviation owned

This pass repeated the token-before-probe ordering slip: queue sync
ran before the newest queue-ticker record was read (0234, branch-only,
read after the sync). The material part was honored - the probe ran
before any token or claim, the token was acquired only after the
probe classified the device offline, `next` was never called, and
NO unit was claimed, so no unit attempt was burned
(vip-2026-11-19-1800 stays in inbox at attempts 0 of 3). The
deviation-watch of fully-honoring passes therefore stays at THREE
(0434, 1347, 1404); this pass joins 1645, 1740, 1926, 2043, 2157,
2304, 0004, 0134 and 0234 as partially honoring. The next pass must read
the newest queue-ticker record first - checking BOTH the main
worktree AND the records/2026-11-20 branch, since the 0234 record
lives only on the branch - then sync, then probe, then token and
claim only if the probe passes.

## Sync and seeding

- Sync: due 22, produced 0, already_queued all 22 (mail, help,
  gifts, harvest, vip, passes, daily-missions, secrets, treasures,
  radar, survivors, trucks, train, training, donations, events,
  arms-race, star-ceremony, duel-score, scout, scout-midday),
  reaped 0, expired 0. Pool after sync: inbox 73, claimed 0, done
  2615 - done grew by 5 since the 0234 read (the planner-0340
  run in between). Branch reconcile warning: fetch of
  records/2026-11-20 failed (remote ref missing, issue #446),
  reconcile skipped.
- Zombie seeding skipped: the event ended at about the 19:00
  reset on 2026-10-30; chain zombie-2026-10-28 is closed and
  chain zombie-2026-11-10 was closed by unit 037 on 2026-11-14
  (no Zombie Invasion tab in the Events hub); no zombie unit
  sits in inbox or claimed; do not seed until the tab is seen
  live again. A live re-check is impossible this pass (device
  offline).

## Own PRs first

- VPS route blocked: ssh to centos@66.179.249.233 returned
  Permission denied (publickey) at about 11:51Z, about 183 hours
  into the outage. The VPS gh CLI check could not run.
- Fallback via the GitHub connector (read-only open-PR list on
  zachmesh/lastwar, 11:53Z): exactly three open PRs, all unchanged
  since 2026-11-12 - #711 knowledge fold (Owner
  lastwar-knowledge-organizer, head e3c3dfd0, updated
  2026-11-12T20:04:57Z), #708 records 2026-11-12 (Owner
  lastwar-pr-integrator, head 2f59c270, updated
  2026-11-12T20:44:37Z), #425 tools log gate (Owner
  lastwar-tool-developer, head 4f41cdd6, updated
  2026-11-12T19:29:37Z). Updated timestamps identical to the
  ticker-0234 read, so no new comment or review can have landed.
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

## Probe - device offline, sixth occurrence

- Mac mini OFFLINE per device.list, last_seen
  2026-11-20T04:16:40Z (20:16:40 PST Nov 19, about 7.6 hours
  stale at probe time). The "Zhen's Mac mini connection
  recovery" entry is frozen at 2026-11-20T04:17:05Z likewise.
- device.describe returned the command set and permissions
  (the metadata path still answers); connection_state offline
  in the same read.
- Attempt 1, 2, 3, connection.health 11:52Z -
  node_offline every time: device is offline and does not
  advertise a wake-up path. Three attempts satisfy the
  retry-at-least-3 rule; no computer session can start against
  an offline device, so no session was started and no window
  probe was possible. The game window state is unverifiable
  while the device channel is down.
- Probe classification: tools/mac_capture_probe.py on the
  assembled evidence (/tmp/lw-probe-0334.json, both
  device_list_online false and device_last_seen_stale true
  included from the start per the 0134 note) returns
  DEVICE_OFFLINE, high confidence, stop_pass yes (exit 13).
  Same label as 2157, 2304, 0004, 0134 and 0234. Recovery still
  stands as bringing the Mac mini back online first (power,
  wake, network); the Dock-icon step and the gateway restart
  both need the Mac reachable, and neither applies while the
  device is offline.

## Unit

- None claimed, none completed. `next` was never called, so no
  unit attempt was burned. The token was acquired after the
  probe (ticker-0334, until 2026-11-20T12:08:39Z) and is
  released before pass end. Tracker untouched.
  vip-2026-11-19-1800 stays in inbox at attempts 0 of 3,
  expires_at 2026-11-21T02:00:00Z.

## Standing counts

- No game unit since ticker-0214 gifts Nov 17 02:14 PT
  (about 73.7 hours missed). The newest finished unit in the
  pool is ghost-ops-2026-11-19-0000, finished
  2026-11-20T04:52:24Z (carried from 0134; stats read
  newest_finished_at 2026-11-20T04:52:24Z, age 419 minutes
  at 11:51Z).
- Seventh consecutive missed VIP day (same reset day 0234
  counted, ending at the 02:00Z boundary Nov 21, 18:00 PST
  Nov 20; the new reset day's VIP unit is in inbox, attempts 0,
  unexecuted).
- Nov 19 pre-reset sweep pair expired unexecuted at 18:19:25 PT
  (carried from 1818/2140); the sweep night is fully missed -
  sixth missed sweep night per retro-2100.
- Missed batches stay 42 per the adopted worker definition
  plus 4 due-but-unexecuted per retro-2100 and the 0240 planner
  (15:00, 19:00, 23:00 Nov 19, and 03:00 Nov 20, which passed
  with no records PR in existence to merge), i.e. 46; no batch
  point falls inside this run window (next 07:00 PT Nov 20).
- Chain gaps stay nine confirmed, plus candidates
  2026-11-13 0839, 2026-11-14 0039, ticker-0104, ticker-0204
  and ticker-0304 (the 0304 slot left no record anywhere,
  fourth recordless slot today after 0034, 0104 and 0204)
  flagged for retro ruling, not counted. This pass leaves a
  record, so it adds no new gap.
- Contradiction with MEMORY.md (43 as of the 15:00 batch, 44
  after the 19:00 batch) carried as retro flag (i); the
  sweep-night count discrepancy carried as retro flag (k);
  neither adopted.
- Duel day 4 Train Heroes ended 18:00 PT Nov 19, unreachable;
  day 5 posture unread while the device is offline.
- VPS SSH still Permission denied (publickey), about 183 hours
  into the outage; delivery blocked, commit left on local
  records/2026-11-20, no PR. This pass is partial.

## Repo-state note

- The main worktree sits on branch work/ops-execution-records
  with another job's in-flight state, so this delivery reuses
  the existing clean worktree
  lastwar-worktrees/ticker-0004-1120-records on records/2026-11-20
  (verified clean at tip d4661ca3ba before writing) and stages by
  explicit pathspec only: the record file, the day INDEX section,
  and the action-log entry. No tools/ symlink artifact appears
  in this worktree's status.

## Time note

- The reset-day boundary is 02:00Z: the sweep windows end
  02:00Z and the VIP unit expires 02:00Z. In winter (PST,
  UTC-8) that is 18:00 PT; the repo's standing "19:00 PT
  reset" label is the PDT-era reading of the same 02:00Z
  instant. Times in this record use PST (UTC-8) unless marked
  Z. The integrator batch points (19:00, 23:00, 03:00, 07:00,
  11:00, 15:00 local) are a separate local-time schedule and
  are unaffected.
