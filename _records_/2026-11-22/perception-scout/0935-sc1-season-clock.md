---
title: Season clock read SC1
created: 2026-11-23T09:38:00Z
modified: 2026-11-23T09:38:00Z
version: 1.0.0
description: Unit scout-midday-growth-snapshot-2026-11-23-019 - read-only look at the season countdowns; no season icon under the VS button, no Obelisk found, every timer ends at the 02:00Z reset, the Black Market on 2026-12-14
status: done
grounded_in:
  - source: cu_bridge run 20261123T093538Z-b998eb, events, final result and frames step-0000 to step-0007, 2026-11-23T09:35:38Z to 09:36:30Z; the first run 20261123T093311Z-a59935 stopped on a model question
  - source: unit brief scout-midday-growth-snapshot-2026-11-23-019 (Story 868, SC1) and coordinator assignment A-20261123-0931-operator
---

# Season clock read SC1

Rows in [0935-sc1-season-clock.csv](../growth/0935-sc1-season-clock.csv) (schema l_clock), each
end computed as the read time plus the countdown.

- **No season icon.** The right-edge column reads Thanksgiving Event, Events (badge 1),
  Warzone Duel, the VS timer, Alliance, Mail, Inventory. No countdown icon with text sits
  under the VS button; the Season II globe seen on 2026-11-09 is gone. The Season 3 date
  cannot be read from the base now.
- **Obelisk or chrono: not found** on the base, on any Events tab or on the Age of Oil page.
- **Events tabs seen** after dragging the bar both ways: The Age of Oil, Arms Race, Black
  Market, Black Market Challenge (badge), Desert Battlefield (New), Winter Battlefield, Wanted
  Boss, Community.
- **Timers, all ending on a 02:00Z reset.** VS 16:24:22 at 09:35:39Z, ends 2026-11-24T02:00Z.
  Black Market Challenge 6d 16:24:07 at 09:35:53Z, ends **2026-11-30T02:00Z**. The Age of Oil
  page (stage 3 of 4 highlighted) shows two cards, Unlock Lv. 31-35 Zombies on World Map
  (3348/2000) and Rapid Rescue (674067/25000), both 6d 16:23:54 at 09:36:07Z, ending
  2026-11-30T02:00Z. Black Market 20d 16:23:47 at 09:36:13Z, ends **2026-12-14T02:00Z**
  (matches the 09:29Z read).
- **Base clock tower** reads 07:35 at 09:35:39Z and 07:36 at 09:36Z, two hours behind UTC, so
  it shows the game server clock (UTC-2) and 02:00Z is 00:00 on it. Unverified, one source.
- **Not settled.** The Age of Oil end date (2026-12-13 is a guess) and a 14-day season icon
  were not seen; the Age of Oil page shows no main timer, only the stage-3 card timers.
- **Run.** The first run (`20261123T093311Z-a59935`, one step, about 0.0218 USD) ended on a
  model question that the bridge cannot answer; I stopped it, restarted the bridge daemon and
  relaunched. The second run took 8 steps, cost 0.127914 USD (0.149719 with the first run) against a stated cap of 0.60
  (harness stops near 0.216), 0 refused, no `local_input` pause. Nothing bought, claimed or
  tapped inside a page; the Warzone Duel and VS buttons were not touched.
- Closing state: the base, no panel open, token released.
