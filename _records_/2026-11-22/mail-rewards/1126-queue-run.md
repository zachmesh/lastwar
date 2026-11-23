---
title: Mail run 1126
created: 2026-11-23T11:32:00Z
modified: 2026-11-23T11:32:00Z
version: 1.0.0
description: Unit mail-2026-11-23-1017 - the Event category read at 11:26Z; the Train arrival reward mail is not there yet (the 10:14Z train has only a departure notice), nothing claimed, nothing deleted
status: partial
grounded_in:
  - source: cu_bridge run 20261123T112551Z-5cd646, events, final result and frame step-0002, 2026-11-23T11:25:51Z to 11:26:40Z
  - source: unit brief mail-2026-11-23-1017 (coordinator instruction after the 10:14Z boarding) and mail-rewards rule digest rules 1, 3, 4 and 7
---

# Mail run 1126

Rows in [1126-queue-run.csv](1126-queue-run.csv). Claimed 11:25:27Z (window end 11:35Z), mail read 11:26Z.

- **Entry.** The Mail envelope at (670,787) opened the Mail screen, not Alliance. The category rail showed red dots
  on Event, Regular and In-app Purchases and **no gift icon** on any category row (digest rule 3).
- **Event list (6 visible).** Newest first: an ally's Mega Express notice (32m ago, unread), the owner alliance
  conductor's "train has de..." notice (1h, unread; the departure of the 10:14Z train), a commander's train notice
  (3h, unread), and three read "Code 87 Individual Reward" mails (4h). None shows a gift icon.
- **Train arrival reward: not present.** Only the departure notice exists, so the ride has not ended; the arrival time
  is unknown (about 1h05 after departure at 10:21Z). Per the brief the time and the list are recorded and the unit
  stops: nothing claimed, **Claim All not pressed** (no gift icon, digest rule 4), **Delete All not touched** (rule 1).
- **Close.** The blue back arrow twice (Event to the category list, then the base); no TIPS popup appeared.
- **HUD, before and after, identical:** food 648.5M, iron 1.0G, coin 14.4M, diamonds 11,136, Total Power
  150,211,809. No ledger row: nothing changed state.
- **Next.** Re-read the Event list after the train arrives; the planner may stage a later mail unit and read the first
  rows only, since the reward mail would be the newest. Regular and In-app Purchases still carry unread dots, left
  alone.
- **Run.** `claude-gateway/claude-sonnet-5-5`, 6 steps, 9 actions, 0 refused, no `local_input` pause, 0.091743 USD
  (stated cap 0.6; 13 usable turns).
- Closing state: the base, no panel, token released.
