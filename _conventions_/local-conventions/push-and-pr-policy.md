---
title: Push and PR Policy
created: 2026-11-01T05:31:00Z
modified: 2026-11-01T05:51:00Z
version: 2.0.0
status: draft
description: PR-only main policy draft - main advances only by pull request merge and records ride date branches
grounded_in:
  - source: owner decision 2026-10-31 - disallow direct commits to main and require a pull request for all pushes
  - source: owner decision 2026-10-31 - records PR merge cadence option A, the integrator merges every 15 minutes when new commits exist
  - source: platform check 2026-10-31 - the GitHub account is on the Free plan and branch protection and rulesets return 403 on this private repository
---

# Push and PR policy

This is version 2.0.0 in draft. It states the owner's direction
of 2026-10-31: main becomes PR-only and direct pushes to main
are disallowed. It takes effect only when it lands on main
through its own pull request and the standing jobs' push steps
have been migrated to it; until then version 1.0.0 remains the
active policy. The migration checklist is kept with the goal
workspace, not in this repository.

## The rule

Main advances only by pull request merge. No job, agent or
script pushes directly to main, for any path. The tier-1
direct-push tier of version 1.0.0 is abolished: there is no
class of file that may be committed straight to main. Every
commit that lands on main is a pull request merge - a squash
merge for knowledge and code, a merge commit for records -
recognisable in the commit graph by its pull request
reference. The single exception is the break-glass clause
below.

## Records flow - date branches

Append-only trajectories and live state keep their continuity
without touching main directly:

- `_records_` - play records and ops execution records,
  append-only under C1.
- `_queue_` - the task unit pool and its state transitions.
- `_logs_` - the input and action logs.
- `tools/state/` - runtime state written by the tools
  themselves (for example the regulars tracker state).

Writers commit these paths to a date branch named
`records/<YYYY-MM-DD>`, the local date of the records being
committed. The branch is created from current main on its
first use that day, is pushed through the standard VPS route
(bundle to the IONOS VPS, fetch in `~/lastwar-push`,
`git push github records/<date>`), and is never deleted: it
keeps receiving that day's appends, before and after each
merge, and the next day starts a fresh date branch. The
pathspec discipline of
[recording rules](recording-rules.md) is unchanged - records
commits stage only the four records paths, by explicit
pathspec, never a blanket add, and a load-bearing change found
sitting in the working tree is left exactly as it is, noted in
the run record, and left for its own pull request. A writer
never waits for its records to reach main; the branch is its
record, and main catches up on the integrator's cadence.

## Records pull requests - cadence A

Owner decision, 2026-10-31 at 22:49 PDT - cadence option A:
the integrator merges every 15 minutes when new commits exist,
so main stays near real-time. (Option B, one merge at each
trade-day close, was considered the same evening and not
chosen; it is not part of this policy.)

The integrator keeps exactly one open records PR per live date
branch. When a records branch has no open PR, the integrator
opens one (`gh pr create`, base main, head `records/<date>`;
the body names the date and this policy - records PRs carry no
per-PR improvement id, their ledger entry is this flow). On
every integrator pass, if the open records PR has new commits,
the integrator merges it with a merge commit
(`gh pr merge --merge`, never `--delete-branch`). The merge
commit is what keeps the scheme working: the date branch
survives the merge and keeps taking appends, and the next pass
opens a fresh PR for whatever arrived after the merge. Main
therefore trails the live records by at most one integrator
cycle.

A records PR that conflicts with main is never force-merged
and never silently dropped. The integrator comments the
conflict on the PR, notes it in its run record, and the
conflict is resolved on the branch side; the normal cadence
resumes once the branch is clean.

## Knowledge and code pull requests

Everything outside the four records paths is load-bearing and
lands by its own pull request: `tools/` (the only exception
inside `tools/` is `tools/state/` above), `_conventions_`,
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

## PR branches carry no log appends

A pull request branch - records or work - never carries
appends to the append-only logs under `_logs_` (the input log
and the action log). The evidence is from this repository on
2026-10-31: PR #2 went through two rebase rounds, main
advanced three times inside ten minutes on records commits,
and every conflict sat in the log tails and the day index
those commits keep appending. Log lines race main's
high-frequency records flow by construction; a branch that
carries them is a branch built to conflict.

The record duty does not disappear, it moves:

- During the PR's life, the record is the PR body and the
  commit messages, which already state what the change
  serves, what was validated and what files it touches.
