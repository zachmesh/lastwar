---
title: Zombie Invasion queue run 0604
created: 2026-11-14T14:08:17Z
modified: 2026-11-14T14:08:17Z
version: 1.0.0
description: Queue unit 032, chain zombie-2026-11-10 - no attacks, Mac mini still offline (node_offline, no wake-up path, last seen 2026-11-12T17:52:28Z), unit failed, successor enqueued
status: verified
grounded_in:
  - source: device channel reads on Zhen's Mac mini, 2026-11-14 06:04-06:09 PT
---

# Zombie Invasion — queue run 0604 (unit 032, chain zombie-2026-11-10)

- Unit: `zombie-invasion-zombie-2026-11-10-032`, chain `zombie-2026-11-10` seq 32
- Executor: ticker-0604; token acquired about 06:04 PT (until 14:20:19Z), claimed 06:05 PT; finished about 06:08 PT
- Session: no computer session could start — the Mac mini reports offline
- Status: failed — execution impossible; no attacks, no kills, no claims, tracker untouched, successor 033 enqueued
- New evidence for Issue #689 (tooling): the failure mode is still the whole device being offline, not the outcome_unknown input-path lock. `computer.session` fails with `node_offline` ("device is offline and does not advertise a wake-up path"), and the recovery channel (`connection.repair` on the Mac mini connection-recovery device) times out after 25s. The Mac mini last_seen is still 2026-11-12T17:52:28Z (09:52 PT), about 44 hours before this pass. No game state could be verified at all. Unlike units 006-008 of the scout chain, this is not the control-lock failure, and `_queue_/blockers/` is empty — so no blocker_overlay is recorded and the next tick probes again.

## Own PRs first

- Records PR 708 (2026-11-12) still OPEN, owner lastwar-pr-integrator, not this job. Re-verified open via the GitHub connector `list_pull_requests` at about 06:04 PT; the comment-level re-read was unavailable in this pass (the MCP server does not currently advertise `get_pull_request` / `get_pull_request_status`), and the last verified comment state was "no comments, mergeable clean" by ticker-0445 at about 04:53 PT. No questions addressed to this job.
- Knowledge PR 711 is owned by the knowledge organizer, tools PR 425 by lastwar-tool-developer; neither names this job. No action for this job.
- No open PR exists for records/2026-11-14 yet. This pass cannot open one: the push route is down (VPS SSH) and no gh login is available locally. The pass is partial on delivery; its commit stays on the local records/2026-11-14 branch.

## Sync and seed

- `queue.py sync`: reaped 0, expired 8, produced none (due 22, already queued 22 regulars). Roster warning stands: the live pool holds units for building-queues, research and zombie-invasion, regulars missing from the loaded roster (Issue #198). The sync also warned that the fetch of records/2026-11-14 failed (no remote ref yet — the branch exists only locally until the VPS route is restored), so branch reconcile was skipped (Issue #446).
- Zombie seeding: not needed — zombie unit 032 already sat in inbox (chain zombie-2026-11-10). The Zombie Invasion event (Glacieradon) was verified live by ticker-0004 at about 00:04 PT with 1 day 17:37 left, so it should still be available; whether it is still live cannot be verified without the Mac, and the zombie unit stays queued for a later tick to probe.

## What this unit was to do

One chain round of Zombie Invasion per the activity metadata: dispatch squads in parallel (march queue cap 4), fight until the nearby zombies are cleared, refill stamina with the Free Claim and 10/50 stamina items from inventory, collect coins from the gift-box LOOT panel (Claim All, free only), execute the Coin Chests rule (open owned chests, redeem medals for Coin Chests in the event Store as authorized), and record zombies_killed, cleared, coin_before/after, coins_collected, medals_before/after, chests_opened and squads_parallel.

## Entry state

- No entry state could be read: the device is offline, so no base screen, power, HUD, coin panel, medal balance, or stamina figure was observed in this unit. Nothing is claimed from memory — the last verified live game read in this chain was ticker-0004's zombie unit 023 at about 00:04 PT (event live, Glacieradon 1 day 17:37 left, stamina refilled with 1x 50-stamina item). No "active on a different device" dialog, no login demand, no access error of the "lacks owner-authorized device access" kind — the owner authorization is not in question. This is a transport/offline failure, not a permission failure.

## The failure — device offline (Issue #689)

- Recovery attempts, all failed (3, the standing minimum):
  1. `computer.session` start on Zhen's Mac mini — `node_offline`, device offline with no wake-up path.
  2. `connection.repair` (target native) on the Mac mini connection-recovery device — invoke timed out after 25s.
  3. `computer.session` start on Zhen's Mac mini again — `node_offline` again.
- This is the fourth consecutive zombie-chain unit to fail on access in the same way (029, 030, 031, 032 — all node_offline since 2026-11-12T17:52:28Z), and the fourth consecutive ticker pass to record the Mac offline (ticker-0445 scout 011, ticker-0504 scout 007, this pass). What clears it is still unknown: the Mac must come back online (user action at the machine, or the Muse daemon there restarting) — no detached pass can provide that, and the recovery channel times out, so even the repair path cannot be verified remotely.
- The pass stopped after this unit rather than cascading failed units (precedent: ticker-0445, ticker-0504). The other 21 due regulars stay queued for later ticks.

## Result stats

- zombies_killed: 0
- cleared: false
- coin_before: unread
- coin_after: unread
- coins_collected: 0
- medals_before: unread
- medals_after: unread
- chests_opened: 0
- squads_parallel: 0
- target: clear nearby zombies in one chain round
- achieved: no attacks; device transport down before first input
- resources_gained: none
- costs: about 5 minutes probe, no stamina or items
- verified: no
- blocker_category: f
- blocker: Mac mini offline (node_offline, last_seen 2026-11-12T17:52:28Z); recovery channel timeout; 3 recovery attempts failed
- follow_up: successor zombie-invasion-zombie-2026-11-10-033 enqueued (chain zombie-2026-11-10); next tick probes again - see Issue #689

## Delivery (appended after the push attempt)

- Push attempted about 06:11 PT: bundle ticker-0604-1114-records.bundle created (14.9 MB, verified); scp to centos@66.179.249.233 failed Permission denied (publickey) — the VPS SSH outage since 2026-11-12 about 12:46 PT persists. No PR opened (no gh login available locally, VPS gh unreachable). The pass is partial on delivery; the commit waits for the VPS route to be restored. No force push used.
