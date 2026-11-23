---
title: Lint Gate Hooks
created: 2026-11-23T04:50:00Z
modified: 2026-11-23T08:35:35Z
version: 1.1.0
description: The tracked git hook folder that install points core.hooksPath at
---

# Lint gate hooks

`pre-commit` and `pre-merge-commit` both run `lint_gate.py check --staged` and block when it finds a new or changed
oversized or misshapen document. `pre-merge-commit` exists because `git merge` skips `pre-commit`: a merge commit gets
the same check, and a blocked merge stays pending (fix it or `git merge --abort`). `install` sets `core.hooksPath` to
this folder. Rollback with `git config --unset core.hooksPath`; skip once with `git commit --no-verify` or
`git merge --no-verify`. A fast-forward makes no merge commit, so no hook runs.
