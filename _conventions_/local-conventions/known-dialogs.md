---
title: Known dialogs
created: 2026-11-25T00:35:29Z
modified: 2026-11-25T00:42:43Z
version: 0.2.0
description: The dialogs the game has shown that a unit may meet, each with its text, its buttons and the one safe answer; anything not in the table is a stop
---

# Known dialogs

Identify a dialog by its text in a frame taken just before the tap, tap once, and stop on any other dialog. The operator's copy is the route card (`_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md`). Back to [what stays the same](task-unit-queue-sections/8-what-stays.md).

| Dialog and its text | Buttons | Answer | Source |
|---|---|---|---|
| TIPS "Enable notifications and never miss important messages again." | Cancel, Enable Now | Cancel, never Enable Now (Steer A) | `_records_/2026-11-22/perception-scout/0412-queue-run.md` |
| TIPS about another device | Confirm | Stop, never Confirm; the one exception is the single Confirm of a controlled relaunch, never a second within 30 minutes (Steer A, 2026-11-24) | OD-20261123-17, OD-20261123-21 |
| Radar claim "Completing Radar Tasks today will not grant Alliance Duel points, and you are about to claim 10 radar task rewards at once. Continue?" | Cancel, Confirm, no price | Confirm, for that exact text only | `_records_/2026-11-22/radar-tasks/0339-queue-run.md` |
| Profile like dialog "You're very popular!" ("... people think you're awesome!"), opened by tapping the avatar | one blue "Awesome!" | Tap "Awesome!" once (393,677), then the profile's X (627,77) to return to the base, nothing else on the profile (the coordinator's ruling of 2026-11-25 00:36Z, confirmed by Steer A at 00:40Z, no veto) | `_records_/2026-11-22/daily-activities/0025-queue-run.md` |

The avatar is never tapped again by any unit: it opens the profile. The VIP lines are read from the VIP panel (the VIP entry in the left column or the HUD, read-only) or stay unreadable. The profile shows the owner's in-game name, and no record carries it, not in a summary, a frame description or a `state_read`: write "the profile page" only.
