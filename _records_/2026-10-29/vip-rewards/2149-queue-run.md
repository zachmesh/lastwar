---
title: VIP rewards queue run
created: 2026-10-30T04:50:00Z
modified: 2026-10-30T04:50:00Z
version: 1.0.0
description: Queue unit vip-2026-10-29-1900 execution
status: partial
---

# VIP rewards - 2026-10-29 21:49 PDT queue run

Unit: vip-2026-10-29-1900, executor ticker-2134.

## Daily Freebie claimed

- Commander profile opened from the base (a "You're very
  popular!" popup dismissed with Awesome first; likes
  1,788 to 1,791).
- VIP screen: VIP13, 53 day login streak, points
  1,571,510 of 2,000,000 toward VIP14, "Collect 200 VIP
  points tomorrow".
- VIP13 Daily Freebie claimed (first Claim tap at 810,635
  did not register; a second tap at 810,640 opened the
  CONGRATULATIONS popup): puzzle piece x2, food crate
  x13, iron crate x13, coin crate x13. The Freebie button
  then showed a countdown (21:11:14 at last read).
- VIP Exclusive $99.99 offer not tapped, points-plus
  button and cart not tapped. Nothing bought.

## Login chest still pending

- The gold login chest at the top right of the VIP screen
  carries a small red dot, and the profile VIP13 badge
  kept its red dot after the Freebie claim, so the day
  login points are still waiting.
- Four taps on the chest (855,205; 850,210; 855,195;
  855,215) produced no change; the control channel
  reported background clicks do not reach this control.
  No login points were claimed in this unit.
- Next tick should retry the chest with a different input
  route; the Freebie itself is already claimed and must
  not be re-claimed.

## Outcome

Partial. Freebie claimed; login chest unclaimed for the
reason above. Tracker left untouched so the regular
re-produces next tick.
