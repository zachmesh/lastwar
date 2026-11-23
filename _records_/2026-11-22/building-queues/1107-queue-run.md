---
title: Growth fill read 1107
created: 2026-11-23T11:20:00Z
modified: 2026-11-23T11:20:00Z
version: 1.0.0
description: Unit building-queues-growth-fill-2026-11-23-006 - builders, labs and all four barracks training queues read with the tag text beside every number; everything busy except Barracks Lv.24 and Lv.20, which are blocked by Drill Ground Full; nothing started
status: done
grounded_in:
  - source: cu_bridge runs 20261123T110751Z-3bb1c9 (builders, labs, three barracks; ended at max_steps with the Lv.27 panel open) and 20261123T111130Z-ddc38b (close-out and Barracks Lv.30), frames and events, 2026-11-23T11:07Z to 11:13Z
  - source: unit brief building-queues-growth-fill-2026-11-23-006 (planner, decision record 2350), building-queues rule digest rules 1, 4, 5 and 7, the 1030 base map
---

# Growth fill read 1107

Rows in [1107-queue-run.csv](1107-queue-run.csv). Claimed 11:06:57Z, window end 11:35Z.

- **Builders (4 of 4 busy).** Four Training Base upgrades to Lv.25, 22:12:13 to 22:12:23 left at about
  11:08:00Z, finishing about **2026-11-24T09:20:13Z to :23Z**.
- **Labs (2 of 2 busy).** Unlock Oil Well Lv.0, 00:34:46 left at 11:08:08Z, frees about **11:42:54Z**
  (the research-growth-convert unit's); Defense Training VIII Lv.7, 2d 20:10:53 left. No COMPLETE button.
- **Barracks, by tag text.** **Barracks Lv.24**: toast "Drill Ground Full: Unable to add more units." at 11:08:22Z.
  **Barracks Lv.20**: the same toast at 11:09:15Z. **Barracks Lv.27**: TRAIN UNITS, Lv.9 batch of 726,
  "Training in progress 08:46:34", finishing about **19:56:30Z**. **Barracks Lv.30**: TRAIN UNITS, Lv.10 batch of
  793, "Training in progress 1d 00:06:14" at 11:12:10Z, finishing about **2026-11-24T11:18:24Z**. The Lv.30
  panel showed Squad Load Capacity 2200 and Morale 750.0; the Lv.27 panel 2000 and 625.0.
- **Idle slots (MISS).** Barracks Lv.24 at 11:08:22Z and Barracks Lv.20 at 11:09:15Z are idle but blocked by the
  full Drill Grounds; no start was possible and none was tried. No builder or lab slot was idle.
- **Fill.** Nothing started or spent; Speed Up was not pressed on either panel. HUD unchanged: food 648.5M, iron
  1.0G, coin 14.4M, diamonds 11,136, Total Power 150,211,809.
- **Reading, unverified.** A "112min" survivor bubble at the lower left counted down 116 to 111 minutes between
  11:04Z and 11:09Z; unread.
- **Run.** `claude-gateway/claude-sonnet-5-5`, 12 + 8 steps, 0 refused, no `local_input` pause, 0.188781 and
  0.108910 USD, 0.297691 in all (stated cap 0.6 and 0.4). The first run ended at max_steps with the Lv.27 panel
  open, closed by the second run; the WORLD then BASE toggle sometimes needs a third tap.
- Closing state: the base, fresh frame, no panel, token released.
