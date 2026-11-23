---
title: Lint gate summary
created: 2026-11-23T04:53:59Z
modified: 2026-11-23T04:53:59Z
version: 1.0.0
description: Verbatim index rows for lint-gate
---

# Lint gate summary

Moved verbatim from the former `_tools_/INDEX.md` table; only link destinations are adjusted for this folder. Back to the [tool index](../INDEX.md).

| Tool | Purpose | Data |
|---|---|---|
| [lint-gate](../lint-gate/INDEX.md) | Commit gate and size trigger over the reflection convention linter (IMP-20261123-03): `lint_gate.py check --staged` blocks a new or changed document at 500 body words or more, a new folder without `INDEX.md` and a new file in a type folder, in about a second, while legacy findings never block; `check --base REF` is the full-lint form for review; `install` sets `core.hooksPath` to the tracked pre-commit hook (rollback `git config --unset core.hooksPath`); `watch` counts documents over 300 and 500 words (legacy versus new, by top folder), lists the 10 largest and any document that grew more than 20 percent, and writes a summary baseline; `record-check PATH` exits 1 at 480 body words so a record is trimmed before it closes a unit; exit 0 ok, 1 blocked, 2 cannot run | `_tools_/state/lint-baseline.json`, `exempt.txt` and the linter at `~/dtadpole/reflection` |
