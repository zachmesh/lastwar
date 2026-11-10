---
title: Research Queue
created: 2026-10-25T18:58:00Z
modified: 2026-11-10T04:50:04Z
level: L1
version: 1.2.0
description: Completing finished research and keeping research slots working, one activity folder for research knowledge
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-10-25
  - source: owner structure direction on activity folders, 2026-10-25
  - source: ticker-0736 scout-discovery execution record 2026-11-09 0744 queue run (done, research queue read live - Defense Training VIII completed and unpressed, no owning regular (Issue #513), Lv.1 Missile Mastery II 2d 02:29:17 left, flask centre (59,249); record commit 36992d92e on records/2026-11-09)
  - source: ticker-1934 research-queue execution record 2026-11-09 2031 queue run (done, Defense Training VIII completed via Complete, power +15,000 to 146,751,949, Missile Mastery II 1d 13:54:11 left; record commit 69d8e38ec on records/2026-11-09)
---


# Research queue

## What this activity is

Checking the research queue, completing finished research so its bonus
applies, and noting idle slots. This folder accumulates research
knowledge - slot count, completion flow and research directions.
Starting a new research is a direction decision, so idle slots are
reported for the owner choice unless a standing choice exists.
Executions are recorded in `_records_/<date>/research-queue/`, one file per execution.

## How it is done

- Open the research queue from the base screen queue icons.
- Ground the flask icon centre from a fresh crop - measured (59,249) on 2026-11-09; taps at the icon's left edge (x 44-47) misroute (Decoration Gallery, map pan, nothing). Never re-tap the left-edge x.
- Press Complete on any finished item and record the power change.

## What is known from 2026-10-25

- Two research slots exist. HP Boost 11 and Attack Boost 11 had finished
  and were completed, adding 30,000 power in total.
- Both slots were idle afterwards (2026-10-25 read) and no new research was started,
  pending the owner choice of direction.
- Correction, live read 2026-11-09 0744 (scout-discovery unit, ticker-0736): slot 1 holds "Research on Defense Training VIII completed" with a green Complete button, full bar, NOT pressed - a scout unit observes only, and the completion belongs to the owning regular's unit, and there is no owning regular (Issue #513, tooling). Slot 2 holds a Lv.1 Missile Mastery II upgrade in progress, Time Left 2d 02:29:17, progress bar about half full. Speed Up button present, NOT tapped. The 2026-10-25 idle-slots claim is superseded by this newest verified read. (2026-11-09 2031 update: the owning regular now exists and the completion is done - Defense Training VIII completed via Complete, power +15,000 to 146,751,949, slot 1 now Idle; Missile Mastery II 1d 13:54:11 left. The "sits uncompleted" state is superseded.)

## Open questions

- The research tree order that best serves this account, once the squads
  are recorded.
- There is no owning regular for the research queue (Issue #513, tooling): the finished Defense Training VIII sits uncompleted and its slot stays occupied until a regular exists to complete it. The completion is not pressed by a scout unit. (Added 2026-11-09 0744. 2026-11-09 2031 update: the owning regular now exists - sync produced research-2026-11-09-1803, which ran 20:25-20:28 and completed Defense Training VIII (+15,000 power); slot 1 is now Idle and its next direction is the owner's choice. Issue #513's gap is closed in substance; the ticker-1934 pass commented it.)

## What the 2026-11-09 0744 scout-discovery unit added - Defense Training VIII finished and uncompleted, Missile Mastery II 2d 02:29 left, flask centre grounded

- Unit scout-scout-discovery-2026-11-09-002 by ticker-0736, about 07:44 to 07:53 local, status done. Evidence in `_records_/2026-11-09/building-queue-1-of/0744-queue-run.md` (commit 36992d92e on records/2026-11-09). Read-only exploration of the building and research queue state; the building half is folded in building-queues 1.1.0.
- Entry-point grounding (R2 method note): the flask icon's hitbox centre is at normalized (59,249) - the icon is wider than its left edge suggests. Three taps at x 44-47 (the icon's left edge) misrouted: [44,284] opened the Decoration Gallery, [47,282] panned the map and selected Builder's Hut, [44,277] did nothing. A fresh crop of the left edge showed the flask centre at x 59; the tap there opened the Research Queue at once. Next unit: ground the icon centre from a fresh crop, never re-tap the left-edge x.
- Research queue, read live 07:51 PT: slot 1 "Research on Defense Training VIII completed", green Complete button, full bar, NOT pressed - a scout unit observes only, and the completion belongs to the owning regular's unit. There is no owning regular - filed as Issue #513 (tooling): "No owning regular for research-queue / building-queues: finished Defense Training VIII sits uncompleted". The Defense Training VIII Complete stays unpressed until that regular exists; the slot stays occupied until then. Slot 2: Lv.1 Missile Mastery II upgrade in progress, Time Left 2d 02:29:17, progress bar about half full. Speed Up button present, NOT tapped.
- Correction of the standing claim: the 2026-10-25 "both slots idle" claim is superseded by this live read (slot 1 completed-unpressed, slot 2 running). The old claim stands as dated history in the section above, not deleted.
- Incidental sighting, cross-noted in perception-scout 1.50.0: the mis-tap at [44,284] opened the Decoration Gallery (Overview tab), a new candidate signal appended to the day observation file - Collection Progress UR 18/39, SSR 7/19, SR 4/4; Total Decor Combat Power 6,160,413; bonuses Hero Attack +5494, Hero Defense +810, Hero HP +172515, March Size +2, Increase Damage to Monsters +1.62%, Construction Speed +15.00%, Secret Mobile Squad Dispatch +3. Nothing was tapped inside the gallery; closed with the blue back arrow at [156,952].
- Result stats: target learn-building-research-queue-state, achieved 1 (both panels read live), resources_gained none, costs about 13 minutes, no items spent, verified yes (same-unit live reads), blocker_category none.

## What the 2026-11-09 2031 unit added - Defense Training VIII completed, power +15,000 to 146,751,949, Missile Mastery II 1d 13:54 left, done

- Unit research-2026-11-09-1803 by ticker-1934, about 20:25 to 20:28 local, status done. The finished research is completed and its bonus applied; the running research is recorded live; no new research started. Evidence in `_records_/2026-11-09/research-queue/2031-queue-run.md` (commit 69d8e38ec on records/2026-11-09). The owning regular now exists (Issue #513, tooling - sync produced this unit); the ticker-1934 pass commented Issue #513.
- Entry: flask icon centre at norm (59,249) opened the RESEARCH QUEUE panel on the first try (the left-edge x44-47 misroute from the 0744 unit was not repeated).
- Slot 1: "Research on Defense Training VIII completed." Full green bar, green Complete button. Slot 2: "Lv.1 Missile Mastery II upgrade in progress", Time Left 1d 13:54:36, progress bar about half full. Speed Up button present, NOT tapped. Power before the Complete tap: 146,736,949 (base HUD).
- Complete pressed once on Defense Training VIII (green button centre norm 743,457). Slot 1 now reads Idle with a blue Research button, which was NOT tapped - starting a new research is a direction decision and stays owner-only. Power after: 146,751,949, a gain of exactly +15,000, read live on the base HUD after closing the panel. The finished research's bonus is applied and the slot is free. Commented on Issue #482 by this run: the power fall levelled at 146,736,949 across four same-pass reads and now rises +15,000 on the research completion - the fall itself stays unexplained, the completion is one identified contributor to the recovery.
- Slot 2 unchanged: Missile Mastery II in progress, Time Left 1d 13:54:11 at the closing read (12h36m on from the 07:51 read of 2d 02:29:17, coherent with wall time).
- Computer session cc-340 dropped between units and cc-342 was started to recover, no game state lost. No different-device dialog, no login or verification demanded, no password or Touch ID step used. No diamonds or money spent, no speedup used, no stamina item opened, no building or research started. Small bubbles are already regrowing over the left-middle buildings; they belong to the next harvest unit by design.
- Result stats: target 1, achieved 1, resources_gained defense-training-viii-completed-power-15000, costs about 3 minutes, no items spent, verified yes (same-unit live reads), blocker_category none.
