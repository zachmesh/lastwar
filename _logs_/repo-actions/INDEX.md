---
title: Repo Actions
created: 2026-10-25T17:56:00Z
modified: 2026-10-25T17:56:00Z
version: 1.0.0
description: Append-only action log for changes to tracked content
grounded_in:
  - source: human-authored
---

# Repo actions

Instance folder. `action-log.jsonl` carries one JSON entry per action, with
`timestamp`, `actor`, `action`, `paths`, `reason` and `commit`. The
`commit` field is null for the entry shipped inside the commit it
describes. Append-only under constitution C1.
