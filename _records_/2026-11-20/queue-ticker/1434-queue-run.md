---
title: Queue ticker run failure - Mac mini offline, ninety-third consecutive occurrence
created: 2026-11-20T23:05:00Z
modified: 2026-11-20T23:05:00Z
version: 1.0.0
description: Queue ticker 2026-11-20 14:34 PT run failure, Mac mini offline, no unit claimed
status: run-failure
grounded_in:
  - source: _records_/2026-11-20/queue-ticker/1334-queue-run.md read during the run (records/2026-11-20 branch, commits 1b972a80fd and 9e59f49dfd) - the newest ticker record
  - source: _records_/2026-11-19/queue-ticker/2304-queue-run.md read during the run (main worktree copy)
  - source: _records_/2026-11-20/INDEX.md tail read during the run (records/2026-11-20 branch through the 1334 section; main worktree through knowledge-organization-1432 and queue-planning-1440)
  - source: device.list and device.describe on 1c817413-83e2-0545-cb90-36d5e096a6bd, 2026-11-20T22:55-22:56Z
  - source: connection.health x2, computer.session start, connection.repair on the same device, 2026-11-20T22:56-22:58Z, all node_offline
  - source: tools/mac_capture_probe.py --evidence /tmp/lw-probe-1434.json, 2026-11-20T22:59Z
  - source: tools/queue.py sync and stats --format json, 2026-11-20T22:54Z
  - source: GitHub REST open-PR read on zachmesh/lastwar, 2026-11-20T22:56Z
  - source: VPS SSH probe, 2026-11-20T22:55Z
---

# Queue ticker 2026-11-20 14:34 to about 15:06 PT (ticker-1434) - FAILED

No unit claimed, no unit completed. No screen entered, nothing
read or claimed. The blocker is the ninety-third consecutive failed
ticker pass by recorded-slot chain arithmetic (ticker-1334 at 13:34
PT Nov 20 was the ninety-second and left a record; this pass is
the next recorded slot, so the count advances by this pass alone;
the counting basis is retro-owned - chain arithmetic here,
process-failure-record basis elsewhere). This is the FIFTEENTH
device-offline occurrence: the Mac mini itself is offline, not
merely windowless.

Executor name is ticker-1434, matching the scheduled slot: the
schedule fired at 14:34 PT and this run started about 14:54 PT
(dependency_probe trigger).

Caveat on the count: slot 1404 left no record anywhere checked
(branch queue-ticker folder, branch INDEX, branch action-log for
today, main-worktree INDEX and action-log, git log --all - the
only ticker-1404 commit anywhere is ebf5f9db72, dated
2026-11-19), so it stands as a NEW chain-gap candidate for retro
ruling (candidate NINETEEN, possible total twenty-eight; 1304
was adopted by KO-1432 as eighteen). The 1404 window closed
about 14:34 PT and the token-acquire in this pass succeeded, so
no 1404 pass is still running. If the 1404 slot ran and failed,
the true consecutive-failed count is higher than 93 and the true
device-offline occurrence count higher than 15. The 93/15
figures are the recorded-slot figures only.

## Route - PARTIALLY honored, deviation owned

