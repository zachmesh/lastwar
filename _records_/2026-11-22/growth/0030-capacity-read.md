---
title: Capacity read 0030
created: 2026-11-23T08:36:00Z
modified: 2026-11-23T08:36:00Z
version: 1.0.0
description: Growth continuation A-20261123-0830-operator, read-only capacity read - Drill Ground Lv.28 Unit Count +9211 confirmed, Hospital Collect has no quantity selector, no soldier-icon cap found
status: run-partial
grounded_in:
  - source: cu_bridge runs 20261123T083008Z-f82839, 20261123T083151Z-382453 and 20261123T083309Z-070798, events, final results and frames, 2026-11-23T08:30Z to 08:33Z
  - source: earlier frames cited per row in the CSV, runs 20261123T075737Z-10f416, 20261123T080021Z-522249, 20261123T074723Z-fdee03
  - source: coordinator assignment A-20261123-0830-operator
---

# Capacity read 0030

- Rows in [0030-capacity-read.csv](0030-capacity-read.csv). Three runs on
  `claude-gateway/claude-sonnet-5-5`: 4, 1 and 3 steps, actions done 8, 2 and 4, refused 0.
  Cost 0.083168, 0.025531 and 0.047247 USD, total 0.155946, six thousandths over the 0.15
  cap: the harness cost cap stops runs near 0.36 of the stated figure. The first run left
  the read early, the second hit that cap after one tap. No takeover, no dialog, no
  boarding banner. Nothing trained, collected, upgraded, converted or spent.
- **(1) Soldier icon count and cap: not found.** No HUD or base element shows a soldier
  icon with an x/y text. The two blue-helmet portrait bubbles carry tiny digits, about
  523 and about 110 on an earlier crop, meaning unknown. The Hospital line
  "Severely Wounded Units 364/7999" is the only x/y troop figure seen. Where an army cap
  lives is open.
- **(2) Drill Ground Building Details, read twice, identical:** Lv.28, Unit Count +9211,
  no used-over-cap wording, four survivor slots all post Officer, only Quick Dispatch
  (not tapped).
- **(3) Formations:** two separate red formations are visible, the large one labelled
  Drill Ground Lv.28 and a second at the bottom right edge whose label stayed unread
  (the WORLD button covers its tap point). Only one Drill Ground is confirmed.
- **(4) Hospital panel, from the 07:58Z frame:** a quantity selector (slider at maximum,
  minus, plus, number field 364) exists for the Severely Wounded unit row only. The
  Completed 5306 line has no selector, and Collect is the only control. The Collect
  toast names all 5306 at once: "Drill Ground Full: Unable to add 5306 units." Reading
  stands; the (i) text stays unread because the panel would not reopen twice. The
  portrait bubble opens the Hospital only after a tap on the Hospital roof in the same
  run.
- Base now: no panel, no radial menu.
- Follow-up: select the second formation after hiding the WORLD button overlap, read the
  Hospital (i), and find the army cap screen, perhaps the Heroes troops page.
