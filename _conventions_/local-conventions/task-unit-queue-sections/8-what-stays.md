---
title: 8. What stays the same
created: 2026-11-23T09:03:48Z
modified: 2026-11-25T00:35:29Z
version: 0.9.0
sequence: 18
description: The red lines, the kick rule for the different-device dialog, the Arms Race just-enough rule and
---
## 8. What stays the same

- The red lines, the kick rule for the different-device dialog, the
  Arms Race just-enough rule and every other standing order bind units
  exactly as they bind segment runs. A unit inherits its regular's
  activity metadata in `_activities_`.
- Known dialogs: the table of each dialog's text, buttons and safe answer is [known dialogs](../known-dialogs.md); a dialog not in it is a stop.
- Scrolling a clipped page, 2026-11-24 (recipe and table in `_activities_/shop-claims/scroll-recipe.md`):
  in ONE message press at the page's start point, hold 1 s, ONE move of 175 px, hold 1 s, release, then the screenshot after the up. 
  Start per page: a blank right margin on the shop and History pages, the centre of a tile-gap crossing on the Backpack grids.
- The regulars tracker stays the cadence source of truth; the pool is
  a work distribution layer over it, not a replacement.
- The `segment` field survives only as a reporting tag recording
  which slice a regular belonged to under the old routine; nothing
  schedules by it anymore.
- The round summary for Slack assembles from the `done` units'
  structured result sections, gathered by `_tools_/queue.py stats`,
  instead of three segment records. The same command doubles as the
  pool health report for the owner.

