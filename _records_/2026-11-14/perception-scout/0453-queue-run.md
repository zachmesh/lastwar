---
title: Perception Scout queue run 0453
created: 2026-11-14T12:57:03Z
modified: 2026-11-14T12:57:03Z
version: 1.0.0
description: Queue unit 011, chain scout-2026-11-10 - alliance remainder not walked, Mac mini still offline (node_offline, no wake-up path, last seen 2026-11-12T17:52:28Z), unit failed, successor enqueued
status: verified
grounded_in:
  - source: device channel reads on Zhen's Mac mini, 2026-11-14 04:45-04:53 PT
---

# Perception Scout — queue run 0453 (unit 011, chain scout-2026-11-10)

- Unit: `scout-scout-2026-11-10-011`, chain `scout-2026-11-10` seq 11
- Executor: ticker-0445; token acquired about 04:46 PT (until 13:06:32Z), claimed 04:46 PT; finished about 04:53 PT
- Session: no computer session could start — the Mac mini reports offline
- Status: failed — execution impossible; no surfaces walked, tracker untouched, successor 012 enqueued
- New evidence for Issue #689 (tooling): the failure mode is still the whole device being offline, not the outcome_unknown input-path lock. `computer.session` fails with `node_offline` ("device is offline and does not advertise a wake-up path"), `connection.health` on the Mac fails the same way, and the recovery channel (`connection.health` and `connection.repair` on the Mac mini connection-recovery device) times out after 25s. The Mac mini last_seen is still 2026-11-12T17:52:28Z (09:52 PT), about 43 hours before this pass. No game state could be verified at all. Unlike units 006-008, this is not the control-lock failure, and unlike unit 009 there is no control-lock blocker standing anymore (`_queue_/blockers/` is empty, the blocker aged out 2026-11-12 16:08 PT) — so no blocker_overlay is recorded and the next tick probes again.

## Own PRs first

- Records PR 708 (2026-11-12) OPEN, no comments, mergeable clean. Verified through the public GitHub API (VPS gh is unreachable — SSH down — and local gh is not logged in, so the check was read-only over HTTPS, not the VPS route). No questions addressed to this job.
- Knowledge PR 711 is owned by the knowledge organizer, tools PR 425 by lastwar-tool-developer; neither names this job. No action for this job.
- No open PR exists for records/2026-11-14 yet. This pass cannot open one: the push route is down (VPS SSH) and no gh login is available locally. The pass is partial on delivery; its commit stays on the local records/2026-11-14 branch.

## Sync and seed

- `queue.py sync`: reaped 0, expired 0, produced none (due 22, already queued 22 regulars). Roster warning stands: the live pool holds units for building-queues, research and zombie-invasion, regulars missing from the loaded roster (Issue #198). The sync also warned that the fetch of records/2026-11-14 failed (no remote ref yet — the branch exists only locally until the VPS route is restored), so branch reconcile was skipped (Issue #446).
- Zombie seeding: not needed — a zombie-invasion unit already sits in inbox (chain zombie-2026-11-10, unit 032). The Zombie Invasion event was expected to run to about 2026-11-13; whether it is still live cannot be verified without the Mac, and the zombie unit stays queued for a later tick to probe.

## Tool-version note (Issue #694)

- This pass ran `sync`, `token-acquire`, `next`, `claim` and (below) `complete` through the main working tree's `tools/queue.py`, which predates PR #692 (md5 82ee98fe275bf57aabf8415328a63309, byte-identical to `_tools_/queue.py`). PR #692 has since merged, but this checkout has not picked it up; Issue #694 stays open.
- The stale-tool handout risk does not affect this pass's decision: `_queue_/blockers/` is empty, no control-lock blocker stands, and the `next` handout (scout-011) is the due unit by earliest-expiry/priority order either way. The failure here is node_offline at the device, not a handout the current tool would have refused.

## What this unit was to do

The alliance remainder of pass scout-2026-11-10, per unit 005's follow-up and units 006, 007, 008, 009 and 010's records: Alliance Wars page, Alliance Store state, station and train panel, Mail six categories, world map pins and loot box. Unit 005 (ticker-2333) had walked the Alliance panel, Gifts both tabs, Help and Techs both tabs, leaving 5 surfaces unwalked and 2 red dots unexplained (Alliance Wars, Alliance Store).

## Entry state

- No entry state could be read: the device is offline, so no base screen, power, or HUD figure was observed in this unit. Nothing is claimed from memory — the last verified live game read was unit 027's base screen at about 09:55 PT on 2026-11-12 (power 149,218,973 per unit 008's record; the game was live then). No "active on a different device" dialog, no login demand, no access error of the "lacks owner-authorized device access" kind — the owner authorization is not in question. This is a transport/offline failure, not a permission failure.

## The failure — device offline (Issue #689)

- Recovery attempts, all failed:
  1. `computer.session` start on Zhen's Mac mini — `node_offline`, device offline with no wake-up path.
  2. `connection.health` on Zhen's Mac mini — `node_offline` again.
  3. `connection.health` on the Mac mini connection-recovery device — invoke timed out after 25s.
  4. `connection.repair` (target native) on the same recovery device — invoke timed out after 25s.
- This is the sixth consecutive scout-chain unit to fail on access (006, 007, 008 on the outcome_unknown lock; 009, 010, 011 on node_offline) and the Mac has now been unreachable for about 43 hours. What clears it is still unknown: the Mac must come back online (user action at the machine, or the Muse daemon there restarting) — no detached pass can provide that, and the recovery channel times out, so even the repair path cannot be verified remotely.
- The pass stopped after this unit rather than cascading failed units (precedent: ticker-0504, ticker-1200, ticker-1933). The other 21 due regulars stay queued for later ticks.

## Result stats

- surfaces_walked: 0
- items_observed: 0
- red_dots_seen: 0
- red_dots_explained: 0
- unexplained_red_dots: 0
- unknown_items: 0
- target: walk the alliance remainder of pass scout-2026-11-10, observe-only
- achieved: no surfaces walked; device offline before first input
- resources_gained: none (observe-only)
- costs: about 9 minutes, no stamina or items
- verified: no
- blocker_category: f
- blocker: Mac mini offline (node_offline, last_seen 2026-11-12T17:52:28Z); recovery channel timeouts; 4 recovery attempts failed
- follow_up: successor scout-scout-2026-11-10-012 enqueued (chain scout-2026-11-10); next tick probes again - see Issue #689

## Delivery (appended after the push attempt)

- Commit 64fce3046d as first created sits on the local
  records/2026-11-14 branch only; it was amended after this
  section was appended, so the branch tip is the amended commit.
- Push attempted about 05:00 PT: bundle
  ticker-0445-1114-records.bundle created (14.9 MB); scp to
  centos@66.179.249.233 failed Permission denied (publickey) —
  the VPS SSH outage since 2026-11-12 about 12:46 PT persists.
  `git ls-remote` over GitHub HTTPS confirms no
  records/2026-11-14 ref exists on the remote. No PR opened (no
  gh login available locally, VPS gh unreachable). The pass is
  partial on delivery; the commit waits for the VPS route to be
  restored. No force push used.
