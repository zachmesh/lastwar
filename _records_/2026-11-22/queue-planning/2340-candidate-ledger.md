---
title: Queue Planning Growth Plan Candidate Ledger Design 2340 2026-11-22
created: 2026-11-22T23:44:00-08:00
modified: 2026-11-22T23:44:00-08:00
level: L0
version: 1.0.0
description: Planner design for story 870 part one - the candidate ledger CSV template, a ranking rule, three evidence-based challenges to the growth-plan model, and a serves-line proposal; the ranking itself waits for the snapshot
status: done
activity: queue-planning
run_id: queue-planning-2026-11-22-2340-candidate-ledger
trigger: coordinator assignment A-20261123-0741-planner, Epic 867 story 870 first part
started_at: 2026-11-22T23:37:11-08:00
finished_at: 2026-11-22T23:44:00-08:00
verified: every figure recomputed from the cited records; nothing in the game touched, no unit staged for this item yet
grounded_in:
  - source: _records_/2026-11-22/queue-planning/2340-candidate-ledger-template.csv, 4 example rows
  - source: _activities_/troop-training/changelog-section-p11.md, _activities_/research-queue/run-20261109-2031.md, _knowledge_/events-and-cycles/alliance-duel-the.md
  - source: _tools_/queue.py FM_ORDER at line 378 and dump_frontmatter at lines 453 to 456
---

# Candidate ledger, 2340

The template is [the CSV](2340-candidate-ledger-template.csv): 10 columns, 4 example rows. A cell not read says `unread`, and an item with an unread cell cannot be ranked.

## 1. Schema

- **Columns:** item, category, cost_by_resource, time, power_gain, binding_constraint, time_gate, serves, evidence_source, status.
- **Categories:** build, research, train, promote, hero-level, hero-skill, hero-weapon, hero-specialized.
- **Status:** unread, read, ranked, started, collected, verified, dropped.
- **Cost:** `resource=amount;...` as the panel shows it.
- **Power:** `+N`, tagged panel read or observed on collection.

## 2. Ranking rule

Score = power gained divided by the amount of the binding constraint consumed, per day. The binding constraint is the scarcest of a slot (builder, research or barracks, priced in slot-days), a capacity cap (Drill Ground units), or a resource whose stock covers the cost less than 3 times (priced in days of its measured income). Cost is read from the panel, never estimated. Power registers on collection, so the denominator includes the wait until the tent is tapped or Complete is pressed. Fit is a window, not a deadline: duel themes and Arms Race phases score only completions inside them, so an item whose finish lands inside its window beats an equal item that cannot. That bonus is a tie-break until duel points per power are measured.

## 3. Three challenges to the model, with evidence

1. **The baseline is a two-point difference, not a rate.** On 2026-11-09 Total Power read 149,217,331 at 16:35 and 146,730,949 at about 17:53 (issue #482, cause unverified): a fall of 2,486,382, 6.4 times the 390,502 net change over 29 days. Daily maxima rise only 19,124 a day from 10-26 to 11-22. The snapshot needs a control: Total Power at a fixed state twice daily.
2. **The larger lever is already measured: troops.** A 666-troop T8 batch gave +707,958 power (1,063 each) for 2.9M food and 2.9M iron in 1d 04:19:43, about 600k per barracks-day against 2,396 per builder-day. In food and iron it is 794 and 2,371 times cheaper per power than the Hut. A 313-troop T9 batch gave +423,176 (1,352 each). The constraint is not cost but Drill Ground capacity (39,460 of 39,460, the Full toast) and barracks time. Heroes and gear have no per-upgrade power read in the repo.
3. **The time gate is a window plus a collection delay.** Off-theme spending scores zero and completions score in the window they land in (`alliance-duel-the.md`; Arms Race rule 6).

## 4. `serves:` line

`FM_ORDER` lists the only keys `dump_frontmatter` writes, so a `serves:` key added by hand is silently dropped at the next claim. Proposal to the toolsmith: add `serves` to `FM_ORDER`, add `enqueue --serves`, have `validate` warn when an upgrade unit lacks it, and add the line to `_queue_/unit-template.md`. Until then, the first body line of an upgrade unit's brief is `serves: <plan item>`, which survives rewrites.

## 5. Next

No ranking until the snapshot (#868) exists. Snapshot units are staged when the scout's protocol lands, due 08:15Z.
