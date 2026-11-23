---
title: Split pilot findings and decisions - 2026-11-22 21:53 PT
created: 2026-11-22T21:53:00-08:00
modified: 2026-11-22T21:55:00-08:00
level: L3
version: 0.1.0
description: The scribe's pilot split of alliance-donations is lossless but hard to navigate; decisions to fix the splitter before splitting the other profiles and registers
status: in-progress
activity: team-operations
run_id: team-operations-2026-11-22-2153-split-findings
trigger: scribe and toolsmith replies on A-20261123-0548
started_at: 2026-11-22T21:53:00-08:00
finished_at:
duration_seconds:
verified: scribe's measurements read; toolsmith's keep-entry branch reviewed (scope, 28 tests re-run) and its register dry-run list read
---

# Split pilot findings and decisions

## Pilot (scribe, branch work/split-alliance-donations, commit 8acf4295, not pushed)

- Lossless: 218 articles, 8 catalog pages, article words sum to the original 84,459; `--verify` PASS and `--check` EQUAL (body sha256 7656c5649cd3); INDEX 1.104.0 to 1.105.0 with one changelog line; main untouched.
- Finding 1: the gate passes the unsplit file too, because legacy size is ignored; size is judged with `record-check` and `watch`, not the gate.
- Finding 2, navigation only: 184 of 218 file names are `what-the-2026`; 89 of 118 level-2 headings start mid-article; 76 of 106 unit sections sit in a neighbour article and 2 are in no title or catalog line; the INDEX lost the live rule.

## Toolsmith (`--keep-entry`, merged as `463b4ab0`, 28 tests)

The registers keep their paths as entry pages. Dry runs: `owner-decisions.md` 25 articles plus a catalog page, entry page 116 words; `improvements.md` 12 articles, entry page 171 words. Names are sensible there, but one article holds several entries.

## Decisions

1. Not applying the register split and not splitting the six profiles yet. The exemption lines stay, as a documented temporary measure.
2. Toolsmith `A-20261123-0553` (due 06:30Z): split at heading boundaries, name articles from the heading key, list every key in a catalog line; target findability 100 percent and zero `what-the-` names.
3. Scribe `A-20261123-0553` (due 06:25Z): the rule digest the INDEX lost, 200 words, each rule cited.
4. Open PRs #711 #713 #753 #754 #755 #827 edit the INDEX files and would conflict; the Steward is asked to merge, close or sequence them.

## Outcome

Pending both replies.

## PR route (appended 2026-11-23T05:54Z)

The Steward read the seven conflicting PRs against origin/main: #711 (four profiles) and #828 (building-queues 1.6.0) are pure duplicates, 100 percent of added text already verbatim on main; #713, #753, #754, #755 and #827 (resource-collection, targeting 1.67.0 and 1.68.0 while main is at 1.70.0) have 72 to 86 percent of their lines already on main, and the 10 distinct lines are version-history entries that main's changelog replaces plus probe observations that live in the immutable records. All are mergeable=false.

Decision: close all seven with a one-line comment, delete no branch so any line can be recovered; leave #838, #425 and #858 alone. The coordinator replied "close" at 05:54Z; the Steward does it and reads the states back. This removes every INDEX conflict before the splits.
