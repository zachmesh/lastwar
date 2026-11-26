---
title: Strategy log 2026-11-26 part l
created: 2026-11-26T18:10:00Z
modified: 2026-11-26T18:10:00Z
version: 1.0.0
level: L3
description: The hospital reservoir of Completed troops, promotion as a lossless eviction that lends room, and the read before the conveyor
status: unverified
grounded_in:
  - source: coordinator message of 2026-11-26 17:52Z (perception-scout/1743)
  - source: _records_/2026-11-22/strategy/strategy-log-1126k.md and 0750-hospital-room.md
---

# Strategy log 2026-11-26 part l

- 2026-11-26 18:10Z. **Facts** [M, 17:43Z]: Completed 5,104, wounded 1,364 (all Lv.10), capacity 7,999, free room 1,531 (the guard's). The Completed count was 5,306 on 11-25 (0750), so 202 left it, about one +200 level: a partial collect was admitted, F-184 to p 0.75 [G].
- **The reservoir:** if the 5,104 are Lv.10, they are 5,104 x 1,647 = 8.4M power waiting for room, 5.5 percent of Total Power; the barracks 67 add 110K.
- **A better lever than the disband.** A promotion in progress takes its troops out of the ground and lends exactly its batch of room, and the promoted troops come back as a finished batch that waits without loss. So one batch of 726 Lv.8, 887.6K food and iron, swaps 726 Lv.8 slots (1,063) for 726 Lv.10 (1,647): +584 a slot, +424K now, and the 726 Lv.9 wait to enter (981K) when room comes. Counting the batch of 726 already in, the first one paid +1.196M of entry while the promoted 726 left 772K. No troop is destroyed, which the disband does. It needs the entry to happen right after the Promote confirm (the room is lent only while the promotion runs). If the promoted do return into room at completion (prediction a), the lent room was a loan and the swap is partly undone; the 20:13Z read decides.
- **Order of what enters the lent room** [D]: Lv.10 ready (67), Lv.10 hospital Completed (if Lv.10), then the Lv.9 promoted, then the Lv.8 ready batches at 1,063.
- **The read first, and why:** the hospital tier is unread (P 0.7 mostly Lv.10 [G]). If it is low tier, collecting into a lent slot gives up to 289 a troop against the Lv.8 it replaced. The info button read is a plain read: approve it before the conveyor. The coordinator's refusal of the Collect while room is 0 is right; the Collect belongs right after a Promote confirm.
- **Pick:** approve the info read now; approve the conveyor in the order Promote confirm, Lv.30 pistol, hospital Collect (Lv.10 only), with the HUD and Total Power read after each; stop the Collect if Total Power rises by less than 1,500 a troop.
- **Row:** F-184 p 0.75; F-new, the Completed pool is Lv.10 (P 0.7).
