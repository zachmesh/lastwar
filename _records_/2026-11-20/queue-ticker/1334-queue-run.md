---
title: Queue ticker run failure - Mac mini offline, ninety-second consecutive occurrence
created: 2026-11-20T21:48:00Z
modified: 2026-11-20T21:49:00Z
version: 1.0.0
description: Queue ticker 2026-11-20 13:34 PT run failure, Mac mini offline, one radar attempt burned by claim-after-probe
status: run-failure
grounded_in:
  - source: _records_/2026-11-20/queue-ticker/1204-queue-run.md read during the run (records/2026-11-20 branch, commit e3727ecb93) - the newest ticker record
  - source: _records_/2026-11-20/INDEX.md tail read during the run (records/2026-11-20 branch through pr-integration-1330; main worktree through tool-development-1332)
  - source: device.list and device.describe on 1c817413-83e2-0545-cb90-36d5e096a6bd, 2026-11-20T21:39-21:40Z
  - source: computer.session start x3, connection.health, connection.repair on the same device, 2026-11-20T21:40-21:44Z, all node_offline
  - source: tools/mac_capture_probe.py --evidence /tmp/lw-probe-1334.json, 2026-11-20T21:44Z
  - source: tools/queue.py sync, 2026-11-20T21:38Z
  - source: tools/queue.py stats --format json, 2026-11-20T21:38Z
  - source: knowledge-organization-1332 run record (main worktree), GitHub REST open-PR read at about 21:32Z
  - source: VPS SSH probe, 2026-11-20T21:41Z
---

# Queue ticker 2026-11-20 13:34 to about 13:50 PT (ticker-1334) - FAILED

No unit completed, no screen entered, nothing read or claimed in
the game. The blocker is the ninety-second consecutive failed
ticker pass by recorded-slot chain arithmetic (ticker-1204 at
12:04 PT Nov 20 was the ninety-first and left a record; this
pass is the next recorded slot, so the count advances by this
pass alone; the counting basis is retro-owned - chain
arithmetic here, process-failure-record basis elsewhere). This
is the FOURTEENTH device-offline occurrence: the Mac mini
itself is offline, not merely windowless.

Executor name is ticker-1334, matching the scheduled slot: the
schedule fired at 13:34 PT and this run started about 13:37 PT
(dependency_probe trigger).

Caveat on the count: slots 1134 and 1234 left no record anywhere
checked (branch queue-ticker folder, branch INDEX, branch
action-log, main-worktree INDEX and action-log, git log --all),
so both stand as chain-gap candidates for retro ruling (1134
adopted by KO-1132, 1234 adopted by KO-1332). If either slot
ran and failed, the true consecutive-failed count is higher
than 92 and the true device-offline occurrence count higher
than 14. The 92/14 figures are the recorded-slot figures only.

## Route - PARTIALLY honored, deviation owned

This pass repeated the ordering slip in the 0604, 0704, 0834,
0934, 1104 and 1204 forms: the sync ran before the newest
queue-ticker record was read (1204, branch-only, read after
the probe). The material part was honored - the probe ran
before any token or claim, and the claim came after the probe
(unlike 1204's claim-before-probe). But the 1104 precedent
goes further and was NOT followed: never call `next` or claim
at all when the device is offline. This pass called `next`
(radar-2026-11-20-1003) and claimed it after the probe had
already settled the device as offline, and the claim burned
1 radar attempt (attempts now 1 of 3). The unit was released
back to inbox with queue.py release, still due, 2 attempts
left - so no game work was lost, only the attempt counter
moved. The deviation-watch of fully-honoring passes therefore
stays at THREE (0434, 1347, 1404). The next pass must stop
after the probe when the device is offline: no `next`, no
claim, no token.

## Sync and seeding

- Sync: due 22, produced 0, already_queued all 22 (mail, help,
  gifts, harvest, vip, passes, daily-missions, secrets, treasures,
  radar, survivors, trucks, train, training, donations, events,
  arms-race, star-ceremony, duel-score, scout, scout-midday),
  reaped 0, expired 0, completion_markers_reaped
  [harvest-2026-11-20-1003]. Pool after sync: inbox 76, claimed
  0, done 2651. Branch reconcile warning: fetch of
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
  Permission denied (publickey) at about 21:41Z, about 192.8
  hours into the outage. The VPS gh CLI check could not run.
- Fallback via the newest available read: the
  knowledge-organization-1332 pass read the open-PR list live
  via the unauthenticated GitHub REST API at about 21:32Z, five
  minutes before this run started - exactly three open PRs,
  all unchanged since 2026-11-12 - #711 knowledge fold (Owner
  lastwar-knowledge-organizer, head e3c3dfd0, updated
  2026-11-12T20:04:57Z), #708 records 2026-11-12 (Owner
  lastwar-pr-integrator, head 2f59c270, updated
  2026-11-12T20:44:37Z), #425 tools log gate (Owner
  lastwar-tool-developer, head 4f41cdd6, updated
  2026-11-12T19:29:37Z). No open PR exists for
  records/2026-11-20, none is owned by this job, and no new
  comment or review can have landed. No new question or
  numbered fix point is addressed to this job. No fresh
  connector read was spent re-proving a five-minute-old read.
