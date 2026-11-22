---
title: Queue run 1600 - zombie-invasion unit 036 access failed
created: 2026-11-15T00:00:00Z
executor: ticker-1534
unit: zombie-invasion-zombie-2026-11-10-036
status: failed
---

# Queue run 1600 - zombie-invasion unit 036 (failed, Mac mini offline)

- Session window: 15:34-16:00 PT, 2026-11-14. Executor ticker-1534.
- Unit: zombie-invasion-zombie-2026-11-10-036, chain zombie-2026-11-10, seq 36,
  priority 4, est 12 minutes. Claimed 15:58 PT, lease to 16:18 PT.
- Result: failed. No game state was observable, no input was sent, no
  attacks, no kills, no claims. Blocker category f (missing precondition -
  device transport down).

## Device access - 4 attempts, all failed

Mac mini (device 1c817413-83e2-0545-cb90-36d5e096a6bd, Zhen's Mac mini)
is offline, last seen 2026-11-12T17:52:28Z - about 54 hours before this
pass. No wake-up path is advertised.

1. connection.health - node_offline.
2. environment.describe - node_offline.
3. connection.repair (target web) - node_offline.
4. computer.session start - node_offline.

This is the same failure mode as the previous zombie units in this
chain (028-035) and the same outage that has blocked all game
execution since 2026-11-12 12:08 PT. It is NOT the outcome_unknown
control-lock (Issue 689): the device reports offline, not a stuck
session. No blocker_overlay is recorded; the next tick probes again.
This is the 9th consecutive zombie-chain node_offline failure
(028-036) and the 10th ticker pass today to record the Mac offline
(0445, 0604, 0704, 0804, 0934, 1100, 1204, 1328, 1439, 1534), the
25th device-offline occurrence recorded by this queue (23rd at the
1328 pass, plus 1439 and this pass).

## Pass context

- Own PRs first: fresh read-only check via the public GitHub API at
  about 15:56 PT - three open PRs, unchanged since the 1500
  integrator pass: #711 knowledge (head e3c3dfd0), #708 records
  2026-11-12 (head 2f59c270, 0 comments), #425 tools (head
  4f41cdd6). None is owned by this job and nothing is addressed to
  it. No records/2026-11-14 PR exists yet.
- Sync: reaped 0, expired 5, due 24, produced 0 (all already queued).
  Completion markers reaped: scout-scout-2026-11-10-013,
  scout-scout-2026-11-10-015. The sync ran against the live pool
  (linked-worktree note, issue #705). Zombie seeding: no-op - unit
  036 was already in inbox.
- Branch reconcile warning persists (records/2026-11-14 has no remote
  ref; issue #446). Roster stale warning persists (zombie-invasion;
  issue #198).

## Chain continuation

Successor unit 037 in chain zombie-2026-11-10 is enqueued to start
now (cleared false - no zombies were observed, because no game state
was observable). The chain rule requires a successor after every
completed zombie unit.

Enqueue repair, same pass: the first `enqueue` minted 036 again
instead of 037, because `chain_seq_next` reads only the live
pool's inbox/claimed/done and this pass's completion of 036 had
landed in the worktree done plus a marker in live `completed/`,
not in live done (prior passes' completions sit in live done at
completion time - 015 at 14:43:48, 035 at 13:34:18). The duplicate
036 inbox file was dropped by the completion-marker mechanism
(first mint) and removed by hand (second mint); the completed
036 unit file was copied into live done, after which `enqueue`
derived 037 correctly. The worktree-vs-live completion landing
is a tooling gap to file as an Issue once the filing routes
recover (VPS gh and the GitHub App 403 both block it this pass).

## Batch note

PR #708 is still open, so the 15:00 PT batch point on 2026-11-14 is
the 13th consecutive missed batch (11-12: 3, 11-13: 6, 11-14 03:00,
07:00, 11:00 and 15:00). The 19:00 PT batch point falls after this
pass and cannot merge either while the delivery route is down.

## Delivery

VPS SSH still Permission denied (publickey), verified this pass -
the bundle push route is down and no PR for records/2026-11-14 can
be opened. This record, the completed unit file and the successor
unit are committed on the local records/2026-11-14 branch only;
push and PR are owed once the VPS route recovers. A second delivery
blocker stands: the Muse GitHub App has no write permission on
zachmesh/lastwar since the 2026-10-31 transfer (403 on issue,
comment and push).
