---
title: Box policy v1
created: 2026-11-23T09:20:00Z
modified: 2026-11-23T12:53:00Z
version: 1.0.0
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

The long line needs coin 1.83B, iron 618M, food 618M (guide, factor unverified); nine ground levels coin 1.07G, food 4.0G. Over 9 weeks coin is short by 0.9G to 1.5G and food by about 2.1G, so the choice chests cover both and ground levels after the first two or three wait for surplus.

## The rules, with my changes to Steer A's draft in bold

- **R1 never:** diamond items and diamond choices; hero levers outside their windows. **Unread tiles are read before use, not never.**
- **R2 coin just in time:** fixed Coin Chests UR then SSR in bulk, plain Resource Chests for small top-ups, choice chests last (SR, SSR, UR). Amount is the shortfall plus 10 percent, **under 5M from SR chests so it lands within 1 percent**. Quantity typed and read in a frame before every Use, within 2 hours before the start.
- **R3 buffer:** **coin on hand is at most the 10M floor plus spend due within 6 hours plus 25 percent; the 72-hour figure is a planning horizon**, checked daily: convertible stock must cover 72 hours of planned spend. The plunder reason is unproven (H48).
- **R4 food and iron:** typed chests first, for a shortfall against the floors. Choice and plain chests pay 67 percent more food or iron than coin, so if food runs short they open as food (H78).
- **R5 reserve:** released by decision 03: UR and SSR choice chests open node by node for the long line, as coin or food whichever the shortfall asks (food pays 67 percent more); the owner is told in the digest.
- **R6 sample, then low priority:** boxes to 22 by one typed Use of 11 in an idle gap (about 0.07 USD), else stop at 10; **no routine box unit** (per-box runs cost 24 USD for 356 boxes); the rest only by bulk typed quantity; **Violet's Loot likewise**; read one SSR and one UR choice chest before any large conversion; **read the Coin Vault protection.**
- **R7 windows** by the Duel screen: Thursday hero items, Monday drone, Wednesday components, Tuesday construction speed-ups.
- **R8 cadence:** event-driven, a daily check, a weekly review.
- **R9 log** every open; one forecast row per conversion batch (F-033 to F-037).

## First conversions

11-24 about 07:20Z (decision 02): fixed Coin Chests for the three starts, shortfall sized from the HUD (about 270M), and about 110 typed Food Chests UR. Today a lab node only if it needs coin.

## KPIs for the coach

Slot starts delayed by a shortage (0); coin above buffer plus 25 percent overnight; reserve intact; conversions with a forecast row (100 percent).
