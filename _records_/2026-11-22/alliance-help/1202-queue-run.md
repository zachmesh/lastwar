---
title: Alliance help: Help All once, tile dot cleared 1202
created: 2026-11-26T12:03:42Z
modified: 2026-11-26T12:03:42Z
version: 1.0.0
description: Unit help-2026-11-26-0230 (version 1.0.366(908); front LastWar at the start 12:02:47Z; owner idle 710 s; the different-device dialog never on screen; no UserNotificationCenter) - FIRST FRAME (12:02:53.4Z): the BASE, no help bubble or help icon visible, the Alliance button with a red dot; HUD: food 48.6M, iron 682.7M, coin 14.6M, oil 581.0K, diamonds 10,673; the Alliance button (670,708) tapped once; THE HELP TILE BEFORE (12:03:06.8Z): a RED DOT with no number (Alliance Techs and Alliance Events also with dots); the Help tile (513,516) tapped once; THE HELP PAGE: header 'Today's points gained from Alliance Help' 540 of 1,000; four rows, all the owner account's OWN requests (which an ally's Help All cannot help): the Oil Output I research, the Defense Training VIII research, the building Lv.26 Oil Well, the building Lv.28 Drill Ground (cut off at the fold; more rows may sit below: not scrolled); all four read 30/30 helps before the press; HELP ALL (393,766), green and not greyed, pressed ONCE at 12:03:21.1Z: no toast in the next frame; the rows then showed 'Time reduced' values; the page closed by its X (611,232) and REOPENED (513,516): the header 600 of 1,000 (+60 points) and the rows back to 30/30; no row disappeared; no individual Help, Send, Buy or priced control pressed; the page closed again; THE HELP TILE AFTER (12:03:47Z, read on the Alliance menu): NO DOT: CLEARED; Alliance Techs and Alliance Events still with dots; the Alliance back arrow (177,918); the base: the Alliance button still with a red dot (the other tiles); HUD unchanged; drags 0
status: done
grounded_in:
  - source: cu_bridge run 20261126T120247Z-24b98d, final report read by the operator, 2026-11-26T12:02Z to 12:04Z
  - source: unit brief help-2026-11-26-0230 and the alliance-help rule digest
---

# Alliance help: Help All once, tile dot cleared 1202

Rows in [1202-queue-run.csv](1202-queue-run.csv). Claimed 12:02:47Z; no different-device dialog.

- **Help tile's dot:** a red dot before (12:03:06.8Z), none after (12:03:47Z): cleared.
- **Help All once** (12:03:21.1Z): the four rows (Oil Output I, Defense Training VIII, Oil Well Lv.26, Drill Ground Lv.28) are the owner account's own requests at 30/30; the header rose 540 to 600 of 1,000 (+60) after a reopen; no row disappeared; no toast seen.
- **Counts.** No individual Help, Send, Buy pressed; the dialog never showed; drags 0.
- **Run.** One run, 10 steps, 8 actions, 0.121352 USD, cap 0.5; 0 refused; foreground stayed LastWar.
- **Closing state.** The base, no panel; token released 12:04:00Z.
