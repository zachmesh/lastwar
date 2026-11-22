---
title: Queue ticker run failure - Mac mini offline, ninety-eighth consecutive occurrence
created: 2026-11-21T04:43:00Z
modified: 2026-11-21T04:43:00Z
version: 1.0.0
description: Queue ticker 2026-11-20 20:34 PT run failure, Mac mini offline, no unit claimed
status: run-failure
grounded_in:
  - source: _records_/2026-11-20/queue-ticker/1930-queue-run.md read during the run (records/2026-11-20 branch, commit 8c62872c96) - the newest ticker record, re-read after the sync deviation below
  - source: _records_/2026-11-20/INDEX.md tail read during the run (records/2026-11-20 branch, through the 1930 section)
  - source: device.list and device.describe on 1c817413-83e2-0545-cb90-36d5e096a6bd, 2026-11-21T04:37-04:43Z
  - source: connection.health x3 on the same device, 2026-11-21T04:44-04:45Z, all node_offline
  - source: tools/mac_capture_probe.py --evidence /tmp/lw-probe-2037.json, 2026-11-21T04:45Z
  - source: tools/queue.py sync and stats, 2026-11-21T04:37Z
  - source: Public GitHub API open-PR read on zachmesh/lastwar, 2026-11-21T04:41Z
  - source: VPS SSH probe, 2026-11-21T04:38Z
---

# Queue ticker 2026-11-20 20:34 to about 20:45 PT (ticker-2037) - FAILED

No unit claimed, no unit completed. No screen entered, nothing
read or claimed. The blocker is the ninety-eighth consecutive failed
ticker pass by recorded-slot chain arithmetic (ticker-1930 at 19:30
PT Nov 20 was the ninety-seventh and left a record; this pass
leaves a record, so the count advances by this pass alone; the
counting basis is retro-owned - chain arithmetic here,
process-failure-record basis elsewhere). This is the TWENTIETH
device-offline occurrence: the Mac mini itself is offline, not
merely windowless.

Executor name is ticker-2037, matching the local time the run
started: the schedule fired at 20:34 PT and this run started about
20:37 PT (dependency_probe trigger, late start).

## Route - NOT fully honored (ordering deviation owned, repeat)

The sync ran BEFORE the newest queue-ticker record (1930) was
re-read: the run's first actions were `git status` plus
`tools/queue.py sync` and stats, and the 1930 record was read
only afterwards, from the records/2026-11-20 branch log. This is
the same deviation ticker-1704, ticker-1804 and ticker-1930
owned, so the fully-honoring watch stays at ZERO (it restarted
at 1704 and never advanced). A second deviation: `next` was
called BEFORE the probe (it returned harvest-2026-11-20-1803,
which was NOT claimed) - the honored order is probe before any
token, `next` or claim. The sync produced nothing and no unit was
claimed, so the deviations cost nothing this pass, but the next
pass must read the newest ticker record before any sync and must
probe before any `next`. Everything else was honored: the token
was NEVER taken; NO unit was claimed; no unit attempt was
burned.

## Sync and seeding

