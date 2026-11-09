---
title: Logs
created: 2026-10-25T17:56:00Z
modified: 2026-10-25T17:56:00Z
version: 1.0.0
description: Append-only repository logs
grounded_in:
  - source: human-authored
---

# `_logs_`

Type folder, from reflection's vocabulary — append-only entries. This is
the repository's own record and sits at the root. Lines are never edited,
reordered or deleted; a correction is a new line.

## Contents

- [`repo-actions/`](repo-actions/INDEX.md) — one entry per action that
  changes tracked content.
- [`user-inputs/`](user-inputs/INDEX.md) — the owner's inputs to this
  project, redacted where they carry secrets or personal data.
