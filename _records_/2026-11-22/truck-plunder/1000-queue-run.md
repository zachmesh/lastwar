---
title: Own truck dispatch 1000
created: 2026-11-24T10:09:30Z
modified: 2026-11-24T10:09:30Z
version: 1.0.0
description: Unit trucks-dispatch-2026-11-24-001 - three own trucks dispatched by rule 2: an SR (arrives in 04:53:35, after a free dice and one Trade Contract refresh), an SSR (04:07:28, as rolled) and a UR (04:00:10, after a free dice and two contract refreshes); trade count 3/5; contracts 261 to 258; no returned truck to settle; the PATH to the Intercity Trade screen: the tram icon (107,580) with a red badge 3 at 10:02:13.551Z opens it on 'Others' Trucks' (the plunder list, pressed nothing); the Your Truck tab at (479,942); drags 0
status: done
grounded_in:
  - source: cu_bridge run 20261124T100510Z-ad2994, final report read by the operator, 2026-11-24T10:00Z to 10:09Z
  - source: unit brief trucks-dispatch-2026-11-24-001 and the truck-plunder rule digest
---

# Own truck dispatch 1000

Rows in [1000-queue-run.csv](1000-queue-run.csv). Claimed 10:00:01Z; no different-device dialog.

- **Path.** Tram icon (107,580) with a **red badge 3**: one tap at **10:02:13.551Z** opens **INTERCITY TRADE** on **Others' Trucks** (the plunder list: count 0/4, nothing pressed); the **Your Truck** tab (479,942) holds the own slots; each empty slot's plus opens the dispatch dialog.
- **Settled.** None: no returned truck (the badge 3 was the three empty slots).
- **Dispatched (rule 2).** **SR** arrives in 04:53:35 (about 14:59:21Z), **SSR** 04:07:28 (about 14:13:31Z), **UR** 04:00:10 (about 14:07:11Z); count **3/5**; Trade Contracts **261 to 258** (three refreshes); no diamond; no Mega Mode.
- **Plunder list.** Not touched. **Chrome for Testing** (an owner-side job) was in front 10:00:05Z to 10:01:01Z.
- **Run.** One run, 43 steps, 38 actions, 0.392 USD, cap 0.5; 0 refused; foreground stayed LastWar.
- **Closing state.** The base, no panel; token released 10:09:08Z.