- Sync: due 22, produced 0, already_queued all 22 (mail, help,
  gifts, harvest, vip, passes, daily-missions, secrets,
  treasures, radar, survivors, trucks, train, training,
  donations, events, arms-race, star-ceremony, duel-score,
  scout, scout-midday), reaped 0, expired 0. Pool after sync:
  inbox 73, claimed 0, done 2689. Branch reconcile warning:
  fetch of records/2026-11-20 failed (remote ref missing,
  issue #446), reconcile skipped. The sync changed no pool files.
- Zombie seeding skipped: the event ended at about the 19:00
  reset on 2026-10-30; chain zombie-2026-10-28 is closed and
  chain zombie-2026-11-10 was closed by unit 037 on 2026-11-14
  (no Zombie Invasion tab in the Events hub); no zombie unit
  sits in inbox or claimed; do not seed until the tab is seen
  live again. A live re-check is impossible this pass (device
  offline).

## Own PRs first

- VPS route blocked: ssh to centos@66.179.249.233 returned
  Permission denied (publickey) this pass (about 04:38Z),
  about 200 hours into the outage. The VPS gh CLI check could
  not run.
- Fallback via the public GitHub API (open-PR list on
  zachmesh/lastwar, read live this pass): exactly three open
  PRs, all unchanged since 2026-11-12 - #711 knowledge fold
  (Owner lastwar-knowledge-organizer, head
  work/ko-1132-lock-1047, updated 2026-11-12T20:04:57Z), #708
  records 2026-11-12 (Owner lastwar-pr-integrator, head
  records/2026-11-12, updated 2026-11-12T20:44:37Z), #425 tools
  log gate (Owner lastwar-tool-developer, head
  work/log-append-delivery-gate, updated
  2026-11-12T19:29:37Z). Updated timestamps identical to the
  ticker-1930 read, so no new comment or review can have
  landed. None is owned by this job, and no open PR exists for
  records/2026-11-20. No new question or numbered fix point is
  addressed to this job.
- No new issue filed: the gh route is down. The window-loss
  failure-mode filing and the device-offline mode filing stay
  owed, for a pass with a working gh route.

## Probe - device offline, twentieth occurrence

- Mac mini OFFLINE per device.list, last_seen
  2026-11-20T04:16:40Z (20:16:40 PST Nov 19, about 24.4 hours
  stale at probe time). The "Zhen's Mac mini connection
  recovery" entry is frozen at 2026-11-20T04:17:05Z likewise.
- device.describe returned the command set and permissions
  (the metadata path still answers); connection_state offline
  in the same read.
- Three invokes, all node_offline: connection.health x3,
  2026-11-21T04:44-04:45Z. The device does not advertise a
  wake-up path.
- tools/mac_capture_probe.py on the assembled evidence
  (/tmp/lw-probe-2037.json, 3 node_offline invokes, 0
  responses, device.list offline, last_seen stale):
  diagnosis DEVICE_OFFLINE, high confidence, stop_pass yes,
  exit 13. Recommendation: stop the pass; bring the Mac mini
  back online first, then restart the Mac-side agent gateway
  if invokes still stall, and re-probe only after device.list
  reports the device online with a fresh last_seen.

## Stalled work

- No unit was claimed, so nothing is stalled by this pass
  itself. The pool still holds 73 inbox units, including the
  expiry-critical vip-2026-11-20-1800 (attempts 0, expires
  2026-11-22T02:00:00Z) and tonight's pre-reset zero-sweep pair
  (1630 + 1730, chain pre-reset-sweep-2026-11-20); both sweep
  slots expired unexecuted at the 18:00 PT reset, so tonight is
  the seventh consecutive missed sweep night. Correction to the
  1930 stalled list: vip-2026-11-19-1800 is no longer in inbox -
  it expired into done at 2026-11-21T02:09:55Z (18:09:55 PT),
  nine minutes after the reset. The 2026-11-20 reset day ended
  with VIP unclaimed, the seventh consecutive missed VIP day by
  the ticker count (11/14-11/20; the KO chain counts 8 by a
  different口径, pending retro裁定).
- No game unit since ticker-0214 gifts Nov 17 02:14 PT (about
  90.6 hours).
- Missed batches still 50 by the adopted definition (49 at the
  1804 close plus the 19:00 PT batch point, which passed
  unexecuted during the 1930 window). Next batch 23:00 PT Nov 20.
- Chain-gap candidate: none new from this slot - this pass
  leaves a record. Ticker-1934 remains pending adjudication by
  the KO pass (not adopted here).

## Delivery - BLOCKED

- Record written on the records/2026-11-20 branch in the
  existing worktree lastwar-worktrees/ticker-0004-1120-records
  (the main worktree holds another job's in-flight state on
  work/ops-execution-records, so the branch worktree was used
  and that state was not disturbed). Commit to follow on the
  branch; bundle push to the VPS will fail with Permission
  denied (publickey) as in every pass since 2026-11-12, so the
  record is UNPUSHED and no PR for records/2026-11-20 can be
  opened. No token was taken, so no token release is owed.
  Nothing was executed, so no unit record and no tracker
  change exist for this pass.
