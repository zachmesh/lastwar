---
title: Queue Planning The Oil Well Chain Re-Timed After The Flat Reduction 3080 2026-11-23
created: 2026-11-23T15:55:00-08:00
modified: 2026-11-23T15:55:00-08:00
level: L0
version: 1.0.0
description: Planner pass after the builders panel was measured 6 h 32 min shorter than the upgrade preview on three builds - the Oil Well chain re-timed to the real finish, the attempt cost of an early claim, and the units that moved
status: done
activity: queue-planning
run_id: queue-planning-2026-11-23-1555-flat-reduction
trigger: coordinator message 23:34Z, operator records 2320 and 2328
started_at: 2026-11-23T15:34:00-08:00
finished_at: 2026-11-23T15:55:00-08:00
verified: the release code read for its effect on attempts; the inbox checked for the forecast flip, the quiet windows and claimability at 02:17:53Z; word counts under 450; validate exit 0
grounded_in:
  - source: _records_/2026-11-22/building-queues/2320-queue-run.md and 2328-queue-run.md (as relayed)
  - source: _records_/2026-11-22/strategy/dec-20261123-08.md
  - source: _tools_/queue.py _release
---

# The Oil Well chain re-timed after the flat reduction, 3080

## What was measured

The Oil Well Lv.20 to 21 started at 23:29:34.8Z with a preview effective time of 09:20:18; the panel read 02:47:58 left at 23:29:55.2Z, so it ends 2026-11-24T02:17:53Z: a difference of 6 h 32 min 00 s from the preview, the same flat amount on the 9 hour Oil Well build and on the 10 and 14 day ground builds. My chain used the preview, so every hand-off was too late: unit `-002` would have opened at 08:41Z for a finish at 02:17Z and the builder would have idled six hours.

## What moved

Oil Well unit `-002` opens at 02:17:53Z and expires 04:30Z. For `-003` to `-010` I used Decision 08's effective durations minus the flat 6 h 32 min to estimate the real finishes (07:53Z, 17:08Z on 11-24, 08:42Z on 11-25, 09:06Z on 11-26, 21:52Z on 11-27, 03:58Z on 11-30, 10:18Z on 12-03, 18:07Z on 12-07, 11:01Z for the last on 12-13), which is a model with one measured point [G]. Each unit opens before its expected finish by 3 hours at level 22 growing to about 39 hours at level 29, because the error accumulates, and runs 24 to 36 hours or more after it. An early claim that releases the unit does not give the attempt back: the release code keeps the count, and max_attempts was 3, so three early claims would have dead-lettered a chain unit; the chain units now carry max_attempts 8. The three slot reads moved from 02:10Z to 02:30Z so the operator is free from 02:17Z. Sheets 2900 and 2830 carry the new schedule.

## Open

Level 22 is expected to end about 07:54Z, six minutes before the daily quiet window, so its Complete and the next Upgrade press must finish before 08:00Z or wait for 08:25Z; level 24 about 08:43Z on 11-25 is 18 minutes after it. Every real finish read after a start should be sent to me, because the later windows are estimates: I re-time the next unit from each. The research Completes, the speed-up unit and the oil collections do not depend on these times.
