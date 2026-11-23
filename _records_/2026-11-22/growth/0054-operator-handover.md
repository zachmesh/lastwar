---
title: Operator handover 0054
created: 2026-11-23T09:10:00Z
modified: 2026-11-23T09:10:00Z
version: 1.0.0
description: Handover of the Last War operator seat at about 85 percent context - launch route, safeguards for any Use press, open items; detail rows in the sidecar
status: handover
grounded_in:
  - source: operator session work 2026-11-23T05:30Z to 09:10Z, runs and records cited in 0054-box-chest-read.md and the day INDEX
  - source: coordinator addendum A-20261123-0850 safeguards, Steer A decision 2425
---

# Operator handover 0054

Detail rows: [0054-operator-handover-detail.md](0054-operator-handover-detail.md).

- **Seat.** Only the operator holds the device token and sends game input. Reply to the
  coordinator in four lines (STATUS, ARTIFACT, MEASUREMENT, NEXT) with the session-relay
  command in the sidecar. Never name the owner account in a file or message.
- **Launch route.** Per run: `queue.py token-acquire`, `claim` for a queue unit, then in one
  shell `killall -9 UserNotificationCenter NotificationCenter`, check `lsappinfo front`
  names LastWar, then `cu_bridge.py start --task ... --model claude-gateway/claude-sonnet-5-5
  --max-steps N`. N steps means N-1 executed; the last turn is the report. One action per
  turn, never zoom, never Escape. The harness cost cap stops near 0.36 of the stated
  `--max-cost`; a step costs about 0.012 to 0.015 USD.
- **Hard safeguards for any Use press.** Owner red lines: no purchase, no diamond spend,
  no speed-up or Finish Now, no PvP or march, no diplomacy, no ally exchange. A quantity
  slider defaults to the full count for the Mystery Supply Box (about 365) and to the first
  selected tile; check the number field reads exactly 1 in a frame before Use, press Use
  once per run, split the check and the press into two runs, read the popup.
- **Interrupts.** Account dialog: tap Confirm once, never twice within 30 minutes. Train
  boarding banner with 70 s or more: board first. Local pointer input pauses a run: stop it
  with `cu_bridge.py control --command stop` and relaunch.
- **Done today.** Troop, hospital, capacity, F1, S1, T2 reads; the 4-hour UR claim at
  08:51:08Z; inventory read; one box, one SR choice chest and one SR coin chest opened.
- **Open items.** Part A names (Universal Shard counts, Gear tab, Bond Badges,
  Guidebooks, Training Certificates, Black Market currency); rarity of the box's chest;
  Hidden Treasures badge; the next 4-hour claim; the Drill Ground (+200 Unit Count per
  level) and Headquarters (needs Base Expansion research) upgrade plans; Lv.27 barracks
  finishes about 19:56Z; builders free 2026-11-24T09:20Z; research frees about 11:43Z.
- **Game state.** On the base, no panel open. Coin 9.7M, food 641.3M, iron 1.0G,
  diamonds 11,136, Total Power 150,211,809.
