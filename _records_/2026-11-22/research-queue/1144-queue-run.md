---
title: Research conversion run 1144
created: 2026-11-23T12:10:00Z
modified: 2026-11-23T12:10:00Z
version: 1.0.0
description: Unit research-growth-convert-2026-11-23-001 - Unlock Oil Well completed (power +3,900), the Drill Ground Expansion node not found in the Development tree, nothing converted or started; the second research slot stays idle
status: partial
grounded_in:
  - source: cu_bridge runs 20261123T115241Z-cb0c2b (Complete, paused), 20261123T115451Z-f92ecc, 20261123T115642Z-9c9d0e, 20261123T115826Z-dcbc2d and 20261123T120037Z-99d0f8, frames and events, 2026-11-23T11:52Z to 12:01Z
  - source: unit brief research-growth-convert-2026-11-23-001, 2430-conversion-rules, coordinator assignment A-20261123-1144-operator
---

# Research conversion run 1144

Rows in [1144-queue-run.csv](1144-queue-run.csv); ledger row 11:53:00Z. Claimed 11:45:03Z. The first start was refused until 11:52:41Z
("another desktop run holds this Mac (seat cu-integrator, run gate-pr895-pf, since 11:43:02Z); D-024").

- **Complete.** Research on Unlock Oil Well, finished at 11:42:55Z, was completed at **11:53:00.984Z**: toast **POWER +3,900**, Total Power
  **150,211,809 to 150,215,709**; research slot 1 became idle. The Research button at (550,464) of that row opened the TECH hub.
- **Pause.** The run was paused by a `local_input` pointer event at **11:53:16.761Z** (step 4). I stopped it and retried once. Other
  jobs then: cu-team node `--test` runs (sessions gate-code and cu720), headless Chrome, a verifier mutant build earlier; no
  winq or mut script of mine.
- **Tech hub (read 11:53Z):** Development 84%, Economy 98%, Hero 69%, Units 77%, Squad 1 Max Level, Squad 2 11%, Alliance Duel Max
  Level, Intercity Truck 95%, Special Forces 73% (Boost Power, badge 1); the slot bar shows slot 2 idle.
- **Development tree, nodes named by tag text:** Infirmary Expansion III 4/5 (Hospital's Capacity, +4% to +5%): coin 14.4M of **20.1M**
  (short), iron 6.7M, food 6.7M, Tech Center Lv.21 met, **2d 12:57:11** effective; Barracks Expansion III 4/5 (Number of Trainees, +2% to
  +2.5%): same costs; Research Enhancement III, Infirmary and Barracks Expansion II, Research Enhancement II, Rapid Field Dressing
  II, Focused Training II, Master Craftsman and Fast Builder II are **MAX**; **Extra Barracks is MAX (Unlocked)**.
- **Drill Ground Expansion: not found** in the nodes opened; the tree continues below, or it sits in another tree. Per the brief
  nothing was converted and nothing started (coin 14.4M unchanged).
- **Idle lab.** Slot 2 has idled since 11:42:55Z. The candidates read need 20.1M coin (5.7M short, 15.7M above the 10M reserve),
  one UR Coin Chest is 2.4364M.
- **Run.** `claude-gateway/claude-sonnet-5-5`, five runs, 34 steps, 0 refused, 0.484035 USD in all (0.065002, 0.045525, 0.117880, 0.190226, 0.065402), no Research pressed. HUD at the end: food 648.5M, iron
  1.0G, coin 14.4M, diamonds 11,136.
- Closing state: the base, no panel, token released.
