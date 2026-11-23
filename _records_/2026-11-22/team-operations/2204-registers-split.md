---
title: Registers split and splitter merged - 2026-11-22 22:04 PT
created: 2026-11-22T22:04:00-08:00
modified: 2026-11-22T22:08:00-08:00
level: L3
version: 0.1.0
description: The toolsmith's key-named splitter was reviewed and merged, and the two registers were split in place with their paths kept as entry pages; the 14 open owner decisions listed
status: done
activity: team-operations
run_id: team-operations-2026-11-22-2204-registers-split
trigger: toolsmith reply on A-20261123-0553; owner instruction to split large files
started_at: 2026-11-22T22:00:00-08:00
finished_at: 2026-11-22T22:08:00-08:00
duration_seconds: 480
verified: 38 tests re-run; --verify and --check run by the coordinator; the gate passed the staged split with no exemption; open list parsed from each article's own status line
---

# Registers split and splitter merged

## Splitter

`work/split-keys` merged as `1a0f6f5d`: 3 files under `_tools_/split-doc`, 38 tests green. My own run on `alliance-donations/INDEX.md` repeats the toolsmith's numbers: 84,459 words, 267 articles plus 11 catalog pages, verify PASS (sha256 `7656c5649cd3`), 118 of 118 heading keys findable, no `what-the` file names (pilot: 184). Two deviations approved: parts are `-p1`, `-p2` (a 3-word key plus `-part-1` would break the 2 to 4 word name rule), and each article carries a sequence field because names no longer carry a number.

## Registers

Applied in place with `--keep-entry`, originals saved for `--check`:

| Register | Words before | Entry page | Log folder | Check |
|---|---:|---:|---|---|
| owner-decisions.md | 8,907 | 244 body | owner-decisions-log, 35 files | EQUAL, 58,116 characters |
| improvements.md | 4,181 | 225 words | improvements-log, 33 files | EQUAL, 30,317 characters |

Both entry pages stay at their old paths, so the 532 and 341 citing files keep working. The two exemption lines were removed in the same change and the gate passed the staged split with none. Commits `99dc1119` and `fc778fc5`; coach duties updated (`c3f9c61e`): entries are articles, dated notes go to the daily retro.

## Finding for the owner

The owner-decisions entry page now lists the open items, read from each article's status line: **14 open**, the oldest OD-20261031-01 (23 days). OD-20261109-01 was decided by expiry on 2026-11-12 though its first entry still reads open.

## Next

The scribe re-splits `alliance-donations` with the new tool and remaps its digest; then six more profiles. Held for a free model-turn slot.
