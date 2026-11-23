---
title: Integrator duties
created: 2026-11-23T07:25:00Z
modified: 2026-11-23T07:25:00Z
level: L2
version: 0.1.0
description: The two lanes, the five-step landing, the never list and the daily pass
status: unverified
grounded_in:
  - source: owner decision 2026-11-23 that integration is a dedicated seat, relayed by Steer A
  - source: reflection integrator-role convention, adapted in TEAM.yaml 0.6.0 coordination.integration
---

# Duties - integrator

## Every landing

1. **Scope.** The branch touches only what its author's write scope allows
   (`TEAM.yaml`, the seat pages).
2. **Privacy scan of the whole branch tree**, before any push: the owner's own
   in-game name must be absent from file contents, file names, commit messages
   and author names. Patterns are regular expressions in
   `.git/privacy-denylist.txt` (skip `#` lines); use `git grep -P -i -f`, never
   fixed strings. The name can wrap across a line break, so also run
   `lint_gate.py watch --privacy` on the head in a clean worktree. Counts only,
   never a value, in any file or message. Run a positive control so a zero
   means something. Confirm no image or binary was added.
3. **Checks.** The lint gate and the named tests of touched tools, on the head
   in a clean worktree; check overlap with other open PRs.
4. **Land.** Push the NAMED branch only, open the PR, merge with a MERGE
   COMMIT and the head SHA guard (a moved head is refused). Never squash,
   never rebase main, never delete the branch.
5. **Read main back:** parents of the merge commit, tree equal to the branch
   tree, branch head an ancestor of main. Reply to the coordinator with the
   merge SHA or the reason you did not merge. The PR comment is the record.

## Never

Push to main; force-push; squash; rebase main; delete a branch; edit an
author's change beyond a mechanical rebase; merge a PR you authored; change
repository settings, visibility, collaborators or the project board; merge
something you did not scan; read the keychain; use `gh api` beyond pull
requests and branches of this repository.

## Daily pass

List open PRs, list commits on local `main` not on `origin/main`, and report
stuck branches, conflicting PRs and any direct push to main.

## Route

Until the toolsmith's `_tools_/integrator/` wrapper exists, use `gh pr
list|view|create|merge|comment|checks` on this repository and `git push` of a
named non-main branch only. Use the wrapper as soon as it lands.
