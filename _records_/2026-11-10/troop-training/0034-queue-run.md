---
title: Troop training queue run 0034
created: 2026-11-10T08:34:00Z
modified: 2026-11-10T08:34:00Z
level: L0
version: 1.0.0
description: Ticker-0034 training unit, partial - Drill Ground screen not re-read live, no barracks requeued, formation taps select squads and the Wall
status: unverified
---

# 0034 queue run - Troop Training

Executor: ticker-0034. Unit: training-2026-11-09-2203.
Session window about 00:34 to 00:50 America/Los_Angeles.
Computer session cc-370 on the owner Mac mini (started and
ended cleanly, no drops, no different-device dialog).

## What was done

- Camera panned down to the base lower edge, exposing the
  fenced troop formation yard (Formation 1, 2 and 3 signs,
  parked squads). Three fresh grounding taps were tried for
  the Drill Ground, per the 1330 unit's handover to re-read
  its screen live:
  - Tap at norm (413,541) on the green truck at the yard's
    left edge: no selection, only an alliance announcement
    banner scrolled across the top.
  - Tap at norm (592,547) on the red car: selected
    2nd Squad Lv.20 (label read live; an earlier compact
    read showed Lv.2, an OCR misread of Lv.20), with a
    speech bubble "The truck is full, waiting for your
    command" and a tank-icon button plus a green up arrow.
    No squad button was tapped: dispatching a squad is
    truck-type work and must not merge into this unit.
  - Tap at norm (545,421) on the wooden FORMATION sign on
    the fence: selected Wall Lv.26, with a house-icon
    button and a green up arrow. The green arrow was not
    tapped: no upgrades on the agent's initiative.
  - Tap at norm (670,736) on empty pavement inside the
    fence: selected 2nd Squad Lv.20 again (the blue tank).
- The Drill Ground screen was therefore NOT re-read live in
  this unit. What this unit establishes is a negative
  grounding result: at this camera view, taps inside the
  formation yard resolve to the individual squads parked
  there or to the Wall, never to a Drill Ground building.
  The 0039 unit's tap that selected Drill Ground Lv.30
  does not reproduce from these points; the next unit
  needs a different selection route (for example the
  formation ground at a wider zoom, or the Drill Ground
  entry from a building list), not another tap on a
  vehicle, a sign or the fence.
- A green truck at the yard's left edge read "Collecting
  supplies, ready to depart again" - a full truck waiting,
  truck-type work for its own unit, left untouched.
- No diamonds, money, speedups or paid buttons were used,
  and no other task type was executed in this unit.
  The squad selection was cleared by tapping empty snow
  before the session ended.

## What was not done

- No barracks was requeued: no barracks state was verified
  live in this unit, and every barracks remains blocked
  in the carried-forward state by the Drill Ground Full
  toast (39,460 of 39,460, last read live 2026-10-31).
  Lv.30's batch (requeued 2026-11-07 about 17:08, 1d 17h)
  was due about 10:22 on 2026-11-09 and its state is
  unverified; Lv.27 was idle and blocked at the 1330
  read on 2026-11-09; Lv.24 and the fourth barracks were
  not checked. Tracker untouched, per the partial rule;
  the next tick re-produces the training regular.
- Quick Dispatch stays untapped: its effect is still
  unverified and it may march troops out, left for an
  owner decision or a learn-first exploration unit.

## Figures read live on screen

- Food 598.9M, iron 922.5M, coin 80.6M, power
  146,751,949, diamonds 6,207, energy 81 at entry.
- Build slot in use: Oil Well (0/1), 1/4 hammer icon.
- No login or verification was demanded, and no
  different-device dialog appeared.

## Result statistics

- target 4, achieved 0, resources_gained none, costs
  about 15 minutes play, verified yes, blocker_category e,
  device_takeovers 0

## Delivery note

- The pass executed one unit only: the 15 minute unit cap
  plus the delivery work left no room for a second unit
  inside the about 25 minute pass budget. The inbox holds
  69 units; the next tick picks up.
- Record, day INDEX append and action-log append were
  written to the records/2026-11-10 branch in the
  ticker-0004-1110 worktree (that pass is finished and
  its worktree is the branch checkout); the main-tree day
  INDEX.md is a condensed copy and was not touched.
