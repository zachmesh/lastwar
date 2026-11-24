---
title: S1 claim experiment six wait unit 1254
created: 2026-11-24T12:55:30Z
modified: 2026-11-24T12:55:30Z
version: 1.0.0
description: Unit passes-s1-claim-experiment-2026-11-24-006 - stopped before the batch: the model's wait action takes only whole SECONDS (the parameter duration, an integer from 1 to 300): it cannot send wait with duration_ms 300 or 100; what it can send in one message: mouse_move, left_mouse_down, left_mouse_up, left_click_drag, scroll and wait in whole seconds; no batch sent (so no refusal text), no pan (count 0), no Claim tap (the S1 Claim clipped at y about 915), no Iron or Coin read; the shop was closed by the model with its back arrow; drags 0; tram badge none
status: partial
grounded_in:
  - source: cu_bridge run 20261124T125355Z-fac89f, final report read by the operator, 2026-11-24T12:53Z to 12:55Z
  - source: unit brief passes-s1-claim-experiment-2026-11-24-006 and the shop-claims rule digest
---

# S1 claim experiment six wait unit 1254

Rows in [1254-queue-run.csv](1254-queue-run.csv). Claimed 12:53:55Z; no different-device dialog.

- **Stopped before the batch.** The model's wait action takes only whole seconds (duration, 1 to 300): it cannot send wait with duration_ms 300 or 100; no batch sent, no refusal, no pan.
- **What it can send in one message.** mouse_move, left_mouse_down, left_mouse_up, left_click_drag, scroll and wait in whole seconds.
- **Variant for Steer A.** A composed pan with whole-second waits (1 s each, about 8 s with the button down); the unit's one retry is unused.
- **Nothing pressed.** No pan, no Claim tap, no Iron or Coin read; the shop closed; tram badge none; drags 0.
- **Run.** One run, 7 steps, 9 actions, 0.093335 USD, cap 0.5; 0 refused; foreground stayed LastWar.
- **Closing state.** The base, no panel; token released 12:54:52Z.
