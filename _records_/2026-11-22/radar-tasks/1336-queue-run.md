---
title: Radar run 1336
created: 2026-11-23T13:50:00Z
modified: 2026-11-23T13:50:00Z
version: 1.0.0
description: Unit radar-2026-11-23-0203 under the quick-execute-only ruling - the radar screen holds no tasks now (12 restore in 1h02m), so nothing was executed or claimed; oil counter 647.0K before and after
status: done
grounded_in:
  - source: cu_bridge run 20261123T133538Z-bdc0c2 (frame step-0002), events and final result, 2026-11-23T13:35Z to 13:37Z
  - source: unit radar-2026-11-23-0203, coordinator ruling RADAR QUICK-EXECUTE ONLY of 13:34Z, radar rule digest rules 1, 2 and 6
---

# Radar run 1336

Rows in [1336-queue-run.csv](1336-queue-run.csv). Claimed 13:35:19Z; no different-device dialog at the no-click first frame.

- **Entry verified.** The dish icon (107,715) opened a radar scene (beam over the snow map), not a task list: top bar level label v.13, a bar 596, a gift box icon, a bar 100%, energy **91**, and a counter 0/40.
- **Nothing to run.** The screen says "**12 Radar Task(s) will be restored in 01:02:12**" (read about 13:36:00Z, so the next tasks arrive about 14:38Z). There is no bottom bar: no Quick Execute, no Claim All, no
  Refresh, no Bingo entry and no pins. Nothing was pressed beyond the dish icon and the back arrow; the gift box icon was not tapped.
- **Oil.** The oil counter reads **647.0K** before and after; no oil figure appeared on any reward, and the Bingo lines (the one-time 240K oil) were not on screen.
- **Energy.** 91 (82 at 13:09Z, +9 in 27 minutes); the Quick Execute cost stays unobserved.
- **Reading.** The tasks were most likely run on the other device before 13:30Z. A radar unit after 14:38Z may find the 12 new tasks; the Bingo screen may sit behind the gift box icon (unverified).
- **Run.** `claude-gateway/claude-sonnet-5-5`, 4 steps, 0 refused, no `local_input` pause, 0.065759 USD (stated cap 0.5). HUD unchanged.
- Closing state: the base, no panel, token released.
