---
title: Box sample batch 1
created: 2026-11-23T09:20:00Z
modified: 2026-11-23T09:30:00Z
version: 2.0.0
description: Assignments A-20261123-0925 and A-20261123-0921 of the operator - batch 1 of the bounded Mystery Supply Box sample complete at n=10, nine blue-frame SR choice chests and one Refined Iron Module x20, no shards, no diamonds; one local_input pause retried once
status: done
grounded_in:
  - source: cu_bridge runs 20261123T091324Z-8428ef, 20261123T091529Z-14f618, 20261123T091640Z-e3a6bc, 20261123T092205Z-e727f5, 20261123T092256Z-aab5c3, 20261123T092426Z-262280 and 20261123T092603Z-8e9f57, events, final results and frames, 2026-11-23T09:13Z to 09:27Z
  - source: coordinator assignments A-20261123-0925-operator and A-20261123-0921-operator, owner-delegated via Steer A
---

# Box sample batch 1

Rows in [0913-box-sample-1.csv](0913-box-sample-1.csv); each Use is also in the
[ledger](ledger.csv) with `serves: box sample`. Boxes are numbered n of 22; n=1 is the
08:55:43Z opening in [0054-box-chest-read.md](0054-box-chest-read.md).

- **Result, n=1 to 10.** Nine boxes paid one chest tile x1 on a **blue frame** (an SR
  choice chest by colour: on the Resources tab UR is orange, SSR purple, SR blue). One box,
  n=5 (09:17:27Z), paid **Refined Iron Module x20, green frame**, named by run
  20261123T092205Z-e727f5 in the Gear tab (stack 36.1K; "Assemble 4 Refined Iron Modules to
  create a Superalloy."). **No shard, no diamonds, no medals, no cost prompt in ten boxes.**
  Box count 366 to 356.
- **Safeguard held.** Before every Use the name read Mystery Supply Box, the number field
  exactly 1, the slider at the far left and the button just Use. The slider returns to the
  full count after each Use, so each box needed its own drag.
- **Unchanged.** Diamonds 11,136 and Total Power 150,211,809 at the start and end of
  every box run (iron read 1.0G; one end read gave 1.06G, a misread).
- **local_input pause.** Run 20261123T092426Z-262280, `local_input` pointer event at
  **09:24:42.854Z** (step 2, after the box tile was selected; no Use pressed); I stopped it at
  09:25:31Z and retried once from the open Backpack, run 20261123T092603Z-8e9f57, which
  finished. Other jobs on the Mac then: `mut1368.sh` (since 09:16Z), `gap-3146.sh` and
  `/tmp/cu-coord/wait.sh` (09:24Z), `at-pause-gates.sh`, `winq3.sh`, `m607-window.sh`.
- **Cost.** 7 runs, 49 steps, 0 refused, 0.664553 USD (0.123103, 0.085424, 0.124637,
  0.068094, 0.126998, 0.048272 stopped, 0.088025); stated cap 0.4 per run. Nothing spent.
  The token was held only around live runs (and across the stop and retry).
- **Reading.** Ten boxes, one pool result: a choice chest 90 percent, a green material
  10 percent; no shards or diamonds seen (n=10, small sample).
- Closing state: the base, no panel, token released. Batch 2, eleven boxes, awaits the
  Strategist's word.
