---
title: Push and PR Policy
created: 2026-11-01T05:31:00Z
modified: 2026-11-01T05:31:00Z
version: 1.0.0
status: active
description: Two-tier push policy - execution records push straight to main, load-bearing knowledge and code land by pull request
grounded_in:
  - source: owner decision 2026-10-31 - lock main in effect by process, with the two-tier scheme chosen (records direct, knowledge and code by PR)
  - source: platform check 2026-10-31 - the GitHub account is on the Free plan and branch protection and rulesets return 403 on this private repository
---

# Push and PR policy

The owner asked on 2026-10-31 whether main should be locked and
all future pushes tracked as pull requests, and chose the
two-tier scheme: execution records keep flowing straight to
main, and load-bearing knowledge and code land by pull request.
The pull request list is the change ledger of this system -
every reviewed change states what it serves and how it was
verified, in one place the owner and the retro can read.

## The two tiers

### Tier 1 - direct push

Append-only trajectories and live state, whose value is their
continuity and which a review step would only delay:

- `_records_` - play records, append-only under C1.
- `_queue_` - the task unit pool and its state transitions.
- `_logs_` - the input and action logs.
- `tools/state/` - runtime state written by the tools
  themselves (for example the regulars tracker state).

Tier 1 keeps the existing route unchanged: commit locally,
`git bundle` to the IONOS VPS, fetch and fast-forward merge in
`~/lastwar-push`, `git push github main`, and verify with
`git ls-remote`. The ticker's per-pass commits are tier-1
commits and follow the pathspec discipline of
[recording rules](recording-rules.md): they stage only the
tier-1 paths above, by explicit pathspec, never a blanket add.

### Tier 2 - pull request

Everything the system stands on - knowledge and code whose
change deserves a reviewable record:

- `tools/` - all tool code, and `tools/regulars.json` by name;
  the only exception inside `tools/` is `tools/state/` above.
- `_conventions_` - designs, rules and specifications.
- `_activities_` - the task type profiles.
- Anything not listed under tier 1 defaults to tier 2,
  including this file, the root documents and `AGENTS.md`.

## The PR flow

1. **Branch.** Locally, branch from current main:
   `git checkout -b work/<slug>`. One branch carries one
   coherent change.
2. **Commit.** Conventional Commits with the `Confidence` and
   `Scope-risk` trailers, as everywhere in this repository.
3. **Ship the branch.** Bundle the branch to the VPS
   (`git bundle create /tmp/<slug>.bundle ^main work/<slug>`,
   scp with the known-hosts file and the standard key), then
   in `~/lastwar-push`: fetch the bundle into the branch and
   `git push github work/<slug>`.
4. **Open the PR.** From `~/lastwar-push`, where the `gh` CLI
   is logged in as the repository owner: `gh pr create`. The
   PR body is required to state four things:
   - the improvement task it serves (a backlog id from the
     retro improvements backlog, or the owner decision that
     called for it);
   - its target metric, from
     [evaluation metrics](evaluation-metrics.md) where one
     applies, with the current value;
   - the validation actually performed and its result;
   - the file list.
5. **Review.** Routine changes are reviewed by the main agent
   or by the daily retro before merging. A change that touches
   a red line, or loosens any standing rule, is not merged on
   agent review - it waits for the owner's approval, recorded
   in the PR.
6. **Merge.** `gh pr merge --squash --delete-branch` from the
   VPS route. The squash commit on main, with the PR number in
   its subject, is what the retro audit recognises as a
   PR-landed change.
7. **Sync main back.** A squash merge creates a commit that
   exists only on GitHub, so local main must be brought back
   in step before the next local commit, or the two mains
   diverge. In `~/lastwar-push`: `git fetch github main`,
   fast-forward its main, `git bundle create` that main and
   scp the bundle back to this machine; locally,
   `git fetch <bundle>` and `git merge --ff-only FETCH_HEAD`
   on main. Local main fast-forwards cleanly because every
   local commit reached GitHub through the same VPS route
   before the merge. Never force either side; if the
   fast-forward fails, stop and reconcile by hand.

## The ticker discipline

The execution loop commits records several dozen times a day,
and it must never sweep a tier-2 change into one of those
commits. This has already happened once: the scout production
seeds in `tools/queue.py` landed inside a ticker records
commit (d1fa5b9, 2026-10-31) instead of through a reviewed
change. The rule, stated for executors in
[recording rules](recording-rules.md), is: execution commits
stage only `_records_`, `_queue_`, `_logs_` and `tools/state/`
by explicit pathspec; a tier-2 change found sitting in the
working tree is left exactly as it is, noted in the run
record, and left for the PR flow.

## Emergency exception

An urgent fix may be pushed straight to main even when it
touches tier-2 paths - a broken tool that blocks the loop
does not wait for a review cycle. The exception is spent, not
silent: the same day's retro names the direct push, and a
retroactive PR is opened for the record, or the retro states
why none was needed.

## Audit

The daily retro's loop-health check gains one item under this
policy: scan the commits that landed on main since the
previous retro, and name every commit that touches tier-2
paths without being a PR squash merge (recognisable by the
PR reference in its subject) or a retro-named emergency
exception. Each one is counted as a loop-health gap in the
retro file and in the evaluation metrics' loop-health family.

## Platform facts and the road to enforcement

This policy is enforced by discipline and the retro audit,
not by the platform. Measured on 2026-10-31: the GitHub
account is on the Free plan, and for this private repository
both branch protection and rulesets return 403 - they require
a paid plan. Pull requests themselves work, and the VPS route
carries a `gh` login with the scope to open and merge them.
If the account is upgraded, add path-level required review
for the tier-2 paths (a CODEOWNERS-style rule), keep the
tier-1 paths unblocked so the execution heartbeat keeps
flowing, and raise this policy's version with the change
recorded in its changelog.

## Changelog

- 1.0.0, 2026-11-01 - first version. The two-tier scheme the
  owner approved on 2026-10-31: tier-1 records, queue, logs
  and tool state push directly; tier-2 knowledge and code
  land by pull request through the VPS `gh` route; the
  ticker pathspec discipline, the emergency exception and
  the retro audit stated; the Free plan platform facts
  recorded. This document itself lands as PR #1 under its
  own flow.
