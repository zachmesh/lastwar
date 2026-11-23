---
title: Conversion Rules For Conversion And Spend Units 2430 2026-11-23
created: 2026-11-23T00:25:00-08:00
modified: 2026-11-23T05:20:00-08:00
level: L0
version: 1.1.0
description: The shared operating rules a conversion-and-spend unit follows, from the coordinator's coin plan and the 0009 inventory read
status: done
activity: queue-planning
run_id: queue-planning-2026-11-23-0025-conversion-rules
trigger: coordinator coin plan after the inventory read
started_at: 2026-11-23T00:24:00-08:00
finished_at: 2026-11-23T00:25:00-08:00
verified: amounts copied from _records_/2026-11-22/growth/0009-inventory-read.md
grounded_in:
  - source: _records_/2026-11-22/growth/0009-inventory-read.md
  - source: coordinator coin plan message
---

# Conversion rules

1. Convert only what the next ranked spend needs: the exact coin cost of the item about to start. Leftover may be at most one UR Coin Chest (2.43M) and is spent within the hour. Coin in the base can be plundered; inventory cannot.
2. Sources in order. First open Coin Chests, read by description: UR 87 at 2.4364M (Total line read), SSR 71 at 812.16K, SR 40 at 101.52K (122 until the other device used 82 on 2026-11-23; fixed chests about 273.7M now), using the fewest that cover the cost. Only if more is needed, Resource Choice Chests (UR 552, SSR 587, SR 1,523): their popup was never opened and the two-step conversion is assumed, so read the popup first, record the yield, choose Coin, then open. Resource Chests and coin items last.
3. Never convert hero levers: Mystery Supply Box (299, they wait for the owner), Skill Medals, hero chests, blueprints, exclusive weapons, universal shards, Bond Badges, Guidebooks, Training Certificates.
4. Red lines: speed-ups, stamina items and diamond items are never used. A dialog showing a diamond price or a purchase ends the unit as needs-owner.
5. Read the cost on the panel before converting; if it cannot be read, convert nothing. Read coin on the HUD before the conversion and after the spend, and run the snap command with K or M numbers only.

## Planning figure and speed-up items (owner decisions, record 2425)

6. Plan only on the coin READ, 405,976,800. The 1.97B inferred from Resource Choice Chests stays unverified until ONE is opened. No bulk opening of Mystery Supply Boxes: the operator opens exactly one to read it.
7. Speed-up items (about 352,000 general minutes) are approved, bounded: only on capacity-critical or best-power-per-slot-day upgrades (Drill Ground first, then barracks), AFTER the preview shows the gain. Never Finish Now, diamonds or real money, never the owner's running queue. At most 10 percent a week, about 35,000 minutes; this planner's default cap is 10,000 minutes on one upgrade unless the coordinator sets another. Prefer theme windows: the Base Expansion duel day and the Arms Race City Building phase; the in-game Duel screen is the authority. Log the minutes used and the power before and after.
