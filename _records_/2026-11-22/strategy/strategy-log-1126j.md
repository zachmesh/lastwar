---
title: Strategy log 2026-11-26 part j
created: 2026-11-26T17:45:00Z
modified: 2026-11-26T17:45:00Z
version: 1.0.0
level: L3
description: The Full state as a finished batch that cannot enter, the room a promotion lends, and the two predictions for the promotion completion
status: unverified
grounded_in:
  - source: coordinator message of 2026-11-26 17:30Z (training-2026-11-26-0603)
  - source: _records_/2026-11-22/strategy/0790-promotion-headroom.md
---

# Strategy log 2026-11-26 part j

- 2026-11-26 17:45Z. **The reading** [D from M]: the Lv.30 pistol collected a finished batch, 726 Lv.10 troops, +1,195,722 power (726 x 1,647 exactly), Total Power 150,917,717 to 152,113,439. The Full state was a finished batch that could not enter. A promotion in progress takes its troops out of the ground (726 x 1,063 off Total Power), which lent room for exactly one batch of the same size.
- **Room is the constraint, not resources.** Food is near a possible store figure, iron is 645M. Value per slot [D]: Lv.10 1,647, Lv.9 1,352, Lv.8 1,063. Per resource they are not equal, against the coordinator's line: training a Lv.10 troop gives 239 power per 1K food plus 1K iron (1,647 for about 6.9K each), a promotion 118 (289 for 1,223 each). Training pays twice as much per resource and needs room; a promotion needs no room and pays half. With room at 0 only promotion can run.
- **After the batch entered, free room is probably 0 again** (the lent 726 went to the batch), so the Lv.30 train panel will likely offer a small or zero maximum [G, P 0.7]. Train only at the maximum the panel offers and only if it is at least 200 troops; if it is 0 or refused, no spend.
- **Two predictions for the promotion completion near 20:13Z** [G]: (a) the 726 Lv.9 return and count: Total Power +981,552 (726 x 1,352) over the 152,113,439 now, 153,094,991 (P 0.45); (b) the room is taken, so they wait as "Training complete, ready" and Total Power stays at 152,113,439 until room (P 0.55). In case (b) the promotion still paid: the lent room moved 1.2M of power in and the promoted troops wait without loss (981K when room comes).
- **Order of room use when it is lent or freed:** a ready batch collects for nothing (free power now); a new Lv.10 batch costs resources but is the best slot (1,647). With resources in surplus, a slot goes first to a ready batch of Lv.10, then a new Lv.10 batch, then lower-tier ready batches; a lower-tier batch collected is later promoted at 289.
- **Limits for a train confirm:** read the maximum, the cost and the time before the confirm; Train only, never Finish Now; food after at least 35M (5.0M leaves 43.5M); no coin; stop if a troop costs over 8K food or iron.
- **Row:** F-new, the Lv.9 troops count at completion (a). H13 to H15: the Full state is a finished batch that cannot enter.
