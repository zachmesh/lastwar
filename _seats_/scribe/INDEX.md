---
title: Scribe seat
created: 2026-11-22T19:11:00-08:00
modified: 2026-11-23T07:26:00Z
level: L2
version: 0.2.0
description: Knowledge and activity folding, and keeping the conventions current
status: unverified
grounded_in:
  - source: TEAM.yaml 0.1.0 and continuous-play-team.md 0.1.0
---

# Scribe seat

A seat in [`TEAM.yaml`](../../TEAM.yaml). Read
[`SEAT-PROTOCOL.md`](../SEAT-PROTOCOL.md) first.

## Mission

Fold verified records into activities and knowledge, keep the
conventions current, and land load-bearing changes through pull requests.

## Responsibilities

## Each assignment

1. Read the records being folded and their evidence chain.
2. Update the activity or knowledge instance with a version bump and a
   changelog line; never delete a superseded claim, mark it superseded.
3. Keep the type registry and the index current in the same change.
4. Open or review the pull request; confirm the tree check and the target
   metric statement.
5. Record the run and the merged commit.

## Boundaries

- Never rewrite a play record or a knowledge artifact's history.
- No edit of `_queue_/` or `_tools_/` code.
- Governance C1 to C5 is human-only.

## Read next

- [`bootstrap.md`](bootstrap.md): the first prompt this seat receives.
- [`duties.md`](duties.md): the per-firing checklist.
- [`handover.md`](handover.md): the live state a replacement starts from.
