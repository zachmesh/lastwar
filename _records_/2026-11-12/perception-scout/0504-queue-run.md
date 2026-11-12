---
title: Perception Scout queue run 0504
created: 2026-11-12T13:15:00Z
modified: 2026-11-12T13:15:00Z
version: 1.0.0
description: Queue unit 007, chain scout-2026-11-10 - alliance remainder not walked, computer-control channel still locked with outcome_unknown, unit failed, successor enqueued
status: verified
grounded_in:
  - source: live game screens on Zhen's Mac mini, sessions cc-706 and cc-707, 2026-11-12 05:05-05:15 PT
---

# Perception Scout — queue run 0504 (unit 007, chain scout-2026-11-10)

- Unit: `scout-scout-2026-11-10-007`, chain `scout-2026-11-10` seq 7
- Executor: ticker-0504; token acquired about 05:05 PT (until 13:21:47Z), claimed 05:06 PT; finished about 05:15 PT
- Session: cc-706 started, then ended and restarted as cc-707 — all three recovery attempts failed with the same outcome_unknown lock as unit 006; no game state lost, no game input ever sent
- Status: failed — execution impossible; no surfaces walked, tracker untouched, successor 008 enqueued
- New evidence for Issue #689 (tooling): the lock does NOT clear on its own after about 3.5 hours, and survives fresh sessions started hours later

## Own PRs first

- Records PR 685 (2026-11-12) OPEN, mergeable CLEAN (head 3f6d579b6, verified by the integrator 0500 pass against main 2f46eea9a); awaits the 07:00 PT batch. No questions addressed to this job.
- Tools PR 425 is owned by lastwar-tool-developer, not this job; still owner-gated on OD-20261108-01. No action for this job.

## Sync and seed

- `queue.py sync`: reaped 0, expired 0, produced none (due 23, already queued 22 regulars). Roster warning stands: the live pool holds units for building-queues, research and zombie-invasion, regulars missing from the loaded roster (Issue #198).
- Zombie seeding: not needed — zombie-invasion-zombie-2026-11-10-026 already sits in inbox (chain zombie-2026-11-10, done 19, pending 1).

## What this unit was to do

The alliance remainder of pass scout-2026-11-10, per unit 005's follow-up and unit 006's record: Alliance Wars page, Alliance Store state, station and train panel, Mail six categories, world map pins and loot box. Unit 005 (ticker-2333) had walked the Alliance panel, Gifts both tabs, Help and Techs both tabs, leaving 5 surfaces unwalked and 2 red dots unexplained (Alliance Wars, Alliance Store).

## Entry state (base HUD, read live, read-only)

- Session cc-706, Last War window 676414 selected (642x951 windowed, not fullscreen). Base screen read live about 05:07 PT: power 149,218,973; task line "Build: Oil Well [0/1]"; VS timer about 1d 13h; Events badge 3; cart top-right 6,717 with a red dot; alliance banner text visible.
- A closing read-only observe at about 05:14 PT confirmed the game still live on the base screen (same power, HEROES and WORLD buttons visible), so the game is healthy — only the control channel's input path is locked.
- No "active on a different device" dialog, no login demand, no access error of the "lacks owner-authorized device access" kind — the owner authorization is not in question.

## The failure — control channel lock persists (Issue #689)

- The first input, activate on window 676414 in session cc-706, failed with `outcome_unknown`: "An earlier action has an unresolved outcome. Stop sending input; read-only inspection is allowed. Report the uncertainty. A new local user submission is required before input can resume. The reconcile action cannot clear this state." Action ID C78F5B9E-82E6-4E6F-A6D9-971969828AD1. `input_dispatched: false`, no retained evidence — nothing was sent, so nothing was replayed.
- Read-only inspection still worked throughout (computer.observe returned the live base screen twice).
- Recovery attempts, all with the identical outcome_unknown:
  1. Activate window 676414 in the fresh session cc-706.
  2. Session cc-706 ended explicitly, brand-new session cc-707, then activate window 676414 (action ID 885E4100-6766-4B53-B48F-98DEFDB53213).
  3. open_app LastWar in session cc-707 (action ID FF2CD74E-DA91-462D-BAC5-A8DB7972C9E9).
- This is the same lock unit 006 hit at 01:34-01:42 PT. It has now persisted about 3.5 hours and across sessions started hours apart, so the Issue #689 question "whether it clears on its own after a timeout" is answered in the negative for a 3.5-hour window. What clears it is still unknown: a local user submission on the Mac (per the error text) is the only stated path, and no detached pass can provide one.
- The pass stopped after this unit: with the input channel locked, every further unit in this pass would fail identically, so the loop was not continued into a cascade of failed units. The token is released and the pass ends here.

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
- costs: about 10 minutes, no stamina or items
- verified: no
- blocker_category: f
- blocker: computer-control outcome_unknown lock after session drop; channel requires a new local user submission; 3 recovery attempts failed; lock persists 3.5h+ since unit 006
- follow_up: successor scout-scout-2026-11-10-008 enqueued (chain scout-2026-11-10); the next tick will hit the same wall unless the channel clears or the owner submits locally — see Issue #689, commented this pass
