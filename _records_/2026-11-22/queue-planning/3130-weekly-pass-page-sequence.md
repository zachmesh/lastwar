---
title: Weekly Pass Page Sequence Four Pans From The Top 3130 2026-11-24
created: 2026-11-24T05:40:00-08:00
modified: 2026-11-24T05:40:00-08:00
level: L0
version: 1.0.0
description: The procedure for the Weekly Pass tab of the shop - up to four composed pans from the top reach the S1 Drone Parts, EXP, Iron and Coin pickups; each card is read before any tap - built from records 1301 and 1327 and Steer A's ruling of 2026-11-24 13:33Z
status: done
activity: queue-planning
run_id: queue-planning-2026-11-24-0540-weekly-pass-page-sequence
trigger: Steer A message 13:33Z
started_at: 2026-11-24T05:34:00-08:00
finished_at: 2026-11-24T05:40:00-08:00
verified: pan geometry copied from the operator records 1301 and 1327; pans 3 and 4 and the Iron and Coin Claims have not been run yet
grounded_in:
  - source: _records_/2026-11-22/shop-claims/1301-queue-run.md
  - source: _records_/2026-11-22/shop-claims/1327-queue-run.md
---

# Weekly Pass page sequence, 3130

## Facts

The page resets to the TOP at every visit; each composed pan moves it about 150 px (150, 150, 149 measured). In record 1301 one pan brought the S1 Claim inside (y 915 to 765) and the tap paid Drone Parts x15; in 1327 the second pan brought the EXP card with a green Claim to y about 855; the Iron and Coin cards lie about two pans below it, so FOUR pans from the top reach them.

## Rules

Read the Weekly Pass tab only; never the G tab (Gold Brick Mall), never Go on the check-in banner, never Renew or Extension. At most FOUR composed pans, each its own message with a frame after it; at most ONE correction pan the same way in all; no fifth pan; the unit's cap is 12 minutes. Each pan is ALL IN ONE MESSAGE: mouse_move (685,650); left_mouse_down; wait 1 (second); mouse_move (685,475); wait 1 (second); left_mouse_up; a screenshot after the up; nothing else between the down and the up. If the batch is refused: write the refusal text and STOP.

## Sequence

A frame at the top. Pan 1: the S1 Drone Parts card. Pan 2: the EXP card. Pans 3 and 4: the Iron and Coin cards. For EACH card READ in the frame BEFORE any tap its label, its price line, any gem icon and its state (Remaining Nd, Purchased, Active, Locked or Already claimed today). 'Already claimed today' is a COMPLETE for that card. Tap its Claim ONCE only if ALL hold: a plain CLAIM; no price and no gem or diamond icon; no Buy, Purchase, Unlock, Upgrade or Activate; an OWNED state (a Remaining time or Active); fully inside the content, not at the window's bottom edge. Otherwise record the label and the state and press nothing.

## Record

Each pan's measured move in px (from a card title); each claim's reward per card (items, quantities); and per card whether its pickup was already claimed when the unit arrived.

## Stops

A price line, diamond spend, real-money line or app store sheet: STOP, press nothing. Any other element (tooltip, menu, highlight, dialog): touch nothing, take the frame, stop and tell the Coordinator. Another app in front: STOP and touch nothing.
