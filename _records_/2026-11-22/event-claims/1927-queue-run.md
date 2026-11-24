---
title: Thanksgiving store rows read, Lottery tab stuck loading 1927
created: 2026-11-24T19:35:01Z
modified: 2026-11-24T19:35:01Z
version: 1.0.0
description: Unit events-thanksgiving-store-read-2026-11-24-001 (four runs; read only; nothing redeemed or obtained) - the Thanksgiving STORE (the first tab, a cornucopia icon, badge 3, countdown 6d 06:31:38 at 19:28Z): turkey tickets held 6 (the red numerator on rows 1 to 3, white on row 4); row 1 a cornucopia item x1 for 6/100 tickets, Limit 1, Go Obtain; row 2 a Lv.5 chest x1 for 6/100, Limit 1, Go Obtain; row 3 a golden puzzle piece x1 for 6/10, Limit 10, Go Obtain; row 4 a golden trophy x1 for 6/1, Limit 600, a green Redeem; a fifth row (Limit 40) clipped and unread: ONE composed pan at x 639 (start y 812, end y 637) moved the list 0 px, so panning stopped; an 'Exchange Reminder' checkbox ticked; the tabs: the Store, Thanksgiving Lottery (no badge), Gift of Thanks (badge 1) and a cut-off 'Th'; the Lottery tab tapped once (19:29:18.5Z) showed ONLY A FULL-WINDOW LOADING SCREEN (an orange lottery machine with a red button, no controls) for 5 minutes (19:29:20Z to 19:34:03Z, 15 wait frames): the Lottery page and the Gift of Thanks page NOT READ; the screen left on the loading screen (unresolved at 19:34:14Z); nothing pressed on any row; the tram icon not drawn
status: partial
grounded_in:
  - source: cu_bridge run 20261124T192740Z-6bd54f, final report read by the operator, 2026-11-24T19:27Z to 19:34Z
  - source: unit brief events-thanksgiving-store-read-2026-11-24-001 and the event-claims rule digest
---

# Thanksgiving store rows read, Lottery tab stuck loading 1927

Rows in [1927-queue-run.csv](1927-queue-run.csv). Claimed 19:27:39Z; no different-device dialog.

- **Store.** 6 turkey tickets held: rows 1 to 3 cost 100, 100 and 10 (not affordable); row 4 a golden trophy x1 for 1 ticket, Limit 600 (Redeem: not pressed); row 5 clipped (the pan moved 0 px).
- **Event.** Ends about 2026-12-01T01:00Z (6d 06:31:38 at 19:28Z); tabs Store (badge 3), Lottery, Gift of Thanks (badge 1).
- **Stuck.** The Lottery tab shows only a full-window loading screen for 5 minutes: the Lottery and Gift of Thanks pages are unread; the screen is left on it, unresolved.
- **Counts.** Nothing pressed on any row; drags 1 (the pan); tram icon not drawn.
- **Run.** One run, 39 steps, 22 actions, 0.508827 USD, cap 0.5; 0 refused; foreground stayed LastWar.
- **Closing state.** NOT the base: the game is on the Thanksgiving Lottery loading screen (no controls) at 19:34:14Z; token released 19:34:14Z.
