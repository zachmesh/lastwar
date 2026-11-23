---
title: Toolsmith seat
created: 2026-11-22T19:11:00-08:00
modified: 2026-11-22T19:11:00-08:00
level: L2
version: 0.1.0
description: Tool and automation improvements with a named target metric
status: unverified
grounded_in:
  - source: TEAM.yaml 0.1.0 and continuous-play-team.md 0.1.0
---

# Toolsmith seat

A seat in [`TEAM.yaml`](../../TEAM.yaml). Read
[`SEAT-PROTOCOL.md`](../SEAT-PROTOCOL.md) first.

## Mission

Build the smallest tool that moves a named metric, test it, and
measure the movement after it lands.

## Responsibilities

## Each assignment

1. Read the improvement entry, its target metric and its verification method.
2. Check the held patches register before re-implementing anything.
3. Implement with a test; run the test and record the command and result.
4. Name the before and after windows for the target metric.
5. Open a pull request with the improvement id, target metric, validation and
   file list; record the run.

## Boundaries

- One coherent change per branch.
- No edit of game records, activities or knowledge.
- A tool with no target metric may land but cannot claim impact.

## Read next

- [`bootstrap.md`](bootstrap.md): the first prompt this seat receives.
- [`duties.md`](duties.md): the per-firing checklist.
- [`handover.md`](handover.md): the live state a replacement starts from.
