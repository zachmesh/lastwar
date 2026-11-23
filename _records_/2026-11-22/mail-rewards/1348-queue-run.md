---
title: Mail run 1348
created: 2026-11-23T14:05:00Z
modified: 2026-11-23T14:05:00Z
version: 1.0.0
description: Unit mail-2026-11-23-0230 - the train arrived (an arrival notice sits at the top of the Event list) but it carries no attachment and no Claim button, and no mail is titled Train arrival reward; nothing claimed; the train shortcut icon opens the trade truck panel
status: done
grounded_in:
  - source: cu_bridge runs 20261123T134837Z-193195 and 20261123T135002Z-0d8475, events and final results, 2026-11-23T13:48Z to 13:51Z
  - source: unit mail-2026-11-23-0230 (planner, coordinator 13:44Z) and mail-rewards rule digest rules 1 to 5
---

# Mail run 1348

Rows in [1348-queue-run.csv](1348-queue-run.csv). Claimed 13:48:16Z; no different-device dialog in either no-click first frame; nothing pressed beyond navigation.

- **Train shortcut (107,580):** badge **2** now; it opens the **trade truck panel** ("Today's Trade Count: 5/5", "No more dispatches available.", three trucks and a locked slot, tabs Your Truck badge 2 and
  Others' Trucks 4), not the station view. It was closed with its back arrow.
- **Event list, newest first:** an ally's **"train has arrived"** mail (1h, unread), a Mega Exp mail (2h), the departure notice (3h), another train mail (5h), two read Code 87 Individual Reward mails (7h).
  No gift icon, and no row titled "Train arrival reward".
- **The arrival mail** (opened, second run): title "train has arrived!", a conductor card and a passenger list of ally accounts, **no attachment, no Claim button**; buttons Details, back arrow, star, trash can (not pressed).
  So the arrival reward is not a mail in this list; it may sit behind Details or in the train's own screen (unverified, Details not opened).
- **Claim:** none; HUD unchanged (coin 529.2K, Total Power 150,413,046).
- **Run.** `claude-gateway/claude-sonnet-5-5`, 8 + 10 steps, 0 refused, no `local_input` pause, 0.110500 and 0.122585 USD (0.233085 in all; stated caps 0.6 and 0.5).
- Closing state: the base, no panel, token held for the next unit.
