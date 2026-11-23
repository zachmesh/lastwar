---
title: Perception scout queue run 0022
created: 2026-11-23T08:27:00Z
modified: 2026-11-23T08:27:00Z
version: 1.0.0
description: Growth snapshot unit P2 scout-midday-growth-snapshot-2026-11-23-011, operator seat, read-only look for the troop Promote control on the Lv.30 barracks, none found, arrows are card markers
status: run-partial
grounded_in:
  - source: cu_bridge start, status poll, events and final result on run 20261123T082236Z-f0bb84, 2026-11-23T08:22Z to 08:23Z
  - source: frames step-0003.png (TRAIN UNITS) and step-0004.png (Hospital menu) read by the operator, the first saved as _tools_/state/cu_growth_p2_0022.png (untracked)
  - source: unit brief and snapshot schema j_promote in 2345-snapshot-schemas.csv
---

# Perception scout queue run 0022

- Unit scout-midday-growth-snapshot-2026-11-23-011, operator seat, assignment
  A-20261123-0821-operator, attempt 1, claimed 08:22:29Z. Rows, in schema j_promote, are in
  [../growth/0022-p2-promote.csv](../growth/0022-p2-promote.csv).
- Run `20261123T082236Z-f0bb84`, model `claude-gateway/claude-sonnet-5-5`, max-steps 8,
  ended `completed` after 5 steps. Actions done 10, refused 0. Model time 7.7 s per step.
  Cost 0.087692 USD. The run started on the Backpack and went back to the base first:
  no boarding banner, no account dialog. No takeover.
- **Barracks Lv.30, busy.** Pistol opened TRAIN UNITS with no toast. Training in progress
  1d 02:55:29, Lv.10 x793. Cards Lv.7 1,116, Lv.8 2,141, Lv.9 1,878, Lv.10 35.1K selected,
  Lv.6 cut off. Green up arrows on the corner of the Lv.7, Lv.8 and Lv.9 cards, enabled,
  no red dot. **No (i) help icon, no Promote button, no promote panel**, no cost, no
  requirement line, no Drill Ground wording. Only a Speed Up button, not tapped.
- **Why the arrow did nothing.** Per the brief the arrows were not tapped, because the
  lower-tier counts are not zero. The 08:02Z run tapped the Lv.9 arrow twice: it only
  selected the card and switched the six stats to Lv.9, with no popup. So the arrow is a
  card marker, and a busy barracks offers no promote action.
- **Per-troop power is on the panel:** Power 1647 on Lv.10 and 1352 on Lv.9 match the
  guide claim; promoting one Lv.9 troop would add 295 power, if the guide holds.
- **Second read not done.** The upper-right tent read Hospital Lv.20 (blue people icon,
  orange tent icon, green arrow, no pistol), so there was no barracks pistol to read.
  An earlier run read it as Barracks Lv.20: unresolved. The idle Barracks Lv.24 still
  gives "Drill Ground Full: Unable to add more units." with no panel.
- **Verdict:** the promote panel stays unreachable while the barracks are busy or the
  Drill Ground is full; cost per troop, requirements and time are unknown. Blocker f.
- Closing state: the base with the Hospital menu open around its tent. Nothing pressed.
- Red lines held: no Promote, Train, Collect, Speed Up or Upgrade.
- Follow-up: retry when a barracks finishes (Lv.27 about 19:56Z) with Drill Ground room.
