---
title: Lint Gate Hooks
created: 2026-11-23T04:50:00Z
modified: 2026-11-23T04:50:00Z
version: 1.0.0
description: The tracked git hook folder that install points core.hooksPath at
---

# Lint gate hooks

`pre-commit` runs `lint_gate.py check --staged` and blocks the commit when it
finds a new or changed oversized or misshapen document. Rollback with
`git config --unset core.hooksPath`; skip once with `git commit --no-verify`.
