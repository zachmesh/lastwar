---
title: Oil Well locate 1541
created: 2026-11-23T15:46:00Z
modified: 2026-11-23T15:46:00Z
version: 1.0.0
description: Read-only search for the Oil Well building by tag text - 8 buildings and 2 base pans in 12 turns found Smelter, Iron Mine, Gold Mine, Material Workshop and Tavern but no Oil Well; the upper left and top of the base were never in view; no preview read
status: partial
grounded_in:
  - source: cu_bridge run 20261123T154120Z-b841fc, events and the final report, 2026-11-23T15:41Z to 15:44Z
  - source: coordinator assignment of 15:37Z (read-only locate, 12 turns, never Upgrade, Finish Now, Speed Up, Obtain, Collect or Details)
---

# Oil Well locate

Rows in [1541-oil-well-locate.csv](1541-oil-well-locate.csv). An assignment, not a queue unit; no ledger row (no state changed). The desktop lock was free; no different-device dialog; nothing pressed except the WORLD and BASE button, building taps and two map pans.

- **Result: not found.** After WORLD then BASE the run tapped 8 candidates, one building per frame. Tags read: **Smelter Lv.26** (top left, about 330,250), **Iron Mine Lv.27** (left, about 215,472), **Gold Mine Lv.28** (left, about 172,580), **Material Workshop Lv.20** (top left, about 152,182) and **Tavern Lv.20** (about 527,680 after the first pan). The grey tanks at the bottom of the frame show no selection tag, so they are decoration.
- **Pans.** Two drags from bare ground, (540,780) to (290,530) and (400,470) to (150,220); both move the view toward the **bottom right**, to the open snow beyond the south-east wall.
- **Areas covered.** The core base (HQ, airfield, the top-left industrial cluster), the left mines and farmland, the centre and right tents, the bottom troop grounds and wall. **Not in view:** the upper left and the top of the base.
- **Not read.** No Oil Well tag, storage, output or Lv.N to N+1 preview; the green arrow was never pressed.
- **Next.** The well was built by the other device at about 12:26Z [G]; a second search should pan the other way (drag from about 290,450 to 540,700) to bring the upper left and top into view, or take the Steer A word to press the OIL panel's Details button.
- **Run.** `claude-gateway/claude-sonnet-5-5`, 13 steps, 0.226382 USD against a stated cap of 0.5; 0 refused. The tag rows join the tag index.
- **Closing state.** The base view panned to near the bottom-right edge, no panel or selection; LastWar frontmost. The next run starts with WORLD then BASE.
