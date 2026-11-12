---
title: 1850 queue run
created: 2026-11-11T19:01:00-08:00
modified: 2026-11-11T19:01:00-08:00
level: L0
version: 1.0.0
description: perception-scout events-group queue run by ticker-1843, unit scout-scout-2026-11-10-001, partial
status: unverified
---

# 1850 queue run

Executor ticker-1843, unit scout-scout-2026-11-10-001, chain
scout-2026-11-10, session about 18:50 to 19:01 local, computer
session cc-657. Observe-only throughout; nothing claimed,
fought, dispatched, donated, dug or bought. Status partial:
Events hub, Arms Race and Age of Oil walked live; VS/duel page,
Wanted Boss, Desert Battlefield and radar NOT walked - they go
to the chain successor (seq 002, enqueued by this unit).

## Duplicate-head origin of this unit

This unit was created by the 16:54 sync while the chain head
unit scout-2026-11-10-1800 was still executing (ticker-1634,
16:48 to 17:00). The sync saw scout still due in the tracker -
the 1634 unit did not mark the tracker done - and produced a
second chain head with an empty planned_for, so the
(regular, planned_for) invariant did not catch it. The base
group was already walked by ticker-1634, so this unit executed
as the events-group unit instead of re-walking base. The 1634
record said it enqueued an events successor; no seq 002 unit
exists in the pool, so this unit filled that role. Filed as a
tooling Issue #664 - sync must not produce a second
chain head while the first is claimed or done for the same
chain.

## Events hub, read live about 18:53 to 19:00 local

Tab strip, left to right as walked (dragged once to reveal the
left end): The Age of Oil (red badge 1), Arms Race, Desert
Battlefield, Zombie Invasion (selected at entry, red badge 1 /
exclamation), Wanted Boss. Whether further tabs sit left of
The Age of Oil is unverified - the strip was not dragged past
it. Top banner: "Unknown Warzone are on a secret Ghost Ops in
our Warzone! Send scouts!"

### Zombie Invasion - Glacieradon

- 1d 23:09:04 remaining at first read (1d 23:08:17 at second
  read). "Challenge begins in: 23:09:05". "Your Timezone:
  2026-11-12 18:00".
- 40/40 bar (top-right of the panel, meaning unverified).
- Store button carries a red dot (store not opened in this
  unit). Ranking and Rewards buttons present, not opened.
- Alliance Finding tab: four boss cards visible - Lv.80
  Zombie Boss 138km SAPPER1DOG 02:34:54; Lv.80 294km
  ANGEL777 Apex 02:36:13; Lv.85 208km SAPPER1DOG 02:39:49;
  Lv.80 212km SAPPER1DOG 02:40:08; a fifth card cut off at
  the right edge. My Findings tab not opened.
- "The next wave of Invading Zombies will arrive in
  00:03:41" at first read, 00:02:54 at second read.
- The event is LIVE with about 1d 23h left - the zombie chain
  continues; zombie-invasion unit 019 sits in inbox.

### Arms Race - Base Building

- Phase Base Building, Contest Segment Lv.29-30. Chest 0/2.
- Score 0 (star 0). 03:07:30 remaining in the phase at read.
- Tier rewards: 2,360 at 6,250 points; 4,800 at 12,500;
  11,800 at 30,000 (tier 3).
- Scoring paths: Increase Building Power by 1pt, +1; Use
  1-min Construction Speed-up, +10; Buy Packs containing
  Diamonds (1 Diamond), +30.
- Ranking row: #2103 [WINA]Zhie688 above; #2110
  [AP3x]Bears Lair, segment rank 8, score 0.
- Calendar button top-right, not opened.
- Flag for the arms-race unit: score 0 with 3h07m left and
  tier 3 at 30,000. Of the three paths, only Building Power
  +1 sits inside the red lines - the speed-up path burns
  speedup items and the diamond path is a purchase. The
  arms-race unit judges this phase under R4 from this read.

### The Age of Oil

- Stage track: stage 1 active with a red badge 1; stages 2,
  3, 4 locked. Play button top-right, not tapped.
- "Unlock Tech: The Age of Oil", 3d 23:06:56 remaining:
  "Complete a total of 500 Tech Research in this Warzone",
  9475/500 - exceeded, bar full.
- "Unlock Stage: Base Expansion II", 3d 23:06:56:
  "Complete a total of 500 Building Upgrades in this
  Warzone", 22232/500 - exceeded, bar full.
- Reward claim state unmeasured - the reward icons below
  each card were not scrolled to or tapped, so the stage-1
  badge 1 is NOT proven to be a claimable reward; the
  exceeded counters are only a candidate cause. Handed to
  the diff / event-claims unit.

## Base screen, read live at entry (about 18:51) and exit (about 19:01)

- Power 149,218,973; food 694.1M, iron 1.0G, coin 137.5M,
  diamonds 13.22K. Level 63 avatar. Task line: "Build: Oil
  Well [0/1]".
- VS timer 23:09:49; Season II 1d 23:19:49; radar timer
  3d 23:09:49. Events icon badge 3 at entry. Cart 6,717
  with a red dot. Chat badge 99+.
- The blue house marker bottom-right now reads "35 km"
  (49 km at 16:50 in the 1634 unit) - the distance moves;
  meaning still unverified.

## Red dots and unknowns, this unit

Seen this unit (4): Events icon badge 3; The Age of Oil tab
badge 1 (same signal as the stage-1 node badge); Zombie
Invasion tab badge 1; Zombie Store red dot. Explained: 0 -
no cause proven to a tap this unit. Unexplained (4), carried
to the successor: all four above.
Carried unexplained from the 1634 unit, not re-checked:
skull cycle timer; "Others' Trucks" tab badge 4; "Recover"
button red dot. Unknown items carried (4): the small "9"
beneath the Mission terminal; the second left-column icon
(white truck); the blue gift-box marker above the dispatched
truck; the "35 km" blue house marker (re-read, distance
changed).

## Follow-up

- Chain successor seq 002 enqueued: VS/duel page, Wanted
  Boss, Desert Battlefield, radar, skull-timer re-check, and
  the four unexplained dots above.
- Arms-race unit (arms-race-2026-11-11-1803, in inbox) reads
  the Base Building phase from this record under R4.
- Event-claims / diff: Age of Oil stage-1 badge 1 with both
  counters exceeded - claim state to verify.
- Issue filed: sync duplicate chain head, tooling Issue #664.
