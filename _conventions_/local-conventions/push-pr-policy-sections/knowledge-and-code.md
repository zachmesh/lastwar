---
title: Knowledge and code pull requests
created: 2026-11-23T08:37:00Z
modified: 2026-11-23T08:37:00Z
version: 0.1.0
sequence: 5
description: Everything outside the four records paths is load-bearing and lands by its own pull request -
---
## Knowledge and code pull requests

Everything outside the four records paths is load-bearing and
lands by its own pull request: `_tools_/` (the only exception
inside `_tools_/` is `_tools_/state/` above), `_conventions_`,
`_activities_`, the root documents and `AGENTS.md`, and
anything not listed under the records flow by default.

1. **Branch.** Locally, branch from current main:
   `git checkout -b work/<slug>`. One branch carries one
   coherent change.
2. **Commit.** Conventional Commits with the `Confidence` and
   `Scope-risk` trailers, as everywhere in this repository -
   and no `_logs_` appends on the branch (next section).
3. **Ship the branch.** Bundle the branch to the VPS, fetch
   it in `~/lastwar-push`, `git push github work/<slug>`.
4. **Open the PR.** `gh pr create` from the VPS route. The PR
   body is required to state four things: the improvement
   task it serves (a backlog id from the retro improvements
   backlog, or the owner decision that called for it); its
   target metric, from
   [evaluation metrics](evaluation-metrics.md) where one
   applies, with the current value; the validation actually
   performed and its result; and the file list.
5. **Review and merge.** The integrator reviews and merges
   clean PRs by squash (`gh pr merge --squash
   --delete-branch`); see the integrator section for the full
   duty list, including the classes it must never merge.
6. **Sync main back.** A merge creates commits that exist
   only on GitHub, so after any merge the integrator syncs
   main back to the local clone through the VPS bundle route
   before the next local commit, exactly as in version 1.0.0.
   Never force either side; if a fast-forward fails, stop and
   reconcile by hand.

