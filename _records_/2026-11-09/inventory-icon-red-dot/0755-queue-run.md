---
title: Inventory icon red dot exploration
created: 2026-11-09T15:58:00Z
modified: 2026-11-09T15:58:00Z
version: 1.0.0
description: Scout discovery exploration of the Inventory red dot - read-only learning
status: done
grounded_in:
  - source: live game screens on the owner Mac mini, 2026-11-09 07:55-07:57 PT
---

# Inventory icon red dot - 0755 queue run

Unit scout-scout-discovery-2026-11-09-003, executor ticker-0736.
Session cc-241, LastWar window 489932, no device dialog, no
contention, no login demand.

## What was learned

The red dot on the base HUD Inventory icon (right edge, above the
WORLD button) is explained by the Inventory's own badges:

- Opening the icon (tap [927,868]) shows the INVENTORY on the
  Special tab, which carries a red badge reading 1509.
- Inside Special, many individual items carry a small red dot
  (new/unopened items): the gold chest x240, the purple ? chest
  x1,169, the green gift box x2, the gold chest x42, the purple
  chest x1, the blue chest x2, the orange chest x1, the orange
  chest x1, and the gold chest in row 4, among others.
- Special tab contents read live (selected item Amethyst Crystal
  x4,882; detail: "A rare ore produced by the Crystal Factory.
  Use to redeem items in the Crystal Shop."): a grey-blue crystal
  x248,600, chests x240 / x1,169 / x2 / x42 / x1 / x2 / x1 / x2 /
  x3 / x1, plus Lv.5, Lv.3 and Lv.2 chests in row 4.
- The other tabs (Resources, Speed-up, Heroes, Gear, Gift) were
  NOT opened in this unit - whether they carry their own dots is
  untested. The Special badge alone explains the icon dot.
- The detail pane's Use button was NOT tapped (read-only
  exploration; using an item is an action, not a read). No item
  was opened, used or redeemed.

## Result

Done - the mechanism is explained: the Inventory red dot is the
new-items badge on the Special tab (1509) plus per-item red dots,
not a claimable reward with a deadline. No reward, cost,
deadline or scoring attaches to viewing it: candidate REJECTED
as a task (informational counter only), same verdict class as
unit 001's 99+ badge. No diamonds or money spent, nothing used.

- Follow-up: none for this candidate. The unopened chests are
  inventory the owner opens at will; no regular is proposed for
  opening them (opening chests spends nothing but is the owner's
  choice, and the 1509 badge will clear as items are used).
- Token note: this unit ran at the end of the token window (held
  until 07:57:33Z, known Issue #461 - re-acquire before expiry
  does not renew). The session was ended at about 07:57, inside
  the window; no game input ran after expiry.

## Stats

- target: explain-inventory-red-dot-mechanism
- achieved: 1
- resources_gained: none
- costs: about 3 minutes, no items spent
- verified: yes (same-unit live reads)
- blocker_category: none
