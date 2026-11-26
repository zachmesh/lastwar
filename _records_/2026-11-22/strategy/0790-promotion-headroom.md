---
title: Promotion headroom of the Lv.27 barracks priced
created: 2026-11-26T16:35:00Z
modified: 2026-11-26T16:35:00Z
version: 1.0.0
level: L3
description: The power, the cost and the barracks time of promoting Lv.7 and Lv.8 troops to Lv.9 at the Lv.27 barracks, with the first confirm and the guards
status: unverified
grounded_in:
  - source: coordinator message of 2026-11-26 16:20Z (troop-training, 16:13:52Z to 16:17:36Z)
  - source: _records_/2026-11-22/strategy/hypothesis-register.csv rows H13 to H15
---

# Promotion headroom of the Lv.27 barracks

**Facts** [M, the dialog read]: Lv.8 to Lv.9 for 726 troops (the maximum batch) costs 887.6K food and 887.6K iron, no coin, time 3 h 26 min; power per troop 1,063 to 1,352, +289. Counts: Lv.7 1,116, Lv.8 2,415, Lv.9 2,604; Lv.10 is not trainable at this barracks. Promotion needs no room, which answers H13 in part.

**Value** [D]: one batch is +209.8K power for 1.775M food and iron together, 118K per million; in the plan's weights (food 1.0, iron 0.5) 79K per million equivalent, against the ground ladder's 4.3K per million coin. Per resource it is the best lever read so far, and it uses no coin.

**Headroom at this barracks** [D, G where marked]:
- All 2,415 Lv.8 to Lv.9: +698K power for 2.95M food and 2.95M iron, 3.3 batches, 11.4 hours.
- The 1,116 Lv.7 up two tiers: about +0.56M power for about 2.5M each [G, the Lv.7 power and step costs are unread; the coordinator's scale is 1.34M for both groups, mine 1.26M].
- Together about 1.3M power for about 5.5M food and 5.5M iron, 5 batches, about 17 hours of the barracks. Food would stay at about 41M, above the 30M floor. The barracks is the limit, not the stock; it is empty, so nothing is displaced.
- This is part of the H15 headroom of 2.75M; the Lv.10 step needs the Lv.30 barracks, which refuses while Full.

**Pick:** confirm the first batch. After its result (cost as read, power up by about 209.8K when it completes), run the rest as a chain of batches, Lv.8 first, then Lv.7.

**Guards:** Promote only, never Finish Now (a sibling button on the dialog); quantity untouched; the HUD at +10 and +60 seconds (a drop of about 772K in Total Power is the batch in progress, 726 x 1,063, about 0.5 percent, returning at completion); stop the chain if a cost differs from 1,223 food and iron a troop by more than 10 percent. Keep no batch in progress between 21:45Z and 01:30Z, so Total Power is whole at the owner's 11-27T01:15Z search; a batch started after 21:30Z waits.

**Rows:** H13 and H15 close from the first batch result; F-new, a promotion batch costs 887.6K food and iron and adds 289 a troop.
