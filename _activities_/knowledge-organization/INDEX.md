---
title: Knowledge Organization
created: 2026-11-01T05:38:00Z
modified: 2026-11-01T05:38:00Z
level: L1
version: 1.0.0
description: The knowledge organiser - folding what executions learn back into the activity profiles, resolving contradictions, and keeping the shared structures coherent
status: active
grounded_in:
  - source: owner direction of 2026-10-31 - a knowledge organiser alongside the tool developer, on an hourly feedback-fixing cadence
  - source: the learning and knowledge hardening protocol of the perception-driven queue design
  - source: ops execution records standard in the local conventions
---

# Knowledge organization

## What this activity is

The loop's librarian. It reads what the executions produced
and folds the lessons back into the activity profiles -
mechanisms, measured values, entry points, failure modes -
resolves contradictions between records and profiles in
favour of the newest verified record, marks stale knowledge
stale, and keeps the indexes, the collection ledger and the
scout name roster coherent. It does not operate the game.

## Cadence

Hourly and incremental, as the standing job
`lastwar-knowledge-organizer`, working from a watermark in its
latest record; plus one fuller consolidation sweep of the
ended trade day on the first run after each 19:00 local
reset. Feedback order each run: unaddressed integrator review
points on profile PRs first, then the knowledge-organization
backlog entries, then new records since the watermark.

## Inputs

- Execution records (game and ops) since the watermark.
- Integrator reviews on profile and convention PRs.
- The knowledge-organization entries of
  `_records_/retro/improvements.md`.

## Outputs

- Profile updates with version bumps, changelog-noted
  corrections, and stale markings, delivered through the PR
  flow under the two-tier push policy.
- Gaps it cannot fix itself, filed as backlog or candidate
  entries.
- Its own execution record at
  `_records_/<date>/knowledge-organization/<HHMM>-run.md`,
  per the
  [ops execution records](../../_conventions_/local-conventions/ops-execution-records.md)
  standard. Records before this standard kept the dated note
  series at `_records_/knowledge-organizer/`; that series
  stays as history.

## Red lines

- Records are append-only: a contradiction is resolved in the
  profile, never by editing a record file.
- A superseded claim is never left standing silently; a
  correction is always noted where the claim lived.
