---
title: Perception scout queue run 0025
created: 2026-11-23T08:30:00Z
modified: 2026-11-23T08:30:00Z
version: 1.0.0
description: Growth snapshot unit T2 scout-midday-growth-snapshot-2026-11-23-002, operator seat, Lv.24 barracks pistol toast and Drill Ground tag read, the two details panels not reached, a tent mis-pick used two turns
status: run-partial
grounded_in:
  - source: cu_bridge start, status poll, events and final result on run 20261123T082546Z-831319, 2026-11-23T08:25Z to 08:26Z
  - source: frames step-0003.png to step-0005.png read by the operator, saved as _tools_/state/cu_growth_t2_0025.png (untracked)
  - source: Drill Ground Building Details read at 07:48Z in run 20261123T074723Z-fdee03, cited for the Unit Count
---

# Perception scout queue run 0025

- Unit scout-midday-growth-snapshot-2026-11-23-002, operator seat, assignment
  A-20261123-0825-operator, attempt 1, claimed 08:25:44Z. Rows in the sidecar
  [0025-queue-run-detail.md](0025-queue-run-detail.md).
- Run `20261123T082546Z-831319`, model `claude-gateway/claude-sonnet-5-5`, max-steps 8,
  ended `completed` after 7 steps. Actions done 12, refused 0. Model time 6.9 s per step.
  Cost 0.094026 USD. No takeover, no account dialog, no boarding banner.
- Closing the Hospital menu worked with one empty-ground tap. HUD unchanged: food 638.0M,
  iron 1.0G, coin 9.6M, diamonds 11,136, Total Power 150,211,809.
- **Tent mapping.** The first tent tapped, upper right in the group, read **Barracks
  Lv.20**, so the run lost two turns re-picking. The next tent, lower right and without a
  clock bubble, read **Barracks Lv.24**. The Hospital Lv.20 read at 08:23Z was another
  building in a different camera view; a Hospital and a Barracks may both be Lv.20.
- **Barracks Lv.24, idle.** The pistol gave the toast "Drill Ground Full: Unable to add
  more units." and no TRAIN UNITS panel. Its Building Details (Training Count,
  instructors) were not read: out of turns.
- **Drill Ground.** The red formation read **Drill Ground Lv.28**. Its details were not
  re-read. The 07:48Z read stands: Unit Count +9211, four survivors all post Officer, no
  next-level text. No upgrade has finished since, because all four builders are busy until
  2026-11-24T09:20Z.
- The brief's old figure 39,460 (2026-10-31) is not on the panel; Unit Count +9211 is the
  only capacity number shown, and no used-over-cap figure appears.
- Closing state: the base with the Drill Ground radial menu open, no panel. Nothing
  pressed that trains, collects, upgrades or spends.
- Red lines held: no Train, Collect, Upgrade, Quick Dispatch or green up arrow.
- Blocker c, a wrong tent pick. Follow-up: a three-step read of the Lv.24 and Drill
  Ground Building Details would close the unit.