This pass repeated the ordering slip in the 0604, 0704, 0834,
0934, 1104, 1204 and 1334 forms: the sync ran before the newest
queue-ticker record was read (1334, branch-only, read after the
sync). It added a second slip against the 1334 instruction
("no `next`, no claim, no token"): the token was acquired at
about 14:55 PT, before the probe, and released at about 14:57
PT once the probe had classified the device offline. The
material part was honored - the probe ran before any claim,
`next` was never called, NO unit was claimed, and no unit
attempt was burned (unlike 1334's burned radar attempt). The
deviation-watch of fully-honoring passes therefore stays at
THREE (0434, 1347, 1404); this pass joins 1645, 1740, 1926,
2043, 2157, 2304 and 1334 as partially honoring. The next pass
must read the newest queue-ticker record first - checking BOTH
the main worktree AND the records/2026-11-20 branch - then
sync, then probe, then token and claim only if the probe passes.

## Sync and seeding

- Sync: due 22, produced 0, already_queued all 22 (mail, help,
  gifts, harvest, vip, passes, daily-missions, secrets,
  treasures, radar, survivors, trucks, train, training,
  donations, events, arms-race, star-ceremony, duel-score,
  scout, scout-midday), reaped 0, expired 0. Pool after sync:
  inbox 77, claimed 0, done 2662. Branch reconcile warning:
  fetch of records/2026-11-20 failed (remote ref missing, issue
  #446), reconcile skipped. The sync changed no pool files;
  the 11 expired units finished 22:41:29Z belong to the
  queue-planning-1440 sync (12 staged, 11 expired).
- Zombie seeding skipped: the event ended at about the 19:00
  reset on 2026-10-30; chain zombie-2026-10-28 is closed and
  chain zombie-2026-11-10 was closed by unit 037 on 2026-11-14
  (no Zombie Invasion tab in the Events hub); no zombie unit
  sits in inbox or claimed; do not seed until the tab is seen
  live again. A live re-check is impossible this pass (device
  offline).

## Own PRs first

- VPS route blocked: ssh to centos@66.179.249.233 returned
  Permission denied (publickey) at about 22:55Z, about 194
  hours into the outage. The VPS gh CLI check could not run.
- Fallback via the unauthenticated GitHub REST API (open-PR
  list on zachmesh/lastwar, read live this pass): exactly three
  open PRs, all unchanged since 2026-11-12 - #711 knowledge
  fold (Owner lastwar-knowledge-organizer, head e3c3dfd0,
  updated 2026-11-12T20:04:57Z), #708 records 2026-11-12
  (Owner lastwar-pr-integrator, head 2f59c270, updated
  2026-11-12T20:44:37Z), #425 tools log gate (Owner
  lastwar-tool-developer, head 4f41cdd6, updated
  2026-11-12T19:29:37Z). Updated timestamps identical to the
  ticker-1334, pr-catchall-1339, pr-integration-1330,
  knowledge-organization-1432 and queue-planning-1440 reads,
  so no new comment or review can have landed. None is owned
  by this job, and no open PR exists for records/2026-11-20.
  No new question or numbered fix point is addressed to this
  job.
- No new issue filed: the gh route is down. The window-loss
  failure-mode filing and the device-offline mode filing stay
  owed, for a pass with a working gh route.

## Probe - device offline, fifteenth occurrence

- Mac mini OFFLINE per device.list, last_seen
  2026-11-20T04:16:40Z (20:16:40 PST Nov 19, about 18.7 hours
  stale at probe time). The "Zhen's Mac mini connection
  recovery" entry is frozen at 2026-11-20T04:17:05Z likewise.
- device.describe returned the command set and permissions
  (the metadata path still answers); connection_state offline
  in the same read.
- Attempt 1, 2, connection.health, attempt 3, computer.session
  start, attempt 4, connection.repair (target web), 22:56Z to
  22:58Z - node_offline every time: device is offline and does
  not advertise a wake-up path. Four attempts satisfy the
  retry-at-least-3 rule; no computer session can start against
  an offline device, so no session was started and no window
  probe was possible. The game window state is unverifiable
  while the device channel is down.
- Probe classification: tools/mac_capture_probe.py v1.2.0 on
  the assembled evidence (/tmp/lw-probe-1434.json) returns
  DEVICE_OFFLINE, high confidence, stop_pass yes (exit 13).
  Same label as 1104, 1204 and 1334. Recovery still stands as
  bringing the Mac mini back online first (power, wake,
  network); the Dock-icon step and the gateway restart both
  need the Mac reachable, and neither applies while the device
  is offline.

## Unit

- None claimed, none completed. `next` was never called, so no
  unit attempt was burned. The token was acquired before the
  probe (ticker-1434, until 2026-11-20T23:11:50Z) and released
  at about 14:57 PT, before pass end. Tracker untouched.

## Standing counts

- No game unit since ticker-0214 gifts Nov 17 02:14 PT
  (about 84.8 hours missed). The newest finished units in the
  pool are the 11 expired at 2026-11-20T22:41:29Z (planner-1440
  sync); the newest executed unit remains
  harvest-2026-11-20-1003, finished 2026-11-20T20:26:31Z (the
  1204 pass's failed completion, carried).
- Result status totals: done 479, partial 566, failed 212,
  skipped-needs-owner 16, expired 1389 (expired up 11 on the
  planner-1440 sync).
- Stalled priority-1 inbox units: vip-2026-11-19-1800,
  zero-sweep-2026-11-20-1630, vip-2026-11-20-1800,
  zero-sweep-2026-11-20-1730.
- Seventh consecutive missed VIP day (the reset day ending at
  the 02:00Z boundary Nov 21, 18:00 PST Nov 20; the new reset
  day's VIP unit is in inbox, attempts 0, unexecuted).
- Tonight's pre-reset sweep pair (zero-sweep-2026-11-20-1630
  and -1730) is staged in the pool, not yet due; last night's
  pair expired unexecuted at 18:19:25 PT Nov 19, sixth missed
  sweep night, seventh if tonight also goes unexecuted.
- Missed batches stay 48 per the adopted worker definition
  (pr-integration-1100/1330); the 15:00 batch point arrived
  during this pass and is NOT counted as missed here - whether
  it executes is the integrator's record to make.
- Chain-gap candidates stay EIGHTEEN confirmed plus ONE NEW
  candidate (ticker-1404 today), possible total twenty-eight,
  for retro ruling.
- VPS SSH still Permission denied (publickey), about 194 hours
  into the outage; delivery blocked, commit left on local
  records/2026-11-20, no PR. This pass is partial.

## Repo-state note

- The main worktree sits on branch work/ops-execution-records
  with another job's in-flight state, so this delivery used the
  existing clean branch worktree
  lastwar-worktrees/ticker-0004-1120-records (verified clean at
  the branch tip 9e59f49dfd before reuse) and staged by explicit
  pathspec only: the record file, the day INDEX section, and
  the action-log entry. The tools/ to _tools_ compatibility
  symlink makes git status report tools/* as deleted in this
  worktree; that artifact was not touched and is not part of
  this delivery. The token lease was created and removed in the
  main worktree; no residue.

## Time note

- The reset-day boundary is 02:00Z: the sweep windows end
  02:00Z and the VIP unit expires 02:00Z. In winter (PST,
  UTC-8) that is 18:00 PT; the repo's standing "19:00 PT
  reset" label is the PDT-era reading of the same 02:00Z
  instant. Times in this record use PST (UTC-8) unless marked
  Z. The integrator batch points (19:00, 23:00, 03:00, 07:00,
  11:00, 15:00 local) are a separate local-time schedule and
  are unaffected.
