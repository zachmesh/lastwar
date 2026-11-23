---
title: Train boarding 1014
created: 2026-11-23T10:18:00Z
modified: 2026-11-23T10:18:00Z
version: 1.0.0
description: Alliance train boarded at carriage 2 with a 3 Trade Contract ticket under the standing rule, taken as an interrupt of the T1 test with 2:50 left on the boarding banner
status: done
grounded_in:
  - source: cu_bridge run 20261123T101405Z-d2f7c5, events, final result and frames step-0005 and step-0006, 2026-11-23T10:14Z to 10:15Z
  - source: alliance-train rule digest rules 1, 2, 5 and 6, standing instruction board carriage 2 with 3 Trade Contracts
---

# Train boarding 1014

Rows in [1014-queue-run.csv](1014-queue-run.csv); ledger row 10:14:46Z, serves `upkeep`.

- **Why.** A "Boarding closes in 00:02:55" pop-up covered the donation test at 10:13:25Z; the
  standing interrupt rule says board first when 70 seconds or more remain (digest 1, 6).
- **Route.** The pop-up opened the Station Platform (timer 00:06:10); the plus of **carriage 2**
  (rule 2) opened THANK THE CONDUCTOR; the quantity went 1 to **3** with the plus button
  (read exactly 3 before the press); **Gift Contract** at 10:14:46.240Z. Stock read **266**
  Trade Contracts before the gift (about 263 after, not read).
- **Result.** The owner avatar replaced the plus in carriage 2. The occupancy label read 17/7
  before and after, so the headcount did not prove the boarding; the banner came back at
  00:00:54 on the base. Departure timer 00:06:10 at 10:14:55Z, so the train leaves about 10:21Z.
- **Open.** Claim the "Train arrival reward" Event mail after the ride (digest 7); the Like and
  Thank button was not used; the 266 count is above the 200 floor of the truck assignment.
- **Run.** `claude-gateway/claude-sonnet-5-5`, 9 steps, 14 actions, 0.118 USD at a stated cap of
  0.4 (harness stops near 0.144), 0 refused, no `local_input` pause. No diamonds, no summon, no
  conductor role.
- Closing state: the base, no panel open, token released.
