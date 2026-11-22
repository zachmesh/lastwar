---
title: Queue ticker run failure - Mac mini offline, ninety-first consecutive occurrence
created: 2026-11-20T20:31:00Z
modified: 2026-11-20T20:32:00Z
version: 1.0.0
description: Queue ticker 2026-11-20 12:04 PT run failure, Mac mini offline, one harvest attempt burned by claim-before-probe
status: run-failure
grounded_in:
  - source: _records_/2026-11-20/queue-ticker/1104-queue-run.md read during the run (records/2026-11-20 branch, commit 26cb83cff8) - the newest ticker record
  - source: _records_/2026-11-20/INDEX.md tail read during the run (records/2026-11-20 branch through ticker-1104; main worktree through queue-planning-1140)
  - source: device.list and device.describe on 1c817413-83e2-0545-cb90-36d5e096a6bd, 2026-11-20T20:22-20:23Z
  - source: computer.session start, connection.health and computer.session start on the same device, 2026-11-20T20:23-20:26Z, all node_offline
  - source: tools/mac_capture_probe.py --evidence /tmp/lw-probe-1204.json, 2026-11-20T20:26Z
  - source: tools/queue.py sync, 2026-11-20T20:21Z
  - source: tools/queue.py stats --format json, 2026-11-20T20:21Z and 20:26Z
  - source: GitHub connector open-PR read on zachmesh/lastwar, 2026-11-20T20:22Z
  - source: VPS SSH probe, 2026-11-20T20:21Z
---

# Queue ticker 2026-11-20 12:04 to about 12:32 PT (ticker-1204) - FAILED

One unit claimed and completed failed; no screen entered, nothing
read or claimed in the game. The blocker is the ninety-first
consecutive failed ticker pass by recorded-slot chain arithmetic
(ticker-1104 at 11:04 PT Nov 20 was the ninetieth and left a
record; this pass is the next recorded slot, so the count advances
by this pass alone; the counting basis is retro-owned - chain
arithmetic here, process-failure-record basis elsewhere). This is
the THIRTEENTH device-offline occurrence: the Mac mini itself is
offline, not merely windowless.

Executor name is ticker-1204, matching the scheduled slot: the
schedule fired at 12:04 PT and this run started about 12:21 PT
(dependency_probe trigger).

Caveat on the count: slot 1134 left no record anywhere checked
(branch queue-ticker folder, branch INDEX, branch action-log
executor field, main-worktree INDEX and action-log executor
field, git log --all), so it is a NEW chain-gap candidate for
retro ruling. If that slot ran and failed, the true
consecutive-failed count is higher than 91 and the true
device-offline occurrence count higher than 13. The 91/13
figures are the recorded-slot figures only. (The two
ticker-1134 executor entries in the main-worktree action-log
are from 2026-11-10 and 2026-11-12, not today; the 13 branch
action-log hits for "ticker-1134" are other passes mentioning
it as pending.)

## Route - NOT honored, deviation owned

This pass repeated the ordering slip in the 0604, 0704, 0834,
0934 and 1104 forms: the sync ran before the newest
queue-ticker record was read (1104, branch-only, read after the
probe). Worse than 1104, this pass also claimed BEFORE probing:
following the body order literally (next, claim, then play), the
token was acquired, `next` returned harvest-2026-11-20-1003,
and the unit was claimed at 20:22:59Z before any device probe
ran. The 1104 precedent - probe before claim so no unit is
burned - was not followed, and the cost is real: one attempt
burned on the harvest unit, now closed failed (see Unit). The
deviation-watch of fully-honoring passes therefore stays at
THREE (0434, 1347, 1404). The next pass must probe BEFORE
token-acquire and claim, as 1104 already showed: the probe
costs one cheap call and the claim costs an attempt.

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
  Permission denied (publickey) at about 20:21Z, about 191
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
  ticker-1104 and earlier reads, so no new comment or review
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

## Probe - device offline, thirteenth occurrence

- Mac mini OFFLINE per device.list, last_seen
  2026-11-20T04:16:40Z (20:16:40 PST, about 16 hours stale at
  probe time). The "Zhen's Mac mini connection recovery" entry
  is frozen at 2026-11-20T04:17:05Z likewise.
- device.describe returned the command set and permissions
  (the metadata path still answers); connection_state offline
  in the same read.
- Attempt 1, computer.session start, attempt 2,
  connection.health, attempt 3, computer.session start,
  20:23Z to 20:26Z - node_offline every time: device is
  offline and does not advertise a wake-up path. Three
  attempts satisfy the retry-at-least-3 rule; no computer
  session can start against an offline device, so no window
  probe was possible. The game window state is unverifiable
  while the device channel is down.
- Probe classification: tools/mac_capture_probe.py v1.2.0 on
  the assembled evidence (/tmp/lw-probe-1204.json) returns
  DEVICE_OFFLINE, high confidence, stop_pass yes (exit 13).
  Same label as 1104 and the eleven device-offline passes
  before it. Recovery still stands as bringing the Mac mini
  back online first (power, wake, network); the Dock-icon step
  and the gateway restart both need the Mac reachable, and
  neither applies while the device is offline.

## Unit