- No new issue filed: the gh route is down. The window-loss
  failure-mode filing and the device-offline mode filing stay
  owed, for a pass with a working gh route.

## Probe - device offline, fourteenth occurrence

- Mac mini OFFLINE per device.list, last_seen
  2026-11-20T04:16:40Z (20:16:40 PST Nov 19, about 17.5 hours
  stale at probe time). The "Zhen's Mac mini connection
  recovery" entry is frozen at 2026-11-20T04:17:05Z likewise.
- device.describe returned the command set and permissions
  (the metadata path still answers); connection_state offline
  in the same read.
- Attempt 1, 2, 3, computer.session start, 21:40Z to 21:42Z -
  node_offline every time: device is offline and does not
  advertise a wake-up path. Attempt 4, connection.health, and
  attempt 5, connection.repair (target web), 21:44Z - node_offline
  likewise. Five attempts satisfy the retry-at-least-3 rule; no
  computer session can start against an offline device, so no
  window probe was possible. The game window state is
  unverifiable while the device channel is down.
- Probe classification: tools/mac_capture_probe.py v1.2.0 on
  the assembled evidence (/tmp/lw-probe-1334.json) returns
  DEVICE_OFFLINE, high confidence, stop_pass yes (exit 13).
  Same label as 1104 and 1204. Recovery still stands as
  bringing the Mac mini back online first (power, wake,
  network); the Dock-icon step and the gateway restart both
  need the Mac reachable, and neither applies while the device
  is offline.

## Unit

- radar-2026-11-20-1003 claimed after the probe at 21:45Z
  (priority 2, window duel day 5 - radar release, est 6 min,
  expires 2026-11-20T22:03:00Z) and released back to inbox at
  21:47Z with queue.py release. No game input was attempted
  against it, nothing claimed, no completion recorded; the
  unit stays due in inbox at attempts 1 of 3. Tracker
  untouched. The claim-then-release cost 1 attempt; the 1104
  form (no next, no claim) would have cost 0.
- The token was acquired after the probe (ticker-1334, until
  2026-11-20T21:56:32Z) and is released before pass end.

## Standing counts

- No game unit since ticker-0214 gifts Nov 17 02:14 PT
  (about 83.7 hours missed). The newest finished unit in the
  pool is harvest-2026-11-20-1003, finished 2026-11-20T20:26:31Z
  (the 1204 pass's failed completion, carried).
- Result status totals: done 479, partial 566, failed 212,
  skipped-needs-owner 16, expired 1378.
- Stalled priority-1 inbox units: vip-2026-11-19-1800 (30.6h),
  zero-sweep-2026-11-20-1630 (8.7h), vip-2026-11-20-1800 (7.6h),
  zero-sweep-2026-11-20-1730 (7.6h).
- Seventh consecutive missed VIP day (the reset day ending at
  the 02:00Z boundary Nov 21, 18:00 PST Nov 20; the new reset
  day's VIP unit is in inbox, attempts 0, unexecuted).
- Tonight's pre-reset sweep pair (zero-sweep-2026-11-20-1630
  and -1730) is staged in the pool, not yet due; last night's
  pair expired unexecuted at 18:19:25 PT Nov 19, sixth missed
  sweep night, seventh if tonight also goes unexecuted.
- Missed batches stay 48 per the adopted worker definition
  (pr-integration-1100/1230); next batch point 15:00 PT Nov 20.
- Chain-gap candidates stay SEVENTEEN, possible total
  twenty-six (per KO-1332, ticker-1234 adopted; ticker-1134
  already adopted by KO-1132).
- VPS SSH still Permission denied (publickey), about 192.8
  hours into the outage; delivery blocked, commit left on
  local records/2026-11-20, no PR. This pass is partial.

## Repo-state note

- The main worktree sits on branch work/ops-execution-records
  with another job's in-flight state, so this delivery used the
  existing clean branch worktree
  lastwar-worktrees/ticker-0004-1120-records (verified clean at
  the branch tip 67aeb6d7bf before reuse) and staged by explicit
  pathspec only: the record file, the day INDEX section and the
  action-log entry. The tools/ to _tools_ compatibility symlink
  makes git status report tools/* as deleted in this worktree;
  that artifact was not touched and is not part of this delivery.
- The radar claim and release changed only the main worktree's
  _queue_ pool files (inbox/claimed state, attempts 1 of 3);
  those changes stay uncommitted in the main worktree with the
  other passes' pool state, as in the 1104 and 1204 forms.

## Time note

- The reset-day boundary is 02:00Z: the sweep windows end
  02:00Z and the VIP unit expires 02:00Z. In winter (PST,
  UTC-8) that is 18:00 PT; the repo's standing "19:00 PT
  reset" label is the PDT-era reading of the same 02:00Z
  instant. Times in this record use PST (UTC-8) unless marked
  Z. The integrator batch points (19:00, 23:00, 03:00, 07:00,
  11:00, 15:00 local) are a separate local-time schedule and
  are unaffected.
