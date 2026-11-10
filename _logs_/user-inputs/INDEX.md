---
title: User Inputs
created: 2026-10-25T17:56:00Z
modified: 2026-10-25T17:56:00Z
version: 1.0.0
description: Append-only log of the owner's inputs to this project
grounded_in:
  - source: human-authored
---

# User inputs

Instance folder. `input-log.jsonl` carries one JSON entry per owner input,
with `timestamp`, `channel`, `session`, `text` and `redacted`. Text is
verbatim; secrets and personal data are masked as a redacted marker with
`redacted` set, because git history is permanent. Only inputs the harness
delivers are captured, so the log cannot be complete. Append-only under
constitution C1.
