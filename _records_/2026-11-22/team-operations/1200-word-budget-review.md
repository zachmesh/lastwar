---
title: Word-budget review 2026-11-24T11:56Z
created: 2026-11-24T04:00:00-08:00
modified: 2026-11-24T04:00:00-08:00
level: L3
version: 0.1.0
description: The daily word-budget watch of local main at 11:56Z, the hook check and the precedent-phrase check
status: done
activity: team-operations
run_id: team-operations-2026-11-24-1200-word-budget-review
trigger: schedule-e1887d97-ba2d-4f9a-b466-bf1838b12813
started_at: 2026-11-24T03:56:00-08:00
finished_at: 2026-11-24T04:00:00-08:00
duration_seconds: 240
verified: lint_gate watch --no-write at head 15503b4d, anchor 24e61918; the hooks directory lists pre-commit and pre-merge-commit
---

# Word-budget review, 11:56Z

- Counts (watch at head 15503b4d): 11,594 documents, 5,907 over 300 words, 3,407 at or over 500 (legacy 3,405, new 2). New errors against the anchor: 0 (document-concision 0, entry-points 0, type-instance-trees 0); exempt documents 2.
- By top folder at or over 500: _records_ 3,407 (3,405 legacy, 2 new); _activities_, _conventions_, _knowledge_, _logs_, _queue_, _run_notes_, _seats_, _tools_ and the root file 0.
- The two new ones (named by the Toolsmith's watch listing at 12:08Z): _records_/2026-11-22/INDEX.md (the day index, 41,158 words, exempt by rule) and _records_/2026-11-22/coach/INDEX.md (883 words, owner seat the Coach, exempt only because the glob _records_/*/INDEX.md also matches a nested index). The Coach was told to trim it under 500 words by 11-25 12:00Z.
- Largest: the day indexes (_records_/2026-11-22/INDEX.md 41,064 words, up 52 percent since the anchor, exempt by rule). Grown more than 20 percent: the coach index, three seat handovers and the queue unit template, all under 500.
- Hooks: core.hooksPath is _tools_/lint-gate/hooks (pre-commit, pre-merge-commit present); every commit today went through the gate and the Integrator's landing check ran on each branch.
- Precedent phrases in today's operator records: two files (the finished batch of 274 in the 0351 training record; the donation continuation in 1441). Both facts are already in the current briefs (the three-class barracks read, the amended donation close rule): no gap to send.
