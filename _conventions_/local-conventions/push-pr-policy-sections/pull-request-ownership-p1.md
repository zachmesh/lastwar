---
title: Pull request ownership part 1
created: 2026-11-23T09:02:35Z
modified: 2026-11-23T09:02:35Z
version: 0.1.0
sequence: 7
description: Owner instruction, 2026-10-31 at 2300 PDT - every pull request has an owner, and no pull
---
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

