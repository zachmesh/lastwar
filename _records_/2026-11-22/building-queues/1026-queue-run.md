---
title: Growth fill read 1026
created: 2026-11-23T10:31:00Z
modified: 2026-11-23T10:31:00Z
version: 1.0.0
description: Unit building-queues-growth-fill-2026-11-23-004 - builders and labs read, all busy, nothing to fill; the barracks training queues were not read because the Barracks Lv.24 tent was not found
status: partial
grounded_in:
  - source: cu_bridge run 20261123T102543Z-fa696e, events, final result and frames, 2026-11-23T10:25:43Z to 10:27:20Z
  - source: unit brief building-queues-growth-fill-2026-11-23-004 (planner, decision record 2350) and building-queues rule digest rules 1, 3, 4, 5 and 7
---

# Growth fill read 1026

Rows in [1026-queue-run.csv](1026-queue-run.csv). Claimed 10:25:13Z, window end 10:35Z.

- **HUD.** Food 648.5M, iron 1.0G, coin 14.4M, diamonds 11,136, Total Power 150,211,809, unchanged
  at the start and end.
- **Builders (4 of 4 busy, rule 1).** Four Training Base upgrades to Lv.25, 22:54:22 to 22:54:32 left
  at 10:25:51Z, finishing about **2026-11-24T09:20:13Z to :17Z**; no builder is idle.
- **Labs (2 of 2 busy).** Unlock Oil Well Lv.0, 01:16:54 left at 10:26:00Z, frees about
  **11:42:54Z** (the unit research-growth-convert-2026-11-23-001); Defense Training VIII Lv.7,
  2d 20:53:01 left, ends 2026-11-26T07:19Z. No COMPLETE button showed.
- **Training queues, not read.** The tents tapped read Barracks Lv.30, Lv.20 and Lv.20; an
  empty-ground tap selected a Farmland Lv.28 (tag read only); a tap on a third tent opened a
  Barracks Lv.20 to 21 upgrade info panel, closed with its X, nothing pressed. The Lv.24 tent and the
  two clock-bubble tents (the Lv.27 batch) were not read; no toast or TRAIN UNITS panel appeared.
  No pistol was tapped.
- **Fill.** Nothing idle at builders or labs, so nothing was started and the unit spent nothing;
  the training fill stays blocked by Drill Ground Full (the earlier read) and the hospital
  Collect was not retried.
- **Gap.** The barracks are not told apart from the base view: the camera drifts between runs
  and tents show no label until tapped. A fixed route (tap a building from the left-column
  shortcut, or read its clock bubble) is needed for the training read.
- **Run.** `claude-gateway/claude-sonnet-5-5`, 10 steps, 19 actions, 0 refused, no `local_input`
  pause, 0.163455 USD (stated cap 0.5 for 11 usable turns; the unit budget is 8 steps).
- Closing state: the base, no panel open, token released.
