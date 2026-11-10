---
title: Troop training queue run 1330
created: 2026-11-09T21:30:00Z
modified: 2026-11-09T21:30:00Z
level: L0
version: 1.0.0
description: Ticker-1304 training unit, partial - Lv.27 barracks idle and blocked by Drill Ground Full, tents grounded by a fresh route
status: unverified
---

# 1330 queue run - Troop Training

Executor: ticker-1304. Unit: training-2026-11-09-1003.
Session window about 13:13 to 13:30 America/Los_Angeles.
Computer sessions cc-277 then cc-278 on the owner Mac mini
(cc-277 dropped mid-unit, observation_unavailable; cc-278
restarted, LastWar re-selected, no game state lost).

## What was done

- Barracks tents grounded by a fresh route, as the 0039 unit
  required under queue rule R2 (the yellow-green fenced
  structure method ended there). The diagonal row of
  blue-roofed tents in the upper base is Material Workshops,
  not barracks: a tap at norm (267,365) selected Material
  Workshop Lv.20, and a tap at norm (460,290) selected
  Eternal Pyramid Lv.3. The barracks are the beige tents
  with blue zigzag markings at the base lower-right edge,
  each with an instructor portrait circle overlapping the
  tent body - tap the body, not the circle, as the 1655
  unit already noted.
- Barracks Lv.27 selected live (label read on screen, norm
  tap (799,871) on the tent body; the earlier tap at
  (748,910) hit the tent's left edge and selected nothing).
  Its button row reads paw, pistol, green up-arrow; the
  pistol TRAIN UNITS button grounds at norm (787,931) for
  this screen position.
- Pistol tap produced the toast "Drill Ground Full: Unable
  to add more units" (read live by OCR), and no TRAIN
  UNITS panel opened. Lv.27 is idle and blocked - the
  same blocker the 2050 unit read for Lv.24 on
  2026-11-07, now re-confirmed live on a second barracks
  two days later. No timer bubble stands above the Lv.27
  tent, consistent with idle. No diamonds, money,
  speedups or paid buttons were used, and no other task
  type was executed in this unit.
- The building at norm (435,518) is the ICU hospital, not
  a barracks - the 2050 grounding point no longer maps to
  a barracks in the current camera view. A gold-mine timer
  bubble read 97min then 94min during the unit; it is a
  mine production timer, unrelated to training.

## What was not done

- No barracks was requeued: Lv.27 is idle but blocked by
  the full Drill Ground. Lv.30 (batch requeued 2026-11-07
  about 17:08, 1d 17h, due about 10:22 today), Lv.24 and
  the fourth barracks were not checked in this unit - the
  second beige tent sits half off the bottom edge and
  needs the camera panned down first. Tracker untouched,
  per the partial rule; the next tick re-produces the
  training regular.
- The Drill Ground screen was not re-read live in this
  unit; the 0039 unit read it this morning (Lv.30, Unit
  Count +10080, officers Samantha, William, Chloe and
  Catherine, single action Quick Dispatch, untapped). The
  next unit pans the camera down to find the red troop
  formation at the base lower edge, re-reads the Drill
  Ground screen live, and checks Lv.30, Lv.24 and the
  fourth barracks. Quick Dispatch stays untapped: its
  effect is still unverified and it may march troops out,
  left for an owner decision or a learn-first
  exploration unit.

## Figures read live on screen

- Food 553.9M, iron 879.2M, coin 51.9M, power
  149,217,331, diamonds 13.22K, energy 68 at entry.
- No login or verification was demanded, and no
  different-device dialog appeared.

## Result statistics

- target 4, achieved 0, resources_gained none, costs
  about 17 minutes play, verified yes, blocker_category e,
  device_takeovers 0

## Delivery note

- The main-tree day INDEX.md (412 lines) is a condensed
  ticker-only copy; the records branch INDEX.md (2256 lines)
  is the full day record, holding the integrator, planner
  and tool-developer sections as well. The same split holds
  for the action log (443 lines main tree, 1362 branch).
  This pass appended to the branch versions in the
  worktree and did NOT copy the main-tree files over them;
  copying them would delete about 1800 lines of other
  jobs' records. The next ticker pass must append in the
  worktree the same way.
