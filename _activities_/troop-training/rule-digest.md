---
title: Troop Training Rule Digest
created: 2026-11-23T06:48:39Z
modified: 2026-11-26T16:51:14Z
level: L1
version: 0.12.0
description: The standing rules an operator must follow when training troops, each cited to the split article file that carries it
status: unverified
grounded_in:
  - source: split articles what-this-activity, cadence-section, limits-section, how-it-is-p1 to p3, how-to-enter-p1 to p5, day-20261025, day-20261031-p1 to p6, day-20261105, open-questions, changelog-section-p1 and run-20261122-0134-p2, _records_/2026-11-22/troop-training/0134-queue-run.md, run-20261122-0958-p2, _records_/2026-11-22/troop-training/0958-queue-run.md and _records_/2026-11-22/arms-race/1005-queue-run.md in this folder, read for the standing rules, every cited phrase matched against the article text (39 of 39 matched)
  - source: assignment A-20261123-0632-scribe spare-time batch
---

# Rule digest

1. Keep every barracks busy: one batch each, highest unlocked tier, count at the cap, then Train (how-it-is-p1).
2. Tiers: Lv.24 T8, Lv.27 T9, Lv.30 T10; batches cost food and iron (cadence-section, how-it-is-p3).
3. Never tap Finish Now or the green upgrade arrow on a building tag; the grey up-arrow beside the cost row opens the promotion ([promotion](promotion.md)) (limits-section, how-to-enter-p5).
4. Read busy or idle from the "Training in progress" line, not the button time (how-it-is-p2).
5. A tap collects a finished batch; requeue is separate and can meet the Drill Ground Full toast (day-20261031-p3, day-20261031-p4). Press the pistol once per barracks per read when room could exist: a panel means an empty queue, the toast means a finished batch waits [D], and a collect admits what fits ([finished-batch lesson](finished-batch-lesson.md)). Also: a blocked slot closes with slots_blocked_by_capacity=<N> and capacity_blocker="<text>" (for example "Drill Ground Full"); a count without a blocker exempts nothing (`_tools_/strategy-conformance/INDEX.md`).
6. 2026-11-22: the toast did not reproduce; Lv.27 and Lv.30 requeued (day-20261031-p5, _records_/2026-11-22/troop-training/0958-queue-run.md).
7. Leave Quick Dispatch untapped: effect unverified (day-20261031-p1).
8. Ground tents and the button row fresh; a reused point selected another building (how-to-enter-p1, how-to-enter-p2). The buttons are small; the tap must be precise: a stray tap opened Building Details or the world map (`_records_/2026-11-22/troop-training/0134-queue-run.md`). Record the tag text, the name and level above the building, beside each panel number; none means [G] ([snapshot protocol](../perception-scout/snapshot-protocol.md); `_records_/2026-11-22/perception-scout/0022-queue-run.md`, `_records_/2026-11-22/growth/1047-f1b-drill-ground.md`).
9. Ruled out: tent long-press, lower-left portrait tent, formation flag (how-to-enter-p2, how-to-enter-p5, day-20261031-p5).
10. Four identical partials are a process failure; change route first (day-20261031-p3).

Unverified: [claims](unverified-claims.md). Errata: [errata](errata.md).

## Changelog

- 0.2.0 to 0.8.0, 2026-11-23 to 24 - Errata, decision, growth start, tag text, capacity names, pistol rule.
- 0.9.0, 2026-11-24 - A collect admits what fits.
- 0.10.0, 2026-11-24 - The toast means a finished batch waits.
- 0.11.0, 2026-11-25 - The stray-tap hazard of the button row.
- 0.12.0, 2026-11-26 - Promotion pointer.
