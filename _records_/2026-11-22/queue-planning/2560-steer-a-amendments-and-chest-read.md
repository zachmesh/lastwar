---
title: Queue Planning Steer A Amendments And Chest Limits Read 2560 2026-11-23
created: 2026-11-23T03:14:00-08:00
modified: 2026-11-23T03:14:00-08:00
level: L0
version: 1.0.0
description: Planner pass on Steer A's verdict on decision 2603 - construction speed-ups first and the Tuesday window written into both builder units and the sheet, and a read-only unit staged for the chest quantity limits and the Speed-up tab
status: done
activity: queue-planning
run_id: queue-planning-2026-11-23-0314-amendments-and-chest-read
trigger: coordinator message with Steer A's verdict on 2603
started_at: 2026-11-23T03:09:00-08:00
finished_at: 2026-11-23T03:14:00-08:00
verified: unit files read back; word counts 381, 447 and 368; the read unit's run time simulated; validate exit 0
grounded_in:
  - source: _records_/2026-11-22/team-operations/2603-first-builder-decision.md
  - source: _records_/2026-11-22/growth/0009-inventory-read.md
---

# Amendments and the chest limits read, 2560

## 1. Amendments

Speed-ups use the construction items first (about 167,760 minutes, building only, Backpack Speed-up tab) and keep the general items (about 352K) in reserve; the caps are unchanged at 10,000 minutes per upgrade and 30,000 in all, after each preview, never Finish Now. The three upgrades start and the speed-ups apply inside Tuesday's Base Expansion window, which runs to 2026-11-25T02:00Z, so the construction speed-ups also score duel points; the unit reads the Duel screen, the authority, before the speed-up step. The builder windows (09:22Z to 10:20Z on 2026-11-24) already fall inside it. Both units and the sheet [2540](2540-drill-ground-sheet.md) say so; the sheet is now 1.1.0.

## 2. The read

`scout-midday-growth-snapshot-2026-11-23-026`, priority 1, read-only, 10 minutes, window 11:14Z today to 2026-11-24T08:30Z, `serves: baseline coin conversion`. In the Backpack Resources tab it selects by one tap, never Use, the plain Resource Chest and the Coin Chest UR, SSR and SR, and for each records the name, the quantity owned, and the quantity field and slider: whether a quantity can be typed, the maximum per Use, whether the slider caps below the stock, and the text of any Use-all or batch button, never pressed. It also reads the Speed-up tab as text. The result decides whether the third ground's 119.0M coin, about 19,800 plain chests, is feasible in a few runs or must come from SSR and SR Coin Chests, and Steer A is told before any choice chest is touched. Because expiry orders the queue, the long window puts it behind everything today; simulated at 5 minutes per read it runs at about 13:22Z, inside the idle gap before the 14:03Z wave, with about 20 hours of margin before the builders free.
