---
title: Queue Planning Age Of Oil Survey Additions From The Oil Analyst 2640 2026-11-23
created: 2026-11-23T04:53:00-08:00
modified: 2026-11-23T04:53:00-08:00
level: L0
version: 1.0.0
description: Planner pass adding Steer A's oil analyst items to the Age of Oil survey unit - the research speed percent first, base and effective time and cost for twelve named nodes, the dependency and parallel order for two labs, and the oil held
status: done
activity: queue-planning
run_id: queue-planning-2026-11-23-0453-survey-additions
trigger: coordinator message with the oil analyst's interim figures
started_at: 2026-11-23T04:50:00-08:00
finished_at: 2026-11-23T04:53:00-08:00
verified: the unit confirmed unclaimed before the edit; word count 442; validate exit 0
grounded_in:
  - source: coordinator message 12:50Z relaying Steer A's oil analyst
  - source: _records_/retro/owner-decisions-log/od-20261123-19.md
---

# Survey additions, 2640

`research-age-of-oil-survey-2026-11-23-001` (priority 1, read-only, window 12:55Z to 14:00Z) now reads, in this order: (1) the account's research speed percent and any research-speed bonus line, with where it was found and the tag text beside the number; (2) for Oil Output I level 1, Coin Output, Iron Output, Food Output V, Fast Builder V, Research Enhancement V, More Oil Wells, the Third Tech Center node, Parts Workshop, Oil Output II and III and Base Expansion, the BASE (original) time, the EFFECTIVE time, the coin, iron, food and oil cost, and the prerequisites; (3) the dependency order as a list, with the nodes that can run in parallel on two labs marked from the prerequisite lines; (4) the oil held (434K at the last read) and whether the Oil Well shows a stock or an output figure. It stays read-only, presses nothing, may take three runs split by tree rows, and continues the earlier partial reads (Special Forces, the Economy tail, the Development tail) only where they touch the Age of Oil path.

The oil analyst's interim figures are carried in the brief as [G] until read: 19 nodes, 4.08M oil, 618M iron, 618M food, 1.83B coin and about 942 lab-days of base time, serial, so lab time binds and not oil; about 885 base days with two labs. The finish depends on the research speed percent, which is why it is read first. The brief is 442 words.
