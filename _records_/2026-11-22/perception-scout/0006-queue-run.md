---
title: Perception scout queue run 0006
created: 2026-11-23T08:12:00Z
modified: 2026-11-23T08:12:00Z
version: 1.0.0
description: Growth snapshot unit scout-midday-growth-snapshot-2026-11-23-004, operator seat, read-only look at the Lv.30 and Lv.27 barracks, both busy, tier counts and six unit stats read
status: run-done
grounded_in:
  - source: cu_bridge start, status poll, events and final result on run 20261123T080610Z-7faa88, 2026-11-23T08:06Z to 08:07Z
  - source: frame step-0004.png (Lv.27 panel) read by the operator, saved as _tools_/state/cu_growth_snap_0006.png (untracked)
  - source: resource_map.py snap entry at 2026-11-23T00:07:19 local
---

# Perception scout queue run 0006

- Unit scout-midday-growth-snapshot-2026-11-23-004, operator seat, assignment
  A-20261123-0805-operator, attempt 1, claimed 08:05:5xZ. Rows in the sidecar
  [0006-queue-run-detail.md](0006-queue-run-detail.md).
- Run `20261123T080610Z-7faa88`, model `claude-gateway/claude-sonnet-5-5`, max-steps 8,
  ended `completed` after 6 steps. Actions done 12, refused 0. Model time 4.9 s per step.
  Cost 0.078709 USD. No takeover, no account dialog, no boarding banner.
- Read-only: nothing pressed, no tier tab tapped, no Speed Up, Train or Promote. Both
  panels were closed with their X. No finished batch was waiting and no Training
  complete toast showed.
- **Barracks Lv.30: busy.** Lv.10 batch of 793, Training in progress 1d 03:12:00 at
  08:06:31Z, so it ends about 2026-11-24T11:18:31Z. Power 1647, Morale 750.0, Squad Load
  Capacity 2200, Unit HP 4779.05, Unit Attack 38.87, Unit Defense 7.96. Only a Speed Up
  button, no slider, cost or Train button.
- **Barracks Lv.27: busy.** Lv.9 batch of 726, Training in progress 11:49:49 at
  08:06:45Z, so it ends about 19:56:34Z today. Power 1352, Morale 625.0, Squad Load
  Capacity 2000, Unit HP 4167.45, Unit Attack 33.87, Unit Defense 6.96. Lv.10 shows a
  lock, so Lv.9 is this barracks' top tier. Only Speed Up.
- **Tier counts**, the same on both panels: Lv.7 1,116, Lv.8 2,141, Lv.9 1,878, Lv.10
  35.1K, Lv.6 cut off. Green arrows sit on Lv.7 to Lv.9.
- **Batch cost and slider cap** are not readable on a busy barracks; the Lv.9 and Lv.10
  cost rows stay unread until a barracks is idle and the Drill Ground has room.
- **HUD before and after, identical:** food 638.0M, iron 1.0G, coin 9.6M, diamonds
  11,136, Total Power 150,211,809. Snapshot taken with `resource_map.py snap`, coin flagged
  below its 10M floor.
- Red lines held: no diamonds, purchase, Upgrade, Train or Finish Now.
- Closing state: the base screen. No successor was enqueued.
- Follow-up: the Lv.27 batch ends about 19:56Z, the next chance to see it idle.
