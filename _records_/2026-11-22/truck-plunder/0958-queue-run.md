---
title: Truck dispatch run 0958
created: 2026-11-23T10:04:00Z
modified: 2026-11-23T10:04:00Z
version: 1.0.0
description: Continuation of trucks-2026-11-23-0711 under assignment A-20261123-0958-operator - three own trade trucks dispatched (UR, SSR, SSR) with one Trade Contract and one free refresh, 266 contracts left, returns about 13:34Z, 13:45Z and 14:18Z
status: done
grounded_in:
  - source: cu_bridge runs 20261123T095651Z-2f296a (entry miss) and 20261123T095838Z-5962a1, events, final results and frames step-0001 and step-0002, 2026-11-23T09:56Z to 10:00Z
  - source: coordinator assignment A-20261123-0958-operator (Trade Contract refreshes under the trucks profile rule 2, limits 12 per slot, 30 per run, floor 200)
---

# Truck dispatch run 0958

Rows in [0958-queue-run.csv](0958-queue-run.csv); every state change is in the
[ledger](../growth/ledger.csv) with `serves: upkeep`. Continues [0953-queue-run.md](0953-queue-run.md).

- **Entry changed.** The left-column vehicle icon at about (107,580) opened the train station
  (camera pan) this time, not Intercity Trade: with no truck returned and no red dot it is the
  train shortcut (run 20261123T095651Z-2f296a, 1 step, 0.040692 USD, nothing pressed). Tapping
  the small white truck-glyph bubbles above the parked trucks at the left of the station view
  (about 165,408; 120,438; 79,469) opens the truck offer panel directly, one per truck.
- **Offer panel.** Rarity letter, Arrives in timer, loot tiles, a dice Refresh button with a
  contract icon and owned/cost (267/1, then 266/1) and the blue Let's Go (dispatch) button
  at about (290,855); Mega Mode beside it was not touched.
- **Truck 1:** R 04:41:52, one contract refresh, then **UR 03:46:05** (iron 3.8M, bread 3.8M,
  gold 2.4M, chests, gold bar): dispatched 09:59:00Z, returns about 13:45Z.
- **Truck 2:** **SSR 03:34:26** (3.0M, 3.0M, 1.9M, 500 medals x3 twice): dispatched
  09:59:14Z, returns about 13:34Z.
- **Truck 3:** R 04:29:22, one Free refresh, then **SSR 04:17:55**: dispatched 09:59:42Z,
  returns about 14:18Z.
- **Contracts** 267 to 266 (one spent; limits 30 and floor 200 kept). Trade Count 2/5, 4/5
  at the last look, expected 5/5 (not seen). No Plunder, no diamonds, HUD diamonds unchanged.
- **Open.** The three trucks can be plundered by others on the trip (accepted by the
  profile); the next trucks unit should settle them after 13:34Z.
- **Run.** `claude-gateway/claude-sonnet-5-5`, 9 steps, 16 actions, 0.133107 USD at a stated
  cap of 0.4 (harness stops near 0.144); 0.173799 with the entry miss, 0 refused, no
  `local_input` pause.
- Closing state: the base, no panel open, token released.
