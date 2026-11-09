---
title: Queue Run 2140 Perception Scout Station Panel
created: 2026-11-08T05:44:00Z
modified: 2026-11-08T05:44:00Z
level: L0
version: 1.0.0
description: Scout chain scout-mid-2026-10-31 unit 007, station panel remainder, partial with R2 metadata change
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-11-07
---

# 2140 queue run - perception scout, station panel remainder (partial)

Unit scout-midday-scout-mid-2026-10-31-007, executor ticker-2134,
session cc-51 about 21:37 to 21:40 America/Los_Angeles. Status
partial: the station panel remainder was re-checked live; no train
is preparing, so the platform has no live state to read. This is
the third consecutive partial with the same blocker (units 005,
006, 007), so under design rule R2 the blocker is written into
the alliance-train activity metadata in this pass and the entry
route is changed before any further unit of this type runs. The
tracker is left untouched.

## What was read live

- Alliance panel (entry state, left over from the ticker-2104
  scout unit): [AP3x] The Apex, 5.0 stars, Leader Abŷss Apex,
  Power 13,360,041,845, Members 96/100, Language English.
  Red dots on Help and Alliance Gifts only. Alliance Star
  (Event 40) banner, Time Left 20:11:46 falling to 20:11:35.
  Closed with the panel back arrow; nothing tapped inside.
- Base screen, read live about 21:39 local: account power
  149,850,353; resources 478.8M, 802.1M, 6.9M, 25.0M,
  922.2K; diamonds 13.22K; cart 4,217; stamina 120.
  A building countdown read 03:38 (unidentified building,
  not a train signal).
- Preparation signals, both absent: the left icon column
  reads avatar Lv.30, hammer 2/4, flask 2/2, green face
  (6.5C), white truck, radar, wrench - no train icon; and
  no Boarding closes in banner under the resource bar.
  Reading, as in units 005 and 006: no train is preparing
  in this window, so the STATION PLATFORM screen has no
  live state to read. No pan of the base edge was made -
  the changed entry route from unit 006 (check the two
  signals first) was followed and the check stopped there.
- Nothing claimed, fought, dispatched, donated, boarded or
  bought anywhere in this unit. Observe-only throughout.

## Red dot accounting

- Seen 9: alliance panel Help and Alliance Gifts dots;
  base Events badge 1, Season II badge, skull timer badge
  (7d 20:21:23), 99+ badge, Alliance dot, Mail dot,
  Inventory dot.
- Explained 9: Help and Gifts map to their owning
  regulars; Events maps to the events regular; Season II
  and the skull timer map to the season/event surfaces;
  99+ maps to chat and mail; Alliance, Mail and Inventory
  map to their owning regulars.
- Unexplained red dots: 0.
- Unknown items: the furnace overdrive toast
  ("...rnace total overdrive time (in sec) [22/60]"),
  recurring and still unexplained, carried.

## Outcome

- Status: partial (station panel remainder, no train
  preparing). Successor unit enqueued under chain
  scout-mid-2026-10-31 for the same remainder, with the
  changed entry route in its window: check the two
  preparation signals first; if neither is present, close
  partial without panning.
- R2 metadata change (tier 2, left uncommitted in the
  working tree for the knowledge PR flow, not staged in
  this pass's tier-1 commit): `_activities_/alliance-train/INDEX.md`
  version 1.5.0 to 1.6.0 - the station panel is recorded
  as a preparation-only surface, with the check-signals-first
  entry route. The pre-existing uncommitted change to
  `_activities_/alliance-donations/INDEX.md` (another job's
  in-flight state, noted by ticker-2104) was left untouched.
- No new Issue filed: the station remainder is a
  pre-existing carried item, now hardened in metadata; the
  furnace toast is a standing unknown, not a new gap.
- No zombie chain seeded: no Zombie Invasion tab was seen;
  the event ended 2026-10-30 and the chain stays closed
  until its tab is seen live again.
- Red lines: nothing spent, no paid button tapped, no
  donation, no rally join, no toggle changed.
- Game left on the own base screen.
