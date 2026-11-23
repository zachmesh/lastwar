---
title: Integrator
created: 2026-11-23T08:56:35Z
modified: 2026-11-23T09:06:31Z
version: 1.1.0
description: The Integrator seat's wrapper for landing a branch on main - status, check, push, open, merge, readback
---

# Integrator

`integrator.py` is the one sanctioned route for landing a branch (steps in `_seats_/integrator/duties.md`), through `gh` (already
logged in) and git. Nothing reads, prints or stores a credential; every line is scrubbed of token shapes.

| Command | Does |
|---|---|
| `status [--json]` | Open PRs, local main ahead and behind origin/main with the local-only SHAs, direct pushes to main in 24 h, the claimed folder, a shallow-clone warning. |
| `check BRANCH --seat KEY [--test DIR]...` | Scope against the seat's `write_scopes` in TEAM.yaml; the denylist by `git grep -P -i -f` over contents, file names, messages and authors, and by the wrap-aware `lint_gate.py watch --privacy --worktree` in a clean worktree; a positive control on made-up text; no binaries; the lint gate in its landing form (`--base --landing`: a gate that cannot run, exit 2, blocks); the named tests; overlap with open PRs. Counts only. |
| `push BRANCH` | Pushes that named branch, never forced, only at a head with a passing check. |
| `open BRANCH --title T` | Opens the PR into main; the head must be on origin. |
| `merge PR --head-sha SHA` | `gh pr merge --merge --match-head-commit`; refused when the head moved, base is not main, or no passing check is recorded. |
| `readback PR` | Two parents, tree equal to the branch tree, head an ancestor of main. |

**Privacy gate of a landing:** this `check`'s whole-tree scans (`git grep -P -i -f` plus the wrap-aware census) are it. `lint_gate.py check --base` never scans added lines for the denylist, only its census guard; keep the scans.

It REFUSES main, force, squash, rebase, branch deletion and `--no-verify` (not options; on the command line they stop the run).
One JSON line per action goes to `_records_/<date>/integration/actions.jsonl`: counts and SHAs. Exit 0 ok, 1 failed or not
passing, 3 refused. Tests run on a bare repository and `fake_gh.py`: `python3 -m unittest discover -s _tools_/integrator`.
