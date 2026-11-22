---
title: Queue ticker run failure - Mac mini offline, ninety-fifth consecutive occurrence
created: 2026-11-21T01:20:00Z
modified: 2026-11-21T01:20:00Z
version: 1.0.0
description: Queue ticker 2026-11-20 17:04 PT run failure, Mac mini offline, no unit claimed
status: run-failure
grounded_in:
  - source: _records_/2026-11-20/queue-ticker/1604-queue-run.md read during the run (records/2026-11-20 branch, commit c6abe3dca6) - the newest ticker record
  - source: _records_/2026-11-20/INDEX.md tail read during the run (records/2026-11-20 branch, through the 1604 section)
  - source: device.list and device.describe on 1c817413-83e2-0545-cb90-36d5e096a6bd, 2026-11-21T01:14-01:15Z
  - source: connection.health x3 on the same device, 2026-11-21T01:15-01:17Z, all node_offline
  - source: tools/mac_capture_probe.py --evidence /tmp/lw-probe-1704.json, 2026-11-21T01:18Z
  - source: tools/queue.py sync and stats, 2026-11-21T01:13Z
  - source: GitHub connector open-PR read on zachmesh/lastwar, 2026-11-21T01:14Z
  - source: VPS SSH probe, 2026-11-21T01:14Z
---

# Queue ticker 2026-11-20 17:04 to about 17:20 PT (ticker-1704) - FAILED

No unit claimed, no unit completed. No screen entered, nothing
read or claimed. The blocker is the ninety-fifth consecutive failed
ticker pass by recorded-slot chain arithmetic (ticker-1604 at 16:04
PT Nov 20 was the ninety-fourth and left a record; this pass is
the next recorded slot, so the count advances by this pass alone;
the counting basis is retro-owned - chain arithmetic here,
process-failure-record basis elsewhere). This is the SEVENTEENTH
device-offline occurrence: the Mac mini itself is offline, not
merely windowless.

Executor name is ticker-1704, matching the scheduled slot: the
schedule fired at 17:04 PT and this run started about 17:13 PT
(dependency_probe trigger, late start).

## Route - NOT fully honored (ordering deviation owned)

The sync ran BEFORE the newest queue-ticker record (1604) was
re-read: the run's first action was `tools/queue.py sync` plus
stats, and the 1604 record was read only afterwards, from the
records/2026-11-20 branch log. The deviation-watch therefore
restarts at ZERO (was FOUR: 0434, 1347, 1404, 1604). The sync
produced nothing and no unit was claimed, so the deviation cost
nothing this pass, but the fully-honoring streak is broken and
the next pass must read the newest ticker record before any sync.
Everything after the deviation was honored: the probe ran BEFORE
any token, `next` or claim; the token was NEVER taken; `next` was
never called; NO unit was claimed; no unit attempt was burned.

## Sync and seeding

- Sync: due 22, produced 0, already_queued all 22 (mail, help,
  gifts, harvest, vip, passes, daily-missions, secrets,
  treasures, radar, survivors, trucks, train, training,
  donations, events, arms-race, star-ceremony, duel-score,
  scout, scout-midday), reaped 0, expired 0. Pool after sync:
  inbox 77, claimed 0, done 2667. Branch reconcile warning:
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
  Permission denied (publickey) at about 01:14Z, about 196.5
  hours into the outage. The VPS gh CLI check could not run.
- Fallback via the GitHub connector (open-PR list on
  zachmesh/lastwar, read live this pass): exactly three open
  PRs, all unchanged since 2026-11-12 - #711 knowledge fold
  (Owner lastwar-knowledge-organizer, head e3c3dfd0, updated
  2026-11-12T20:04:57Z), #708 records 2026-11-12 (Owner
  lastwar-pr-integrator, head 2f59c270, updated
  2026-11-12T20:44:37Z), #425 tools log gate (Owner
  lastwar-tool-developer, head 4f41cdd6, updated
  2026-11-12T19:29:37Z). Updated timestamps identical to the
  ticker-1604 read, so no new comment or review can have
  landed. None is owned by this job, and no open PR exists for
  records/2026-11-20. No new question or numbered fix point is
  addressed to this job.
- No new issue filed: the gh route is down. The window-loss
  failure-mode filing and the device-offline mode filing stay
  owed, for a pass with a working gh route.

## Probe - device offline, seventeenth occurrence

- Mac mini OFFLINE per device.list, last_seen
  2026-11-20T04:16:40Z (20:16:40 PST Nov 19, about 21 hours
  stale at probe time). The "Zhen's Mac mini connection
  recovery" entry is frozen at 2026-11-20T04:17:05Z likewise.
- device.describe returned the command set and permissions
  (the metadata path still answers); connection_state offline
  in the same read.
- Three invokes, all node_offline: connection.health x3,
  2026-11-21T01:15-01:17Z. The device does not advertise a
  wake-up path.
- tools/mac_capture_probe.py on the assembled evidence
  (/tmp/lw-probe-1704.json, 3 node_offline invokes, 0
  responses, device.list offline, last_seen stale):
  diagnosis DEVICE_OFFLINE, high confidence, stop_pass yes,
  exit 13. Recommendation: stop the pass; bring the Mac mini
  back online first, then restart the Mac-side agent gateway
  if invokes still stall, and re-probe only after device.list
  reports the device online with a fresh last_seen.

## Stalled work

- No unit was claimed, so nothing is stalled by this pass
  itself. The pool still holds 77 inbox units, including the
  expiry-critical vip-2026-11-19-1800 and
  vip-2026-11-20-1800 and tonight's pre-reset zero-sweep pair
  (1630 + 1730, chain pre-reset-sweep-2026-11-20, staged by
  planner-1540); the 1630 sweep slot opened at 16:30, inside
  this pass's window, and the 1730 slot opens at 17:30, about
  10 minutes after this pass ends. Tonight would be the seventh
  missed sweep night if the pair also goes unexecuted.
- Seventh consecutive missed VIP day (the reset day ends
  18:00 PT Nov 20, 40 minutes after this pass ends). No game
  unit since ticker-0214 gifts Nov 17 02:14 PT (about 87
  hours).
- Missed batches stay 49 by the adopted definition (42 missed
  + 7 due-but-blocked, pr-integration-1545). Next batch 19:00 PT.
- Chain-gap candidate TWENTY (ticker-1504 left no record
  anywhere checked) stands unchanged; this slot leaves a
  record, so no new gap candidate arises from it.

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
