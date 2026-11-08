---
title: Queue Run 0118 - Perception Scout Alliance Remainder Station Check
created: 2026-11-08T09:12:00Z
modified: 2026-11-08T09:12:00Z
level: L0
version: 1.0.0
description: Ticker-0104 scout-midday unit, alliance remainder station panel check, sixth no-train confirmation, partial observe-only
status: unverified
grounded_in:
  - source: live game screens on the owner Mac mini, 2026-11-08 about 01:14 to 01:19 local
---

# 0118 queue run - perception scout, alliance remainder station check

Unit scout-midday-scout-mid-2026-10-31-008 by ticker-0104,
session about 01:08 to 01:12 local, status partial,
observe-only throughout: nothing claimed, fought,
dispatched, donated, dug or bought. Evidence in this file
and the appended section of the 2026-11-08 observation
file.

## Entry

- The game was found on the Alliance main panel, left there
  by a previous unit. The panel back arrow at norm 139,935
  returned to the base screen.
- Tooling note: the first click attempt failed with
  stale_observation (missing observation_id) and sent no
  input; the retry carried the observation id and
  dispatched at once.

## Alliance panel, read live about 01:09 local

- [AP3x] The Apex, 5.0 stars, Leader Abyss Apex, Power
  13,350,333,388, Members 96/100, Language English.
- Red dots on Help and Alliance Gifts. Alliance Star
  (Event 40) banner, Time Left 16:40:54 falling to
  16:40:39 during the read, Enter button observed only,
  not tapped.
- Bottom row Record, Applicants, Alliance Star, Settings -
  none opened this unit.

## Base screen, read live about 01:11 local

- Level 30, power 149,850,353. HUD top row 478.8M food,
  802.1M iron, 6.9M coin; second row 25.0M, 922.2K,
  13.22K with a plus button; stamina 120; cart 4,217.
- Left column top to bottom: hammer 2/4 with a red dot,
  flask 2/2, weather face 6.5C, radio with a red dot,
  truck with a red dot, radar dish, hammer. No
  train-head icon in this column set.
- Right column: Events with an x2 badge, VS, Season II
  with a 7d 16:50:22 timer, Alliance with a red dot,
  Mail, Inventory with a red dot, WORLD.
- Bottom: HEROES, chat ticker, 99+ badge.
- Lines under the resource bar: the furnace overdrive
  toast and the Breaking News ticker. No "Boarding closes
  in" banner.

## Station panel check - the unit's window

- The two preparation signals were checked first, per the
  unit window: the left-column train icon is ABSENT, and
  the "Boarding closes in" banner is ABSENT.
- With neither signal present, the unit closed partial
  without panning, per the window instruction. This is
  the sixth no-train confirmation in this chain's
  station-panel checks (after 1345, the 2140/2153 third
  and the 2311/2317 fifth). The station panel is a
  preparation-only surface: it has no live state to read
  while no train is preparing.
- Resource bubbles standing on many buildings, observed
  only, not collected; the harvest regular owns
  collection and its 1003 unit is already queued.

## Red dot accounting, this unit's walked surfaces

- Seen 8: panel Help dot, panel Gifts dot, base Alliance
  dot, Events x2 badge, Inventory dot, 99+ badge, radio
  dot, truck dot.
- Explained 6: Help dot maps to the help regular, Gifts
  dot to the gifts regular, Events x2 to the events
  regular, radio dot to the help regular, truck dot to
  the trucks regular, and the base Alliance dot is the
  roll-up of the panel dots; units for all of these are
  already queued.
- Unexplained 2: the Inventory dot and the 99+ badge.
  Both belong to other groups (store, base/chat) and are
  carried by the current day's scout pass, not by this
  unit.
- unmatched_labels: none in the surfaces actually walked.

## Unknown items, carried

- Furnace overdrive toast ("High-temp Furnace total
  overdrive time (in sec)"), seen again on the base
  screen; still unexplained, furnace observed only,
  never switched on or off, a red-line surface.
- Alliance Power read 13,350,333,388, up from
  13,016,623,359 on 2026-11-03; live member power
  movement is possible and read variance is possible,
  recorded as displayed, not asserted either way.

## Unwalked, carried to successor seq 009 of chain scout-mid-2026-10-31

- Station panel only (preparation-only surface; re-check
  when a train is preparing). Successor unit enqueued
  under the same chain.
- No train summoned, no conductor role taken, no
  different-device dialog, no login demand. Game left on
  the base screen.

## Result statistics

- surfaces_walked 1, items_observed 12, red_dots_seen 8,
  red_dots_explained 6, unexplained_red_dots 2,
  unknown_items 2, target 1 (station panel read),
  achieved 0 (no train preparing, panel unreadable),
  resources_gained none, verified yes,
  blocker_category h (by-design partial, preparation-only
  surface with no train preparing).
