---
title: Survivor intake run 1338
created: 2026-11-23T13:55:00Z
modified: 2026-11-23T13:55:00Z
version: 1.0.0
description: Unit survivors-2026-11-23-0203 - one figure with a question bubble at the left gate vanished after one tap with no card or Recruit button; no recruit verified; the train icon now carries a red badge 1
status: partial
grounded_in:
  - source: cu_bridge run 20261123T133840Z-2eea5c (frame step-0002), events and final result, 2026-11-23T13:38Z to 13:40Z
  - source: unit survivors-2026-11-23-0203, survivor-intake rule digest rules 1 to 5, coordinator standing rules
---

# Survivor intake run 1338

Rows in [1338-queue-run.csv](1338-queue-run.csv). Claimed 13:38:39Z; no different-device dialog at the no-click first frame.

- **Entry.** No survivor bubble stood beside the avatar (it read 9min at 12:51Z), so the survivors may have arrived earlier and been taken by the other device.
- **Gate.** A "?" bubble with a small figure sat at the left edge; one tap on the figure at (143,687) showed a white speech strip ending "...soon!" beside the jeep icon, then the strip, the bubble and the figure
  vanished. No survivor card and no Recruit button opened; nothing was pressed beyond that tap.
- **Result.** No recruit is verified (digest rule 4: a cleared "?" is processed state); no "?" bubble remains anywhere on the base afterwards, but the line is not presumed clear (rule 5). A re-read unit
  after the next survivor countdown is named.
- **Left column.** The train shortcut icon (107,580) carries a red badge **1** (new): the train may have arrived, so the Train arrival reward mail may be claimable; unverified.
- **Not touched.** The red crosshair icon at (670,640), harvest bubbles, the trophy bubble. Nothing spent; HUD unchanged (coin 529.2K, Total Power 150,413,046).
- **Run.** `claude-gateway/claude-sonnet-5-5`, 4 steps, 0 refused, no `local_input` pause, 0.061136 USD (stated cap 0.5).
- Closing state: the base, no panel, token released.
