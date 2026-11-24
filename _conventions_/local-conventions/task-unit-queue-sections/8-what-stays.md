---
title: 8. What stays the same
created: 2026-11-23T09:03:48Z
modified: 2026-11-24T20:28:39Z
version: 0.7.0
sequence: 18
description: The red lines, the kick rule for the different-device dialog, the Arms Race just-enough rule and
---
## 8. What stays the same

- The red lines, the kick rule for the different-device dialog, the
  Arms Race just-enough rule and every other standing order bind units
  exactly as they bind segment runs. A unit inherits its regular's
  activity metadata in `_activities_`.
- Known dialogs, 2026-11-24 (the operator's copy is the route card,
  `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md`). Identify a dialog by its
  text in a frame taken just before the tap, tap once, and stop on any other dialog. The TIPS
  "Enable notifications and never miss important messages again." (Cancel, Enable Now): Cancel,
  never Enable Now (Steer A; `_records_/2026-11-22/perception-scout/0412-queue-run.md`). The TIPS
  about another device: stop, never Confirm; the one exception is the single Confirm of a controlled relaunch (Steer A,
  2026-11-24; the operator's hazards sheet). The radar claim "Completing Radar Tasks today will not
  grant Alliance Duel points, and you are about to claim 10 radar task rewards at once. Continue?"
  (Cancel, Confirm, no price): Confirm is allowed for that exact text only
  (`_records_/2026-11-22/radar-tasks/0339-queue-run.md`).
- Scrolling a clipped page, 2026-11-24 (the full recipe is `_activities_/shop-claims/scroll-recipe.md`, verified in
  `_records_/2026-11-22/shop-claims/1301-queue-run.md`; the operator's copy is the route card): from the blank right margin, in
  ONE message press, hold 1 s, ONE move of 175 px, hold 1 s, release, then the screenshot after the up; a single drag event
  is not enough.
- The regulars tracker stays the cadence source of truth; the pool is
  a work distribution layer over it, not a replacement.
- The `segment` field survives only as a reporting tag recording
  which slice a regular belonged to under the old routine; nothing
  schedules by it anymore.
- The round summary for Slack assembles from the `done` units'
  structured result sections, gathered by `_tools_/queue.py stats`,
  instead of three segment records. The same command doubles as the
  pool health report for the owner.

