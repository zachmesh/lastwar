---
title: Passes daily pickup clipped 1011
created: 2026-11-24T10:13:00Z
modified: 2026-11-24T10:13:00Z
version: 1.0.0
description: Unit passes-2026-11-23-2257 - closed 'blocked by route: Claim clipped': the S1 Drone Parts Daily Pickup (gear item x15, total x105) has a green Claim with a red dot cut off at the bottom edge of the shop page; ONE drag up from mid-page (394,700 to 394,380) at 10:11:56.6Z did not move the page; two taps at (572,914) and (572,913) changed nothing; Free Supply Claimed, S2 'Already claimed today'; diamonds 11,153; drags 1 tried, 0 cancelled
status: partial
grounded_in:
  - source: cu_bridge run 20261124T101125Z-d791c2, final report read by the operator, 2026-11-24T10:11Z to 10:13Z
  - source: unit brief passes-2026-11-23-2257 and the shop-claims rule digest
---

# Passes daily pickup clipped 1011

Rows in [1011-queue-run.csv](1011-queue-run.csv). Claimed 10:11:25Z; no different-device dialog.

- **S1 Drone Parts.** The Daily Pickup (gear item x15) is **not claimed**: its green Claim is clipped at the bottom edge of the shop page; one drag up from mid-page did not move the page; two taps changed nothing: closed **blocked by route: Claim clipped**.
- **Others.** Free Supply Claimed; S2 Drone Components 'Already claimed today'; diamonds 11,153 unchanged.
- **Counts.** Drags 1 tried, 0 cancelled; wait 0 s; the same block as 04:43Z to 05:01Z.
- **Run.** One run, 13 steps, 12 actions, 0.147535 USD, cap 0.5; 0 refused; foreground stayed LastWar.
- **Closing state.** The base, no panel; token released 10:12:58Z.
