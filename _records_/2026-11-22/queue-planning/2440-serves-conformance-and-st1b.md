---
title: Queue Planning Serves Conformance And ST1b 2440 2026-11-23
created: 2026-11-23T00:32:00-08:00
modified: 2026-11-23T00:32:00-08:00
level: L0
version: 1.0.0
description: Planner pass for the serves conformance loop - every unclaimed inbox unit now carries a frontmatter serves line, the unit template says what to write, ST1b is staged, and the plan and sync minting inputs are flagged for the toolsmith
status: done
activity: queue-planning
run_id: queue-planning-2026-11-23-0032-serves-conformance
trigger: coordinator message after the slot plan
started_at: 2026-11-23T00:30:00-08:00
finished_at: 2026-11-23T00:32:00-08:00
verified: a count of inbox units without a frontmatter serves line before and after; validate exit 0
grounded_in:
  - source: _tools_/queue.py FM_ORDER at line 380 and enqueue --serves
  - source: _tools_/regulars.json, whose entries carry no serves field
---

# Serves conformance, 2440

## 1. Count

Before: 56 of 79 inbox units had no frontmatter `serves:`, all unclaimed. The coordinator's 38 are the regular units; the other 18 are my own chain (16 snapshot units and the two power units), which carried the line in the body only, where the tool does not see it. After: 0 of 79. Values: `upkeep` on 38 regular units, `snapshot (Story 868)` on 16, `baseline (fixed-state Total Power)` on 2. Units I mint now pass `--serves`, so they carry it from the start; ST1b (`scout-midday-growth-snapshot-2026-11-23-021`, 09:05Z to 09:47Z, after ST1) is the first.

## 2. Template

`_queue_/unit-template.md` has one `serves:` line, saying `upkeep` for a regular unit, a plan item id for a growth unit, and `fill idle slot` until the Strategist's plan exists. A first edit left a stray blank line inside the frontmatter; I removed it, and the diff against HEAD is that one line.

## 3. Not mine to change

The roster `_tools_/regulars.json` has no `serves` field, and `plan` and `sync` do not copy one into the units they mint. Once enqueue refuses a unit without serves (the toolsmith's P2), the next waves staged by `plan` or `sync` would lack it. Proposal for the toolsmith: a `serves` key per roster entry, default `upkeep`, copied in `_produce_for_window`. Until then I patch units those commands mint at each pass.

## 4. Accepted

The 10,000-minute default per upgrade, with the 35,000-minute weekly cap. The one Mystery Supply Box and the one Resource Choice Chest are the operator's after the 08:51Z claim; I did not add the chest to the lab unit.
