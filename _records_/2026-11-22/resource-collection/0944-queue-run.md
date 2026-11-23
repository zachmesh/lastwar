---
title: Harvest run 0944
created: 2026-11-23T09:48:00Z
modified: 2026-11-23T09:48:00Z
version: 1.0.0
description: Unit harvest-2026-11-23-0709 - Armed Truck check (not fully loaded) and panel Collect for food, iron and coin, each pool taken once and verified, Total Power unchanged
status: done
grounded_in:
  - source: cu_bridge run 20261123T094453Z-c44922, events, final result and frames, 2026-11-23T09:44:53Z to 09:45:50Z
  - source: unit brief harvest-2026-11-23-0709 (planner A-20261123-0706), resource-collection rule digest rules 1, 4, 5 and 9, coordinator assignment A-20261123-0943-operator
---

# Harvest run 0944

Rows in [0944-queue-run.csv](0944-queue-run.csv); the three Collects are also in the
[ledger](../growth/ledger.csv) with `serves: upkeep`.

- **Armed Truck first (rule 9).** The blue truck had no loot bubble or full-load indicator, only
  a round marker. Not fully loaded, nothing to claim; the truck was not tapped. The panel
  entry route stays unrecorded.
- **Panel Collect (rule 5), one tap per resource.**
  - Food: Available 2,116,639, Owned 641,338,706 to **643,475,084** (+2,136,378), Available 0.
  - Iron: Available 1,659,829, Owned 1,066,239,631 to **1,067,900,324** (+1,660,693), Available 0.
  - Coin: Available 1,405,869, Owned 9,760,629 to **11,178,643** (+1,418,014), Available 0.
- **HUD, start to end.** Food 641.3M to 643.4M, iron 1.0G both, coin 9.7M to 11.1M,
  diamonds 11,136 both, **Total Power 150,211,809 both** (building output has no power).
  Coin is now 1.18M above the 10M reserve.
- **Method.** No bubble taps; the panels take the whole accumulated pool at once (rule 5,
  Issue #585), each panel closed with its own X in the same turn as the next icon tap.
- **Run.** `claude-gateway/claude-sonnet-5-5`, max-steps 8, completed in 8 steps, 18
  actions done, 0 refused, no `local_input` pause, 0.096084 USD against a stated cap of
  0.60 (harness stops near 0.216). Token held from 09:44Z across the next read, as
  allowed while a run is live.
- Closing state: the base, no panel open.
