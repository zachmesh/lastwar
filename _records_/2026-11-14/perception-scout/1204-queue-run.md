---
title: Scout queue run 1204
created: 2026-11-14T20:24:58Z
modified: 2026-11-14T20:24:58Z
version: 1.0.0
description: Queue unit 014, chain scout-2026-11-10 - no surfaces walked, Mac mini still offline (node_offline, no wake-up path, last seen 2026-11-12T17:52:28Z), unit failed, successor enqueued as 015
status: verified
grounded_in:
  - source: device channel reads on Zhen's Mac mini, 2026-11-14 12:21-12:24 PT
---

# Scout — queue run 1204 (unit 014, chain scout-2026-11-10)

- Unit: `scout-scout-2026-11-10-014`, chain `scout-2026-11-10` seq 14
- Executor: ticker-1204; token acquired 12:20:58 PT (until 12:35:58 PT), claimed 12:20:58 PT (lease to 12:40:58 PT); finished 12:25:47 PT (289 s)
- Session: no computer session could start — the Mac mini reports offline
- Status: failed — execution impossible; no surfaces walked, no observations, no claims, tracker untouched, successor 015 enqueued
- New evidence for Issue #689 (tooling): the failure mode is still the whole device being offline, not the outcome_unknown input-path lock. `computer.session` fails with `node_offline` ("device is offline and does not advertise a wake-up path"), and the recovery channel (`connection.repair` on the Mac mini connection-recovery device) times out after 25s. The Mac mini last_seen is still 2026-11-12T17:52:28Z (12:24 PT), about 42.5 hours before this pass. No game state could be verified at all. No "active on a different device" dialog, no login demand, no access error of the "lacks owner-authorized device access" kind — the owner authorization is not in question. This is a transport/offline failure, not a permission failure.

## Own PRs first

- Open PRs re-checked read-only via the public GitHub API (VPS gh route down, no local gh login): #711 knowledge (head e3c3dfd0, updated 2026-11-12T20:04:57Z), #708 records 2026-11-12 (head 2f59c270, 0 comments), #425 tools (head 4f41cdd6). Heads unchanged since the 1100 pass.
- Newest comment on #711 is still 2026-11-12T19:55:59Z (zachmesh); #708 has no comments; #425 newest shown is 2026-11-08. None is owned by this job and nothing is addressed to it.
- No records/2026-11-14 PR exists yet. This pass cannot open one: the push route is down (VPS SSH, see Delivery) and no gh login is available locally. The pass is partial on delivery; its commit stays on the local records/2026-11-14 branch.

## Sync and seed

- `queue.py sync`: reaped 0, expired 0, produced none (due 22, already queued 22 regulars). Pool after sync: inbox 101, claimed 0, done 1963.
- Roster warning stands: the live pool holds units for building-queues, research and zombie-invasion, regulars missing from the loaded roster (Issue #198). The sync also warned that the fetch of records/2026-11-14 failed (no remote ref yet — the branch exists only locally until the VPS route is restored), so branch reconcile was skipped (Issue #446).
- Zombie seeding: not needed — zombie-invasion-zombie-2026-11-10-035 already sits in inbox (successor enqueued by the 1100 pass). The Zombie Invasion event (Glacieradon) was verified live by ticker-0004 at about 00:04 PT with 1 day 17:37 left, so it should still be available; whether it is still live cannot be verified without the Mac, and the zombie units stay queued for a later tick to probe.

## What this unit was to do

One scout chain unit per the perception design: walk the game interface surfaces in its group, record what is actually available to do in the day observation file, and never claim, fight, dispatch or buy. The work it finds belongs to the owning regular's own unit.

## Entry state

- No entry state could be read: the device is offline, so no base screen, HUD, red-dot badge, or event tab was observed in this unit. Nothing is claimed from memory — the last verified live game read in this chain was ticker-0004's zombie unit 023 at about 00:04 PT (event live, Glacieradon 1 day 17:37 left).

## The failure — device offline (Issue #689)

- Recovery attempts, all failed (4, above the standing minimum of 3):
  1. `computer.session` start on Zhen's Mac mini — `node_offline`, device offline with no wake-up path.
  2. `computer.session` start again (reopen and retry) — `node_offline` again.
  3. `connection.health` on Zhen's Mac mini — `node_offline`.
  4. `connection.repair` (target native) on the Mac mini connection-recovery device — invoke timed out after 25s.
- This is the eighth consecutive scout-chain unit to fail (007-014); the last six (009-014) failed on node_offline, while 007 and 008 failed on the outcome_unknown control lock (Issue #689). It is the seventh consecutive ticker pass today to record the Mac offline (ticker-0445 scout 011, ticker-0604 zombie 032, ticker-0704 scout 012, ticker-0804 zombie 033, ticker-0934 scout 013, ticker-1100 zombie 034, this pass). What clears it is still unknown: the Mac must come back online (user action at the machine, or the Muse daemon there restarting) — no detached pass can provide that, and the recovery channel times out, so even the repair path cannot be verified remotely.
- The pass stopped after this unit rather than cascading failed units (precedent: ticker-0445, ticker-0504, ticker-0604, ticker-0704, ticker-0804, ticker-0934, ticker-1100). The other due units stay queued for later ticks.

## Result stats

- surfaces_walked: 0
- items_observed: 0
- red_dots_seen: 0
- red_dots_explained: 0
- unexplained_red_dots: 0
- unknown_items: 0
- target: walk scout surfaces and record observations
- achieved: no surfaces walked; device transport down before first input
- resources_gained: none
- costs: about 5 minutes probing (289 s measured), no stamina or items
- verified: no
- blocker_category: f
- blocker: Mac mini offline (node_offline, last_seen 2026-11-12T17:52:28Z); recovery channel timeout; 4 recovery attempts failed
- follow_up: successor scout-scout-2026-11-10-015 enqueued (chain scout-2026-11-10); next tick probes again - see Issue #689

## Batch note

PR #708 is still open, so the 11:00 PT batch point on 2026-11-14 is the 12th consecutive missed batch (11-12: 3, 11-13: 6, 11-14: 03:00, 07:00, 11:00). The next batch point is 15:00 PT.

## Delivery (appended after the push attempt)

- Push attempted: none — VPS SSH was verified Permission denied (publickey) at the start of this pass (~12:17 PT), so the bundle push route is down and no PR for records/2026-11-14 can be opened. No bundle created (precedent: ticker-1100). This record, the completed unit file and the successor unit are committed on the local records/2026-11-14 branch only; push and PR are owed once the VPS route recovers. A second delivery blocker stands: the Muse GitHub App has no write permission on zachmesh/lastwar since the 2026-10-31 transfer (403 on issue, comment and push).
