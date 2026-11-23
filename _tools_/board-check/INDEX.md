---
title: Board Check
created: 2026-11-23T05:05:46Z
modified: 2026-11-23T05:05:46Z
version: 1.0.0
description: Read-only check of the GitHub Project board against the project-boards convention, reported as JSON
---

# Board check

Compares the team board (user dtadpole, project 11 by default) with reflection's project-boards convention. Target
metric: board drift findings, reported by the tool itself in `drift_findings`.

```
GH_TOKEN=... python3 _tools_/board-check/board_check.py [--text] [--project N --seats a,b,c]
```

The token comes only from `GH_TOKEN` or `GITHUB_TOKEN` in the caller's environment. The tool never reads the keychain or
a credential helper, never prints the token, and exits 2 with a message when none is set. It only issues queries.

## What it checks

- Five views, in this order and case: Kanban, By Agent, Recently Done, Feedback loop, Epics. Each must be a board with
  its filter, column field, card fields and no swimlanes. Epics use `label:epic`; `--epic-by type` switches to `type:Epic`.
- Fields and single-select options, including Agent (`owner (zhenc)` plus `lastwar <seat>` per assigned seat in
  `TEAM.yaml`) and Priority (`P0` to `P3`): missing, extra, off by case, wrong order.
- Coverage of open issues: epic parent and Agent percentages, issues off the board, and epics without
  `## Acceptance criteria`; each count carries its first 10 numbers.

Two reference-board variances, `verified` among the Feedback state options and Feedback loop columns by Status, are notes;
`--strict` makes them drift. Tab order is the API listing order.

## Output and tests

JSON by default, `--text` for a short report. Exit 0 clean, 1 drift, 2 cannot read. `--fixture PREFIX` reads recorded
responses from `fixtures/` instead of the network. Tests: `python3 -m unittest discover -s _tools_/board-check`.
