---
title: Oil Well collect 1534
created: 2026-11-23T15:40:00Z
modified: 2026-11-23T15:40:00Z
version: 1.0.0
description: Unit harvest-oil-well-2026-11-23-001 - the OIL panel behind the top-bar barrel icon collected 3,760 oil in one Collect (owned 647,039 to 650,799, output 1.2K an hour); the Oil Well tag, storage and the Lv.1 to 2 upgrade preview were not read because the building was not located
status: partial
grounded_in:
  - source: cu_bridge run 20261123T153410Z-ded5d6, frames step-0001 (before), step-0002 (after) and step-0003 (base), 2026-11-23T15:34Z
  - source: unit brief harvest-oil-well-2026-11-23-001 and _records_/2026-11-22/queue-planning/2650-oil-routine-sheet.md
---

# Oil Well collect

Rows in [1534-queue-run.csv](1534-queue-run.csv); one ledger row. Claimed 15:32:59Z; the cu-integrator gate run (`gate-cu-pr895-10941168a-t663285888`, from 15:31:06Z) held the desktop until 15:33:58Z and I sent no input until it cleared. No different-device dialog; no player names.

- **Route (measured).** The blue barrel icon in the top bar at about (231,115) opens an **OIL panel** like the COIN, FOOD and IRON panels: Owned, Building Acquisition with **1.2K/H**, a Collect Resources row, two in-game task rows and a $19.99 pack. Collect at about (553,501), panel X at (612,209).
- **Collect.** Oil counter **647.0K to 650.7K**; owned **647,039 to 650,799 (+3,760)**; Available **3760 to 0**; one Collect tap at **15:34:22.728Z**. No capacity figure is shown (the bar is full green).
- **Minutes since the last collection.** None earlier exists. 3,760 at 1.2K an hour is about 188 minutes, so accrual began about 12:26Z [G]; Unlock Oil Well was completed at 11:53:01Z. By the routine sheet the next collection is due about 23:30Z, eight hours after this one.
- **Not read: blocked by route.** The panel shows no building name, level or storage, and the tag text of the Oil Well, its storage and the Lv.1 to 2 upgrade preview need the building, which no record locates. The panel's Details button was not pressed (its effect is unrecorded) nor the two Go rows or the offer pack; I did not hunt for the building by tapping.
- **Run.** `claude-gateway/claude-sonnet-5-5`, 4 steps, 0.060045 USD against a stated cap of 0.5; 0 refused. Food 655.1M, iron 1.0G, coin 13.4M and Total Power 150,416,946 unchanged.
- **Closing state.** The base, no panel; LastWar frontmost; token released.
