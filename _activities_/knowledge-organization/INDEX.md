---
title: Knowledge Organization
created: 2026-11-01T05:38:00Z
modified: 2026-11-23T08:32:53Z
level: L1
version: 1.3.0
description: The knowledge organiser - folding what executions learn back into the activity profiles, resolving contradictions, and keeping the shared structures coherent
status: active
grounded_in:
  - source: owner direction of 2026-10-31 - a knowledge organiser alongside the tool developer, on an hourly feedback-fixing cadence
  - source: the learning and knowledge hardening protocol of the perception-driven queue design
  - source: ops execution records standard in the local conventions
  - source: "tool-development 2032 run (daily-reset UTC boundary fix, PR 249) and GitHub Issue #247 - organizer sweep trigger corrected to the 02:00 UTC boundary in this profile"
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

Hourly and incremental, with one fuller sweep after each trade-day reset; the full text, including the 2026-11-03 correction of the reset label, is in [cadence-section](cadence-section.md).


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

## Changelog

- 1.3.0, 2026-11-23 - The Cadence section moved verbatim to cadence-section.md to keep this page under 300 words; a one-line summary stays here.
