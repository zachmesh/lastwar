---
title: Resource map and floors
created: 2026-11-23T07:46:59Z
modified: 2026-11-23T07:46:59Z
version: 0.1.0
sequence: 6
description: Every run that reads the HUD records a snapshot with _tools_/resource_map.py snap, and every run checks
---
## Resource map and floors

- Every run that reads the HUD records a snapshot with
  `_tools_/resource_map.py snap`, and every run checks
  `_tools_/resource_map.py check` before spending anything.
- Floors live in `_tools_/resources.json`: coin warns below 10M and
  is critical below 2M; food and iron warn below 50M.
- State on 2026-10-25 evening - **coin is critical at 565.1K**
  (the owner's own Lv.30 building and research session spent it
  down). Research is the giant coin sink at this tier - the four
  T10 gatekeeper nodes in Special Forces cost over 500M coin
  combined (Packsify research guide) - so coin is a campaign,
  not a one-day fix: research and construction pacing is the
  throttle (owner decisions), and income is pushed steadily.
  Push plan, in order: the weekly Gold Zombie event (the largest
  gold source in the guides - hoard stamina for it, rally the
  boss), intercity trucks (1.2M to 2.4M gold per truck, four a
  day), truck plunder under the shard rule (about 600K gold per
  UR truck), Monica-led world map zombie kills (+25% gold per
  the guides, if she is the fielded treasure hunter), VIP
  freebie boxes, radar rewards. No new coin-heavy commitment is
  started while coin is critical.
- The user's word "stone" maps to iron - the base game has food,
  iron and coin; seasons add their own (this season: coal and
  titanium alloy, both tracked in the resource map).
- Food 276.9M and iron 267.6M are healthy against their floors;
  their steady sinks are training batches (5.5M each at T10) and
  they refill from the same truck cycle.