- At merge time, the integrator adds the input-log and
  action-log lines for the merged work as part of the merge
  bookkeeping, or the lines ride the next records branch
  after the merge. Either way they land once, on a branch
  that does not race itself.
- A retro that cannot find a merged change's log lines names
  the gap like any other loop-health gap; the fix is to add
  the lines, never to start carrying them on PR branches
  again.

## The integrator

The standing PR integrator job (every 15 minutes) owns the
merge point of main. Its duties under this policy:

1. **Records PRs.** Open when missing, merge by merge commit
   on cadence A when new commits exist, comment and report on
   conflict, never force-merge, never delete a records
   branch. At each merge, add the log lines the change is
   owed (previous section).
2. **Knowledge and code PRs.** Review against the PR body
   requirements and the repository's standing rules; merge
   clean PRs by squash; leave numbered criticism comments on
   PRs that are fixable but not clean, and do not repeat a
   comment when no new commit has arrived since it.
3. **Owner-gated classes are never merged by the
   integrator** - a change that loosens a red line, widens an
   authorization, changes a cron definition, or changes this
   policy itself is commented, escalated to the owner in
   chat, and merged only on the owner's recorded approval.
4. **Sync and records.** After merges, sync main back to the
   local clone through the VPS bundle route; and leave an
   ops execution record for every pass, including no-op
   passes, per the ops execution records standard - the
   loop's own activity is recorded as executions like
   everything else.

## Break-glass

The only direct push to main this policy tolerates is one the
owner orders explicitly, in chat, in so many words. No
standing urgency creates the exception on its own - a broken
tool or a blocked loop waits for the next integrator cycle or
for the owner. Every break-glass use is spent, not silent:
the next retro names it, and a retroactive PR is opened for
the record, or that retro states why none was needed.

## Audit

The daily retro's loop-health check scans every commit that
landed on main since the previous retro and classifies each
one: a pull request squash merge (pull request reference in
the subject), a records PR merge commit, a retro-named
break-glass commit - or a violation. Every violation is named
in the retro file, counted in the evaluation metrics'
loop-health family, and filed as an improvement task. Under
this policy there is no fourth legitimate class.

## Platform facts and enforcement

This policy is enforced by pipeline discipline, a push-route
guard and the retro audit - not by the platform. Measured on
2026-10-31: the GitHub account is on the Free plan, and for
this private repository both branch protection and rulesets
return 403; they require a paid plan. Pull requests work, and
the VPS route carries a `gh` login with the scope to open and
merge them.

The push-route guard is a step in the standard route: the
`~/lastwar-push` clone refuses any direct push of the main ref
(a pre-push hook rejecting updates to `refs/heads/main`), so
the route every writer uses cannot push main even by mistake.
Branch pushes are unaffected, and `gh pr merge` operates on
GitHub's side, so merges are unaffected. A hard server-side
lock - branch protection requiring pull requests on main -
needs GitHub Pro; if the account is upgraded, enable it, keep
this policy as the operating procedure on top of it, and
record the change in the changelog below.

## Changelog

- 2.0.0, 2026-11-01 - draft for the owner's PR-only direction
  of 2026-10-31. Main advances only by pull request merge and
  the tier-1 direct tier is abolished; records ride
  `records/<YYYY-MM-DD>` date branches into integrator-opened
  records PRs, merged by merge commit on cadence A - every 15
  minutes when new commits exist, main near real-time - which
  the owner chose the same evening at 22:49 PDT over the
  trade-day-close alternative; knowledge and code PRs stay
  squash; PR branches carry no `_logs_` appends (PR #2's two
  rebase rounds, 2026-10-31, conflicted only on log tails
  racing records commits), the integrator adds the log lines
  at merge; the integrator's duties are stated in full;
  break-glass narrows to the owner's explicit in-chat order,
  named by the next retro with a retroactive PR; enforcement
  is discipline, the VPS push-route guard and the retro audit
  of the main commit graph; the Free plan platform facts
  stand.
- 1.0.0, 2026-11-01 - first version. The two-tier scheme the
  owner approved on 2026-10-31: tier-1 records, queue, logs
  and tool state push directly; tier-2 knowledge and code
  land by pull request through the VPS `gh` route; the
  ticker pathspec discipline, the emergency exception and
  the retro audit stated; the Free plan platform facts
  recorded. This document itself landed as PR #1 under its
  own flow.
