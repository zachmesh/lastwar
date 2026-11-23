---
title: Lint audit and size plan - 2026-11-22 20:36 PT
created: 2026-11-22T20:36:00-08:00
modified: 2026-11-22T20:39:00-08:00
level: L3
version: 0.1.0
description: The reflection linter run against lastwar, the oversized-document findings, and the plan for a commit gate, a size trigger and splitting the large profiles
status: done
activity: team-operations
run_id: team-operations-2026-11-22-2036-lint-audit
trigger: owner instruction 2026-11-23T04:34Z - run the linter, set up triggers and a linter, split oversized files
started_at: 2026-11-22T20:34:00-08:00
finished_at: 2026-11-22T20:39:00-08:00
duration_seconds: 300
verified: lint-conventions.py full run over the working tree, 57 s, JSON at /tmp/lw-lint.json (not committed)
---

# Lint audit and size plan

## Measured

- Errors 505: entry-points 454 (450 are records folders with no INDEX.md), type-instance-trees 29, team-record 16 (known exception), document-concision 5, repo-graph 1.
- Warnings 3,491, of which 3,452 are legacy document-concision.
- Budget is 300 words recommended and under 500 hard. Of 7,467 documents, 4,102 exceed 300 and 3,456 reach 500 (3,451 legacy, 5 new).
- The 5 new errors are today's per-unit operator records, 514 to 656 words.
- 3,406 oversized documents sit under `_records_/` (4.65M words); 31 under `_activities_/` (682,023 words). The seven largest profiles are 39k to 84k words, alliance-donations first.
- Today's day index is 18,411 words and grows with every tick line.
- No commit hook exists.

## Constraints

Play records are immutable (C1), so legacy records are not split; they stay legacy warnings. Knowledge is versioned, never destroyed (C2), so profiles split by verbatim move, with a version bump and a changelog line.

## Plan

1. Gate and trigger: toolsmith builds `_tools_/lint-gate/` (check, install, watch, record-check). Dispatched 04:37:56Z.
2. Pilot split: scribe splits alliance-donations into an index of 300 words or fewer plus articles under 500 words each, by verbatim move. Then the other six large profiles.
3. New records: the operator keeps per-unit records under 480 words, measured data in a sidecar CSV, checked by `record-check`.
4. Open owner or scribe decisions: INDEX.md files for 450 records folders (additive, but whose scope); hourly day-index files; the team-record exception.

## Follow-up

Install the hook after review. The tick runs `watch`; any new error assigns the owning seat.
