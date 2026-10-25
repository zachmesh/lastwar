---
title: Records
created: 2026-10-25T17:56:00Z
modified: 2026-10-25T18:58:00Z
version: 1.1.0
description: Append-only audit records of changes made on the game account
grounded_in:
  - source: human-authored
---

# `_records_`

Type folder, from reflection's vocabulary — append-only audit records of
changes made to an external system, one instance per kind of change. The
external system here is the game account. Records are trajectories under
constitution C1 and are never edited or deleted.

## Contents

- [`play-sessions/`](play-sessions/INDEX.md) — the narrative play record,
  one file per day.
- [`activity-executions/`](activity-executions/INDEX.md) — one file per
  activity type, with a dated entry for every round that performed,
  partly performed, checked, or deliberately did not perform it.
