---
title: Queue Run 0114 Truck Plunder
created: 2026-11-02T09:23:00Z
modified: 2026-11-02T09:23:00Z
level: L0
version: 1.0.0
description: Trucks unit entry failure, partial, tracker untouched
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-11-02
---

# 0114 queue run - truck plunder (partial)

Unit trucks-2026-11-01-2257, executor ticker-0104, session
about 01:09 to 01:13 America/Los_Angeles. Status partial:
the trade screen could not be entered, so no counter was
read live, no truck was dispatched and no plunder was made.
Tracker untouched (partial units do not mark the tracker).

## Duel posture

- Duel day 1, Radar Training (radar release day), from
  tools/duel.py at unit start. Non-UR day rules would
  apply: dispatch SR or above only, plunder UR or SSR
  trucks carrying UR shards with guard below Squad 1.
- Trade-day quota still open from the 22:31 unit on
  2026-11-01 (Trade Count 1 of 5, Plunder Count 1 of 4
  at that unit's close, trade day ending 19:00 on
  2026-11-02). Those figures are carried from that
  record, NOT re-read in this unit - no live counter
  exists for this unit.

## Entry blocker, changed methods tried

Base left column re-grounded fresh on the current
screenshot. The column reads top to bottom: green face,
blue bus/train-front icon, white pickup (red badge 8),
walkie-talkie (red badge 2), hammer, chest. No icon in
the column carries a speech-bubble delivery-truck glyph
with a badge in this view, unlike the 22:31 unit's
[55,584] entry point.

Taps tried, all with no screen change:

- [53,595] snapped.
- [53,555] snapped.
- [55,584] with snap disabled (the 22:31 unit's
  successful method).
- Title-bar tap [180,15] followed by [55,584]
  snap disabled (the 1053 unit's foregrounding
  variant).

Per queue rule R2 this is the entry blocker for the
next trucks unit: do NOT re-tap the left column points
above. The successor must try a different entry route
first - the World map trade entry or the station area -
and re-ground the column from a fresh screenshot before
any column tap. If the column set has flipped, identify
the flip control before tapping a vehicle icon.

## Outcome

- Status: partial, blocker_category e (repeated blocker,
  entry method).
- Claimed in this unit: none.
- Counters: not read live in this unit (see above).
- Red lines: nothing spent, no paid button tapped.
