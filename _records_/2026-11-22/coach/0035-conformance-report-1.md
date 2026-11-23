---
title: Conformance report 1 - plan coverage, slots, adherence, partials, drift
created: 2026-11-23T08:35:00Z
modified: 2026-11-23T08:40:00Z
version: 1.0.2
description: First coach conformance report for the loop, with the six KPIs computed from the queue and the records at 08:36Z, counts only, and the drift list
status: done
activity: coach
run_id: coach-2026-11-23-0035
trigger: coordinator assignment A-20261123-0830-coach
started_at: 2026-11-23T08:30:00Z
finished_at: 2026-11-23T08:35:00Z
duration_seconds: 300
verified: no
grounded_in:
  - source: _queue_/inbox, claimed, done and completed parsed at 08:36Z; the 6 h counts reproduce Steer A (16 done, 14 partial, 2 failed)
  - source: _knowledge_/growth-plan/strategy-plan-p1.md and strategy-plan-p2.md, items P1 to P9
  - source: operator and scout records in _records_/2026-11-22/growth and perception-scout
---

# Conformance report 1

Figures are in [conformance-kpis.csv](conformance-kpis.csv); executed units in [conformance-units.csv](conformance-units.csv). Tags map to plan items: capacity source is P2, collect finished batches P3, fill idle slot P8, snapshot and baseline are read or measure.

**(a) Coverage.** Executed units with a serves tag: 3 of 32 in 6 h (9.4%), 3 of 63 in 24 h; all three are snapshot reads. Executed units serving a growth action: 0. The queue is better: of 79 units, 21 (26.6%) are growth actions (P8 16, P2 4, P3 1), 20 read or measure, 38 upkeep (48.1%). Busy slot-minutes started by a plan item: 0 of 6,818 in 24 h.

**(b) Slots, 24 h.** Idle builder minutes 4,080 of 5,760 (70.8%; 58.3% in 6 h). Labs: 0 idle observed, 16 hours unobserved. Training: 2,062 of 4,320 barracks-minutes idle (47.7%), Lv.24 capacity-blocked, Lv.20 unprobed ([slots](slot-idle-minutes.csv)).

**(c) Adherence.** 7 triggers listed ([triggers](plan-triggers.csv)); none is past its trigger plus 2 h, so 0 of 0. First measurable: the lab at 11:43Z, due 13:43Z.

**(d) Partials.** 43.8% in 6 h (14 of 32), 57.1% in 24 h (36 of 63). Growth-chain units: 2 of 3 partial. Blocker letters over 24 h: h by-design 20, e repeated 5, f missing precondition 5. Growth units' top two, by the operator's text: (1) room, a promote read waits on an idle barracks with Drill Ground room, and Drill Ground Full refused 7 times in 4.3 hours across 6 records; (2) tap method, a Lv.20 barracks taken for the hospital cost re-picking turns. Hospital Collect has no quantity selector, so it is all or nothing.

**(e) Power by category.** No plan targets exist; the charter review is 2026-11-30. Actual 11-08 to 11-22 per day: hero +65,799, drone +2,291, building -37,271, unit plus tech -6,020, total +24,799. Collect-first fixed-state reads: 0 of 1; the slot A read is unfixed.

**(f) Drift** ([list](drift-list.csv)). Top three:
- D5, high: no state-changing growth action since the plan landed; all 21 queued ones wait on a trigger or on room.
- D1, retired: the serves field survives claim and complete in the frontmatter. The done copy of snapshot-003, claimed after the 08:29Z backfill, holds it; my first reading was a pre-backfill artifact.
- D3: tags are free text, not P1 to P9 ids.

The other six are in the list. Next report at the coordinator's 12:00Z wake.
