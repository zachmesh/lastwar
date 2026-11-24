---
title: S1 Drone Parts claimed by the two-second composed pan 1301
created: 2026-11-24T13:03:10Z
modified: 2026-11-24T13:03:10Z
version: 1.0.0
description: Unit passes-s1-claim-experiment-2026-11-24-007 - THE FIRST WORKING PAN: one composed drag in ONE message (mouse_move (685,650); left_mouse_down; wait 1 s; mouse_move (685,475); wait 1 s; left_mouse_up; screenshot) at 13:01:54.9Z moved the Weekly Pass page 150 px (the S2 'Get Now' row y 682 to 532; the S1 title y 769 to 619): the S1 Claim went from y about 915 (clipped) to y 765, fully inside the content with a plain Claim label; ONE tap at (572,767) at 13:02:09.8Z paid Drone Parts x15; the S1 card now 'Already claimed today'; no correction pan; the Iron and Coin cards never came into view; diamonds 11,153; drags 1; tram badge none
status: done
grounded_in:
  - source: cu_bridge run 20261124T130118Z-dbbafb, final report read by the operator, 2026-11-24T13:01Z to 13:03Z
  - source: unit brief passes-s1-claim-experiment-2026-11-24-007 and the shop-claims rule digest
---

# S1 Drone Parts claimed by the two-second composed pan 1301

Rows in [1301-queue-run.csv](1301-queue-run.csv). Claimed 13:01:18Z; no different-device dialog.

- **The pan.** One composed drag in ONE message (down, wait 1 s, move, wait 1 s, up), (685,650) to (685,475), 175 px from the blank margin, at 13:01:54.9Z: the page moved **150 px** (S2 'Get Now' y 682 to 532; S1 title 769 to 619); the batch was accepted.
- **The claim.** The S1 Claim went from y about 915 (clipped) to **765**, fully inside, a plain label: one tap at 13:02:09.8Z paid **Drone Parts x15**; the card reads Already claimed today.
- **Event.** events.jsonl lines 30 and 31 of run 20261124T130118Z-dbbafb: path with holdMs 1000 and composedFrom [mouse_down, wait, move, wait, mouse_up] (copied in the CSV).
- **Counts.** Drags 1; no correction pan; Iron and Coin cards never visible; tram badge none; diamonds 11,153.
- **Run.** One run, 13 steps, 22 actions, 0.172058 USD, cap 0.5; 0 refused; foreground stayed LastWar.
- **Closing state.** The base, no panel; token released 13:03:06Z.
