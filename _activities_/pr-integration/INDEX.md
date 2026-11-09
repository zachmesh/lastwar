---
title: PR Integration
created: 2026-11-01T05:38:00Z
modified: 2026-11-01T06:28:00Z
level: L1
version: 1.0.1
description: The PR integrator - reviewing the loop tier-2 pull requests, merging the clean ones, leaving critical feedback on the rest, and escalating owner-gated changes
status: active
grounded_in:
  - source: owner direction of 2026-10-31 - an integrator task every 15 minutes that reviews PRs, gives critical feedback, or merges
  - source: push and PR policy in the local conventions
  - source: ops execution records standard in the local conventions
---

# PR integration

## What this activity is

The loop's reviewer and gatekeeper for the tier-2 flow of the
[push and PR policy](../../_conventions_/local-conventions/push-and-pr-policy.md).
It reads every open pull request on zachmesh/lastwar, checks
scope, body completeness, safety and consistency, and either
merges it, leaves one consolidated critical review, or
escalates it to the owner. It authors nothing itself.

## Cadence

Every 15 minutes, as the standing job `lastwar-pr-integrator`,
working through the VPS `gh` route.

## Inputs

- The open PR list, bodies and diffs on zachmesh/lastwar.
- The two-tier policy's review checklist and the improvement
  backlog the PRs cite.

## Outputs

- Squash merges of clean PRs, with the merged main synced
  back to the local repository.
- Numbered, actionable review comments on PRs that are not
  ready, left once per PR revision.
- Owner-gated escalations, reported to the owner with the
  exact decision needed.
- Its own execution record at
  `_records_/<date>/pr-integration/<HHMM>-run.md`, per the
  [ops execution records](../../_conventions_/local-conventions/ops-execution-records.md)
  standard - including the no-op record of a pass with no open
  PRs.

## Red lines

- Never merges a change that loosens a red line, widens a
  standing authorisation, edits a schedule definition, or
  amends the push and PR policy itself - those wait for the
  owner.
- Never force-pushes, never merges through a conflict, never
  closes a PR unmerged.
