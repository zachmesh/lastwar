---
title: Records pull requests - batch cadence part 2
created: 2026-11-23T09:02:35Z
modified: 2026-11-23T09:02:35Z
version: 0.1.0
sequence: 5
description: The integrator keeps exactly one open records PR per live date branch.
---
The integrator keeps exactly one open records PR per live
date branch. When a records branch has no open PR, the
integrator opens one (`gh pr create`, base main, head
`records/<date>`; the body names the date and this policy -
records PRs carry no per-PR improvement id, their ledger
entry is this flow). Opening is unchanged by the batch
cadence - a records PR exists as soon as a branch carries
commits; only the merge waits for a batch point. At a batch
point, if the open records PR has new commits, the
integrator merges it with a merge commit
(`gh pr merge --merge`, never `--delete-branch`). The merge
commit is what keeps the scheme working: the date branch
survives the merge and keeps taking appends, and the
integrator opens a fresh PR for whatever arrived after the
merge.

Knowledge and code PRs are unaffected by this section: they
are still reviewed and merged promptly on every integrator
pass, exactly as before.

A records PR that conflicts with main is never force-merged
and never silently dropped. The integrator comments the
conflict on the PR, notes it in its run record, and the
conflict is resolved on the branch side; the normal cadence
resumes once the branch is clean.

