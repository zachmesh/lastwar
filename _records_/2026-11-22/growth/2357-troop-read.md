---
title: Troop read 2357
created: 2026-11-23T08:08:00Z
modified: 2026-11-23T08:08:00Z
version: 1.0.0
description: Growth continuation A-20261123-0758, barracks and hospital read - 5306 healed troops cannot be collected because of Drill Ground Full, the barracks arrow is a building Upgrade, Promote not reachable
status: run-done
grounded_in:
  - source: cu_bridge runs 20261123T075737Z-10f416, 20261123T080021Z-522249 and 20261123T080205Z-eb780c, events, final results and frames, 2026-11-23T07:57Z to 08:03Z
  - source: frames saved as _tools_/state/cu_growth_hospital_0800.png and cu_growth_train_0802.png (untracked)
  - source: coordinator addendum, collect first, ledger and snapshot rules
---

# Troop read 2357

- Rows in [2357-troop-read.csv](2357-troop-read.csv) and the ledger
  [ledger.csv](ledger.csv). Three runs, 7, 6 and 6 steps, actions done 12, 11 and 5,
  refused 0, cost 0.141037, 0.098526 and 0.077016 USD, total 0.316579. The third run went
  past the two-run limit, inside the 15-minute and 0.5 USD caps, because the second
  found the arrow was not Promote.
- **Tents:** A Barracks Lv.27 and B Barracks Lv.30 are busy (clock bubble), C Barracks
  Lv.24 is idle, D Barracks Lv.20 was not probed.
- **The portrait bubble is a Hospital bubble.** Tapped at the building beside tent D, it
  opened HOSPITAL Lv.25: Severely Wounded 364/7999, and a bar "Completed 5306" with a
  green Collect button. The bubble over tent C did nothing when tapped.
- **Collect (ledger row):** one tap gave the toast "Drill Ground Full: Unable to add 5306
  units." Nothing moved. Total Power stayed 150,211,809. So 5306 healed troops are
  finished and cannot be banked: unrealized power, held back by Drill Ground capacity.
- **The green arrow is not Promote.** On Barracks Lv.30 it opens the building Upgrade:
  Lv.30 to 31, Unit Training Cap 570 to 575, Power 283,100 to 329,100. It needs a Lv.31
  Headquarters (Construct), food 638.0M of 671.5M and coin 9.6M of 272.0M, Original Time
  83d 19:46:15, Finish Now 564,732 diamonds. Not pressed.
- **Train panel, busy barracks:** the pistol opens TRAIN UNITS with no toast. Tiers Lv.7
  1,116, Lv.8 2,141, Lv.9 1,878, Lv.10 35.1K, Lv.6 cut off. Green arrows sit on the Lv.7,
  Lv.8 and Lv.9 tabs and look like the promote markers. The panel shows only the running
  batch (Lv.10 x793, 1d 03:16:03) and Speed Up, so a promote popup never appeared. An
  arrow tap only selected the tab.
- **Promote verdict.** Unreached: a busy barracks shows no Promote, an idle one raises
  the Drill Ground Full toast and no panel. Whether promotion works with a full Drill
  Ground stays unsettled.
- **Snapshot** taken: food 638.0M, iron 1.0G, coin 9.6M, diamonds 11,136.
- Follow-up: free Drill Ground capacity first (its upgrade at 2026-11-24T09:20Z), then
  Collect the 5306 and test Promote on an idle barracks.
