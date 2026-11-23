---
title: Box policy v1
created: 2026-11-23T09:20:00Z
modified: 2026-11-23T09:20:00Z
version: 1.0.0
level: L3
description: When, how and which chests and boxes to open regularly so slot starts never wait on a resource, while keeping the choice chests as flexibility
status: unverified
grounded_in:
  - source: owner order relayed by Steer A at 2026-11-23 09:15Z and his draft rules R1 to R9
  - source: inventory read _records_/2026-11-22/growth/0009-inventory-read.md and chest read 0054-box-chest-read.md
---

# Box policy v1

I own R2 to R8; the coordinator stages, the planner writes the convert units, the operator runs them by typed quantity. Stock is the 0009 read (stale) and is re-read before every conversion, because the owner also opens chests by hand (H51). Rules in [the sidecar](0117-box-policy-v1.csv), stock in [the stock table](0117-box-stock.csv).

## What the arithmetic says

Over 28 days the plan needs about 0.48G coin (ground levels 119M, 59.5M, 83M, 162M and the 61M node) against 0.41G read in coin chests plus about 0.56G income. Food needs about 1.6G against 638M plus about 0.55G income, so **food, not coin, is the first resource the chests must cover**, from typed Food Chests UR (169, 686M). Iron is not short. The choice chests (1.97G coin-equivalent, SR measured) are not needed for four weeks: they are the reserve.

## The rules, with my changes to Steer A's draft in bold

- **R1 never:** diamond items and diamond choices; hero levers outside their windows. **Unread tiles are read before use, not never.**
- **R2 coin just in time:** fixed Coin Chests UR then SSR in bulk, plain Resource Chests for small top-ups, choice chests last (SR, SSR, UR). Amount is the shortfall plus 10 percent, **under 5M from SR chests so it lands within 1 percent**. Quantity typed and read in a frame before every Use, within 2 hours before the start.
- **R3 buffer:** **coin on hand is at most the 10M floor plus spend due within 6 hours plus 25 percent; the 72-hour figure is a planning horizon**, checked daily: convertible stock must cover 72 hours of planned spend. The plunder reason is unproven (H48).
- **R4 food and iron:** typed chests only, only for a shortfall against the floors.
- **R5 reserve:** keep at least 1.0G of UR and SSR choice chests and the 70M of SSR and SR fixed chests unopened; release only by my decision with a forecast row; the owner is told in the digest.
- **R6 sample:** Mystery Supply Boxes to 22; **Violet's Loot to 22** (five draws cannot exclude a 30 percent rare rate); one SSR and one UR choice chest read the two-step popup before any large conversion; **read the Coin Vault protection.**
- **R7 windows** by the Duel screen: Thursday hero EXP and medals, Monday drone items, Wednesday components, Tuesday construction speed-ups.
- **R8 cadence:** event-driven, a daily check, a weekly review; no standing open-everything unit.
- **R9 log** every open; one forecast row per conversion batch (F-033 to F-037).

## First conversions

11-24 about 07:20Z: 45 UR Coin Chests (109M) for the builder starts. 11:30Z today only if the lab node is startable: about 27 (66M). A typed Food Chest UR conversion only if a second ground level starts.

## KPIs for the coach

Slot starts delayed by a shortage (target 0); coin above buffer plus 25 percent overnight; share of the reserve intact; conversions with a forecast row (target 100 percent).
