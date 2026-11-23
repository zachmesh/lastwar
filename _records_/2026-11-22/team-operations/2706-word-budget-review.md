---
title: Daily word-budget review - 2026-11-23 12:06Z
created: 2026-11-23T04:06:00-08:00
modified: 2026-11-23T04:12:00-08:00
level: L3
version: 0.1.0
description: The 12:00Z daily watch of the document word budget - counts by top folder, the new documents over 500 words with their owner seats, and the enforcement check
status: done
activity: team-operations
run_id: team-operations-2026-11-23-1206-word-budget-review
trigger: schedule-e1887d97-ba2d-4f9a-b466-bf1838b12813, 2026-11-23T12:00:00Z firing (owner priority P1, IMP-20261123-10)
started_at: 2026-11-23T04:05:00-08:00
finished_at: 2026-11-23T04:12:00-08:00
verified: lint_gate watch --no-write run on local main (head 42c0189e, anchor 24e61918) at 12:05:50Z; core.hooksPath read; the check --base origin/main output read for the two blocking lines
---

# Daily word-budget review

## Counts (watch, 12:05:50Z)

10,915 documents; over 300 words 5,691; at or over 500 words 3,407 (legacy 3,405, new 2). By top folder, at or over 500: `_records_` 3,407 (legacy 3,405, new 2); `_activities_`, `_conventions_`, `_knowledge_`, `_queue_`, `_run_notes_`, `_seats_`, `_tools_`, root and `_logs_` 0.

## New errors against the 08:27Z anchor: 2

| Item | Owner seat | Action |
|---|---|---|
| `_records_/2026-11-22/growth/0054-operator-handover-detail.md`, 544 body words (the base-map and tag-index sections grew it) | operator | split under 500 within 24 hours: move the base-map section to the existing record 1030-base-map and the tag index to its CSV |
| `_queue_/completed`, no entry point (a gitignored live-only folder the watch counts from the working tree: a false positive) | toolsmith | make watch and check skip gitignored folders |

## Enforcement

Hooks in force: `core.hooksPath` is `_tools_/lint-gate/hooks`; its `pre-commit` and `pre-merge-commit` both call `lint_gate.py`. The Integrator's landing check is in the wrapper branch (not yet on origin); until it lands the plain base check applies.

## Growth to watch

The watch lists 20 documents grown over 20 percent since the anchor; the largest are the Integrator's `landings.md` (208 to 429 words), `integration/INDEX.md` (76 to 296), the scribe's `duties.md` (88 to 273) and the model-policy section (122 to 297); none is at 300 words except as shown, none over 500.
