---
title: Push and PR Policy
created: 2026-11-01T05:31:00Z
modified: 2026-11-02T00:20:44Z
version: 2.3.0
status: draft
description: PR-only main policy - main advances only by pull request merge, records ride date branches, every pull request carries a named owning scheduled job, and every executor run checks its own pull requests first and ends by opening one
grounded_in:
  - source: owner decision 2026-10-31 - disallow direct commits to main and require a pull request for all pushes
  - source: owner decision 2026-10-31 - records PR merge cadence option A, the integrator merges every 15 minutes when new commits exist
  - source: owner decision 2026-11-01 - records PR merge cadence superseded by four-hour batches, approved by the owner in chat
  - source: owner instruction 2026-10-31 23:00 PDT - every pull request must name an owning scheduled job, with a catch-all owner job when no class matches
  - source: owner instruction 2026-10-31 23:02 PDT - every executor checks its own previous pull requests before doing anything else, and opens a pull request at the end of every run that produces output
  - source: platform check 2026-10-31 - the GitHub account is on the Free plan and branch protection and rulesets returned 403 on this then-private repository
---

# Push and PR policy

This is version 2.3.0 in draft. It states the owner's direction
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
- `_tools_/state/` - runtime state written by the tools
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

Delivery gate (issue #422). Before a records-branch delivery
bundles the working tree, it runs the log gate on the action
log:

    python3 _tools_/log_append.py gate \
        --file _logs_/repo-actions/action-log.jsonl

A non-zero gate blocks the bundle: the delivery stops, the run
records the failure, and no malformed log reaches the branch.
The gate repairs concatenated lines and drops blank lines in
place (newlines only; the logged objects are verified
unchanged), so a branch-side repair that never propagated back
to the live tree is re-applied at the next delivery instead of
being re-offered on every push. The repair the gate applies is
a records change and rides the same date branch as the
delivery.

## Records pull requests - batch cadence

Owner decision, 2026-11-01 - records PRs are merged in
batches every 4 hours, superseding cadence A (the
2026-10-31 at 22:49 PDT decision that the integrator merge
every 15 minutes when new commits exist, so main stayed near
real-time). Rationale, from the same day's running: on
2026-11-01 the integrator merged more than 16 PRs, nearly
all of them routine records merges carrying zero review
value - the merge ceremony cost the loop passes and bought
no scrutiny. Records are append-only trajectories; nothing
in them is improved by being merged sooner.

A batch lands at the first integrator pass at or after each
of 19:00, 23:00, 03:00, 07:00, 11:00 and 15:00
America/Los_Angeles. The boundary set is chosen so a batch
lands right after the 19:00 trade-day reset and the 20:39
daily retro reads a complete trade day in main. Between
batches, main trails the live records by at most 4 hours;
writers and readers that need the live record read the date
branch, exactly as the records flow section above already
provides.

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

## Pull request ownership

Owner instruction, 2026-10-31 at 23:00 PDT: every pull
request has an owner, and no pull request is left ownerless.
At creation, the PR body names the owner on its own line:

`Owner: <scheduled job id>`

The owner is responsible for the PR's life up to the merge
point: fixing the integrator's review feedback on the same
branch, replying on the PR with what changed, and driving
the PR to a mergeable state. The owner is never the merger -
merging stays with the integrator, exactly as above.

Ownership is assigned by the class of the change:

- `_tools_/` code and tool behaviour changes -
  `lastwar-tool-developer`.
- `_activities_`, `_conventions_` and profile/convention
  changes - `lastwar-knowledge-organizer`.
- Records PRs on `records/*` branches -
  `lastwar-pr-integrator`: it opens them and it merges
  them, so it owns them end to end.
- A mixed PR is owned by the class of its load-bearing
  change; the body also names the secondary classes it
  touches.

When no class matches - a root document, `AGENTS.md`, a
path type this policy has not seen, anything that cannot be
classified - the catch-all owner is
`lastwar-pr-catchall-owner`, a standing scheduled job whose
remit is exactly these otherwise-orphaned PRs. There is no
fourth outcome: a PR is owned by its class job, by the
integrator (records), or by the catch-all.

If the owner line is missing or names the wrong job, the
integrator reassigns it at first review, by the
classification above, and states the reassignment in a
comment on the PR. A PR with no owner on record is not
mergeable until that reassignment is made.

Owner-gated PRs (a loosened red line, a widened
authorization, a cron definition change, or a change to
this policy itself) are owned by the integrator in a
shepherd role: it escalates the PR to the owner, tracks the
decision, and records the outcome. Any fix the decision
calls for is executed afterwards by the job of the change's
own class, not by the integrator.

## Executor PR discipline

Owner instruction, 2026-10-31 at 23:02 PDT: an executor's
pull requests are part of its run, at both ends. This
section is the temporal side of the ownership section
above - ownership says whose a PR is; this section says
when its owner must attend to it. The integrator's
full-sweep review and reassignment rules are unchanged by
it.

**Own PRs first.** Before an executor job does any new
work in a run, it checks the pull requests it opened or
owns - the PRs whose body `Owner:` line names the job,
plus the records PRs it opened itself. It reads the latest
comments on each one. Every question on one of its PRs is
answered on the PR, whether or not the answer needs a code
change; every piece of review feedback is fixed on the
same branch first and replied to on the PR. A job does not
start new work while one of its own PRs still carries an
unanswered question or unaddressed feedback it can act on.

**A run ends by opening a PR.** A run is not finished
until its output is inside a pull request:

- Work output (knowledge, code, conventions) is opened as
  a PR in the same run that produces it, per the knowledge
  and code flow above.
- Records output is pushed to the live records date
  branch, and the run then confirms the records PR for
  that branch exists - a fresh PR for the new commits, on
  top of whatever was merged before. If none exists, the
  executor opens it itself (`gh pr create`, base main,
  head `records/<date>`, body naming the date, this
  policy, and `Owner: lastwar-pr-integrator`, which owns
  records PRs end to end); it does not wait for the
  integrator to notice the branch.
- A run that cannot open or confirm its PR records itself
  partial, with the reason, in its execution record.
  Finished output is never left sitting on a local branch
  as the run's final state.

The daily retro's loop-health check extends to this
section in the same pass as its other scans: run records
are checked for the own-PRs-first step and for the closing
PR, and a run that skipped either is named in the retro
and counted in the loop-health family.

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
   on the batch cadence (the first pass at or after 19:00,
   23:00, 03:00, 07:00, 11:00 and 15:00 America/Los_Angeles)
   when new commits exist, comment and report on conflict,
   never force-merge, never delete a records branch. At each
   merge, add the log lines the change is owed (previous
   section).
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

The same check covers ownership: every PR merged in the
window must show its owner on record - the `Owner:` line in
its body, or an integrator reassignment comment where the
line was missing or wrong. A merged PR with no owner named
anywhere is reported in the retro by number, counted in the
loop-health family, and filed as an improvement task like
any other violation. The standing target is an ownership
coverage of 100 percent of merged PRs.

## Platform facts and enforcement

This policy is enforced by pipeline discipline, a push-route
guard and the retro audit - not by the platform. Measured on
2026-10-31, while this repository was still private: the
GitHub account is on the Free plan, and for this repository
both branch protection and rulesets returned 403; on a
private repository they require a paid plan. The repository
was transferred to zachmesh/lastwar and made public later on
2026-10-31, so that measurement no longer describes the
repository's platform limits and is to be re-measured for the
public repository. Pull requests work, and the VPS route
carries a `gh` login with the scope to open and merge them.

The push-route guard is a step in the standard route: the
`~/lastwar-push` clone refuses any direct push of the main ref
(a pre-push hook rejecting updates to `refs/heads/main`), so
the route every writer uses cannot push main even by mistake.
Branch pushes are unaffected, and `gh pr merge` operates on
GitHub's side, so merges are unaffected. A hard server-side
lock - branch protection requiring pull requests on main -
needed GitHub Pro while the repository was private; for a
public repository it is available on the Free plan. Enabling
it is an owner decision; if it is enabled, keep this policy
as the operating procedure on top of it, and record the
change in the changelog below.

## Changelog

- 2.3.0, 2026-11-01 - records merge cadence, on the owner's
  decision of 2026-11-01 given in chat. Records PRs no
  longer merge on every integrator pass; they merge in
  batches every 4 hours, at the first integrator pass at or
  after 19:00, 23:00, 03:00, 07:00, 11:00 and 15:00
  America/Los_Angeles, superseding cadence A of 2.0.0. The
  boundary set puts a batch right after the 19:00 trade-day
  reset so the 20:39 daily retro reads a complete trade day
  in main. Rationale recorded the same day: the integrator
  merged more than 16 PRs on 2026-11-01, nearly all routine
  records merges with zero review value. Opening records
  PRs is unchanged - a PR exists as soon as a branch carries
  commits - and knowledge and code PRs still merge promptly
  on every pass. This amendment changes the PR policy
  itself and is therefore owner-gated; it lands on the
  owner's recorded in-chat approval of 2026-11-01, the same
  precedent as PR #3 and PR #4.
- 2.2.1, 2026-11-01 - factual correction only, no rule
  change, on the owner's instruction of 2026-10-31 at 23:25
  PDT. The repository was transferred from its previous
  home under the dtadpole account to zachmesh/lastwar and
  made public on 2026-10-31. The
  platform-facts statements that described this repository as
  private are corrected to past tense, and the
  branch-protection measurement taken while the repository
  was private is marked stale pending re-measurement for the
  public repository. The living-doc references to the old
  repository name are updated in the same change.
- 2.2.0, 2026-11-01 - executor PR discipline, on the owner's
  instruction of 2026-10-31 at 23:02 PDT that every executor
  check the questions and issues on its own previous pull
  requests before doing anything else, and open a pull
  request every time a run finishes. Each executor run now
  starts by clearing its own PRs - answering every question
  on the PR, fixing review feedback on the same branch -
  before starting new work, and ends only when its output
  is inside a PR: work output opened as a PR in the same
  run, records output pushed to the date branch with the
  records PR confirmed to exist or opened by the executor
  itself when missing (owned by `lastwar-pr-integrator`).
  A run that cannot open or confirm its PR records itself
  partial with the reason; finished output never ends a run
  sitting on a local branch. The section is the temporal
  side of pull request ownership and leaves the
  integrator's sweep and reassignment rules unchanged; the
  retro audit gains an own-PRs-first and closing-PR check
  on run records. The seven standing executor jobs' texts
  were updated to these two rules the same evening, ahead
  of this amendment; the amendment codifies them so future
  jobs are bound automatically. This amendment changes the
  PR policy itself and is therefore owner-gated; it lands
  by bootstrap squash merge on the owner's recorded in-chat
  instruction of 2026-10-31 23:02 PDT, the same precedent
  as PR #3 and PR #4.
- 2.1.0, 2026-11-01 - pull request ownership, on the owner's
  instruction of 2026-10-31 at 23:00 PDT that every PR have
  an owner and that a catch-all scheduled task own any PR no
  class matches. Every PR names its owning scheduled job in
  its body at creation (an `Owner:` line); the owner fixes
  review feedback on the same branch, replies on the PR, and
  drives it to mergeable, while merging stays with the
  integrator. Assignment is by change class - `_tools_/` to
  `lastwar-tool-developer`, `_activities_` and
  `_conventions_` to `lastwar-knowledge-organizer`, records
  PRs to `lastwar-pr-integrator` - and anything no class
  matches falls to the new standing catch-all job
  `lastwar-pr-catchall-owner`. The integrator reassigns a
  missing or wrong owner at first review and an ownerless PR
  is not mergeable until it does; owner-gated PRs are owned
  by the integrator as shepherd. The retro audit gains an
  ownership-coverage check against a 100 percent target.
  This amendment changes the PR policy itself and is
  therefore owner-gated; it lands by bootstrap squash merge
  on the owner's recorded in-chat instruction of 2026-10-31
  23:00 PDT, the same precedent as PR #3.
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
