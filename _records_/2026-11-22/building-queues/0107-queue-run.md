---
title: Building queues queue run 0107
created: 2026-11-23T09:12:00Z
modified: 2026-11-23T09:12:00Z
version: 1.0.0
description: Growth fill unit building-queues-growth-fill-2026-11-23-002, operator seat, read-only look at builders and labs - all busy, nothing idle to fill, the barracks reads cut short by a wrong tent
status: run-partial
grounded_in:
  - source: cu_bridge start, status poll, events and final result on run 20261123T090741Z-a98618, 2026-11-23T09:07Z to 09:08Z
  - source: barracks reads at 08:06Z in run 20261123T080610Z-7faa88 and the Lv.24 toast at 08:26Z in run 20261123T082546Z-831319, cited for the training queues
---

# Building queues queue run 0107

- Unit building-queues-growth-fill-2026-11-23-002, operator seat, assignment
  A-20261123-0906-operator with the coordinator's correction (001 had expired), attempt
  1, claimed 09:07:35Z. Rows in the sidecar [0107-queue-run-detail.md](0107-queue-run-detail.md).
- Run `20261123T090741Z-a98618`, model `claude-gateway/claude-sonnet-5-5`, max-steps 8,
  ended `completed` after 5 steps. Actions done 12, refused 0. Model time 6.2 s per step.
  Cost 0.104995 USD against a stated 0.60 cap (the harness stops near 0.36 of it). No
  takeover, no pointer pause, no account dialog, no boarding banner.
- **Builders, 4 of 4 busy.** Lv.25 Training Base on all four rows, 1d 00:12:24 to
  1d 00:12:35 left at 09:07:54Z, so they finish 2026-11-24T09:20:18Z to 09:20:29Z. No
  Complete button. No idle builder, so no miss.
- **Labs, 2 of 2 busy.** Unlock Oil Well Lv.0, 02:34:56 left at 09:08:06Z, finishes about
  11:43:02Z. Defense Training VIII Lv.7, 2d 22:11:03 left, finishes about
  2026-11-26T07:19:09Z. No idle lab, no Complete button.
- **Training queues, from the 08:06Z and 08:26Z reads:** Barracks Lv.30 busy (Lv.10 x793,
  ends about 2026-11-24T11:18:31Z); Barracks Lv.27 busy (Lv.9 x726, ends about
  19:56:34Z today); Barracks Lv.24 idle, but its pistol only gives "Drill Ground Full:
  Unable to add more units.", so that slot is a MISS caused by capacity, not fillable.
  This run's own barracks read stopped: the tent tapped read Barracks Lv.20, I stopped by
  rule, and no pistol was pressed.
- **Fill:** nothing started. HUD: food 641.3M, iron 1.0G, coin 9.7M, diamonds 11,136,
  Total Power 150,211,809. Snapshot taken; coin is flagged below its 10M floor.
- Closing state: the base, no panel, no toast.
- Red lines held: no Train, Collect, Speed Up, Research or purchase.
- Blocker f: Drill Ground Full blocks every training start. Follow-up: first free
  lab about 11:43Z and first builder 2026-11-24T09:20Z belong to their own units.
