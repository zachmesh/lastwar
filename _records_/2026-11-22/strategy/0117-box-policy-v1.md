---
title: Box policy v1
created: 2026-11-23T09:20:00Z
modified: 2026-11-23T23:08:00Z
version: 1.1.0
level: L3
description: When, how and which chests and boxes to open regularly so slot starts never wait on a resource, while keeping the choice chests as flexibility
status: unverified
grounded_in:
  - source: owner order relayed by Steer A at 2026-11-23 09:15Z and his draft rules R1 to R9
  - source: inventory read _records_/2026-11-22/growth/0009-inventory-read.md and chest read 0054-box-chest-read.md
---

# Box policy v1

I own R2 to R8; the planner writes the convert units, the operator runs them by typed quantity. Stock is the stale 0009 read, re-read before every conversion because the owner also opens chests by hand (H51). Rules: [sidecar](0117-box-policy-v1.csv); stock: [table](0117-box-stock.csv).

## What the arithmetic says

The long line needs coin about 2.1G and food 1.9G to 3.0G (0515); coin is short by 0.3G to 0.9G over 60 days, so the choice chests cover coin first.

## The rules, with my changes to Steer A's draft in bold

- **R1 never:** diamond items and diamond choices; hero levers outside their windows. **Unread tiles are read before use, not never.**
- **R2 coin just in time:** plain Resource Chests first, then SR, SSR and UR choice chests (fixed Coin Chests are spent). Amount is the shortfall plus 10 percent, **under 5M from SR chests so it lands within 1 percent**. Quantity typed and read in a frame before every Use, within 2 hours before the start.
- **R3 buffer:** **coin on hand is at most the 10M floor plus spend due within 6 hours plus 25 percent; the 72-hour figure is a planning horizon**, checked daily: convertible stock must cover 72 hours of planned spend. The plunder reason is unproven (H48).
- **R4 food and iron:** typed chests first, for a shortfall against the floors. Choice and plain chests pay 67 percent more food or iron than coin, so if food runs short they open as food (H78).
- **R5 reserve (Steer A, 23:07Z, replaces decision 03's wording and the 50M fixed buffer):** the reserve is the plain Resource Chests (20,862, about 125M coin in one Use, each also worth 10K food or iron) and the choice chests (UR 552, SSR 587, SR 1,523, about 1.97G coin-equivalent). The fixed Coin Chests went on the first three ground levels (80 UR and 62 SSR, +245.3M); about 28M remain. A 1.0G choice-chest minimum is the only hard floor.
- **R6 sample, then low priority:** boxes to 22 by one typed Use of 11 in an idle gap, else stop at 10; **no routine box unit** (24 USD for 356 boxes); read one SSR and one UR choice chest before any large conversion; **read the Coin Vault protection.**
- **R7 windows** by the Duel screen: Thursday hero items, Monday drone, Wednesday components, Tuesday construction speed-ups.
- **R8 cadence:** event-driven, a daily check, a weekly review.
- **R9 log** every open; one forecast row per conversion batch (F-033 to F-037).

## Coin line

Dated conversions and the supply against need are in [the coin line](0117-coin-line.md).

## KPIs for the coach

Slot starts delayed by a shortage (0); coin above buffer plus 25 percent overnight; reserve intact; conversions with a forecast row (100 percent).
