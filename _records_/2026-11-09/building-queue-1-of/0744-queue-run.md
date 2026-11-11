---
title: Building queue 1 of 4 and research 1 of 2 exploration
created: 2026-11-09T15:54:00Z
modified: 2026-11-09T15:54:00Z
version: 1.0.0
description: Scout discovery exploration of the building and research queue state - read-only learning
status: done
grounded_in:
  - source: live game screens on the owner Mac mini, 2026-11-09 07:44-07:53 PT
---

# Building queue 1 of 4 and research 1 of 2 - 0744 queue run

Unit scout-scout-discovery-2026-11-09-002, executor ticker-0736.
Session cc-237, LastWar window 489932, no device dialog, no
contention, no login demand.

## What was learned

### Building queue (read live 07:46 PT)

Opened from the base screen hammer icon (tap [44,195] worked).

- Slot 1: Lv.29 Aircraft Center upgrade in progress, Time Left
  2d 18:40:11, progress bar about two thirds full. Speed Up button
  present, NOT tapped (speedups are a red line).
- Slots 2, 3, 4: Idle, Construct button each, NOT tapped (never
  start buildings on own initiative - owner-only).
- Header text: "Commander, manage your Building Queues here.
  Enhance development speed by hiring more queues or accelerating
  building." The cost of hiring an extra queue was NOT read (it
  would need opening a priced hire control - learn-only, left
  untested).

Open question, not a conclusion: the 2026-10-25 knowledge read this
same upgrade at 19d 18h left; 15 days later the arithmetic expects
about 4d 18h left, but the live read is 2d 18:40. About 2.5 days
are unaccounted - possibly speedups applied by the owner at some
point, or the earlier read captured a different state. The live
figure stands; the gap is flagged, not resolved.

### Research queue (read live 07:51 PT)

Opened from the base screen flask icon - see the grounding note
below; the working tap is the icon centre [59,249].

- Slot 1: "Research on Defense Training VIII completed." Green
  Complete button, full bar. NOT pressed: a scout unit observes
  only, and the completion belongs to the owning regular's unit.
  There is no owning regular - see Issue #513.
- Slot 2: Lv.1 Missile Mastery II upgrade in progress, Time Left
  2d 02:29:17, progress bar about half full. Speed Up button
  present, NOT tapped.

### Entry-point grounding (R2 method note)

The flask icon's hitbox centre is at normalized (59,249) - the
icon is wider than its left edge suggests. Three taps at x 44-47
(the icon's left edge) misrouted: [44,284] opened the Decoration
Gallery, [47,282] panned the map and selected Builder's Hut,
[44,277] did nothing. A fresh crop of the left edge showed the
flask centre at x 59; the tap there opened the Research Queue at
once. Next unit: ground the icon centre from a fresh crop, never
re-tap the left-edge x.

### Incidental sighting - Decoration Gallery

The mis-tap at [44,284] opened the Decoration Gallery (Overview
tab), which is NOT in today's observation file - a new candidate
signal, appended to the day observation file by this unit:

- Collection Progress: UR 18/39, SSR 7/19, SR 4/4.
- Total Decor Combat Power 6,160,413.
- Bonuses: Hero Attack +5494, Hero Defense +810, Hero HP
  +172515, March Size +2, Increase Damage to Monsters +1.62%,
  Construction Speed +15.00%, Secret Mobile Squad Dispatch +3.
- Nothing was tapped inside the gallery; closed with the blue
  back arrow at [156,952].

### Base HUD at entry (07:45 PT)

Food 542.1M, iron 866.8M, coin 44.2M, diamonds 6,077, hero EXP
13.22K, Total Power 149,217,331, stamina 120. Banner quest:
"Upgrade Builder's Hut to Lv.26 (0/1)" - owner-only, not started.

## Result

Done - the learning objective is met: both queue panels were read
live with exact values, entry points are grounded, and the
follow-up gap is filed. No diamonds or money spent, nothing
started, nothing sped up, nothing completed.

- Candidate verdict: the queue state itself is learned and is not
  a standalone task. The building side needs no regular action
  beyond owner decisions. The research side needs an owning
  regular to complete finished research: Issue #513 (tooling)
  filed - "No owning regular for research-queue /
  building-queues: finished Defense Training VIII sits
  uncompleted". The Defense Training VIII Complete stays
  unpressed until that regular exists; the slot stays occupied
  until then.
- Token note: the re-acquire at about 07:49 reported the token
  held until 07:57:33Z without renewing (known Issue #461). The
  session was ended at about 07:53, inside the token window; no
  game input ran after expiry.

## Stats

- target: learn-building-research-queue-state
- achieved: 1 (both panels read live)
- resources_gained: none
- costs: about 13 minutes, no items spent
- verified: yes (same-unit live reads)
- blocker_category: none
