---
title: Radar quick execute 1633
created: 2026-11-23T16:36:00Z
modified: 2026-11-23T16:36:00Z
version: 1.0.0
description: Unit radar-2026-11-23-0603 - Quick Execute pressed once (2 tasks, 20 energy, 120 to 100), the oil counter unchanged at 650.7K, the Bingo gift box locked, 11 task rewards left behind Claim All, which was not pressed
status: partial
grounded_in:
  - source: cu_bridge run 20261123T163306Z-d74100, final report read by the operator, 2026-11-23T16:33Z to 16:34Z
  - source: unit brief radar-2026-11-23-0603 and the radar-tasks rule digest rules 4 and 5
---

# Radar quick execute

Rows in [1633-queue-run.csv](1633-queue-run.csv). Claimed 16:33:06Z; no different-device dialog; no pin, march or troop selection.

- **Screen.** The radar map (no task list shown): pins in oil barrel, handshake and skull styles, none tapped; counter 1/40; '12 Radar Task(s) will be restored in 04:04:50', so the next restore is about 20:38Z.
- **Quick Execute.** The bar offered 'You can complete 2 tasks, requires 20 Stamina'; pressed once, **energy 120 to 100**, above the floor of 40. No dialog, no reward popup, no oil figure.
- **After.** The bar became a green **Claim All, 11 task rewards can be claimed**; not pressed (Claim All is forbidden here). The rewards wait behind it.
- **Oil counter.** 650.7K before and after: no oil came from the two tasks.
- **Bingo gift box.** One tap gave a toast 'Boost radar power to unlock it': locked, no lines, nothing to read or claim.
- **Why partial.** The 11 task rewards stay unclaimed because Claim All is the only claim button; a ruling is needed on whether release day allows it.
- **Run.** One run, 8 steps, 11 actions, 0.114712 USD, cap 0.5; 0 refused; the foreground stayed LastWar (polled every 8 s).
- **Closing state.** The base, no panel; the radar dish carries a red badge 11; Total Power 150,416,946 unchanged; token released 16:34:13Z.
