---
title: Scout queue run 0704
created: 2026-11-14T15:22:05Z
modified: 2026-11-14T15:22:05Z
version: 1.0.0
description: Queue unit 012, chain scout-2026-11-10 - no surfaces walked, Mac mini still offline (node_offline, no wake-up path, last seen 2026-11-12T17:52:28Z), unit failed, successor enqueued
status: verified
grounded_in:
  - source: device channel reads on Zhen's Mac mini, 2026-11-14 07:12-07:22 PT
---

# Scout — queue run 0704 (unit 012, chain scout-2026-11-10)

- Unit: `scout-scout-2026-11-10-012`, chain `scout-2026-11-10` seq 12
- Executor: ticker-0704; token acquired about 07:19 PT (until 15:34:43Z), claimed 07:20 PT; finished about 07:20 PT
- Session: no computer session could start — the Mac mini reports offline
- Status: failed — execution impossible; no surfaces walked, no observations, no claims, tracker untouched, successor 013 enqueued
- New evidence for Issue #689 (tooling): the failure mode is still the whole device being offline, not the outcome_unknown input-path lock. `computer.session` fails with `node_offline` ("device is offline and does not advertise a wake-up path"), and the recovery channel (`connection.repair` on the Mac mini connection-recovery device) times out after 25s. The Mac mini last_seen is still 2026-11-12T17:52:28Z (09:52 PT), about 45 hours before this pass. No game state could be verified at all. Unlike units 006-008 of the scout chain, this is not the control-lock failure, and `_queue_/blockers/` is empty — so no blocker_overlay is recorded and the next tick probes again.

## Own PRs first

- Records PR 708 (2026-11-12) still OPEN, owner lastwar-pr-integrator, not this job. Re-verified open via the GitHub connector `list_pull_requests` at about 07:16 PT; the comment-level re-read was unavailable in this pass (the MCP server does not currently advertise `get_pull_request` / `get_pull_request_status`), and the last verified comment state was "no comments, mergeable clean" by ticker-0445 at about 04:53 PT. No questions addressed to this job.
- Knowledge PR 711 is owned by the knowledge organizer, tools PR 425 by lastwar-tool-developer; neither names this job. No action for this job.
- No open PR exists for records/2026-11-14 yet. This pass cannot open one: the push route is down (VPS SSH) and no gh login is available locally. The pass is partial on delivery; its commit stays on the local records/2026-11-14 branch.

## Sync and seed

- `queue.py sync`: reaped 0, expired 6, produced none (due 22, already queued 22 regulars). Roster warning stands: the live pool holds units for building-queues, research and zombie-invasion, regulars missing from the loaded roster (Issue #198). The sync also warned that the fetch of records/2026-11-14 failed (no remote ref yet — the branch exists only locally until the VPS route is restored), so branch reconcile was skipped (Issue #446).
- Zombie seeding: not needed — zombie unit 033 already sits in inbox (chain zombie-2026-11-10). The Zombie Invasion event (Glacieradon) was verified live by ticker-0004 at about 00:04 PT with 1 day 17:37 left, so it should still be available; whether it is still live cannot be verified without the Mac, and the zombie unit stays queued for a later tick to probe.

## What this unit was to do

One scout chain unit per the perception design: walk the game interface surfaces in its group, record what is actually available to do in the day observation file, and never claim, fight, dispatch or buy. The work it finds belongs to the owning regular's own unit.

## Entry state

- No entry state could be read: the device is offline, so no base screen, HUD, red-dot badge, or event tab was observed in this unit. Nothing is claimed from memory — the last verified live game read in this chain was ticker-0004's zombie unit 023 at about 00:04 PT (event live, Glacieradon 1 day 17:37 left). No "active on a different device" dialog, no login demand, no access error of the "lacks owner-authorized device access" kind — the owner authorization is not in question. This is a transport/offline failure, not a permission failure.

## The failure — device offline (Issue #689)

- Recovery attempts, all failed (4, above the standing minimum of 3):
  1. `connection.health` on Zhen's Mac mini — `node_offline`, device offline with no wake-up path.
  2. `environment.describe` on Zhen's Mac mini — `node_offline` again.
  3. `connection.repair` (target native) on the Mac mini connection-recovery device — invoke timed out after 25s.
  4. `computer.session` start on Zhen's Mac mini, after claiming the unit — `node_offline` again.
- This is the fifth consecutive scout-chain unit to fail on access in the same way (007, 008, 009, 010, 011, 012 — the chain has not walked a surface since the Mac went offline), and the third consecutive ticker pass today to record the Mac offline (ticker-0445 scout 011, ticker-0604 zombie 032, this pass). What clears it is still unknown: the Mac must come back online (user action at the machine, or the Muse daemon there restarting) — no detached pass can provide that, and the recovery channel times out, so even the repair path cannot be verified remotely.
- The pass stopped after this unit rather than cascading failed units (precedent: ticker-0445, ticker-0504, ticker-0604). The other 24 due regulars stay queued for later ticks.

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
- costs: about 8 minutes probing, no stamina or items
- verified: no
- blocker_category: f
- blocker: Mac mini offline (node_offline, last_seen 2026-11-12T17:52:28Z); recovery channel timeout; 4 recovery attempts failed
- follow_up: successor scout-scout-2026-11-10-013 enqueued (chain scout-2026-11-10); next tick probes again - see Issue #689

## Delivery (appended after the push attempt)

- Push attempted about 07:24 PT: bundle ticker-0704-1114-records.bundle created (about 14.3 MB, verified); scp to centos@66.179.249.233 failed Permission denied (publickey) — the VPS SSH outage since 2026-11-12 about 12:46 PT persists. No PR opened (no gh login available locally, VPS gh unreachable). The pass is partial on delivery; the commit waits for the VPS route to be restored. No force push used.

## Correction (appended 07:27 PT, verified against _queue_/done)

- The failure paragraph above miscounts the scout-chain streak: unit 012 is the SIXTH consecutive failed unit in chain scout-2026-11-10 (007-012), not the fifth, and only the last four (009, 010, 011, 012) failed on node_offline. Units 007 (finished 2026-11-12T13:11:10Z) and 008 (2026-11-12T15:43:15Z) failed on the outcome_unknown control lock (Issue #689), a different failure mode. The "third consecutive ticker pass today" count (0445, 0604, 0704) stands. "The other 24 due regulars" should read "the other 24 due units".
