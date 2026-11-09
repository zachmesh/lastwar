---
title: Radar Tasks queue run 0644
created: 2026-10-29T13:44:00Z
modified: 2026-10-29T13:44:00Z
level: L0
version: 0.1.0
description: Radar queue unit radar-2026-10-29-0603 on duel Day 4 (stack posture) - radar screen not reached, left-column dish slot currently opens Secret Command Post (verified twice), no tasks checked, claimed or spent, tracker untouched
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-10-29
  - source: owner directions of 2026-10-25, 2026-10-26 and 2026-10-28 - the standing routine, Mac control authorization and the task unit queue ticker
  - source: tools/duel.py readout on 2026-10-29 - duel day 4, Train Heroes, radar posture stack
---

# Radar tasks - queue unit radar-2026-10-29-0603 (partial)

- Executor: ticker-0634. Session window about 06:34-06:44 PT.
- Duel posture first (tools/duel.py): Day 4, Train Heroes, radar
  posture stack - complete but do not claim, so rewards stay
  for the Day 5 release. Day ends 19:00 local.
- Radar screen NOT reached in this unit, so no radar state
  (points, stored tasks, stamina, pins) was verified in-game
  this pass. Nothing claimed, nothing spent, no stamina claim
  taken, no diamond or money spent, no different-device
  dialog appeared.
- Entry attempts, recorded as they happened:
  - Left-column satellite-dish icon with red badge 7, grounded
    at norm 54,667 and tapped at 53,677 and again at 54,667:
    both taps opened SECRET COMMAND POST (Secret Mobile
    Squad, Your Tasks), not the radar screen. The icon slot
    is a rotating shortcut (see _activities_/secret-missions
    - the same slot can open Intercity Trade or the radar
    instead); at 06:41 PT it was assigned to secrets.
  - Magnifier icon at norm 52,766: opened the world search
    panel (Zombies / Gather / Doom Elite tabs), not radar;
    dismissed by tapping empty ground.
  - Yellow radio-device icon at norm 51,851: opened the
    Mission screen (Daily Tasks, including a completed
    "Complete 1 Radar Task(s) (1/1)" line). Its Claim buttons
    belong to another regular and were NOT tapped, per the
    one-unit-one-type rule; the screen was backed out of.
  - A tap on a ground dish structure at norm 601,258 moved
    the camera to a Lv.2 Iron Mine popup instead of opening
    radar; the popup was dismissed by tapping empty ground
    and the base view was restored.
- Contrast: the 02:24 queue unit the same day DID open the
  radar (stored 2 of 40, points 2,948, 7 rewards stacked
  unclaimed, stamina ending 25), so this is a shortcut-
  rotation or state issue in this pass, not a permanent loss
  of the radar entry. The next tick should retry the dish
  slot first and, if it still opens secrets, try the slot
  again after the rotation changes.
- Status partial, tracker untouched: the radar regular stays
  due for the next tick, which re-produces it as a fresh unit.
