---
title: S1 claim experiment five composed pan refused 1248
created: 2026-11-24T12:51:00Z
modified: 2026-11-24T12:51:00Z
version: 1.0.0
description: Unit passes-s1-claim-experiment-2026-11-24-005 - the FIRST COMPOSED PRESS: the model sent the 15-action batch (mouse_move, left_mouse_down, waits, five moves, left_mouse_up, screenshot) in ONE message at 12:49:25.6Z and the tool REFUSED it whole: 'Action 0 (mouse_move) failed: refused (batch_refused): nothing ran: action 2 was refused (malformed)'; action 2 was the first wait: 'a wait inside a press needs a positive whole duration_ms' (the model sent a whole-second wait of 0); nothing ran: no button was pressed, the page did not move (S2 title y 531), no Claim tap, no correction; the shop was closed by a short run; drags 0; tram badge none
status: partial
grounded_in:
  - source: cu_bridge run 20261124T124841Z-948b80, final report read by the operator, 2026-11-24T12:48Z to 12:51Z
  - source: unit brief passes-s1-claim-experiment-2026-11-24-005 and the shop-claims rule digest
---

# S1 claim experiment five composed pan refused 1248

Rows in [1248-queue-run.csv](1248-queue-run.csv). Claimed 12:48:40Z; no different-device dialog.

- **Composed press refused.** The model sent the 15-call batch in ONE message at 12:49:25.6Z; the tool refused it whole: 'batch_refused: nothing ran: action 2 was refused (malformed)'.
- **Cause.** Action 2 (the first wait): 'a wait inside a press needs a positive whole duration_ms': the model used a whole-second wait of 0; the dwells must be sent as duration_ms (300, 100).
- **Nothing ran.** The page unmoved (S2 title y 531, S1 Claim y about 915): no pan, no correction, no Claim tap; the shop closed by a short run.
- **Event.** events.jsonl lines 28 to 42 of run 20261124T124841Z-948b80 (outside the workspace; the lines copied in the CSV).
- **Run.** One run, 8 steps, 7 actions, 0.17 USD, cap 0.5; 0 refused; foreground stayed LastWar.
- **Closing state.** The base, no panel; token released 12:50:27Z.
