---
title: Radar Tasks queue run 1119
created: 2026-10-29T18:19:00Z
modified: 2026-10-29T18:19:00Z
level: L0
version: 0.1.0
description: Radar queue unit radar-2026-10-29-1003 on duel Day 4 (stack posture) - radar screen not reached, left-column dish slot still opens Secret Command Post, no tasks checked, claimed or spent, tracker untouched
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-10-29
  - source: owner directions of 2026-10-25, 2026-10-26 and 2026-10-28 - the standing routine, Mac control authorization and the task unit queue ticker
  - source: tools/duel.py readout on 2026-10-29 - duel day 4, Train Heroes, radar posture stack
---

# Radar tasks - queue unit radar-2026-10-29-1003 (partial)

- Executor: ticker-1104. Session window about 11:04-11:19 PT.
- Duel posture first (tools/duel.py): Day 4, Train Heroes, radar
  posture stack - complete but do not claim, so rewards stay
  for the Day 5 release. Day ends 19:00 local.
- Radar screen NOT reached in this unit, so no radar state
  (points, stored tasks, stamina, pins) was verified in-game
  this pass. Nothing claimed, nothing spent, no stamina claim
  taken, no diamond or money spent, no different-device
  dialog appeared.
- Entry attempts, recorded as they happened:
  - The game was left on the Alliance Techs panel from the
    previous unit. Its inner X and outer X closed cleanly,
    and the Alliance page back arrow, grounded at norm
    163,935 (the earlier 100,930 estimate missed the button),
    returned to base. No donation was made in this unit.
  - Left-column satellite-dish icon with red badge 7, grounded
    at norm 52,672 and tapped at 54,667: the tap opened
    SECRET COMMAND POST (Secret Mobile Squad, Your Tasks),
    not the radar screen. The icon slot is a rotating
    shortcut (see _activities_/secret-missions - the same
    slot can open Intercity Trade or the radar instead);
    at about 11:15 PT it was still assigned to secrets,
    the same assignment the 06:44 queue unit found. The
    screen was left untouched and exited with its back
    arrow at 160,947, which returned to base.
  - An earlier tap at 53,687 (before the dish slot was
    re-grounded) produced no screen change and opened
    nothing; it is recorded as a miss, not a radar entry.
- Contrast: the 02:24 queue unit the same day DID open the
  radar (stored 2 of 40, points 2,948, 7 rewards stacked
  unclaimed, stamina ending 25), so this is a shortcut-
  rotation or state issue in this pass, not a permanent loss
  of the radar entry. The next tick should retry the dish
  slot first.
- Status partial, tracker untouched: the radar regular stays
  due for the next tick, which re-produces it as a fresh unit.
  The 15 minute unit cap arrived during the entry attempts,
  so no further entry route was tried in this unit.
