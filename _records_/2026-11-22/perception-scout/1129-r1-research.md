---
title: Research slots R1
created: 2026-11-23T11:34:00Z
modified: 2026-11-23T11:34:00Z
version: 1.0.0
description: Unit scout-midday-growth-snapshot-2026-11-23-006 - both research slots read (Unlock Oil Well 13 minutes left, Defense Training VIII 2d 19:49); the tech hub trees were not reached from the queue panel
status: partial
grounded_in:
  - source: cu_bridge run 20261123T112935Z-43e7e9, events and final result, 2026-11-23T11:29:35Z to 11:30:30Z
  - source: unit brief scout-midday-growth-snapshot-2026-11-23-006 (Story 868, R1), coordinator assignment A-20261123-1129-operator with the 11:40Z hard stop, research-queue how-it-is-p1
---

# Research slots R1

Rows in [1129-r1-research.csv](1129-r1-research.csv). Claimed 11:29:13Z; token released 11:31Z, before the 11:40Z hard stop.

- **Slot 1.** Unlock Oil Well **Lv.0**, 00:13:11 left at about 11:29:44Z (00:13:04 seven seconds later), so it frees about
  **11:42:55Z**; the research conversion unit goes first.
- **Slot 2.** Defense Training VIII **Lv.7**, 2d 19:49:18 left, ends about 2026-11-26T07:19:02Z. No slot is idle and no
  COMPLETE button showed.
- **Tech hub: not reached.** The flask tap at (110,258) opened the RESEARCH QUEUE list panel (two rows, an X at its top right,
  no back arrow). A tap on the first row's picture at (222,463) did nothing; the panel has no route to the hub. The trees
  with percent and badge and the Valor Badge balance are unread; the 2026-11-11 hub read (Development 84%, Economy 98%,
  Hero 68%, Units 77%, Squad 2 11%, Intercity Truck 95%) is stale.
- **Next.** The hub opens from the research tree (when the flask tap opens it, as on 2026-11-11) or from the Tech Center
  building, which is still unlocated; try after the lab frees and the flask opens a tree.
- **Run.** `claude-gateway/claude-sonnet-5-5`, 4 steps, 6 actions, 0 refused, no `local_input` pause, 0.048347 USD
  (stated cap 0.5). Nothing pressed beyond the flask icon, the first row picture and the panel X.
- Closing state: the base, no panel, token released.
