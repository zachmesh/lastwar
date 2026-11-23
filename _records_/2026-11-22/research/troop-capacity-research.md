---
title: Troop capacity - what counts, what Full blocks, what raises it
created: 2026-11-23T00:31:00-08:00
modified: 2026-11-23T00:31:00-08:00
level: L0
version: 1.0.0
description: Research on the Drill Ground troop cap for assignment A-20261123-0820 - what counts toward it, what the Full toast blocks, every capacity source with cost, hospital behaviour and no-fight ways to free space
status: unverified
grounded_in:
  - source: seventeen guides read 2026-11-23, URLs and labels per row in troop-capacity-claims.csv
  - source: repository records on the Drill Ground toast, Hospital read and upgrade panels, paths per row
---

# Troop capacity

Labels: TESTED (repository screen read), SOURCED (a guide says it), GUESS.

## 1 What counts and what Full blocks

- Hospital troops do not count [SOURCED, 3]. Queued troops do [SOURCED, 2].
  Finished batches waiting uncollected are unsettled: one guide says they
  need space, another says leave them until an event [GUESS].
- Full blocks new training and requeue (an idle barracks refuses TRAIN UNITS,
  seen on five dates) and Collect of healed troops (5,306 refused whole)
  [TESTED]. It did not block collecting a finished batch on 2026-11-10
  [TESTED, cap reading carried]. A partial Collect: no source; one tap, one
  refusal [GUESS].
- Promotion adds no population and is the guides' first fix [SOURCED, 3]. Not
  yet reachable here: an idle barracks shows the toast and no panel [TESTED].
- The 39,460 cap is stale: read live 2026-10-31, and one ground has since gone
  Lv.25 to Lv.28 (+7,812 to +9,211). The cap now is unknown; the soldier
  icon at top left shows count and cap [SOURCED, 9game].

## 2 Capacity sources

| Source | Gain | Cost |
|---|---|---|
| Ground level | +200 a level from Lv.6 to 30, +100 to Lv.35, flat [SOURCED, 4; panel TESTED] | Lv.28 to 29: 170M iron, 520M food, 140M coin, 21 to 39 days (guides differ) |
| 4th ground, Extra Drill Ground (Siege to Seize) | 2,000 at Lv.1, then the same curve | about 700 Valor Badges, 20.4M food, 20.4M iron, 61.3M coin; HQ 30, about 40 percent Special Forces [SOURCED, 2] |
| Drill Ground Expansion (Development, 5 levels) | unpublished [GUESS] | none found |
| VIP | +5 percent at VIP 6 or a rise at VIP 10, sources conflict; VIP 13 has both | diamonds, red line |
| Officers on the ground | readings run 1.12 to 1.26 times the table [TESTED]; cause unknown [GUESS] | none |
| Alliance tech, decorations, hero skills | none found [GUESS] | |

Extra Barracks (Development, more queues) is not Extra Drill Ground; the
planner CSV conflates them. Derived from the tables [GUESS]: a new ground to
Lv.15 is 5,000 slots for 2.9M coin; with the research, about 72 slots per
million coin at Lv.20, against 1.4 for Lv.28 to 29.

## 3 Hospital

Capacity bounds wounded troops; overflow dies, and the Emergency Center saves
21 to 40 percent as fainted units [SOURCED, 4]. Healed troops wait in the
Hospital until Collect [TESTED]. Whether they use its 7,999 slots is unread.

## 4 No-fight ways to free space

Only promotion raises power without capacity, if reachable. Disband works
(one source) but destroys power: an owner decision. Fights, monsters, gather
collisions, rallies and any march are red lines. Waiting is free; power
registers at Collect [TESTED].

## Test order (read-only)

Soldier icon count and cap; each ground's Unit Count and officers, and how
many grounds exist; the Siege to Seize node; Hospital quantity selector.
