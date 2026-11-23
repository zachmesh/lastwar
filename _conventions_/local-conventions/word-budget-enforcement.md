---
title: Word Budget Enforcement
created: 2026-11-23T08:35:00Z
modified: 2026-11-23T09:40:00Z
level: L2
version: 0.2.0
description: The three triggers that enforce the document word budget (300 recommended, under 500 hard) and the fold rule that keeps pages small
status: active
grounded_in:
  - source: owner priority P1 2026-11-23 relayed by Steer B, improvement IMP-20261123-10 (parent IMP-20261123-03)
  - source: lint_gate.py watch on local main 2026-11-23 08:27Z (documents 10,356; at or over 500 words 3,420)
---

# Word budget enforcement

The core concision convention sets 300 words recommended and under 500 hard.
This page says how it is enforced here. Owner priority P1: it comes ahead of
every non-play task; play units are never paused for it.

## Three triggers

1. **Commit and merge hooks.** The pre-commit hook and the pre-merge-commit hook
   run the staged check and block a real edit of any document at or over 500
   body words. The legacy exemption list only shrinks: no entry is added, entries
   are removed as pages are split. A proven redaction-only change is exempt per
   file (`redact --verify-diff`). When the gate itself cannot run (exit 2) both hooks
   WARN AND ALLOW (OD-20261123-06).
2. **The Integrator's landing check.** Every landing runs
   `lint_gate.py check --base origin/main` as a blocking check, records the
   result and, after the merge, the `watch` count at or over 500 words. On exit 2
   the landing is REFUSED until the gate runs (OD-20261123-06). No GitHub
   Actions or workflow files, ever (OD-20261123-08).
3. **Daily review.** The coordinator runs `lint_gate.py watch` at the 12:00Z
   review and records the count at or over 500 by top folder. A new document
   over 500 words names its owner seat, which fixes it within 24 hours.

## The fold rule

Approved by the owner (OD-20261123-09), written in the scribe's duties: a fold
UPDATES the topic article with a version bump and cites the record path in
`grounded_in`; it never writes a per-run summary and never appends to an INDEX; a
new article only when the topic has none. A log that grows by appending rolls over
into a new key-named file before 450 words. Play records stay immutable (C1): a
record is split or rolled over by its writer, never rewritten.

## Baseline, 2026-11-23 08:27Z (local main)

Documents 10,356; at or over 500 words 3,420 (legacy 3,419, new 1): `_records_`
3,407, `_conventions_` 11, `_knowledge_` 1, root 1, `_activities_` 0 (origin
still shows 20 until the records landing merges).
