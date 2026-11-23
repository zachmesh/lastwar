---
title: Thanksgiving event read 1756
created: 2026-11-23T18:00:00Z
modified: 2026-11-23T18:00:00Z
version: 1.0.0
description: Unit events-thanksgiving-read-2026-11-23-001 - Thanksgiving tickets 6, lottery tickets 10, turkeys 7, ingredients 30; the event tabs end 2026-11-30T02:00:00Z and the Store 2026-12-01T02:00:00Z; nothing pressed
status: done
grounded_in:
  - source: cu_bridge run 20261123T175626Z-8a6e59, final report and observation timestamps read by the operator, 2026-11-23T17:56Z to 17:57Z
  - source: coordinator order of 17:50Z (read-only Thanksgiving unit, end timer first) and the 1731 record
---

# Thanksgiving event read

Rows in [1756-queue-run.csv](1756-queue-run.csv). Claimed 17:56:26Z; no different-device dialog; read-only, only the icon, tabs and back arrow tapped.

- **End timer (first).** Store page **7d 08:03:21 at 17:56:39.323Z**, then 7d 08:03:15 at 17:56:45.076Z: it ends **2026-12-01T02:00:00Z**. Lottery 6d 08:02:59 (17:57:01Z), Gift of Thanks 6d 08:02:53 and Login 6d 08:02:44: those tabs end **2026-11-30T02:00:00Z**, so the Store runs one day longer.
- **Store.** Currency Thanksgiving tickets, balance **6**. Rows: 100 tickets (limit 1, Go Obtain) twice, 10 tickets (limit 10, Go Obtain), 1 ticket for a gold trophy item (limit 600, green Redeem, the only affordable row), a fifth row cut off (limit 40). Item names are icons only.
- **Lottery.** **10 tickets**; Draw x1 costs 1 and x10 costs 10; next round at 02:00Z ('Next Round 08:03:00'); prizes and odds sit behind info buttons (not read).
- **Gift of Thanks.** **7 turkeys, 30 ingredients**; Gift Turkey x7; the cooking pot (red dot) shows no recipe cost; each gift returns lottery tickets, a cornucopia item, a Lv.5 chest and a puzzle piece.
- **Login.** Day 01 claimed; days 02 to 07: gold trophy x300, chest x10 three times, Lv.5 chest x1, V1 gold chest x2; none claimable yet.
- **Not pressed.** Redeem, Obtain, Go, Draw, Gift Turkey, the pot, any claim or chest.
- **Run.** One run, 9 steps, 13 actions, 0.113882 USD, cap 0.5; 0 refused; foreground stayed LastWar.
- **Closing state.** The base, no panel; HUD unchanged; icon badge 1; token released 17:57:40Z.