- harvest-2026-11-20-1003 claimed at 20:22:59Z (lease to
  20:42:59Z) and completed FAILED at 20:26:31Z - Mac mini
  offline, no game input possible, nothing claimed. Result
  stats: target "harvest collection 1003 slot", achieved 0,
  resources_gained none, costs "1 claim attempt, device
  offline", verified no, blocker_category f (missing
  precondition). The completion marker suppresses re-picks of
  this unit file; the tracker was left untouched, so the next
  tick re-produces a fresh harvest unit from the tracker.
  Pool after completion: inbox 76, claimed 0, done 2651.
  vip-2026-11-19-1800 and vip-2026-11-20-1800 stay in inbox at
  attempts 0 of 3, expiring 2026-11-21T02:00:00Z and
  2026-11-22T02:00:00Z.
- Token acquired ticker-1204 until 20:37:28Z and released
  before pass end (token released by ticker-1204, 20:26Z).

## Standing counts

- No successful game unit since ticker-0214 gifts Nov 17
  02:14 PT (about 82.1 hours missed). The newest finished
  unit in the pool is now harvest-2026-11-20-1003, finished
  2026-11-20T20:26:31Z (this pass's failed completion).
- Seventh consecutive missed VIP day (the reset day ending at
  the 02:00Z boundary Nov 21, 18:00 PST Nov 20; the new reset
  day's VIP unit is in inbox, attempts 0, unexecuted).
- Tonight's pre-reset sweep pair (zero-sweep-2026-11-20-1630
  and -1730) is staged in the pool, not yet due; last night's
  pair expired unexecuted at 18:19:25 PT Nov 19, sixth missed
  sweep night, seventh if tonight also goes unexecuted.
- Missed batches stay 48 per pr-integration-1100 (the 11:00
  batch is due-but-unexecuted number 6; next point 15:00 PT
  Nov 20, not yet due at this pass's close).
- NEW chain-gap candidate ticker-1134 (no record anywhere
  checked); candidates now SIXTEEN, possible total
  twenty-five (KO-1132 counting basis: FIFTEEN /
  twenty-four before this pass). Confirmed gaps stay NINE.
- Contradiction with MEMORY.md (43 as of the 15:00 batch, 44
  after the 19:00 batch) carried as retro flag (i); the
  sweep-night count discrepancy carried as retro flag (k);
  neither adopted.
- Duel day 4 Train Heroes ended 18:00 PT Nov 19, unreachable.
- VPS SSH still Permission denied (publickey), about 191
  hours into the outage; delivery blocked, commit left on
  local records/2026-11-20, no PR. This pass is partial.

## Repo-state note

- The main worktree sits on branch work/ops-execution-records
  with another job's in-flight state, so this delivery used the
  existing clean branch worktree
  lastwar-worktrees/ticker-0004-1120-records (verified clean at
  the branch tip 26cb83cff8 before reuse) and staged by explicit
  pathspec only: the record file, the day INDEX section and the
  action-log entry. The tools/ to _tools_ compatibility symlink
  makes git status report tools/* as deleted in this worktree;
  that artifact was not touched and is not part of this delivery.
  The log_append.py append also repaired a pre-existing malformed
  line in the branch log: the 0434 and 0604 entries were
  concatenated on one line (no newline between them); the append
  split them, so the branch log now reads 1975 lines, all valid
  JSON per log_append.py check. No inbox unit file rides this delivery commit (the live-pool
  state stays in the working tree; the ticker's sync
  re-produces due units from the tracker in any case).

## Delivery

- Commit built in the existing branch worktree
  lastwar-worktrees/ticker-0004-1120-records on records/2026-11-20
  from the branch tip 26cb83cff8: run record, day INDEX.md
  section, action-log entry.
- Push via the standard bundle route was attempted after commit:
  the bundle (/tmp/ticker-1204-1120.bundle) was created from the
  commit, and the scp transfer to the VPS failed at about
  20:31:15Z (`Permission denied (publickey)`, connection closed)
  - the SSH outage persists. No retry was run: the failure is a
  deterministic transport outage, not a ticker-collision race,
  and the same failure was already verified at 20:21Z at run
  start and by the 2026-11-15, 2026-11-16, 2026-11-17,
  2026-11-18, 2026-11-19 and 2026-11-20 earlier runs. Per the
  body, no further retry: the commit is LEFT on the local
  records/2026-11-20 branch for the next pass or the integrator
  to pick up once VPS SSH is restored. No direct main push was
  made. No PR for records/2026-11-20 exists and none could be
  opened by this run (VPS gh route down; GitHub App without
  write permission).
- After the failed attempt this record was amended (the attempt
  timestamp and finished time, and a correction to the
  action-log entry timestamp, which was written 4 minutes ahead
  of the actual append time and is now set to the commit time
  20:30:55Z). The amendment lands as a follow-up commit, not
  an amend of e3727ecb93: the pr-integration 1230 run committed
  3923d70a0c on top of it while this pass was amending, sweeping
  in the INDEX section and the log-timestamp correction, so
  rewriting e3727ecb93 would rewrite history under a live
  commit. The bundle is recreated from the final commit.

## Time note

- The reset-day boundary is 02:00Z: the sweep windows end
  02:00Z and the VIP unit expires 02:00Z. In winter (PST,
  UTC-8) that is 18:00 PT; the repo's standing "19:00 PT
  reset" label is the PDT-era reading of the same 02:00Z
  instant. Times in this record use PST (UTC-8) unless marked
  Z. The integrator batch points (19:00, 23:00, 03:00, 07:00,
  11:00, 15:00 local) are a separate local-time schedule and
  are unaffected.
