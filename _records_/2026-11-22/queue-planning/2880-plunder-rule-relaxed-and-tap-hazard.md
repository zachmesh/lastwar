---
title: Queue Planning The Plunder Rule Relaxed And The Camera Shift Hazard 2880 2026-11-23
created: 2026-11-23T07:55:00-08:00
modified: 2026-11-23T07:55:00-08:00
level: L0
version: 1.0.0
description: Planner pass applying the answered left-half plunder experiment to the remaining scans and the 18:00Z session, and the camera shift hazard on the safe tap point to the route card and every live unit
status: done
activity: queue-planning
run_id: queue-planning-2026-11-23-0755-plunder-relaxed
trigger: coordinator message 15:36Z, operator record 1523
started_at: 2026-11-23T07:33:00-08:00
finished_at: 2026-11-23T07:55:00-08:00
verified: every plunder unit and every unit naming the old tap point read back; word counts under 450; validate exit 0
grounded_in:
  - source: _records_/2026-11-22/truck-plunder/1523-queue-run.md (as relayed by the coordinator)
---

# The plunder rule relaxed and the tap hazard, 2880

## Plunder

The experiment is answered in [2850](2850-plunder-left-half-experiment.md) version 1.1.0: a left-half UR shard stack paid shards (x3, resources about a third of each stack, no troops wounded, count 2 of 4), against fight 1's right-half x9; one trial each, so the right-half preference is relaxed, not reversed. Scans `trucks-plunder-scan-2026-11-23-003` to `-009` and the 18:00Z session `trucks-plunder-2026-11-23-002` now accept a UR 500-badge stack in either half, with the other checks standing: casualty guard first, guard under Squad 1 (25.61M, which replaces the stale 24.96M in the session unit), an arrival more than 30 minutes away, Quick Plunder once and Battle once. The session unit's stale 'Plunder Count 0/4' reads 2 of 4. Scan `-002` had already run; `-001` too.

## The hazard

The tap point (400,640) is not safe after a camera shift: it selected a Barracks, which hides the left column. The bare spot (310,660) is the safe point, or WORLD then BASE first. The route card (now 1.6.0) and its route table say so; the plunder units and 66 other live units had their wording replaced (the old (400,640) wording survives in no live unit), and sheet 2540 and the conversion rules were corrected. The scribe's lines for the plunder digest rule 9 and the brief rule are the coordinator's to relay; I do not edit the digest.
