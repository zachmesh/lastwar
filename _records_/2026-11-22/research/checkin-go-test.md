---
title: Test T3 - does the shop check-in Go pay in game
created: 2026-11-23T01:54:00-08:00
modified: 2026-11-23T01:54:00-08:00
level: L0
version: 1.0.0
description: One-unit falsification test for the shop-claims card top open question and digest rule 9 about the check-in FREE GIFT Go button
status: unverified
grounded_in:
  - source: shop-claims records of 2026-11-16 2240 and 2026-11-22 1059 under _records_/
  - source: shop-claims card and rule digest in the scribe pilot worktree, commit 0db1a219
---

# T3 - the check-in Go button

**Rule tested:** digest 9 and card Failures, "the check-in Go has no in-game claim; it swipes the carousel or opens the web store", marked verified.

**What the records show.** 11-16: three taps on Go changed nothing and a click on the label Go found no control; the record calls it a tooling gap. 11-22: one tap on the FREE GIFT banner made Chrome flash to front and back; **Go was never tapped.** The web-store route is tested for the banner only. Whether Go claims in game is open.

**Do (8 steps).**
1. Run `lsappinfo front`; LastWar must be present and frontmost, or stop.
2. Shop from the base cart icon, Hot Deals tab.
3. Wait for the check-in page (FREE GIFT, FREE TOMORROW x5); if the points page shows, wait 6 s and look again.
4. Ground Go from that screenshot; confirm the front app again.
5. ONE foreground click on Go. No second click.
6. Screenshots at once and +3 s; `lsappinfo front` after each. Leave the shop open.

**Refuted** (Go pays in game): a reward popup, a Claimed state or a counter change while LastWar stays frontmost and no browser opens. Then press only a button labelled Claim, Collect or OK, never a price. **Supported:** nothing changes, or a browser takes the front.

**Stop rules.** If another app takes the front, touch nothing in it: record needs-owner (the card says the owner clicks the Dock icon). Any login, account link or payment prompt: stop. No price button, Renew, Extension or Take All.

**Risk and spend.** Nothing spent. Moderate risk: the web store is a purchase surface and focus may be lost; the 11-22 flash recovered by itself.
