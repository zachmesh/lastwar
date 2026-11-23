---
title: Age of Oil research survey blocked
created: 2026-11-23T13:05:00Z
modified: 2026-11-23T13:05:00Z
version: 1.0.0
description: Unit research-age-of-oil-survey-2026-11-23-001 - blocked because both labs are busy (Food Output V and Coin Output V, started by the other device) and the flask then opens only the Research Queue list, with no route to the tech trees; nothing pressed
status: partial
grounded_in:
  - source: cu_bridge run 20261123T125632Z-f6b90b, events and final result, 2026-11-23T12:56Z to 12:57Z
  - source: unit brief research-age-of-oil-survey-2026-11-23-001 (planner, OD-18 and OD-19) and the coordinator resume order of 12:49Z
---

# Age of Oil research survey, blocked

Rows in [1257-age-of-oil-survey.csv](1257-age-of-oil-survey.csv). Claimed 12:56:32Z; the no-click first frame showed no different-device dialog and
the HUD of 12:51Z (coin 55.9K, Total Power 150,413,046).

- **Both labs are busy.** Slot 1 "Lv.0 **Food Output V** upgrade in progress", 1d 04:33:08 left at about 12:56:50Z (ends about 2026-11-24T17:29:58Z);
  slot 2 "Lv.0 **Coin Output V** upgrade in progress", 1d 02:02:20 left (ends about 2026-11-24T14:59:10Z). Both are nodes of the Age of Oil
  path; the other device started them (coin 14.4M to 55.9K, unexplained, other device).
- **Defense Training VIII is gone** from the queue (it read 2d 19:10:43 left at 12:08Z); cancelled or replaced between 12:12Z and 12:56Z, not by
  the operator.
- **No route to the trees.** With an idle lab the flask opened the Special Forces tree directly (12:04Z); with both busy it opens only the
  Research Queue list (11:29Z, 12:56Z), whose rows have only Speed Up buttons and whose row pictures do nothing. No hub, no tree, no
  node panel, and no research speed percent were reachable; every node of the Age of Oil path is unread.
- **Options (not taken).** Wait for the first lab to idle (about 2026-11-24T14:59Z); or find the Tech Center building (unlocated since B1) and
  read the hub from its radial menu, one 12-turn run of building taps.
- **Run.** `claude-gateway/claude-sonnet-5-5`, 4 steps, 0 refused, no `local_input` pause, 0.096753 USD (stated cap 0.6). Nothing pressed
  beyond the flask icon and the panel X.
- Closing state: the base, no panel, token released.
