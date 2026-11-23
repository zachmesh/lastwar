---
title: Integrator handover
created: 2026-11-23T07:25:00Z
modified: 2026-11-23T09:08:00Z
level: L2
version: 0.2.0
description: The live state a replacement integrator starts from
status: unverified
grounded_in:
  - source: owner decision 2026-11-23 that integration is a dedicated seat, relayed by Steer A
  - source: reflection integrator-role convention, adapted in TEAM.yaml 0.6.0 coordination.integration
---

# Handover - integrator

Updated 2026-11-23 07:25Z. Earlier versions are in git history.

## Holder

- Session `session-bc838015-7852-464e-8cab-cf2fcc70a335`, started
  2026-11-23T07:15:00Z, model `claude-sonnet-5-5` xhigh.
- Hand-offs come from the coordinator
  (`session-4b4cb08d-fb77-419a-be34-14a72a3b73d1`) as a local branch name.

## State

- PR 858 was merged once by the owner gateway before this seat existed (merge
  commit, branch kept); that was a one-off, not a precedent.
- Pending landings, in order: the owner-name redaction branch, then the held
  splits and the day's records, each as a clean branch built on the tip of
  `origin/main`. Local `main` is a different line (the clone is shallow and is
  re-shallowed by other processes), so branches are snapshot commits on top of
  `origin/main`.
- The owner exception: the owner's own in-game name is redacted tree-wide
  (OD-20261123-04); history is not rewritten; the repository stays public.

## Owner rules (2026-11-23)

The landing check `check --base origin/main` BLOCKS on exit 2: a landing is refused until the gate runs (OD-20261123-06). No GitHub Actions or `.github/workflows`, ever (OD-20261123-08). Landed so far: PRs 873, 875, 876, 877.

## Lessons

The scan must be regex-based and whole-tree; a wrapped name needs the
whole-file census. Merge with a merge commit and read main back every time.
