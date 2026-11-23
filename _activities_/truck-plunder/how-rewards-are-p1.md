---
title: How rewards are delivered part 1
created: 2026-11-23T07:16:21Z
modified: 2026-11-23T07:16:21Z
version: 0.1.0
sequence: 9
description: A returned truck settles when its Truck Details are opened - observed end to end on
---
## How rewards are delivered

- A returned truck settles when its Truck Details are opened -
  observed end to end on the evening of 2026-10-25, closing the
  earlier inference that delivery was automatic. Tapping a returned
  truck on the Your Truck view opens TRUCK DETAILS headed Intercity
  Trade Reward, and a Congratulations overlay pays the cargo out.
  Left and right arrows page through the returned trucks one by one;
  each page shows the escort squad, the delivered cargo, and a
  status line - the vehicle is safe and secure, or a Battle History
  naming each successful plunderer with time and power, the items
  they took listed below, and the looted cargo slots crossed out in
  red. Reviewing all four noon trucks cleared the yard to empty
  slots, and the HUD reconciled - food 319.7M to 334.7M and iron
  311.7M to 326.7M across the settlements, the evening plunders and
  harvests combined. Settlement therefore waits for the return leg,
  not just the outbound arrival estimate - the noon trucks,
  dispatched 12:32 with 4 to 5 hour estimates, were found returned
  by about 20:47.
- Settlement values, measured 2026-11-09 (2250 unit, 4 returned trucks settled by opening each Truck Details; all four read "The vehicle is safe and secure", none plundered): UR-scale cargo pays iron 3.8M, food 3.8M, coin 2.4M; SR pays iron 2.5M, food 2.5M, coin 1.6M. Settlement totals for the 4 trucks: iron 12.6M, food 12.6M, coin 8.0M, badge 500 x8 in total (x1 to x3 per truck), plus chests, red gems and 5m speed-ups. The rarity label of the first truck was unread behind the CONGRATULATIONS banner - read the label before the banner covers it, or take the cargo figures as the scale signal.
- Details-panel paging: the Truck Details panel pages with the side "<" / ">" arrows and the bottom-left blue arrow (previous). The control receipt's no_change_observed flag is UNRELIABLE for this panel - the SR-to-UR page reported no change yet the screenshot proved the page had turned, so verify paging on the screenshot, never on the receipt flag. Tapping outside the panel does not close it; a unit may end with the panel open on the last truck, which is harmless - the next unit re-reads the trade screen fresh.
- History is the ledger. Its Dispatch tab shows each truck cargo
  with green gained amounts and red crossed items for whatever was
  plundered off it en route; its Plunder tab logs the escort battles
  both ways, including Defense Failed records naming the attacker.
  Looted trucks show flame markers on the Your Truck road view.
