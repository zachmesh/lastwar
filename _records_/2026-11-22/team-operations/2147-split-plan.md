---
title: Split plan for oversized files - 2026-11-22 21:47 PT
created: 2026-11-22T21:47:00-08:00
modified: 2026-11-22T21:49:00-08:00
level: L3
version: 0.1.0
description: The verbatim splitter is merged and verified; how the activity profiles and the two registers are split, and what the register split changes for the retro flow
status: in-progress
activity: team-operations
run_id: team-operations-2026-11-22-2147-split-plan
trigger: owner instruction to split large files so they can be managed; toolsmith delivery of split-doc
started_at: 2026-11-22T21:47:00-08:00
finished_at:
duration_seconds:
verified: branch scope read, 21 tests re-run, dry-run verify re-run by the coordinator on improvements.md and alliance-donations (both byte for byte PASS, live repo untouched), tool references searched
---

# Split plan for oversized files

## Verified

- `_tools_/split-doc/split_doc.py` merged as `6aa1341f`: 4 files under `_tools_/`, 21 tests green. My own dry-run `--verify` passed byte for byte on `improvements.md` (4,181 words, 12 articles) and `alliance-donations/INDEX.md` (84,459 words, 218 articles plus 8 catalog pages). The toolsmith's third run covers `owner-decisions.md` (25 articles).
- No tool hard-codes the register paths; only a gate-test fixture names them.

## Decision: the two registers keep their old paths

AGENTS.md, TEAM.yaml and four conventions cite `_records_/retro/owner-decisions.md` and `improvements.md`, and 529 and 339 files cite them, mostly immutable records (C1). A plain split would leave those paths dangling. So each register stays at its path as an entry page of 300 words or fewer, and its articles go to a sibling folder (`owner-decisions-log`, `improvements-log`). The toolsmith adds the option `--keep-entry` (due 06:20Z).

## Decision: profiles split in place

Activity profile `INDEX.md` paths do not change; the folder gains its articles. Scribe pilot on `alliance-donations`, then the other six (perception-scout, radar-tasks, resource-collection, zombie-invasion, arms-race, survivor-intake), each on a branch with `--check` EQUAL and a clean gate.

## What the register split changes

- A new owner decision or improvement becomes one small article file plus one line on the entry page; it is no longer an append to a long file.
- The coach has been appending dated retro notes to `owner-decisions.md`. After the split those notes go to the daily retro file, not the register; the coach's duties change when the split lands.
- The temporary exemption lines for the two registers are removed in the same change as their split.

## Assignments

`A-20261123-0548-scribe` (alliance-donations pilot, due 06:25Z) and `A-20261123-0548-toolsmith` (`--keep-entry`, due 06:20Z).

## Outcome

Pending both replies.
