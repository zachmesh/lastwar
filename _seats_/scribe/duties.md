---
title: Scribe seat duties
created: 2026-11-22T19:11:00-08:00
modified: 2026-11-23T08:53:35Z
level: L2
version: 0.3.0
description: The per-firing checklist for this seat
status: unverified
grounded_in:
  - source: TEAM.yaml 0.1.0 and continuous-play-team.md 0.1.0
---

# Duties - scribe

## Each assignment

1. Read the records being folded and their evidence chain.
2. Update the activity or knowledge instance with a version bump and a
   changelog line; never delete a superseded claim, mark it superseded.
3. Keep the type registry and the index current in the same change.
4. Open or review the pull request; confirm the tree check and the target
   metric statement.
5. Record the run and the merged commit.

## Record

Write the run at `_records_/<date>/<activity>/<HHMM>-run.md` and append the
day index. The record carries inputs, outputs, stats and follow-up.

## The fold rule

1. A fold UPDATES THE TOPIC ARTICLE (the rule digest, cadence, how-it-is or open question the record changes) with a version bump, and cites the record path in `grounded_in`.
2. A fold never writes a per-run "what this run added" summary: the record already holds it, and a second home for per-run facts drifts.
3. A NEW article only when the topic has none; the INDEX gets a pointer line then and is never appended to otherwise.
4. The limits stay: 300 words recommended, under 500 hard; run `lint_gate.py record-check` before editing a page and split a page over 300 words first.

## Changelog

- 0.2.0, 2026-11-23 - The fold rule added (assignment A-20261123-0830-scribe).
- 0.3.0, 2026-11-23 - The fold rule changed (IMP-20261123-12, assignment A-20261123-0853-scribe): a fold updates the topic article and never writes a per-run summary. The 0.2.0 text was: "A fold writes a NEW key-named article and never appends to an INDEX or to an existing page near the limit (300 words recommended, under 500 hard). The INDEX gets one pointer line. Run `lint_gate.py record-check` on a page before editing it; a page over 300 words is split first."
