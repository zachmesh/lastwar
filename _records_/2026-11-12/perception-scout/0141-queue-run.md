---
title: Perception Scout queue run 0141
created: 2026-11-12T09:44:00Z
modified: 2026-11-12T09:44:00Z
version: 1.0.0
description: Queue unit 006, chain scout-2026-11-10 - alliance remainder not walked, computer-control channel locked with outcome_unknown after a session drop, unit failed, successor enqueued
status: verified
grounded_in:
  - source: live game screens on Zhen's Mac mini, sessions cc-693 and cc-694, 2026-11-12 01:34-01:42 PT
---

# Perception Scout — queue run 0141 (unit 006, chain scout-2026-11-10)

- Unit: `scout-scout-2026-11-10-006`, chain `scout-2026-11-10` seq 6
- Executor: ticker-0134; token acquired about 01:34 PT (until 09:50:58Z), claimed 01:35 PT; finished about 01:42 PT
- Session: cc-693 dropped on the first input (connection_changed); restarted in place, then ended and restarted as cc-694 — all three recovery attempts failed with the same outcome_unknown lock (see below); no game state lost, no game input ever sent
- Status: failed — execution impossible; no surfaces walked, tracker untouched, successor 007 enqueued
- New failure mode filed as Issue #689 (tooling)

## Own PRs first

- Records PR 685 (2026-11-12) OPEN, mergeable CLEAN, no comments, no reviews; rides the 03:00 batch.
- Records PR 681 (2026-11-11, post-2300 batch) OPEN, mergeable CLEAN, no comments, no reviews; rides the 03:00 batch.
- Tools PR 425 is owned by lastwar-tool-developer, not this job. No question addressed to this job on any open PR.

## Sync and seed

- `queue.py sync`: reaped 0, expired 0, produced none (due 23, already queued 21 regulars); dropped the stale inbox copy of harvest-2026-11-11-2203, already closed on records/2026-11-12. Roster warning stands: the live pool holds units for building-queues, research and zombie-invasion, regulars missing from the loaded roster (Issue #198).
- Zombie seeding: not needed — units 024 and 025 already sit in inbox (chain zombie-2026-11-10, done 17, pending 2).

## What this unit was to do

The alliance remainder of pass scout-2026-11-10, per unit 005's follow-up: Alliance Wars page, Alliance Store state, station and train panel, Mail six categories, world map pins and loot box. Unit 005 (ticker-2333) had walked the Alliance panel, Gifts both tabs, Help and Techs both tabs, leaving 5 surfaces unwalked and 2 red dots unexplained (Alliance Wars, Alliance Store).

## Entry state (base HUD, read live)

- Session cc-693, Last War window 676414 selected (642x951 windowed, not fullscreen). Base screen read live about 01:37 PT: power 149,218,973; food 701.5M, iron 1.0G, coin 145.7M, diamonds 13.22K; stamina 64; task line "Build: Oil Well [0/1]".
- VS timer 16:22:33; Season II 1d 16:32:33; radar 3d 16:22:33; Events badge 3; cart top-right 6,717 with a red dot; Alliance and Mail buttons carry red dots; alliance banner reads "President HawksMav appointed ... as Secretary of Defense!".
- No "active on a different device" dialog, no login demand, no access error of the "lacks owner-authorized device access" kind — the owner authorization is not in question.

## The failure — control channel lock (new failure mode)

- The first input, a click on the Alliance button at (930,694), failed with `connection_changed`: "No active authorized computer session is available for evidence." The receipt reported `input_dispatched: false`, `side_effect: none` — nothing was sent, so nothing was replayed.
- Read-only inspection still worked after that (computer.observe and screen.snap returned the live base screen), but every input action afterwards failed with `outcome_unknown`: "An earlier action has an unresolved outcome. Stop sending input; read-only inspection is allowed. Report the uncertainty. A new local user submission is required before input can resume. The reconcile action cannot clear this state."
- Recovery attempts, all with the identical outcome_unknown:
  1. New computer.session (reused id cc-693), then activate Last War window 676414.
  2. Session ended explicitly, brand-new session cc-694, then activate.
  3. open_app LastWar (selection route instead of activate).
- A read-only snap at about 01:40 confirmed the game still live on the base screen (VS 16:21:32, clock running), so the game is healthy — only the control channel's input path is locked, and the lock survives fresh sessions. It can only be cleared by a local user submission on the Mac, which a detached 01:40 pass cannot provide.
- This is distinct from Issue #648 (Zoom to Fit breaking canvas taps): the window was windowed 642x951 throughout, and no zoom was ever used. Session drops themselves are a known recurring event (units 049, 053, 054, 057, 058, 021, 023 all recovered with a new session); this is the first time the lock persisted across fresh sessions.
- Filed as Issue #689 (tooling): needs a diagnosis of what holds the outcome_unknown state, whether it clears on its own after a timeout, and a remote restore path or a documented wait-and-retry rule.

## Result stats

- surfaces_walked: 0
- items_observed: 0
- red_dots_seen: 0
- red_dots_explained: 0
- unexplained_red_dots: 0
- unknown_items: 0
- target: walk the alliance remainder of pass scout-2026-11-10, observe-only
- achieved: no surfaces walked; control channel blocked before first input
- resources_gained: none (observe-only)
- costs: about 9 minutes, no stamina or items
- verified: no
- blocker_category: f
- blocker: computer-control outcome_unknown lock after session drop; channel requires a new local user submission; 3 recovery attempts failed
- follow_up: successor scout-scout-2026-11-10-007 enqueued (chain scout-2026-11-10); the next tick will hit the same wall unless the channel clears — see Issue #689
